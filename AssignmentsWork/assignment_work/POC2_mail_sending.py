import smtplib, zipfile, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

basedir = r'F:\Dropbox'
os.chdir(basedir)

zf = zipfile.ZipFile(r'C:\Users\eknath\Desktop\test\Dropbox.zip','w')
      
for dir,subdir,files in os.walk(basedir):
    for filetozip in os.listdir(dir):
        os.chdir(dir)
        zf.write(dir + '/' + filetozip)

zf.close()

fromadd = '1nath.salvi@gmail.com'
toadd = 'jatin@ethans.co.in'

msg = MIMEMultipart()
msg['From'] = fromadd
msg['TO'] = toadd
msg['Subject'] = "teast mail, Please Ignore"
body = "Hello this is test mail,  Please Ignore"
msg.attach(MIMEText(body,'plain'))

attachment = open(r'C:\Users\eknath\Desktop\test\Dropbox.zip','rb')
filename = 'Dropbox.zip'

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromadd,'1nath@gmail')
text = msg.as_string()
server.sendmail(fromadd, toadd, text)
server.quit()
