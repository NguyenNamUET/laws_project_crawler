from importer.pg_importer.pg_operator.pg_insert import insert_table
from constant.crawler_contants import SCHEMA


def produce__relation_type_row(version, schema):
    for s in schema["properties"]["schema"]["properties"].keys():
        relation_name = s
        last_updated_time = version

        inserted_record = (relation_name, last_updated_time)

        insert_table("relation_type", inserted_record)


def populate__relation_type_table(version):
    produce__relation_type_row(version, SCHEMA)


