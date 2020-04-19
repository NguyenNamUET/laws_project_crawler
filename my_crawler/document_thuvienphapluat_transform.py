from my_crawler.url_helper import load_url, get_id_from_url
from utilities.common import extract_raw_text_from_html
from constant.crawler_contants import VERSION


def get_document_content(soup):
    if soup.find("div", attrs={"class": "TaiVanBan"}) is None \
       and soup.find("a", attrs={"style": "color:blue", "class":"clsopentLogin"}) is None:
        #Loại trừ các văn bản không thể xem được
        content = soup.find("div", attrs={"class": "content1"})
        for p_tag in content.find_all(True):
            del p_tag["href"]
        return str(content)
    else:
        return ""


def get_document_attributes_from_ajax(url_id):
    url = "https://thuvienphapluat.vn/AjaxLoadData/LoadLuocDo.aspx?LawID=" + url_id
    try:
        soup = load_url(url, return_content=True)
        atts = {}
        atts['Mô tả'] = soup.find("div", attrs={"class": "tt"}).text.strip() #None type has no "text"

        for att_soup in soup.find_all("div", attrs={"class": "att"}):
            att_name = att_soup.find("div", attrs={"class": "hd fl"}).text.strip().replace(":", "")
            att_value = att_soup.find("div", attrs={"class": "ds fl"}).text.strip()

            atts[att_name] = att_value

        return atts

    except Exception as e:
        print("get_document_attributes_from_ajax error: " + str(e) + " at " + str(url))


def modify_document_attribute(doc_attribute):
    new_atts = {}
    new_atts["official_number"] = [doc_attribute.get("Số hiệu", "")]
    new_atts["document_info"] = [doc_attribute.get('Mô tả', ""),
                                 "Tình trạng: " + doc_attribute.get("Tình trạng", "")]
    new_atts["issuing_body/office/signer"] = [doc_attribute.get("Nơi ban hành", ""),
                                              "",
                                              doc_attribute.get("Người ký", "")]
    new_atts["document_type"] = [doc_attribute.get("Loại văn bản", "")]
    new_atts["document_field"] = [doc_attribute.get("Lĩnh vực, ngành", "")]

    new_atts["issued_date"] = doc_attribute.get("Ngày ban hành", "")
    new_atts["effective_date"] = doc_attribute.get("Ngày hiệu lực", "")
    new_atts["enforced_date"] = doc_attribute.get("Ngày đăng", "")

    #extra atts
    new_atts["the_reason_for_this_expiration"] = []
    new_atts["the_reason_for_this_expiration_part"] = []
    new_atts["effective_area"] = ""
    new_atts["expiry_date"] = ""
    new_atts["gazette_date"] = ""
    new_atts["information_applicable"] = []
    new_atts["document_department"] = []
    new_atts["collection_source"] = []

    return new_atts


def scrapy_thuvienphapluat(url):
    try:
        doc_content = load_url(url, return_content=True)

        extracted_source_id = get_id_from_url(url)
        extracted_attributes = modify_document_attribute(get_document_attributes_from_ajax(get_id_from_url(url)))
        extracted_title = extracted_attributes["document_type"][0].strip() + " " + extracted_attributes["official_number"][0].strip()
        extracted_html_text = get_document_content(doc_content)
        if extracted_html_text == '':
            print("No content at " + url)

        extracted_full_text = extract_raw_text_from_html(extracted_html_text)

        doc_object = {
                        "source_id" : extracted_source_id,
                        "source" : "thuvienphapluat.vn",
                        "url": url,
                        "title" : extracted_title,
                        "html_text": extracted_html_text,
                        "last_updated_time": VERSION,
                        "full_text" : extracted_full_text,
                        "attribute": extracted_attributes,
                        "schema" : {
                                    "instructions_documents" : [], #Văn bản được HD, QĐ chi tiết (from http://vbpl.vn/)
                                    "current_documents" : [], #Văn bản hiện thời (from http://vbpl.vn/)
                                    "instructions_give_documents" : [], #Văn bản HD, QĐ chi tiết (from http://vbpl.vn/)
                                    "canceled_documents" : [], #Văn bản hết hiệu lực (from http://vbpl.vn/)
                                    "cancel_documents" : [], #Văn bản quy định hết hiệu lực (from http://vbpl.vn/)
                                    "pursuant_documents": [],  # Văn bản căn cứ (from http://vbpl.vn/)
                                    "suspended_documents" : [], #Văn bản bị đình chỉ (from http://vbpl.vn/)
                                    "suspension_documents": [],  # Văn bản đình chỉ (from http://vbpl.vn/)
                                    "reference_documents" : [], #Văn bản dẫn chiếu (from http://vbpl.vn/)
                                    "other_documents_related": [],  # Văn bản liên quan khác (from http://vbpl.vn/)
                                    "canceled_one_part_documents" : [], #Văn bản bị đình chỉ 1 phần (from http://vbpl.vn/)
                                    "cancel_one_part_documents" : [], #Văn bản đình chỉ 1 phần (from http://vbpl.vn/)
                                    "amended_documents" : [], # Văn bản được sửa đổi (from http://vbpl.vn/)
                                    "amend_documents" : [], #Văn bản sửa đổi (from http://vbpl.vn/)
                                    "extended_documents": [], #Văn bản được bổ sung (from http://vbpl.vn/)
                                    "extend_documents" : [],  #Văn bản bổ sung (from http://vbpl.vn/)
                                    "suspended_one_part_documents": [],  # Văn bản bị đình chỉ 1 phần(from http://vbpl.vn/)
                                    "suspension_one_part_documents": [],  # Văn bản đình chỉ 1 phần(from http://vbpl.vn/)
                                     }
                         }

        return doc_object
    except Exception as e:
        print("scrapy_thuvienphapluat() error: ", e)


if __name__ == "__main__":
    doc_obj = scrapy_thuvienphapluat("https://thuvienphapluat.vn/TCVN/Tai-nguyen-Moi-truong/QCVN-18-2019-BTNMT-Du-bao-canh-bao-lu-918505.aspx")
    print(doc_obj)