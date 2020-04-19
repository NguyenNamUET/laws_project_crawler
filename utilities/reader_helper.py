import gzip
import json
import os


def get_content_by_gz(file_path):
    try:
        with gzip.open(file_path, 'rt') as f:
            file_content = f.read()
        return file_content
    except Exception as e:
        print("get_content_by_gz() error: ", e, " at ", file_path)


def load_jsonl_from_gz(file_gz_path):
    try:
        with gzip.open(file_gz_path, 'rt') as f:
            file_content = f.read()
            obj = json.loads(file_content)
            return obj
    except Exception as e:
        print(e)


def load_jsonl_from_json(file_json_path):
    try:
        with open(file_json_path, 'rt') as f:
            file_content = f.read()
            obj = json.loads(file_content)
            return obj
    except Exception as e:
        print(e)


def load_record_to_list(file_path):
    record_lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            record_lines.append(line.strip())

    return record_lines


def count_line(file_path):
    with open(file_path, "r") as file:
        count = 0
        for line in file.readlines():
            count += 1
    return count


def count_file_in_directory(file_path):
    return len([name for name in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, name))])


if __name__ == "__main__":
    print(count_file_in_directory("/home/nguyennam/PycharmProjects/ExtractAndImport (copy)/vnu-law/crawler/thuvienphapluat2.vn/transform"))