from string import Template
from datetime import datetime
from email import policy



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'desousa.jessicasilva@outlook.com'
minha_senha = '!M@gin320'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_hj = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Lucas Viamonte', data=data_hj)


msg = MIMEMultipart(policy=policy.default)
msg['from'] = 'desousa.jessicasilva@outlook.com'
msg['to'] = 'desousa.jessicasilva@gmail.com' # cliente
msg['subject'] = 'Sou lindo'


corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('image.jpeg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)