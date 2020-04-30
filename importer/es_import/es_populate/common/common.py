def get_by_attribute_from_array_dict(array_dict, attribute_name, atribute_value):
    for item in array_dict:
        if (item.get(attribute_name) == atribute_value):
            return item
    return None