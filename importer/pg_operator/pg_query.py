from importer.pg_connect import postgreSQL_pool

ps_connection = postgreSQL_pool.getconn()


def get_obj_by_attribute(columns, table, attribute_names, attribute_values):
    cursor = ps_connection.cursor()
    condition = " WHERE "
    for index, attribute_name in enumerate(attribute_names):
        if index == len(attribute_names) - 1:
            condition += attribute_name + " = %s"
        else:
            condition += attribute_name + " = %s AND "
    if len(columns) > 0:
        query = '''SELECT {} FROM {}'''.format(",".join(columns), table) + condition
    else:
        query = '''SELECT * FROM {}'''.format(table) + condition


    cursor.execute(query, tuple(attribute_values))

    return cursor.fetchall()


def delete():
    cursor = ps_connection.cursor()
    query = '''DELETE FROM public.laws_extractivedocument WHERE doc_id = 1;'''
    cursor.execute(query)
    ps_connection.commit()


def restart_seq():
    cursor = ps_connection.cursor()
    query = '''SELECT MAX(id) FROM laws_extractivedocument;
                SELECT nextval('laws_extractivedocument_id_seq');
                BEGIN;
                LOCK TABLE laws_extractivedocument IN EXCLUSIVE MODE;
                SELECT setval('laws_extractivedocument_id_seq', COALESCE((SELECT MAX(id)+1 FROM laws_extractivedocument), 1), false);
                COMMIT;'''
    cursor.execute(query)
    ps_connection.commit()


def view_tables():
    cursor = ps_connection.cursor()
    cursor.execute("""SELECT * FROM information_schema.tables
               WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)


def get_columns(table, columns):
    cursor = ps_connection.cursor()
    if len(columns) > 0:
        query = """SELECT {} FROM {}""".format(",".join(columns), table)
    else:
        query = """SELECT * FROM {}""".format(table)
    cursor.execute(query)

    return cursor.fetchall()


def view_data():
    ps_cursor = ps_connection.cursor()
    ps_cursor.execute("SELECT COUNT(*) FROM laws_extractivedocument")
    tmp = ps_cursor.fetchone()
    print(tmp[0])


def join():
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


def join_2():
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


if __name__ == "__main__":
    join_2()
