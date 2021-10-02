import smtplib, ssl
from getpass import getpass

port = 465

def main():
    entry_message = """Hello and welcome to the email client created by /sarthak1905!
    This client can login to a gmail account and send the message typed out.
    However, this requires that your account allows logins from 'less secure apps'.
    If this feature is disabled in the security settings, then this client will not work!
    Having said that,let's begin sending emails!\n\n"""
    print(entry_message)
    
    sender_email = str(input("Enter your email address:"))
    password = getpass("Enter your password(will NOT appear as you type):")
    receiver_email = str(input("Enter the receiver email address:"))

    subject = str(input("Enter the subject-"))
    print("Enter the body of the email(press enter twice when done)-\n")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    body = '\n'.join(lines)
    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email, receiver_email, message)
    print("Thank you for using. Check your inbox for the message sent.")

if __name__=='__main__':
    main()

