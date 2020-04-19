from utilities.reader_helper import count_file_in_directory, count_line


def give_me_log(output_file_path, information):
    try:
        with open(output_file_path, "w") as lf:
            lf.write("Số lượng urls crawl được " + 'tại ' + information[0] + ' : ' + str(count_line(information[0])) + '\n')
            lf.write("Số lượng văn bản crawl được " + 'tại ' + information[1] + ' : '+ str(count_file_in_directory(information[1]))  + '\n')
            if len(information) > 2:
                lf.write("Thời gian ghi urls và sitemaps(): " + information[2] + '\n')
                lf.write("Thời gian trích xuất và ghi văn bản: " + information[3] + '\n')
    except Exception as e:
        print("give_me_log() error: ", e)
