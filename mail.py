import smtplib as s

server=s.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()

server.login("joeytribbianinakli@gmail.com",'Joeytribbiani@07')
msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % ('joeytribbianinakli@gmail.com', ", ".join('16bit159@nirmauni.ac.in'), 'dsf', 'TEXT')
server.sendmail("joeytribbianinakli@gmail.com",'16bit159@nirmauni.ac.in',msg)
server.quit()
