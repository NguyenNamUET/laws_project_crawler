from importer.pg_populate.extractive_document_populate import populate__extractive_document_and_extractive_document_metadata__table
from importer.pg_populate.relation_type_populate import populate__relation_type_table
from importer.pg_populate.document_metadata_term_populate import populate__document_metadata_term_table
#from importer.pg_populate.document_schema_populate import populate__document_schema_table

from utilities.reader_helper import load_jsonl_from_gz
import sys
import os


def importer(path):
    VERSION_2 = load_jsonl_from_gz(path+"/"+os.listdir(path)[0])['last_updated_time']
    print("Populate relation type table")
    populate__relation_type_table(VERSION_2)
    print("Populate document metadata term")
    populate__document_metadata_term_table(VERSION_2)

    print("Populate extractive document and extractive document metadata table")
    populate__extractive_document_and_extractive_document_metadata__table(path)

    # print("Populate document schema table")
    # populate__document_schema_table(path)


if __name__ == "__main__":
    data_path = sys.argv
    if len(data_path) > 2:
        print("Only pass transform directory path")
    else:
        importer(data_path[1])
