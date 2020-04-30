from importer.pg_importer.pg_operator.pg_insert import insert_table
from constant.crawler_contants import SCHEMA


def produce__document_metadata_term_row(version, schema):
    for attribute in schema["properties"]["attribute"]["required"]:
        name = attribute
        last_updated_time = version

        inserted_record = (name, last_updated_time)

        insert_table("document_metadata_term", inserted_record)


def populate__document_metadata_term_table(version):
    produce__document_metadata_term_row(version, SCHEMA)


