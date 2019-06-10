import smtplib
import os


def get_email(file):
    with open(file, 'r') as f:
        first_line = f.readline()
        name = first_line.split()[0]
        email = first_line.split()[1]
        f.close()
    remove_line(file)
    return name, email


def remove_line(file):
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file, 'w') as fout:
        fout.writelines(data[1:])
    if os.path.getsize(file) == 0:
        copy("all_emails.txt", file)


def copy(file_to_copy, file):
    with open(file_to_copy) as f:
        with open(file, "w") as f1:
            for line in f:
                f1.write(line)


sender_email = ''
password = [100, 101, 102, 103, 104, 105, 106, 107]
sender_password = ''.join(chr(i) for i in password)
print(sender_password)
subject = "Python Test"
text = "This message was sent with Python's smtplib."
message = 'Subject: {}\n\n{}'.format(subject, text)
server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
server.starttls()
# server.login(sender_email, sender_password)
# server.sendmail(sender_email, sender_email, message)
server.quit()


