import os
import pathlib
import shutil

from utilities.common import to_Date
from utilities.reader_helper import count_file_in_directory, load_record_to_list
from utilities.writer_helper import write_to_record
from utilities.log import give_me_log


def get_latest_version(path):
    dirs = {to_Date(file_name) : path + file_name
                for file_name in os.listdir(path)
                if os.path.isdir(path + file_name + "/transform")}
    if len(dirs) > 0:
        latest_version = max(k for k,v in dirs.items())
        return dirs.get(latest_version)
    else:
        print("get_latest_version(): no past versions available")
        return None


def get_version_with_largest_crawled_document(path):
    dirs = {count_file_in_directory(path + file_name + "/transform") : path + file_name
                for file_name in os.listdir(path)
                if os.path.isdir(path + file_name + "/transform")}
    if len(dirs) > 0:
        largest_crawled_key = max(k for k,v in dirs.items())
        return dirs.get(largest_crawled_key)
    else:
        print("get_version_with_largest_crawled_document(): no past versions available")
        return None


def get_crawled_document_list(path):
    if pathlib.Path(path+"/transform").exists():
        crawled_documents_id = []
        for document_path in os.listdir(path+"/transform"):
            crawled_documents_id.append(document_path.replace("documents_part", "").replace(".json.gz", ""))

        return crawled_documents_id

    else:
        print("get_crawled_document_list() No such file " + path)
        return None


def merge_two_version(version1, version2):
    #merge urls/urls.lines
    new_urls_list = list(
                        set(load_record_to_list(version1+"/urls/urls.lines")
                            + load_record_to_list(version2+"/urls/urls.lines")
                            )
                    )
    shutil.rmtree(version2+"/urls")
    for url in new_urls_list:
        write_to_record(url, version2+"/urls/urls.lines", by_line=True, is_append=True)

    # merge official_numbers.txt
    if not os.path.isfile(version2+"/official_numbers.txt"):
        for official_number in load_record_to_list(version1+"/official_numbers.txt"):
            write_to_record(official_number, version2+"/official_numbers.txt", by_line=True, is_append=True)
    else:
        new_official_number_list = list(
            set(load_record_to_list(version1 + "/official_numbers.txt")
                + load_record_to_list(version2 + "/official_numbers.txt")
                )
        )
        os.remove(version2 + "/official_numbers.txt")
        for url in new_official_number_list:
            write_to_record(url, version2 + "/official_numbers.txt", by_line=True, is_append=True)

    #merge transform
    if not pathlib.Path(version2+"/transform").exists():
        print("Not exist ", version2+"/transform")
        os.makedirs(version2+"/transform", exist_ok=True)
    for item in os.listdir(version1+"/transform"):
        s = os.path.join(version1+"/transform", item)
        d = os.path.join(version2+"/transform", item)
        if os.path.isfile(s):
            shutil.copy2(s, d)

    #merge sitemap
    if pathlib.Path(version1+"/sitemaps").exists():
        for item in os.listdir(version1+"/sitemaps"):
            s = os.path.join(version1+"/sitemaps", item)
            d = os.path.join(version2+"/sitemaps", item)
            if os.path.isfile(s):
                shutil.copyfile(s, d)

    #add merge log
    give_me_log(version2+"/merge.done.txt",(version2+"/urls/urls.lines", version2+"/transform"))


