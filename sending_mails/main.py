import os
import smtplib
import pytz
from email.message import EmailMessage
Email_Address='unofficial.digital.cell@gmail.com'
Email_Pass='unofficial_digital_cell'
contacts=[
  'sajindal103@gmail.com',
  'arymanyo@gmail.com',
  'avish9212452821@gmail.com',
  'bhartissharma8750@gmail.com',
  'dhruvkakkar39@gmail.com',
  'geetansh.sidhar20@gmail.com',
  'geetikadua241@gmail.com',
  'bhatiagokul@gmail.com',
  'bhatiagokul@gmail.com',
  'hardikmehta9x@gmail.com',
  'hv41096@gmail.com',
  'harshika1406.vats@gmail.com',
  'hs913271@gmail.com',
  'pareekhridyansh@gmail.com',
  'tintinsharma2531@gmail.com',
  'muskantwelveth2002@gmail.com',
  'neeshamraghav0@gmail.com',
  'tiwarinikhil604@gmail.com',
  'nishaparshwal@gmail.com',
  'Nishantagrawal7450@gmail.com', 
  'priyangoel520@gmail.com',
  'chhabrapuneet828@gmail.com',
  'chhabrapuneet828@gmail.com',
  'awesomerahul188@gmail.com',
  'rishabhkaushik1049@gmail.com',
  'shrutii1710@gmail.com',
  'shubhamspidyneema@gmail.com',
  'smritiaspires@gmail.com',
  'Yashugarg23@gmail.com',
  'Vikramaaditya10@gmail.com',
  'abhilakshbansal2001@gmail.com',
  'er.manavbansal@gmail.com',
  'paragthakur56@gmail.com',
  'aroraparas1010@gmail.com',
  'pbatra852@gmail.com',
  'prateeknara05@gmail.com', 
  'priyaltiwary2001@gmail.com',
  'Rishabhsingh9286@gmail.com',
  'riteshgupta51489@gmail.com',
  'ritikjind2018@gmail.com',
  'RITIKGOYAL1710@GMAIL.COM',
  'rohitgarg2825@gmail.com',
  'sameepmago@gmail.com',
  'skaggarwal2001.com@gmail.com',
  'shraddhapandita6@gmail.com',
  'shreyagarg1512@gmail.com',
  'schugh2001@gmail.com',
  'sumantgupta8127@gmail.com',
  'sumantgupta8127@gmail.com',
  'ssunil.kkumar2001@gmail.com',
  'tilakraj8934@gmail.com',
  'vivek.agg.va21@gmail.com',
  'Yashavjain@gmail.com',
  'yashbansal097@gmail.com',
  'jyoti98991234@gmai.com',
  'mandeeppunia08@gmail.com',
  'singwalmohit2020@gmail.com',
  'monikachauhan13102001@gmail.com',
  'munishkumar123264@gmail.com',
  'kharbpraveen86@gmail.com',
  'radhikawadhwa2000@gmail.com',
  'riayadav1199@gmail.com',
  'sahilgoyals1999@gmail.com',
  'yogeshyadav32321212@gmail.com',
  'manusaini189@gmail.com'
]
msg=EmailMessage()
msg['Subject']='Digital Cell'
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
  <div style="background-image: url('D:\python projects\indian flag.jpg');">
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
    <p class="signature">– Digital Cell , YMCAUST</p>
  </div>
</body>
</table>
</html>
""",subtype='html')
files=['digital_cell_republic_day.pdf']
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