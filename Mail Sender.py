import smtplib
import cgi

# ob = smtplib.SMTP("smtp.gmail.com", 587)
# ob.starttls()
# ob.login("amanmourya0097@gmail.com", "Aman@9764")
# subject = "Sending email"
# body = "This is demo mail testing"
# message = "Subject: {}\n\n{}".format(subject, body)
# # print(message)
# listOfAddress = ["adityamourya097@gmail.com", "adityamourya976@gmail.com"]
# ob.sendmail("amanmourya0097@gmail.com", listOfAddress, message)
# print("Send Successfully...")
# ob.quit()

# ------------------------------------------------------------------------------


# mhwj gxuf fjtt thfm
form = cgi.FieldStorage()
name = form.getvalue("Name")
visitor_email = form.getvalue("Sender")
subject = form.getvalue("Subject")
messageInfo = form.getvalue("Message")

# name = "raj"
# visitor_email = "demo@gmail.com"
# subject = "testing"
# messageInfo = "python is best"


email_from = 'amanmourya000097@gmail.com'
password = 'mhwj gxuf fjtt thfm'

email_body = "\n User Name: " + name + "\n Email: " + visitor_email + "\n Subject: " + subject + "\nMessage: " + messageInfo+"\n"
subject = "New Form Submission "
to = "amanmourya0097@gmail.com"
message = "Subject:{}\n\n{}".format(subject,email_body)
server = smtplib.SMTP("smtp.gmail.com", 587)
# server.ehlo()
server.starttls()
server.login(email_from, password)
print("Login Successful")
server.sendmail(email_from, to, message)
print("Email has been sent to ", to)