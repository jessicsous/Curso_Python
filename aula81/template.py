from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'meuemail@gmail.com'
minha_senha = 'minhasenha'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_hj = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Lucas Viamonte', data=data_hj)


msg = MIMEMultipart()
msg['from'] = 'Jéssica Silva de Sousa'
msg['to'] = 'emaildocliente@gmail.com' # cliente
msg['subject'] = 'assunto do email'


corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)