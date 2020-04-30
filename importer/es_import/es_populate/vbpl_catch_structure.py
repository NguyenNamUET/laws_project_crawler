import codecs
import re
from os import listdir
import json
import io


def read_data(path):
    name_regex = r"(?<!\w\W\n)(\ ?(LỆNH|BỘ\ {0,2}LUẬT|CHỈ\ {0,2}THỊ|QUYẾT\ {0,2}ĐỊNH|NGHỊ\ {0,2}QUYẾT|HIẾN\ {0,2}PHÁP|LUẬT|NGHỊ\ {0,2}ĐỊNH|NGHỊ\ {0,2}QUYẾT\ {0,2}LIÊN\ {0,2}TỊCH|PHÁP\ {0,2}LỆNH|THÔNG\ {0,2}TƯ|THÔNG\ {0,2}TƯ\ {0,2}LIÊN\ {0,2}TỊCH|THÔNG\ {0,2}TƯ|\ {0,2}LIÊN\ {0,2}BỘ)((\n?(.*)){1,2}))((?=$)|(?=[\n]))"  # regex bắt tên và loại văn bản, tên , loại văn bản ở group 2, tên ở group 3
    base_regex = r"((?<=^)|(?<=[\n]))(\ ?(Căn cứ)(.*))((?=$)|(?=[\n]))"  # regex bắt phần căn cứ của văn bản
    part_regex = r"((?<=^)|(?<=[\n]))((\ ?(phần)\ {0,2}(thứ)?\ {0,2}(((xc|xl|lx{0,3}|x{1,3})(ix|iv|vi{0,3}|i{1,3})?)|(ix|iv|vi{0,3}|i{1,3})))\n?(.*))((?=$)|(?=[\s]))"  # regex bắt "phần" của văn bản, số thứ tự tại group 6, nội dung ở group 11
    chapter_regex = r"((?<=^)|(?<=[\n]))((\ ?(chương)\ {0,2}(thứ)?\ {0,2}(((xc|xl|lx{0,3}|x{1,3})(ix|iv|vi{0,3}|i{1,3})?)|(ix|iv|vi{0,3}|i{1,3})))\ {0,2}\n?(.*))((?=$)|(?=[\s]))"  # regex bắt "chương" của văn bản, số thứ tự tại group 6, nội dung ở group 11
    item_regex = r"((?<=^)|(?<=[\n]))(((\ ?(mục)\ {0,2}(thứ)?\ {0,2}(\d+))|(((xc|xl|lx{0,3}|x{1,3})(ix|iv|vi{0,3}|i{1,3})?)|(ix|iv|vi{0,3}|i{1,3}))\.)\ {0,2}\n?(.*))((?=$)|(?=[\s]))"  # regex bắt "mục" của văn bản, số thứ tự tại group 7 hoặc 8, nội dung ở group 13
    article_regex = r"((?<=^)|(?<=[\n]))(((điều\ {0,2}(thứ)?\ {0,2}(\d+)\ {0,2}\.?\-?\ {0,2}(.*))))((?=$)|(?=[\n]))"  # regex bắt "điều" của văn bản, số thứ tự ở group 6, nội dung ở group 7
    clause_regex = r"((?<=^)|(?<=[\n]))((((\d+)[\.\-\,\)]\ {0,2}(.*))))((?=$)|(?=[\n]))"  # regex bắt "khoản" của văn bản,  số thứ tự ở group 5, nội dung ở group 6
    point_regex = r"((?<=^)|(?<=[\n]))((((\w)[\,\)\/]\ {0,2}(.*))))((?=$)|(?=[\n]))"  # regex bắt "điểm" của văn bản, số thứ tự ở group 5, nội dung ở group 6

    list_regex = [part_regex, chapter_regex, item_regex, article_regex, clause_regex, point_regex]
    list_replace = ["<PART>", "<CHAPTER>", "<ITEM>", "<ARTICLE>", "<CLAUSE>", "<POINT>"]
    string_file = ""
    for file_name in listdir(path + "/splited_data"):
        feature = {
            "<TYPE>": {},
            "<NAME>": {},
            "<BASE>": {},
            "<PART>": {},
            "<CHAPTER>": {},
            "<ITEM>": {},
            "<ARTICLE>": {},
            "<CLAUSE>": {},
            "<POINT>": {},
            "<STRUCTURE>": {}
        }
        with codecs.open(path + "/splited_data/" + file_name, encoding="utf-8", errors="ignore") as file:
            string_file = file.read()
            string_trimmed = trim_string(string_file)
            string_replaced = string_trimmed

            # bắt phần loại văn bản và tên văn bản
            pattern = re.compile(name_regex, re.I | re.U | re.M)
            match_name = pattern.search(string_replaced)
            string_replaced = string_replaced[:match_name.start()] + "<NAME>" + string_replaced[match_name.end():]
            feature["<TYPE>"] = match_name.group(2)
            feature["<NAME>"] = match_name.group(3)

            # bắt phần căn cứ của văn bản
            length_replace = 0
            index = 0
            for i in re.finditer(base_regex, string_replaced, re.I | re.M | re.U):
                feature["<BASE>"].update({index: i.group()})
                length_origin = len(i.group())
                string_replaced = string_replaced[:i.start() + length_replace] + "<BASE>" + " " + str(
                    index) + string_replaced[i.end() + length_replace:]
                length_replace += len("<BASE> " + str(index)) - length_origin
                index += 1

            # lần lượt duyệt qua các regex để bắt thông tin
            for i in range(len(list_regex)):
                string_replaced = replace_regex(list_regex[i], list_replace[i], string_replaced, feature)
                print("catch " + list_replace[i] + "\n")
                print("\n")
            # merge_string(string_replaced,list_replace,feature)
        feature['<STRUCTURE>'] = string_replaced.split("\n")
        export_data(feature, path + "/splited_json_data/" + file_name + ".json")
        # break
    return string_file


def trim_string(string):  # loại bỏ khoảng trống dư thừa
    string_trimmed = re.sub(r"[\r\t\f\v ]{1,}", " ", string)
    return string_trimmed


def replace_regex(regex, string_replace, string, feature):  # thay thế những đoạn bắt được bằng các nhãn
    string_after_replace = string
    length_replace = 0
    index = 0
    for match in re.finditer(regex, string, re.I | re.M | re.U):
        if (string_replace == "<PART>"):
            number = match.group(6)
            content = match.group(11)
        elif (string_replace == "<CHAPTER>"):
            number = match.group(6)
            content = match.group(11)
        elif (string_replace == "<ITEM>"):
            number = match.group(7) if match.group(7) is not None else match.group(8)
            content = match.group(13)
        elif (string_replace == "<ARTICLE>"):
            number = match.group(6)
            content = match.group(7)
        elif (string_replace == "<CLAUSE>"):
            number = match.group(5)
            content = match.group(6)
        else:
            number = match.group(5)
            content = match.group(6)
        if number is None: number = ''
        if content is None: content = ''
        feature[string_replace].update({index: {'number': number, 'content': content}})
        length_origin = len(match.group())
        string_after_replace = string_after_replace[:match.start() + length_replace] + string_replace + " " + str(
            index) + string_after_replace[match.end() + length_replace:]
        length_replace += len(string_replace + " " + str(index)) - length_origin
        index += 1
    return string_after_replace


def export_data(feature, path):  # xuất ra json file
    with io.open(path, 'w', encoding="utf8") as file:
        string = json.dumps(feature, ensure_ascii=False)
        file.write(string)


if __name__ == "__main__":
    string = read_data("D:/Lab_ML_VDH/")
