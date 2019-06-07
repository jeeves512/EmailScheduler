import smtplib

if __name__ == '__main__':
    sender_email = 'jeevan@email.com'
    password = [100,80,122,79,83,106,95,94]
    sender_password = ''.join(chr(i) for i in password)
    print(sender_password)
    subject = "Python Test"
    text = "This message was sent with Python's smtplib."
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, sender_email, message)
    server.quit()
