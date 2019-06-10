import smtplib
import os


def get_email(file):
    with open(file, 'r') as f:
        # reads first line form the text file
        first_line = f.readline()
        # splits line at space to separate name and email
        name = first_line.split()[0]
        email = first_line.split()[1]
        f.close()
    # remove selected person from the list
    remove_line(file)
    return name, email


def remove_line(file):
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file, 'w') as fout:
        fout.writelines(data[1:])
    if os.path.getsize(file) == 0:
        # if text file is empty reset it by copying a full list from all_emails.txt
        copy("all_emails.txt", file)


def copy(file_to_copy, file):
    # copies file_to_copy into file
    with open(file_to_copy) as f:
        with open(file, "w") as f1:
            for line in f:
                f1.write(line)


sender_email = ''
receiver_name, receiver_email = get_email("emails.txt")
# stores password in ascii
password = [1]
# converts password from ascii into text
sender_password = ''.join(chr(i) for i in password)
subject = "Python Test"
text = f"Dear {receiver_name},\nThis message was sent with Python's smtplib."
message = 'Subject: {}\n\n{}'.format(subject, text)
server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
