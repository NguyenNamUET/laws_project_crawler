from my_crawler.url_helper import load_url, get_id_from_url__vbpl
from utilities.common import extract_raw_text_from_html
from constant.crawler_contants import VERSION

import math
import re


def get_page_count(url):
    soup = load_url(url, return_content=True)
    result = int(soup.find("a", attrs={"class": "selected"}).span.strong.b.text)
    return math.ceil(result / 50)


def get_document_content_and_title(content_url):
    soup = load_url(content_url, return_content=True)
    bm = soup.find("div", attrs={"class": "box-map"})
    title = bm.find_all("a")[-1].text.strip()

    if content_url.find("van-ban-goc") > 0:
        return ("", title)
    else:
        content = soup.find("div", attrs={"class": "fulltext"})
        content = content.find_all("div")[1]
        for p_tag in content.find_all(True):
            del p_tag["href"]

        return (str(content), title)


def get_document_attributes(attribute_url):
    soup = load_url(attribute_url, return_content=True)
    attribute_page_soup = soup.find("div", attrs={"class": "vbProperties"})
    if attribute_page_soup is not None:
        atts = {}

        expiry_date_soup = soup.find("div", attrs={"class": "vbInfo"}).find_all("li")
        if expiry_date_soup[-1].text.find("Ngày hết hiệu lực") > 0:
            atts["Ngày hết hiệu lực"] = expiry_date_soup.text.replace("Ngày hết hiệu lực:", "").strip()

        for att_soup in attribute_page_soup.find_all("td"):
            if att_soup.has_attr("class") and att_soup["class"][0] == "title" and att_soup.text.find(
                    "Tình trạng hiệu lực") < 0:
                atts["Mô tả"] = att_soup.text.strip()

            elif att_soup.has_attr("class") and att_soup["class"][0] == "title" and att_soup.text.find(
                    "Tình trạng hiệu lực") >= 0:
                atts["Tình trạng"] = att_soup.text.replace("Tình trạng hiệu lực:", "").strip()

            elif att_soup.has_attr("class") and att_soup["class"][0] == "label":
                if att_soup.text.strip() == "Cơ quan ban hành/ Chức danh / Người ký" or att_soup.text.strip() == "Issuing body/ Office/ Signer":
                    atts[att_soup.text.strip()] = []
                    for value in att_soup.find_all_next("td")[:3]:
                        atts[att_soup.text.strip()].append(value.text.strip())
                else:
                    atts[att_soup.text.strip()] = att_soup.find_next("td").text.strip()

        return atts

    else:
        return {}


def modify_document_attribute(doc_attribute, isVN=True):
    new_atts = {}
    if isVN:
        new_atts["official_number"] = [doc_attribute.get("Số ký hiệu", "")]
        new_atts["document_info"] = [doc_attribute.get('Mô tả', ""),
                                     "Tình trạng: " + doc_attribute.get("Tình trạng", "")]
        new_atts["issuing_body/office/signer"] = doc_attribute.get("Cơ quan ban hành/ Chức danh / Người ký", [])
        new_atts["document_type"] = [doc_attribute.get("Loại văn bản", "")]
        new_atts["effective_area"] = doc_attribute.get("Phạm vi", "")
        new_atts["collection_source"] = [doc_attribute.get("Nguồn thu thập", "")]

        new_atts["issued_date"] = doc_attribute.get("Ngày ban hành", "")
        new_atts["effective_date"] = doc_attribute.get("Ngày có hiệu lực", "")
        new_atts["enforced_date"] = doc_attribute.get("Ngày đăng công báo", "")
        new_atts["expiry_date"] = doc_attribute.get("Ngày hết hiệu lực", "")
        # extra atts
        new_atts["the_reason_for_this_expiration"] = [doc_attribute.get("Lí do hết hiệu lực", "")]
        new_atts["the_reason_for_this_expiration_part"] = []
        new_atts["document_field"] = []

        new_atts["gazette_date"] = ""
        new_atts["information_applicable"] = []
        new_atts["document_department"] = []

        return new_atts


def get_document_schema(schema_url):
    soup = load_url(schema_url, return_content=True)
    if soup.find("div", attrs={"class": "vbLuocdo"}) is not None:
        schemas = {}

        for schema in soup.find_all("div", attrs={"class": "luocdo"}):
            key = schema.find("div", attrs={"class": ["title", "titleht"]}).find_all("a")[-1].text.strip()
            value = []

            for schema_value in schema.find_all("a", attrs={"class": "jTips"}):
                if schema_value["href"] == "#":
                    name = re.sub("( {2,})", "", schema_value.text).replace("\r\n", " ").strip()
                else:
                    name = re.sub("( {2,})", "", schema_value["title"]).replace("\r\n", " ").strip()
                url = "http://vbpl.vn/" + schema_value["href"].strip()
                if [name, url] not in value:
                    value.append([name, url])

            schemas[key] = value

        return schemas

    else:
        return {}


def modify_document_schema(doc_schema, isVN=True):
    new_schema = {}
    if isVN:
        new_schema["instructions_documents"] = doc_schema.get("Văn bản được HD, QĐ chi tiết", [])
        new_schema["current_documents"] = doc_schema.get("Văn bản hiện thời", [])
        new_schema["instructions_give_documents"] = doc_schema.get("Văn bản HD, QĐ chi tiết", [])
        new_schema["canceled_documents"] = doc_schema.get("Văn bản hết hiệu lực", [])
        new_schema["cancel_documents"] = doc_schema.get("Văn bản quy định hết hiệu lực", [])
        new_schema["pursuant_documents"] = doc_schema.get("Văn bản căn cứ", [])
        new_schema["suspended_documents"] = doc_schema.get("Văn bản bị đình chỉ", [])
        new_schema["suspension_documents"] = doc_schema.get("Văn bản đình chỉ", [])
        new_schema["reference_documents"] = doc_schema.get("Văn bản dẫn chiếu", [])
        new_schema["other_documents_related"] = doc_schema.get("Văn bản liên quan khác", [])
        new_schema["canceled_one_part_documents"] = doc_schema.get("Văn bản bị đình chỉ 1 phần", [])
        new_schema["cancel_one_part_documents"] = doc_schema.get("Văn bản đình chỉ 1 phần", [])
        new_schema["amended_documents"] = doc_schema.get("Văn bản được sửa đổi", [])
        new_schema["amend_documents"] = doc_schema.get("Văn bản sửa đổi", [])
        new_schema["extended_documents"] = doc_schema.get("Văn bản được bổ sung", [])
        new_schema["extend_documents"] = doc_schema.get("Văn bản bổ sung", [])
        new_schema["suspended_one_part_documents"] = doc_schema.get("Văn bản bị đình chỉ 1 phần", [])
        new_schema["suspension_one_part_documents"] = doc_schema.get("Văn bản đình chỉ 1 phần", [])

        return new_schema


def scrapy_vbpl(url):
    try:
        extracted_source_id = get_id_from_url__vbpl(url)
        extracted_attributes = modify_document_attribute(get_document_attributes("http://vbpl.vn/tw/Pages/vbpq-thuoctinh.aspx?dvid=13&ItemID="+str(extracted_source_id)+"&Keyword=&view_adult=true"))
        extracted_schema = modify_document_schema(get_document_schema("http://vbpl.vn/TW/Pages/vbpq-luocdo.aspx?ItemID="+str(extracted_source_id)+"&Keyword=&view_adult=true"))
        extracted_html_text, extracted_title = get_document_content_and_title(url)
        # if extracted_html_text == '':
        #     print("No content at " + url)

        extracted_full_text = extract_raw_text_from_html(extracted_html_text)

        doc_object = {
                      "source_id": extracted_source_id,
                      "source": "vbpl.vn",
                      "url": url,
                      "title": extracted_title,
                      "last_updated_time": VERSION,
                      "html_text": extracted_html_text,
                      "full_text": extracted_full_text,
                      "attribute": extracted_attributes,
                      "schema": extracted_schema,
                      }

        return doc_object

    except Exception as e:
        print("scrapy_vbpl() error: ", e)
