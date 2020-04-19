from datetime import datetime

VERSION = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "required": [
        "source_id",
        "source",
        "url",
        "title",
        "last_updated_time",
        "html_text",
        "full_text",
        "attribute",
        "schema"
    ],
    "properties": {
        "source_id": {
            "$id": "#/properties/source_id",
            "type": "string",
            "default": "",
        },
        "source": {
            "$id": "#/properties/source",
            "type": "string",
            "default": "",
        },
        "url": {
            "$id": "#/properties/url",
            "type": "string",
            "default": "",
        },
        "title": {
            "$id": "#/properties/title",
            "type": "string",
            "default": "",
        },
        "last_updated_time": {
            "$id": "#/properties/last_updated_time",
            "type": "string",
            "default": "",
        },
        "html_text": {
            "$id": "#/properties/html_text",
            "type": "string",
            "default": "",
        },
        "full_text": {
            "$id": "#/properties/full_text",
            "type": "string",
            "default": "",
        },
        "attribute": {
            "$id": "#/properties/attribute",
            "type": "object",
            "default": {},
            "required": [
                "official_number",
                "document_info",
                "issuing_body/office/signer",
                "document_type",
                "effective_area",
                "collection_source",
                "issued_date",
                "effective_date",
                "enforced_date",
                "expiry_date",
                "the_reason_for_this_expiration",
                "the_reason_for_this_expiration_part",
                "document_field",
                "gazette_date",
                "information_applicable",
                "document_department"
            ],
            "properties": {
                "official_number": {
                    "$id": "#/properties/attribute/properties/official_number",
                    "type": "array",
                    "title": "The Official_number Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/official_number/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "document_info": {
                    "$id": "#/properties/attribute/properties/document_info",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/document_info/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "issuing_body/office/signer": {
                    "$id": "#/properties/attribute/properties/issuing_body/office/signer",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/issuing_body/office/signer/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "document_type": {
                    "$id": "#/properties/attribute/properties/document_type",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/document_type/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "effective_area": {
                    "$id": "#/properties/attribute/properties/effective_area",
                    "type": "string",
                    "default": "",
                },
                "collection_source": {
                    "$id": "#/properties/attribute/properties/collection_source",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/collection_source/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "issued_date": {
                    "$id": "#/properties/attribute/properties/issued_date",
                    "type": "string",
                    "default": "",
                },
                "effective_date": {
                    "$id": "#/properties/attribute/properties/effective_date",
                    "type": "string",
                    "default": "",
                },
                "enforced_date": {
                    "$id": "#/properties/attribute/properties/enforced_date",
                    "type": "string",
                    "default": "",
                },
                "expiry_date": {
                    "$id": "#/properties/attribute/properties/expiry_date",
                    "type": "string",
                    "default": "",
                },
                "the_reason_for_this_expiration": {
                    "$id": "#/properties/attribute/properties/the_reason_for_this_expiration",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/the_reason_for_this_expiration/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "the_reason_for_this_expiration_part": {
                    "$id": "#/properties/attribute/properties/the_reason_for_this_expiration_part",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/the_reason_for_this_expiration_part/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "document_field": {
                    "$id": "#/properties/attribute/properties/document_field",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/document_field/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "gazette_date": {
                    "$id": "#/properties/attribute/properties/gazette_date",
                    "type": "string",
                    "default": "",
                },
                "information_applicable": {
                    "$id": "#/properties/attribute/properties/information_applicable",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/information_applicable/items",
                        "type": "string",
                        "default": "",
                    }
                },
                "document_department": {
                    "$id": "#/properties/attribute/properties/document_department",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/attribute/properties/document_department/items",
                        "type": "string",
                        "default": "",
                    }
                }
            }
        },
        "schema": {
            "$id": "#/properties/schema",
            "type": "object",
            "default": {},
            "required": [
                "instructions_documents",
                "current_documents",
                "instructions_give_documents",
                "canceled_documents",
                "cancel_documents",
                "pursuant_documents",
                "suspended_documents",
                "suspension_documents",
                "reference_documents",
                "other_documents_related",
                "canceled_one_part_documents",
                "cancel_one_part_documents",
                "amended_documents",
                "amend_documents",
                "extended_documents",
                "extend_documents",
                "suspended_one_part_documents",
                "suspension_one_part_documents"
            ],
            "properties": {
                "instructions_documents": {
                    "$id": "#/properties/schema/properties/instructions_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/instructions_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/instructions_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "current_documents": {
                    "$id": "#/properties/schema/properties/current_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/current_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/current_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "instructions_give_documents": {
                    "$id": "#/properties/schema/properties/instructions_give_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/instructions_give_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/instructions_give_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "canceled_documents": {
                    "$id": "#/properties/schema/properties/canceled_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/canceled_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/canceled_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "cancel_documents": {
                    "$id": "#/properties/schema/properties/cancel_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/cancel_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/cancel_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "pursuant_documents": {
                    "$id": "#/properties/schema/properties/pursuant_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/pursuant_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/pursuant_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "suspended_documents": {
                    "$id": "#/properties/schema/properties/suspended_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/suspended_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/suspended_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "suspension_documents": {
                    "$id": "#/properties/schema/properties/suspension_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/suspension_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/suspension_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "reference_documents": {
                    "$id": "#/properties/schema/properties/reference_documents",
                    "type": "array",
                    "default": []
                },
                "other_documents_related": {
                    "$id": "#/properties/schema/properties/other_documents_related",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/other_documents_related/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/other_documents_related/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "canceled_one_part_documents": {
                    "$id": "#/properties/schema/properties/canceled_one_part_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/canceled_one_part_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/canceled_one_part_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "cancel_one_part_documents": {
                    "$id": "#/properties/schema/properties/cancel_one_part_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/cancel_one_part_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/cancel_one_part_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "amended_documents": {
                    "$id": "#/properties/schema/properties/amended_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/amended_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/amended_documents/items/items",
                            "type": "string",
                            "title": "The Items Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                        }
                    }
                },
                "amend_documents": {
                    "$id": "#/properties/schema/properties/amend_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/amend_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/amend_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "extended_documents": {
                    "$id": "#/properties/schema/properties/extended_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/extended_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/extended_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "extend_documents": {
                    "$id": "#/properties/schema/properties/extend_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/extend_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/extend_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "suspended_one_part_documents": {
                    "$id": "#/properties/schema/properties/suspended_one_part_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/suspended_one_part_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/suspended_one_part_documents/items/items",
                            "type": "string",
                            "default": "",
                        }
                    }
                },
                "suspension_one_part_documents": {
                    "$id": "#/properties/schema/properties/suspension_one_part_documents",
                    "type": "array",
                    "default": [],
                    "items": {
                        "$id": "#/properties/schema/properties/suspension_one_part_documents/items",
                        "type": "array",
                        "default": [],
                        "items": {
                            "$id": "#/properties/schema/properties/suspension_one_part_documents/items/items",
                            "type": "string",
                            "default": ""
                        }
                    }
                }
            }
        }
    }
}

VBPL_SITEMAP = {
    'Văn bản quy phạm pháp luật': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=13&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản tiếng Anh':'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=13&IsVietNamese=false&TimTrong1=Title&order=VBPQNgayBanHanh&RowPerPage=50&Page=',
    #'Văn bản hợp nhất': 'http://vbpl.vn//TW/Pages/vbpq-vanbanhopnhat.aspx'

    'Bộ Công an': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=316&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Công Thương': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=218&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Giáo dục và Đào tạo': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=317&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Giao thông vận tải': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=315&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Kế hoạch và Đầu tư': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=312&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ khoa học công nghệ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=213&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Lao động - Thương binh và Xã hội': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=318&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Nội vụ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=320&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Nông nghiệp và Phát triển nông thôn': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=319&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Ngoại giao': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=211&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Quốc phòng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=314&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Tài chính': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=281&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Tài nguyên và Môi trường': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=321&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Tư pháp': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=41&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Thông tin và Truyền thông': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=322&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Văn hóa - Thể thao và Du lịch': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=323&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Xây dựng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=324&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Bộ Y tế': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=325&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Kiểm toán Nhà nước': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=330&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Ngân hàng Nhà nước Việt Nam': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=326&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Tòa án nhân dân tối cao': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=331&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Thanh tra Chính phủ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=327&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Ủy ban Dân tộc': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=328&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn phòng Chính phủ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=329&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Viện kiểm sát nhân dân tối cao': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=332&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',

    'Văn bản pháp luật Tỉnh An Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=229&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bà Rịa - Vũng Tàu': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=230&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bạc Liêu': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=234&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bắc Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=232&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bắc Kạn': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=299&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bắc Ninh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=223&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bến Tre': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=235&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bình Dương': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=237&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bình Định': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=236&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bình Phước': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=238&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Bình Thuận': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=239&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Cà Mau': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=240&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Cao Bằng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=241&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Thành phố Cần Thơ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=285&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Thành phố Đà Nẵng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=308&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Đắk Lắk': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=242&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Đắk Nông': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=243&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Điện Biên': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=302&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Đồng Nai': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=245&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Đồng Tháp': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=246&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Gia Lai': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=247&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hà Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=248&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hà Nam': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=249&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Thành phố Hà Nội': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=305&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&IsMultiDonVi=305&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hà Tĩnh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=221&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hải Dương': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=250&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Thành phố Hải Phòng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=310&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hậu Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=286&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hòa Bình': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=252&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Hưng Yên': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=253&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Kiên Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=297&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Kon Tum': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=256&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Khánh Hòa': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=254&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Lai Châu': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=300&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Lạng Sơn': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=258&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Lào Cai': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=282&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&IsMultiDonVi=282&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Lâm Đồng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=227&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Long An': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=259&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Nam Định': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=260&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Ninh Bình': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=298&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Ninh Thuận': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=222&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Nghệ An': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=226&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Phú Thọ': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=220&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Phú Yên': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=279&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Quảng Bình': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=262&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Quảng Nam': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=263&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Quảng Ninh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=265&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Quảng Ngãi': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=264&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Quảng Trị': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=266&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Sóc Trăng': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=267&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Sơn La': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=268&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Tây Ninh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=269&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Tiền Giang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=274&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Tuyên Quang': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=303&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Thái Bình': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=270&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Thái Nguyên': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=271&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Thanh Hóa': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=272&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Thành phố Hồ Chí Minh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=309&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&IsMultiDonVi=309&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Thừa Thiên Huế': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=301&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Trà Vinh': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=275&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Vĩnh Long': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=277&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Vĩnh Phúc': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=304&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page=',
    'Văn bản pháp luật Tỉnh Yên Bái': 'http://vbpl.vn/VBQPPL_UserControls/Publishing/TimKiem/pKetQuaTimKiem.aspx?dvid=278&IsVietNamese=True&&type=0&stemp=1&TimTrong1=VBPQFulltext&TimTrong1=Title&order=VBPQNgayBanHanh&TypeOfOrder=False&RowPerPage=50&Page='
}