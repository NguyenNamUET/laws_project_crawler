from my_crawler.crawler_helper.sitemap_helper import get_all_sitemaps_url, get_all_document_url, get_url_from_page__vbpl
from my_crawler.crawler_helper.multithread_helper import multithread_crawl_with_batch, multithread_with_ouput
from my_crawler.crawler_helper.url_helper import load_url, get_id_from_url, get_id_from_url__vbpl
from my_crawler.transformer.document_vbpl_transform import get_page_count

from utilities.writer_helper import write_to_record
from utilities.common import second_to_hhmmss, countdown
from utilities.version_control import get_latest_version, get_version_with_largest_crawled_document, \
    get_crawled_document_list, merge_two_version
from utilities.reader_helper import load_record_to_list
from utilities.log import give_me_log

from constant.crawler_contants import VERSION, VBPL_SITEMAP
import time
import re
import os
import shutil
from tqdm import tqdm
from datetime import datetime


def store_sitemaps_and_urls__vbpl(root_path):
    start = time.time()

    for index, (name, url) in enumerate(list(VBPL_SITEMAP.items())[45:46]):
        page_per_sitemap = get_page_count(url)
        page_urls = []
        for page in range(page_per_sitemap):
            page_url = url + str(page + 1) + "&view_adult=true"
            page_urls.append(page_url)
        doc_urls_per_page_list = multithread_with_ouput(get_url_from_page__vbpl,
                                                        page_urls)  # [[urls of page1], [url of page2],...]
        for url_list in doc_urls_per_page_list:
            for url in url_list:
                write_to_record(url, root_path + "/urls/urls.lines", by_line=True, is_append=True)

    timer = time.time() - start
    print("Elapsed Time multithread(): %ss" % timer)

    return second_to_hhmmss(timer)


def store_sitemaps_and_urls__thuvienphapluat(root_path):  # , sitemap_dir, url_file
    start = time.time()
    sitemap_urls = get_all_sitemaps_url("https://thuvienphapluat.vn/sitemap.xml")
    for sitemap_url in tqdm(sitemap_urls[10:11], total=len(sitemap_urls[10:11])):
        file_name = root_path + "/sitemaps/sitemaps_part" + re.findall("(\d+)", sitemap_url)[0] + ".xml"
        write_to_record(load_url(sitemap_url, return_content=True).prettify(), file_name)
        document_urls = get_all_document_url(sitemap_url)

        for document_url in document_urls:
            write_to_record(document_url, root_path + "/urls/urls.lines", by_line=True, is_append=True)

    timer = time.time() - start
    # print("Elapsed Time multithread(): %ss" % timer)

    return second_to_hhmmss(timer)


def get_uncrawled_urls_compared_to_version(version_path, current_version):
    crawled_urls_id_from_version = get_crawled_document_list(version_path)
    if crawled_urls_id_from_version is not None:
        current_urls_path = "/".join(version_path.split("/")[:-1]) + "/" + current_version + "/urls/urls.lines"
        #print("current_urls_path: ", current_urls_path)
        current_pending_urls_id = {}
        if current_urls_path.find("thuvienphapluat.vn") >= 0:
            current_pending_urls_id = {get_id_from_url(url): url for url in load_record_to_list(current_urls_path)}
        elif current_urls_path.find("vbpl.vn") >= 0:
            current_pending_urls_id = {get_id_from_url__vbpl(url): url for url in
                                       load_record_to_list(current_urls_path)}

        uncrawled_urls = []
        print("Đang so sánh với " + version_path + "...")
        for id, url in tqdm(current_pending_urls_id.items(), total=len(current_pending_urls_id)):
            if id not in crawled_urls_id_from_version:
                uncrawled_urls.append(current_pending_urls_id.get(id))

        #print("Số lượng văn bản chưa crawl: ", str(len(uncrawled_urls)))
        return uncrawled_urls

    else:
        return None


def crawl(root_path, version, keep_record, check_duplicate,
          record_to_check_file=None, mode="manual"):
    url_list = []
    choosen_version = None

    # MANUAL MODE
    if mode == "manual":
        while True:
            choice_input = input("Chọn phương thức crawl:\n"
                                 "1.Crawl theo version mới nhất \n"
                                 "2.Crawl theo version mới nhất + nhiều văn bản crawl được nhất \n"
                                 "3.Crawl theo version ưa thích (<path>/version)\n"
                                 "4.Crawl lại từ đầu \n"
                                 "Nhập lựa chọn: ")
            if choice_input != "1" and choice_input != "2" and choice_input != "3" and choice_input != "4":
                print("Nhập lại")
            else:
                break

        if choice_input == "1":
            choosen_version = get_latest_version(root_path)
            if choosen_version is not None:
                url_list = get_uncrawled_urls_compared_to_version(choosen_version,
                                                                  current_version=version)
                if check_duplicate and os.path.exists(choosen_version + "/vbpl_duplicate.txt"):
                    duplicate_list = load_record_to_list(choosen_version + "/vbpl_duplicate.txt")
                    url_list = [url for url in url_list if url not in duplicate_list]
            else:
                print("Không tìm thầy version mới nhất, crawl lại từ đầu")
                url_list = load_record_to_list(root_path + version + "/urls/urls.lines")

        elif choice_input == "2":
            choosen_version = get_version_with_largest_crawled_document(root_path)
            if choosen_version is not None:
                url_list = get_uncrawled_urls_compared_to_version(choosen_version,
                                                                  current_version=version)
                if check_duplicate and os.path.exists(choosen_version + "/vbpl_duplicate.txt"):
                    duplicate_list = load_record_to_list(choosen_version + "/vbpl_duplicate.txt")
                    url_list = [url for url in url_list if url not in duplicate_list]
            else:
                print("Không tìm thầy version mới nhất, crawl lại từ đầu")
                url_list = load_record_to_list(root_path + version + "/urls/urls.lines")

        elif choice_input == "3":
            path_input = input("Nhập địa chỉ đến version ưa thích: ")
            choosen_version = path_input
            url_list = get_uncrawled_urls_compared_to_version(choosen_version,
                                                              current_version=version)

        elif choice_input == "4":
            url_list = load_record_to_list(root_path + version + "/urls/urls.lines")
    #################################################################################################

    # AUTO MODE
    elif mode == "auto":
        choosen_version = get_latest_version(root_path)
        if choosen_version is not None:
            url_list = get_uncrawled_urls_compared_to_version(choosen_version,
                                                              current_version=version)
            if check_duplicate and os.path.exists(choosen_version + "/vbpl_duplicate.txt"):
                duplicate_list = load_record_to_list(choosen_version + "/vbpl_duplicate.txt")
                url_list = [url for url in url_list if url not in duplicate_list]

        else:
            print("Không tìm thầy version mới nhất, crawl lại từ đầu")
            url_list = load_record_to_list(root_path + version + "/urls/urls.lines")
    ################################################################################################
    timer2 = 0
    if url_list is not None and len(url_list) > 0:
        print("Đang crawl văn bản pháp luật...", len(url_list))
        start = time.time()

        multithread_crawl_with_batch(document_urls=url_list,
                                     current_version_path=root_path + version,
                                     keep_official_number_record=keep_record,
                                     check_duplicate=check_duplicate,
                                     record_to_check_file=record_to_check_file)

        timer2 = time.time() - start

        if choosen_version is not None:
            print("Đang merge version...")
            if mode == "manual":
                while True:
                    merge_input = input("Merge với version: " + str(choosen_version) + " (Y/N?):")
                    if merge_input != "Y" and merge_input != "y" and merge_input != "N" and merge_input != "n":
                        print("Nhập lại")
                        continue
                    else:
                        if merge_input == "Y" or merge_input == "y":
                            merge_two_version(choosen_version, root_path + version)
                        break

            elif mode == "auto":
                merge_two_version(choosen_version, root_path + version)

    else:
        shutil.rmtree(root_path + version)

    return second_to_hhmmss(timer2), (len(url_list) if url_list is not None else int(0))


def run_crawl_auto(import_after_finished=False):
    global VERSION
    while True:  # remove loop for manual
        FILE_VERSION = str(VERSION)[:10].replace("-", "") + "_" + str(VERSION)[11:19].replace(":", "")
        THUVIENPHAPLUAT_ROOTPATH = "/home/nguyennam/Downloads/My project/laws_project_crawler/crawler/thuvienphapluat.vn/"
        VBPL_ROOTPATH = "/home/nguyennam/Downloads/My project/laws_project_crawler/crawler/vbpl.vn/"

        print("Đang crawl sitemap và url thuvienphapluat.vn...")
        timer_extract_first = store_sitemaps_and_urls__thuvienphapluat(THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION)
        timer_crawl_first, is_sleppy_1 = crawl(root_path=THUVIENPHAPLUAT_ROOTPATH,
                                               version=FILE_VERSION,
                                               keep_record=True,
                                               check_duplicate=False,
                                               mode="auto")  # change to "manual" for manual
        print("\nĐang crawl sitemap và url vbpl.vn...")
        give_me_log(THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION+"/crawl_thuvienphapluat.done.txt",
                    (THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION+"/urls/urls.lines",
                     THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION+"/transform",
                     timer_extract_first, timer_crawl_first))
        LIST_OF_THUVIENPHAPLUAT__OFFICIAL_NUMBERS_PATH = get_latest_version(THUVIENPHAPLUAT_ROOTPATH) + "/official_numbers.txt"
        timer_extract_second = store_sitemaps_and_urls__vbpl(VBPL_ROOTPATH+FILE_VERSION)
        timer_crawl_second, is_sleppy_2 = crawl(root_path=VBPL_ROOTPATH,
                                                version=FILE_VERSION,
                                                keep_record=True,
                                                record_to_check_file=LIST_OF_THUVIENPHAPLUAT__OFFICIAL_NUMBERS_PATH,
                                                check_duplicate=True,
                                                mode="auto")  # change to "manual" for manual
        give_me_log(VBPL_ROOTPATH+FILE_VERSION+"/crawl_vbpl.done.txt",
                    (VBPL_ROOTPATH+FILE_VERSION+"/urls/urls.lines",
                     VBPL_ROOTPATH+FILE_VERSION+"/transform",
                     timer_extract_second, timer_crawl_second))

        if import_after_finished:
            from import_data import run_import_auto
            print("Đang import thuvienphapluat.vn...")
            run_import_auto(THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION)
            print("Đang import vbpl.vn...")
            run_import_auto(VBPL_ROOTPATH+FILE_VERSION)

        if is_sleppy_1 == 0 or is_sleppy_2 == 0:
            print("Đang ngủ...")
            countdown(10) #sleep for 2 days

        VERSION = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def run_crawl_manual():
    FILE_VERSION = str(VERSION)[:10].replace("-", "") + "_" + str(VERSION)[11:19].replace(":", "")
    THUVIENPHAPLUAT_ROOTPATH = "/home/nguyennam/Downloads/My project/laws_project_crawler/crawler/thuvienphapluat.vn/"
    VBPL_ROOTPATH = "/home/nguyennam/Downloads/My project/laws_project_crawler/crawler/vbpl.vn/"

    print("Đang crawl sitemap và url...")
    timer_extract_first = store_sitemaps_and_urls__thuvienphapluat(THUVIENPHAPLUAT_ROOTPATH+FILE_VERSION)
    timer_crawl_first, is_sleppy_1 = crawl(root_path=THUVIENPHAPLUAT_ROOTPATH,
                                           version=FILE_VERSION,
                                           keep_record=True,
                                           check_duplicate=False,
                                           mode="manual")  # change to "manual" for manual
    print("\nĐang crawl sitemap và url...")
    give_me_log(THUVIENPHAPLUAT_ROOTPATH + FILE_VERSION + "/crawl_thuvienphapluat.done.txt",
                (THUVIENPHAPLUAT_ROOTPATH + FILE_VERSION + "/urls/urls.lines",
                 THUVIENPHAPLUAT_ROOTPATH + FILE_VERSION + "/transform",
                 timer_extract_first, timer_crawl_first))
    LIST_OF_THUVIENPHAPLUAT__OFFICIAL_NUMBERS_PATH = get_latest_version(
        THUVIENPHAPLUAT_ROOTPATH) + "/official_numbers.txt"
    timer_extract_second = store_sitemaps_and_urls__vbpl(VBPL_ROOTPATH+FILE_VERSION)
    timer_crawl_second, is_sleppy_2 = crawl(root_path=VBPL_ROOTPATH,
                                            version=FILE_VERSION,
                                            keep_record=True,
                                            record_to_check_file=LIST_OF_THUVIENPHAPLUAT__OFFICIAL_NUMBERS_PATH,
                                            check_duplicate=True,
                                            mode="manual")  # change to "manual" for manual
    give_me_log(VBPL_ROOTPATH + FILE_VERSION + "/crawl_vbpl.done.txt",
                (VBPL_ROOTPATH + FILE_VERSION + "/urls/urls.lines",
                 VBPL_ROOTPATH + FILE_VERSION + "/transform",
                 timer_extract_second, timer_crawl_second))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str,
                        help='''"auto" or "manual"''')
    parser.add_argument("-m", "--mode", action="store_true",
                        help="choose crawl as auto or manual mode")
    args = parser.parse_args()

    if args.mode == "auto":
        run_crawl_auto()
    elif args.mode == "manual":
        run_crawl_manual()