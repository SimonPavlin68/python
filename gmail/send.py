# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security 
s.starttls()

# Authentication 
s.login("simon.pavlin68@gmail.com", "JebiSe#GMAIL")

# message to be sent 
message = "krneki"

# sending the mail 
s.sendmail("simon.pavlin68@gmail.com", "simon.pavlin68@gmail.com", message)

# terminating the session 
s.quit()