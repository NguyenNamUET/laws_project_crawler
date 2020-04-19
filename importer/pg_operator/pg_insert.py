from importer.pg_connect import postgreSQL_pool
ps_connection = postgreSQL_pool.getconn()


def insert__document_metadata_term_table():
    insert_table_query = '''INSERT INTO public.laws_documentmetadataterm(
                                name, last_update_time)
                            VALUES (%s, %s)
                            ON CONFLICT (name) DO UPDATE
                                SET name = EXCLUDED.name,
                                    last_update_time = EXCLUDED.last_update_time;
                            '''
    return insert_table_query


def insert__extractive_document_table():
    insert_table_query = '''INSERT INTO public.laws_extractivedocument(
                                source_id, source, url, title, history, html_text, full_text, last_update_time)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (source_id) DO UPDATE
                                SET source_id = EXCLUDED.source_id,
                                    source = EXCLUDED.source,
                                    url = EXCLUDED.url,
                                    title = EXCLUDED.title,
                                    history = EXCLUDED.history,
                                    html_text = EXCLUDED.html_text,
                                    full_text = EXCLUDED.full_text,
                                    last_update_time = EXCLUDED.last_update_time
                            RETURNING id;'''

    return insert_table_query


def insert__extractive_document_metadata_table():
    insert_table_query = '''INSERT INTO public.laws_extractivedocumentmetadata(
                                extractive_document_id_id, term_id_id, term_value, last_update_time)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (extractive_document_id_id, term_id_id) DO UPDATE
                                SET extractive_document_id_id = EXCLUDED.extractive_document_id_id,
                                    term_id_id = EXCLUDED.term_id_id,
                                    term_value = EXCLUDED.term_value,
                                    last_update_time = EXCLUDED.last_update_time;
	                        '''

    return insert_table_query


def insert__relation_type_table():
    insert_table_query = '''INSERT INTO public.laws_relationtype(
	                            name, last_update_time)
	                        VALUES (%s, %s)
	                        ON CONFLICT (name) DO UPDATE
                                SET name = EXCLUDED.name,
                                    last_update_time = EXCLUDED.last_update_time;'''

    return insert_table_query


def insert__extractive_document_schema_table():
    insert_table_query = '''INSERT INTO public.laws_extractivedocumentschema(
                                last_update_time, destination_id_id, relation_type_id_id, source_id_id)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (destination_id_id, relation_type_id_id, source_id_id) DO UPDATE
                                SET destination_id_id = EXCLUDED.destination_id_id,
                                    relation_type_id_id = EXCLUDED.relation_type_id_id,
                                    source_id_id = EXCLUDED.source_id_id,
                                    last_update_time = EXCLUDED.last_update_time;
                                    '''

    return insert_table_query


def insert_table(table_name, inserted_record):
    cursor = ps_connection.cursor()

    if table_name == "extractive_document":
        cursor.execute(insert__extractive_document_table(), inserted_record)
        ps_connection.commit()

        return cursor.fetchone()[0]

    elif table_name == "relation_type":
        cursor.execute(insert__relation_type_table(), inserted_record)
        ps_connection.commit()

    elif table_name == "extractive_document_metadata":
        cursor.execute(insert__extractive_document_metadata_table(), inserted_record)
        ps_connection.commit()

    elif table_name == "document_metadata_term":
        cursor.execute(insert__document_metadata_term_table(), inserted_record)
        ps_connection.commit()

    elif table_name == "extractive_document_schema":
        cursor.execute(insert__extractive_document_schema_table(), inserted_record)
        ps_connection.commit()