import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from constant.crawler_contants import VERSION

from utilities.reader_helper import count_file_in_directory

def send_email(information):
    message = Mail(
        from_email='namnguyen12399.coder@gmail.com',
        to_emails='namnguyen12399.coder@gmail.com',
        subject='Report of ' + VERSION,
        plain_text_content="Số lượng sitemaps crawl được "+ 'tại ' + information[0] + ' : '+ str(count_file_in_directory(information[0])) + '\n'
                            + "Số lượng văn bản crawl được " + 'tại ' + information[0] + ' : '+ str(count_file_in_directory(information[1]))  + '\n'
                            + "Thời gian store_sitemaps_and_urls(): " + information[2] + '\n'
                            + "Thời gian trích xuất và ghi văn bản: " + information[3] + '\n'
        )

    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


#email_1: 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
if __name__ == "__main__":
    send_email()