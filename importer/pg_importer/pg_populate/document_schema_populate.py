from utilities.reader_helper import load_jsonl_from_gz, get_content_by_gz

from importer.pg_importer.pg_operator.pg_insert import insert_table
from importer.pg_importer.pg_operator.pg_query import get_obj_by_attribute, restart_seq

from tqdm import tqdm
import os
import re


def produce__row(doc_obj):
    source_id = get_obj_by_attribute(selected_columns=["id"],
                                     table="laws_extractivedocument",
                                     attribute_names=["source_id"],
                                     attribute_values=[doc_obj["source_id"]])[0][0]
    last_updated_time = doc_obj["last_updated_time"]
    for schema_field, schema_values in doc_obj["schema"].items():
        if schema_field != "current_documents" and len(schema_values) > 0:
            for schema in schema_values:
                regex = re.search('(\d)+', schema[1])
                id_index = list(regex.span())
                schema_source_id = schema[1][id_index[0] : id_index[1]]
                destination_obj = get_obj_by_attribute(selected_columns=["id"],
                                                       table="laws_extractivedocument",
                                                       attribute_names=["source_id"],
                                                       attribute_values=[schema_source_id])
                relation_type_obj = get_obj_by_attribute(selected_columns=["id"],
                                                         table="laws_relationtype",
                                                         attribute_names=["name"],
                                                         attribute_values=[schema_field])

                if len(destination_obj) > 0:
                    record = (last_updated_time, destination_obj[0][0], relation_type_obj[0][0], source_id)
                    insert_table("extractive_document_schema", record)


def populate__document_schema__table(data_path):
    restart_seq("laws_extractivedocumentschema")
    for file_path in tqdm(os.listdir(data_path)[:100], total=len(os.listdir(data_path)[:100])):
        if get_content_by_gz(data_path + "/" + file_path) != "":
            doc_obj = load_jsonl_from_gz(data_path + "/" + file_path)
            produce__row(doc_obj)


if __name__ == "__main__":
    obj = load_jsonl_from_gz(
        "/home/nguyennam/Downloads/My project/laws_project_crawler/crawler/vbpl.vn/20200420_003853/transform/documents_part42827.json.gz")
    print(obj)
    produce__row(obj)

