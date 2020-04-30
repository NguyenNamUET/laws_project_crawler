import concurrent.futures
from tqdm import tqdm
import math

from my_crawler.crawler_helper.url_helper import get_id_from_url, get_id_from_url__vbpl
from my_crawler.transformer.document_thuvienphapluat_transform import scrapy_thuvienphapluat
from my_crawler.transformer.document_vbpl_transform import scrapy_vbpl

from utilities.writer_helper import store_gz, store_error, write_to_record
from utilities.common import grouper, is_validate_json
from utilities.reader_helper import load_record_to_list


def multithread_crawl_with_batch(current_version_path, document_urls, record_to_check_file=None, max_workers=24,
                                 keep_official_number_record=False, check_duplicate=False):
    if record_to_check_file is not None:
        official_number_list_to_check = set(load_record_to_list(record_to_check_file))

    for index, urls_group in enumerate(grouper(document_urls, 100)):
        print("Batch " + str(index + 1) + "/" + str(math.ceil(len(document_urls) / 100)))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            if current_version_path.find("thuvienphapluat.vn") >= 0:
                future_to_url = {executor.submit(scrapy_thuvienphapluat, url): url for url in urls_group
                                 if url is not None}
            elif current_version_path.find("vbpl.vn") >= 0:
                future_to_url = {executor.submit(scrapy_vbpl, url): url for url in urls_group
                                 if url is not None}

            for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(future_to_url)):
                url = future_to_url[future]
                try:
                    doc_obj = future.result()
                    if doc_obj is not None and doc_obj != '' and is_validate_json(doc_obj) is None:
                        if current_version_path.find("thuvienphapluat.vn") >= 0:
                            file_name = current_version_path + "/transform/documents_part" + str(
                                get_id_from_url(url)) + ".json.gz"
                        elif current_version_path.find("vbpl.vn") >= 0:
                            file_name = current_version_path + "/transform/documents_part" + str(
                                get_id_from_url__vbpl(url)) + ".json.gz"

                        if check_duplicate:
                            if doc_obj["title"].strip().lower() not in official_number_list_to_check:
                                store_gz(doc_obj, file_name)
                            else:
                                write_to_record(url,
                                                current_version_path + "/vbpl_duplicate.txt",
                                                by_line=True, is_append=True)
                        else:
                            store_gz(doc_obj, file_name)

                        if keep_official_number_record:
                            write_to_record(doc_obj["title"].strip().lower(),
                                            current_version_path + "/official_numbers.txt",
                                            by_line=True, is_append=True)
                    else:
                        if current_version_path.find("thuvienphapluat.vn") >= 0:
                            error_file_name = current_version_path + "/error/error_documents_part" + str(
                                get_id_from_url(url)) + ".txt"
                        elif current_version_path.find("vbpl.vn") >= 0:
                            error_file_name = current_version_path + "/error/error_documents_part" + str(
                                get_id_from_url__vbpl(url)) + ".txt"
                        store_error(is_validate_json(doc_obj), error_file_name)

                except Exception as e:
                    print(future_to_url[future])
                    print(e)


def multithread_with_ouput(method, items, max_workers=20):
    output = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(method, item): item for item in items}

        for future in tqdm(concurrent.futures.as_completed(future_to_item), total=len(future_to_item)):
            item = future_to_item[future]
            try:
                data = future.result()
                if data is not None:
                    output.append(data)
            except Exception as e:
                print(item)
                print(e)

    return output
