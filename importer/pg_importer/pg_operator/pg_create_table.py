from importer.pg_importer.pg_connect import postgreSQL_pool

connection = postgreSQL_pool.getconn()


def create___document_metadata_term_table():
    create_table_query = '''CREATE TABLE public.laws_documentmetadataterm
                            (
                                term_id bigserial NOT NULL,
                                name character varying(255) COLLATE pg_catalog."default" NOT NULL UNIQUE,
                                last_update_time timestamp without time zone NOT NULL,
                                CONSTRAINT laws_documentmetadataterm_pkey PRIMARY KEY (term_id),
                                CONSTRAINT laws_documentmetadataterm_name_key UNIQUE (name)
                            )'''

    return create_table_query


def create__extractive_document_table():
    create_table_query = '''CREATE TABLE public.laws_extractivedocument
                            (
                                id bigserial NOT NULL,
                                source_id bigint NOT NULL UNIQUE,
                                source character varying(225) COLLATE pg_catalog."default" NOT NULL,
                                url character varying(1000) COLLATE pg_catalog."default" NOT NULL,
                                title character varying(600) COLLATE pg_catalog."default" NOT NULL,
                                history character varying(600) COLLATE pg_catalog."default",
                                html_text text COLLATE pg_catalog."default",
                                full_text text COLLATE pg_catalog."default",
                                last_update_time timestamp without time zone,
                                CONSTRAINT laws_extractivedocument_pkey PRIMARY KEY (id),
                                CONSTRAINT laws_extractivedocument_source_id_source_key UNIQUE (source_id, source)
                            )
                            '''
    return create_table_query


def create__extractive_document_metadata_table():
    create_table_query = '''CREATE TABLE public.laws_extractivedocumentmetadata
                            (
                                meta_id bigserial NOT NULL,
                                term_value character varying(1000)[] COLLATE pg_catalog."default" NOT NULL,
                                last_update_time timestamp without time zone NOT NULL,
                                extractive_document_id_id bigint NOT NULL,
                                term_id_id bigint NOT NULL,
                                CONSTRAINT laws_extractivedocumentmetadata_pkey PRIMARY KEY (meta_id),
                                CONSTRAINT extractive_document_id__term_id__unique UNIQUE (extractive_document_id_id, term_id_id),
                                CONSTRAINT laws_extractivedocum_extractive_document__2bf643e1_fk_laws_extr FOREIGN KEY (extractive_document_id_id)
                                    REFERENCES public.laws_extractivedocument (id) MATCH SIMPLE
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION
                                    DEFERRABLE INITIALLY DEFERRED,
                                CONSTRAINT laws_extractivedocum_term_id_id_3deaebf2_fk_laws_docu FOREIGN KEY (term_id_id)
                                    REFERENCES public.laws_documentmetadataterm (term_id) MATCH SIMPLE
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION
                                    DEFERRABLE INITIALLY DEFERRED
                            )'''
    return create_table_query


def create__relation_type():
    create_table_query = '''CREATE TABLE public.laws_relationtype
                            (
                                id bigserial NOT NULL,
                                name character varying(255) COLLATE pg_catalog."default" NOT NULL UNIQUE,
                                last_update_time timestamp without time zone,
                                CONSTRAINT laws_relationtype_pkey PRIMARY KEY (id)
                            )'''
    return create_table_query


def create__extractive_document_schema():
    create_table_query = '''CREATE TABLE public.laws_extractivedocumentschema
                            (
                                schema_id bigserial NOT NULL,
                                last_update_time timestamp without time zone NOT NULL,
                                destination_id_id bigint NOT NULL,
                                relation_type_id_id bigint NOT NULL,
                                source_id_id bigint NOT NULL,
                                CONSTRAINT laws_extractivedocumentschema_pkey PRIMARY KEY (schema_id),
                                CONSTRAINT extractive_document_fk_source_and_destination UNIQUE (source_id_id, relation_type_id_id, destination_id_id),
                                CONSTRAINT laws_extractivedocum_destination_id_id_2820c842_fk_laws_extr FOREIGN KEY (destination_id_id)
                                    REFERENCES public.laws_extractivedocument (id) MATCH SIMPLE
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    DEFERRABLE INITIALLY DEFERRED,
                                CONSTRAINT laws_extractivedocum_relation_type_id_id_6b2bf718_fk_laws_rela FOREIGN KEY (relation_type_id_id)
                                    REFERENCES public.laws_relationtype (id) MATCH SIMPLE
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    DEFERRABLE INITIALLY DEFERRED,
                                CONSTRAINT laws_extractivedocum_source_id_id_497758a9_fk_laws_extr FOREIGN KEY (source_id_id)
                                    REFERENCES public.laws_extractivedocument (id) MATCH SIMPLE
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    DEFERRABLE INITIALLY DEFERRED
                            )'''
    return create_table_query


def create__selfdrafted_document():
    create_table_query = '''CREATE TABLE public.laws_selfdrafteddocument
                        (
                            id bigserial NOT NULL,
                            title character varying(45) COLLATE pg_catalog."default" NOT NULL,
                            content text COLLATE pg_catalog."default" NOT NULL,
                            author character varying(255) COLLATE pg_catalog."default" NOT NULL,
                            created_time timestamp without time zone NOT NULL,
                            last_update_time timestamp without time zone NOT NULL,
                            user_id_id bigint NOT NULL,
                            CONSTRAINT laws_selfdrafteddocument_pkey PRIMARY KEY (id),
                            CONSTRAINT laws_selfdrafteddocument_user_id_id_5e4fd938_fk_users_user_id FOREIGN KEY (user_id_id)
                                REFERENCES public.users_user (id) MATCH SIMPLE
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                                DEFERRABLE INITIALLY DEFERRED
                        )'''
    return create_table_query


def create__selfdrafted_document_metadata():
    create_table_query = '''CREATE TABLE public.laws_selfdrafteddocumentmetadata
                            (
                                meta_id bigserial NOT NULL,
                                term_value character varying(1500) COLLATE pg_catalog."default" NOT NULL,
                                last_update_time timestamp without time zone NOT NULL,
                                self_drafted_document_id_id bigint NOT NULL,
                                term_id_id bigint NOT NULL,
                                CONSTRAINT laws_selfdrafteddocumentmetadata_pkey PRIMARY KEY (meta_id),
                                CONSTRAINT laws_selfdrafteddocu_self_drafted_documen_1aa53c3f_fk_laws_self FOREIGN KEY (self_drafted_document_id_id)
                                    REFERENCES public.laws_selfdrafteddocument (id) MATCH SIMPLE
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    DEFERRABLE INITIALLY DEFERRED,
                                CONSTRAINT laws_selfdrafteddocu_term_id_id_4ab48a70_fk_laws_docu FOREIGN KEY (term_id_id)
                                    REFERENCES public.laws_documentmetadataterm (term_id) MATCH SIMPLE
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    DEFERRABLE INITIALLY DEFERRED
                            )'''
    return create_table_query


def create_table(table_name):
    cursor = connection.cursor()

    if table_name == "extractive_document":
        cursor.execute(create__extractive_document_table())
    elif table_name == "relation_type":
        cursor.execute(create__relation_type())
    elif table_name == "extractive_document_metadata":
        cursor.execute(create__extractive_document_metadata_table())
    elif table_name == "document_metadata_term":
        cursor.execute(create___document_metadata_term_table())
    elif table_name == "extractive_document_schema":
        cursor.execute(create__extractive_document_schema())
    elif table_name == "selfdrafted_document":
        cursor.execute(create__selfdrafted_document())
    elif table_name == "selfdrafted_document_metadata":
        cursor.execute(create__selfdrafted_document_metadata())

    connection.commit()
    print("Table " + table_name + " created successfully in PostgreSQL")


if __name__ == "__main__":
    create_table("document_metadata_term")
    create_table("extractive_document")
    #create_table("selfdrafted_document")

    create_table("relation_type")

    #create_table("selfdrafted_document_metadata")
    create_table("extractive_document_metadata")
    create_table("extractive_document_schema")
