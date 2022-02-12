from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%y')
    corpo_msg = template.safe_substitute(nome='Jèssica Silva', data=data_atual)

print(corpo_msg)