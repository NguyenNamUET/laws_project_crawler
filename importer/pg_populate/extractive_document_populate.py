from utilities.reader_helper import load_jsonl_from_gz, get_content_by_gz, load_jsonl_from_json
from utilities.writer_helper import store_json
from utilities.common import remove_accents

from importer.pg_operator.pg_insert import insert_table
from importer.pg_operator.pg_query import get_obj_by_attribute, restart_seq

from tqdm import tqdm
import os
import re


def make_sitemap_json(doc_id, doc_title, doc_field):
    sitemap = "/van-ban/" \
              + remove_accents(re.sub("(\-)+", "-", (re.sub("(\s|\/|\.|\:|\,)", "-", str(doc_field))))) + "/" \
              + remove_accents(re.sub("(\s|\/|\.|\:)", "-", str(doc_title))) \
              + "-" + str(doc_id)

    if not os.path.exists('sitemap/sitemaps.json'):
        sitemap_json = {"sitemaps" : []}
    else:
        sitemap_json = load_jsonl_from_json('test/sitemaps.json')

    sitemap_list = sitemap_json["sitemaps"]
    sitemap_list.append(sitemap)
    store_json(sitemap_json, "test/sitemaps.json")

def produce__row(doc_obj):
    source_id = doc_obj["source_id"]
    source = doc_obj["source"]
    url = doc_obj["url"]
    title = doc_obj["title"]
    html_text = doc_obj["html_text"]
    full_text = doc_obj["full_text"]
    last_updated_time = doc_obj["last_updated_time"]
    history = None

    extractive_document_inserted_record = (source_id, source, url, title, history, html_text, full_text, last_updated_time)

    extractive_document_id = insert_table("extractive_document", extractive_document_inserted_record)

    for attribute_name, attribute_value in doc_obj["attribute"].items():
        term_id = ''
        term_value = None
        if attribute_name == "official_number" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["official_number"])[0][0]
            term_value = attribute_value

        elif attribute_name == "document_info" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["document_info"])[0][0]
            term_value = attribute_value

        elif attribute_name == "issuing_body/office/signer" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["issuing_body/office/signer"])[0][0]
            term_value = attribute_value

        elif attribute_name == "document_type" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["document_type"])[0][0]
            term_value = attribute_value

        elif attribute_name == "document_field" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["document_field"])[0][0]
            term_value = attribute_value
            #Make sitemap json for frontend
            if term_value is not None:
                make_sitemap_json(extractive_document_id, title, term_value[0])

        elif attribute_name == "issued_date" and attribute_value != '':
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["issued_date"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "effective_date" and attribute_value != '':
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["effective_date"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "enforced_date" and attribute_value != '':
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["enforced_date"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "the_reason_for_this_expiration" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["the_reason_for_this_expiration"])[0][0]
            term_value = attribute_value

        elif attribute_name == "the_reason_for_this_expiration_part" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["the_reason_for_this_expiration_part"])[0][0]
            term_value = attribute_value

        elif attribute_name == "effective_area" and attribute_value != "":
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["effective_area"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "expiry_date" and attribute_value != '':
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["expiry_date"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "gazette_date" and attribute_value != '':
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["gazette_date"])[0][0]
            term_value = [attribute_value]

        elif attribute_name == "information_applicable" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["information_applicable"])[0][0]
            term_value = attribute_value

        elif attribute_name == "document_department" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["document_department"])[0][0]
            term_value = attribute_value

        elif attribute_name == "collection_source" and len(attribute_value) != 0:
            term_id = get_obj_by_attribute(table="laws_documentmetadataterm",
                                           columns=["term_id"],
                                           attribute_names=["name"],
                                           attribute_values=["collection_source"])[0][0]
            term_value = attribute_value

        if term_id != '' and term_value is not None:
            extractive_document_metadata_record = (extractive_document_id, term_id, term_value, last_updated_time)
            insert_table("extractive_document_metadata", extractive_document_metadata_record)




def populate__extractive_document_and_extractive_document_metadata__table(data_path):
    restart_seq()
    for file_path in tqdm(os.listdir(data_path), total=len(os.listdir(data_path))):
        if get_content_by_gz(data_path + "/" + file_path) != "":
            doc_obj = load_jsonl_from_gz(data_path + "/" + file_path)
            produce__row(doc_obj)

