def check_status_es(es):
    if not es.ping():
        raise ValueError("Connection failed")
    else:
        print('ES live', es)
    return True


def add_meta_query(query, size, source, offset):
    query.update({'size': size})
    query.update({'_source': source})
    return query
