from importer.pg_importer.pg_connect import postgreSQL_pool

ps_connection = postgreSQL_pool.getconn()


def get_obj_by_attribute(selected_columns, table, attribute_names, attribute_values):
    cursor = ps_connection.cursor()
    condition = " WHERE "
    for index, attribute_name in enumerate(attribute_names):
        if index == len(attribute_names) - 1:
            condition += attribute_name + " = %s"
        else:
            condition += attribute_name + " = %s AND "
    if len(selected_columns) > 0:
        query = '''SELECT {} FROM {}'''.format(",".join(selected_columns), table) + condition
    else:
        query = '''SELECT * FROM {}'''.format(table) + condition

    cursor.execute(query, tuple(attribute_values))

    return cursor.fetchall()


def restart_seq(table_name):
    cursor = ps_connection.cursor()
    query = ""
    if table_name == "laws_extractivedocument":
        query = '''SELECT MAX(id) FROM laws_extractivedocument;
                    SELECT nextval('laws_extractivedocument_id_seq');
                    BEGIN;
                    LOCK TABLE laws_extractivedocument IN EXCLUSIVE MODE;
                    SELECT setval('laws_extractivedocument_id_seq', COALESCE((SELECT MAX(id)+1 FROM laws_extractivedocument), 1), false);
                    COMMIT;'''
    elif table_name == "laws_documentmetadataterm":
        query = '''SELECT MAX(term_id) FROM laws_documentmetadataterm;
                            SELECT nextval('laws_documentmetadataterm_term_id_seq');
                            BEGIN;
                            LOCK TABLE laws_documentmetadataterm IN EXCLUSIVE MODE;
                            SELECT setval('laws_documentmetadataterm_term_id_seq', COALESCE((SELECT MAX(term_id)+1 FROM laws_documentmetadataterm), 1), false);
                            COMMIT;'''
    elif table_name == "laws_extractivedocumentmetadata":
        query = '''SELECT MAX(meta_id) FROM laws_documentmetadataterm;
                            SELECT nextval('laws_extractivedocumentmetadata_meta_id_seq');
                            BEGIN;
                            LOCK TABLE laws_extractivedocumentmetadata IN EXCLUSIVE MODE;
                            SELECT setval('laws_extractivedocumentmetadata_meta_id_seq', COALESCE((SELECT MAX(meta_id)+1 FROM laws_extractivedocumentmetadata), 1), false);
                            COMMIT;'''
    elif table_name == "laws_relationtype":
        query = '''SELECT MAX(id) FROM laws_relationtype;
                            SELECT nextval('laws_relationtype_id_seq');
                            BEGIN;
                            LOCK TABLE laws_relationtype IN EXCLUSIVE MODE;
                            SELECT setval('laws_relationtype_id_seq', COALESCE((SELECT MAX(id)+1 FROM laws_relationtype), 1), false);
                            COMMIT;'''
    elif table_name == "laws_extractivedocumentschema":
        query = '''SELECT MAX(schema_id) FROM laws_extractivedocumentschema;
                            SELECT nextval('laws_extractivedocumentschema_schema_id_seq');
                            BEGIN;
                            LOCK TABLE laws_extractivedocumentschema IN EXCLUSIVE MODE;
                            SELECT setval('laws_extractivedocumentschema_schema_id_seq', COALESCE((SELECT MAX(schema_id)+1 FROM laws_extractivedocumentschema), 1), false);
                            COMMIT;'''
    cursor.execute(query)
    ps_connection.commit()


def get_columns(table, columns):
    cursor = ps_connection.cursor()
    if len(columns) > 0:
        query = """SELECT {} FROM {}""".format(",".join(columns), table)
    else:
        query = """SELECT * FROM {}""".format(table)
    cursor.execute(query)

    return cursor.fetchall()

#######Function for testing########################################
def view_data():
    ps_cursor = ps_connection.cursor()
    ps_cursor.execute("SELECT COUNT(*) FROM laws_extractivedocument")
    tmp = ps_cursor.fetchone()
    print(tmp[0])


def view_tables():
    cursor = ps_connection.cursor()
    cursor.execute("""SELECT * FROM information_schema.tables
               WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)


def delete():
    cursor = ps_connection.cursor()
    query = '''DELETE FROM public.laws_extractivedocument WHERE doc_id = 1;'''
    cursor.execute(query)
    ps_connection.commit()


def join(): #join extractivedocument + documentmetadataterm + extractivedocumentmetadata
    ps_cursor = ps_connection.cursor()
    ps_cursor.execute('''SELECT laws_extractivedocument.id, laws_extractivedocument.url, 
                                laws_documentmetadataterm.name, laws_extractivedocumentmetadata.term_value 
                      FROM laws_extractivedocument
                      INNER JOIN laws_extractivedocumentmetadata
                      ON laws_extractivedocument.id = laws_extractivedocumentmetadata.extractive_document_id_id
                      INNER JOIN laws_documentmetadataterm
                      ON laws_documentmetadataterm.term_id = laws_extractivedocumentmetadata.term_id_id
                      WHERE laws_extractivedocument.id = 360000''')
    tmp = ps_cursor.fetchall()
    for _tmp in tmp:
        print(_tmp)


def join_2(): #join table extractivedocument + relationtype + schema
    ps_cursor = ps_connection.cursor()
    query = '''with source_table as
                (SELECT laws_extractivedocument.id, laws_extractivedocument.url, laws_extractivedocument.title,
                laws_relationtype.name,laws_extractivedocumentschema.destination_id_id
                                      FROM laws_extractivedocumentschema
                                      INNER JOIN laws_extractivedocument
                                      ON laws_extractivedocument.id = laws_extractivedocumentschema.source_id_id
                                      INNER JOIN laws_relationtype
                                      ON laws_relationtype.id = laws_extractivedocumentschema.relation_type_id_id)
                SELECT * FROM source_table
                                      INNER JOIN laws_extractivedocument
                                      ON laws_extractivedocument.id = source_table.destination_id_id;'''

    ps_cursor.execute(query)
    tmp = ps_cursor.fetchall()
    c = 0
    for _tmp in tmp:
        c += 1
    print(c)
#############################################################################################################

if __name__ == "__main__":
    print(get_obj_by_attribute(selected_columns=["id"],
                               table="laws_extractivedocument",
                               attribute_names=["source_id"],
                               attribute_values=[46935]))
