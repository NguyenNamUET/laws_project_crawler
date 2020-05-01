from importer.pg_importer.pg_populate.extractive_document_populate import populate__extractive_document_and_extractive_document_metadata__table
from importer.pg_importer.pg_populate.relation_type_populate import populate__relation_type_table
from importer.pg_importer.pg_populate.document_metadata_term_populate import populate__document_metadata_term_table
from importer.pg_importer.pg_populate.document_schema_populate import populate__document_schema__table

from importer.es_import.es_populate.vbpl_extractor_json import load_vbpl
from utilities.reader_helper import load_jsonl_from_gz
import sys
import os

def pg_import(path):
    VERSION_2 = load_jsonl_from_gz(path + "/" + os.listdir(path)[0])['last_updated_time']
    print("Populate relation type table")
    populate__relation_type_table(VERSION_2)
    print("Populate document metadata term")
    populate__document_metadata_term_table(VERSION_2)

    print("Populate extractive document and extractive document metadata table")
    populate__extractive_document_and_extractive_document_metadata__table(path)

    print("Populate document schema table")
    populate__document_schema__table(path)


def es_import(path):
    print("Populate Elasticsearch")
    load_vbpl(path)


def run_import_manual(data_path):
    while True:
        choice_input = input("Chọn phương thức import:\n"
                                 "1.Import vào Postgresql\n"
                                 "2.Import vào ElasticSearch\n"
                                 "3.Import cả hai (Postgresql sau đó ElasticSearch)\n"
                                 "Nhập lựa chọn: ")
        if choice_input != "1" and choice_input != "2" and choice_input != "3":
            print("Nhập lại")
        else:
            break

    if choice_input == "1":
        pg_import(data_path)
    elif choice_input == "2":
        es_import(data_path)
    elif choice_input == "3":
        pg_import(data_path)
        es_import(data_path)

    print("Finish!")


def run_import_auto(data_path):
    print("run_import_auto from ", data_path)
    pg_import(data_path)
    es_import(data_path)
    print("Finish!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str,
                        help='''"auto" or "manual"''')
    parser.add_argument("-m", "--mode", action="store_true",
                        help="choose import as auto or manual mode")
    parser.add_argument("path", type=str,
                        help="path of transform folder")
    parser.add_argument("-p", "--path", action="store_true",
                        help="choose path of transform folder")
    args = parser.parse_args()

    if args.mode == "auto":
        run_import_auto(args.path)
    elif args.mode == "manual":
        run_import_manual(args.path)
