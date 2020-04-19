import os
import json
import gzip
import fasteners

from utilities.common import is_validate_json


def write_to_record(object, file_output_path, by_line=False, is_append=False):
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    with fasteners.InterProcessLock(file_output_path):
        try:
            if not is_append:
                with open(file_output_path, "w+") as file:
                    if not by_line:
                        file.write(object)
                    else:
                        file.write(object + '\n')

            else:
                with open(file_output_path, "a") as file:
                    if not by_line:
                        file.write(object)
                    else:
                        file.write(object + '\n')
        except Exception as e:
            print("write_to_record error: ", e)


def store_json(json_obj, file_output_path, debug=False):
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    if debug is True:
        if is_validate_json(json_obj) is None:
            with open(file_output_path, 'w') as fp:
                json.dump(json_obj, fp, ensure_ascii=False, sort_keys=True, indent=1)
    else:
        with open(file_output_path, 'w') as fp:
            json.dump(json_obj, fp, ensure_ascii=False, sort_keys=True, indent=1)

def store_gz(json_obj, file_output_path, is_append=False):
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    with fasteners.InterProcessLock(file_output_path):
        if is_append:
            if is_validate_json(json_obj) is None:
                with gzip.open(file_output_path, 'ab') as f:
                    f.write(('\n' + json.dumps(json_obj, ensure_ascii=False, indent=2)).encode('utf-8'))
        else:
            if is_validate_json(json_obj) is None:
                with gzip.open(file_output_path, 'wb') as f:
                    f.write((json.dumps(json_obj, ensure_ascii=False, indent=2)).encode('utf-8'))


def store_error(error, file_output_path):
    os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
    with fasteners.InterProcessLock(file_output_path):
        with open(file_output_path, 'w') as f:
            f.write(error)


if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8]
    print(x[3:4], x[2:5])