SERVER = "smtp.w1nt3f3ll.com"
FROM = "jsknow@w1nt3f3ll.com"
TO = ["astark@w1nt3f3ll.com"] # must be a list

SUBJECT = "Winter is coming"
TEXT = "This is just a test. Put any message here"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login("jsknow@w1nt3f3ll.com", "Targary3n")
server.sendmail(FROM, TO, message)
server.quit()
