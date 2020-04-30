import sys
sys.path.append('./')
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

from utilities.reader_helper import load_jsonl_from_gz
from importer.es_import.es_service.es_connection import elasticsearch_connection, insert_doc
from config.config_project import INDEX_LAW, TYPE_DOCUMENT


def index_record(file, id):
    try:
        law_document = load_jsonl_from_gz(file)

        law_document.update({'id': str(id)})
        if (law_document['attribute'] is not None):
            try:
                law_document['attribute']['issued_date'] = datetime.strptime(law_document['attribute']['issued_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["issued_date"] = None
            try:
                law_document['attribute']['effective_date'] = datetime.strptime(law_document['attribute']['effective_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["effective_date"] = None
            try:
                law_document['attribute']['expiry_date'] = datetime.strptime(law_document['attribute']['expiry_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["expiry_date"] = None
            try:
                law_document['attribute']['gazette_date'] = datetime.strptime(law_document['attribute']['gazette_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["gazette_date"] = None
            try:
                law_document['attribute']['enforced_date'] = datetime.strptime(law_document['attribute']['enforced_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["enforced_date"] = None
        tmp = []

        for item in law_document['attribute']['document_field']:
            tmp += item.split(", " or ",")
        law_document['attribute']['document_field'] = tmp

        index_document_law_to_es(law_document)

    except Exception as e:
        print("------------------------------------------------------------------------------")
        print('error: ', e)


def get_gz_path(base_path):
    files = []
    for r, d, f in os.walk(base_path):
        for file in f:
            if '.gz' in file:
                files.append(os.path.join(r, file))
    return files


def load_vbpl(raw_path):
    files = get_gz_path(raw_path)
    executor = ThreadPoolExecutor(max_workers=10)

    for idx, file in enumerate(files[:100]):
        executor.submit(index_record, file, idx)


def index_document_law_to_es(law_document):
    es = elasticsearch_connection
    index = INDEX_LAW
    doc_type = TYPE_DOCUMENT
    id = law_document.get('id')
    insert_doc(es, index, doc_type, id, law_document, verbose=True)


if __name__ == "__main__":
    raw_path = "/home/nguyennam/20200325_155853/transform/"
    print(elasticsearch_connection)
    load_vbpl(raw_path)