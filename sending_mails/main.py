import os
import smtplib
import pytz
from email.message import EmailMessage
Email_Address='YOUR_EMAIL_ADDRESS'
Email_Pass='EMAIL_ADRESS_PASSWORD'
contacts=['YOUR_COMMA_SEPARATED_CONTACT_LIST']
msg=EmailMessage()
msg['Subject']='SUBJECT'
msg['From']=Email_Address
msg.set_content('good day!!')
msg.add_alternative(r"""
<!DOCTYPE html>
<html>
<head>
 <title>Happy Republic Day</title>
 <meta charset="utf-8" />
</head>
<table width="100%" border="0" cellspacing="0" cellpadding="20" >
<body>
    <h1>Happy Republic Day <span class="redText">Cell Members</span>!</h1>
    <p>
    आओ झुक कर सलाम करे उन्हें,<br>
    जिनकी ज़िन्दगी में ये मुकाम आया है,<br>
    किस कदर खुशनसीब है वो लोग,<br>
    जिनका लहू भारत देश के काम आया है|<br>
    </p>
    <p><span class="redText">72nd</span> Republic Day</p>
    <p>Today we are free because of the hardships faced by our freedom fighters🔥🔥
    Let us remember the golden heritage 💫of our country and feel proud to be an indian   </p>
    <p>Rejoice in the glory of the nation and do not forget to thank the soldiers, and all the covid warriors,whose vigilance and sacrifice keeps us safe.</p>
    <p><strong>𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆 𝗰𝗼𝗺𝗽𝘂𝘁𝗲𝗿 𝗰𝗲𝗻𝘁𝗲𝗿 𝗮𝗻𝗱 𝗱𝗶𝗴𝗶𝘁𝗮𝗹 𝗮𝗳𝗳𝗮𝗶𝗿𝘀 𝗰𝗲𝗹𝗹 𝘄𝗶𝘀𝗵𝗲𝘀 𝘆𝗼𝘂 𝗮 𝘃𝗲𝗿𝘆 𝗵𝗮𝗽𝗽𝘆 𝗿𝗲𝗽𝘂𝗯𝗹𝗶𝗰 𝗱𝗮𝘆 𝟮𝟬𝟮𝟭</strong></p>
    <p>Have lots of fun and enjoy your freedom, but also spare a thought for the numerous sacrifices made by our freedom fighters.<br> Happy Republic Day! <br> Jai hind!!</p>
    <h2>Proud To Be India!</h2>
    <p class="signature">– YOURS TRULY</p>
  </div>
</body>
</table>
</html>
""",subtype='html')
files=['LOCATION_OF_YOUR_PDF_FILE']
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_name=f.name
    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Address,Email_Pass)
    i=1
    for contact in contacts:
      msg['To']=contact
      smtp.send_message(msg)
      print('sent',i)
      del msg['To']
      i+=1
    print('sent')