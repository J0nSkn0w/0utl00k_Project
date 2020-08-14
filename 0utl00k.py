SERVER = "smtp.w1nt3f3ll.com"
FROM = "user@company.com"
TO = ["boss@company.com"] # must be a list

SUBJECT = "Winter is coming"
TEXT = "This is just a test. Put any message here"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login("username", "password")
server.sendmail(FROM, TO, message)
server.quit()
