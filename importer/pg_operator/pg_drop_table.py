from importer.pg_connect import postgreSQL_pool
connection = postgreSQL_pool.getconn()


def drop__extractive_document_table():
    drop_table_query = '''ALTER TABLE laws_extractivedocumentmetadata DROP CONSTRAINT laws_extractivedocum_extractive_document__2bf643e1_fk_laws_extr;
                          ALTER TABLE laws_extractivedocumentschema DROP CONSTRAINT laws_extractivedocum_source_id_id_497758a9_fk_laws_extr;
                          ALTER TABLE laws_extractivedocumentschema DROP CONSTRAINT laws_extractivedocum_destination_id_id_2820c842_fk_laws_extr;
                          DROP TABLE "laws_extractivedocument";'''

    return drop_table_query


def drop__relation_type_table():
    drop_table_query = '''ALTER TABLE laws_extractivedocumentschema DROP CONSTRAINT laws_extractivedocum_relation_type_id_id_6b2bf718_fk_laws_rela;
                          DROP TABLE "laws_relationtype";'''

    return drop_table_query


def drop__extractive_document_metadata_table():
    drop_table_query = '''DROP TABLE "laws_extractivedocumentmetadata";'''

    return drop_table_query


def drop__document_metadata_term_table():
    drop_table_query = '''ALTER TABLE laws_extractivedocumentmetadata DROP CONSTRAINT laws_extractivedocum_term_id_id_3deaebf2_fk_laws_docu;
                          ALTER TABLE laws_selfdrafteddocumentmetadata DROP CONSTRAINT laws_selfdrafteddocu_term_id_id_4ab48a70_fk_laws_docu;
                          DROP TABLE "laws_documentmetadataterm";'''

    return drop_table_query


def drop__extractive_document_schema_table():
    drop_table_query = '''DROP TABLE "laws_extractivedocumentschema";'''
    return drop_table_query


def drop__selfdrafted_document_table():
    drop_table_query = '''ALTER TABLE laws_selfdrafteddocumentmetadata DROP CONSTRAINT laws_selfdrafteddocu_self_drafted_documen_1aa53c3f_fk_laws_self;
                          DROP TABLE "laws_selfdrafteddocument";'''
    return drop_table_query


def drop__selfdrafted_document_metadata_table():
    drop_table_query = '''DROP TABLE "laws_selfdrafteddocumentmetadata";'''
    return drop_table_query


def drop_table(table_name):
    cursor = connection.cursor()

    if table_name == "extractive_document":
        cursor.execute(drop__extractive_document_table())
    elif table_name == "relation_type":
        cursor.execute(drop__relation_type_table())
    elif table_name == "extractive_document_metadata":
        cursor.execute(drop__extractive_document_metadata_table())
    elif table_name == "document_metadata_term":
        cursor.execute(drop__document_metadata_term_table())
    elif table_name == "extractive_document_schema":
        cursor.execute(drop__extractive_document_schema_table())
    elif table_name == "selfdrafted_document":
        cursor.execute(drop__selfdrafted_document_table())
    elif table_name == "selfdrafted_document_metadata":
        cursor.execute(drop__selfdrafted_document_metadata_table())

    connection.commit()
    print("Table " + table_name + " dropped successfully in PostgreSQL")


if __name__ == "__main__":
    drop_table("document_metadata_term")
    drop_table("extractive_document")
    #drop_table("selfdrafted_document")
    drop_table("relation_type")

    drop_table("extractive_document_schema")
    drop_table("extractive_document_metadata")
    #drop_table("selfdrafted_document_metadata")
