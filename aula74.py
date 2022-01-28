'''datetime - trabalhando com data e hora'''
# https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta

data = datetime(2022, 1, 27, 14, 3, 40)  # respectivamente: (ano, mês, dia, hora, minuto, segundo.)
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # formato brasileiro
print(data.strftime('%d/%h/%y %H:%M:%S'))  # outro formato

# recebendo data como str - (str - fmt)
data = datetime.strptime('27/01/2022', '%d/%m/%Y')
print(data)

# timestamp - contagem de segundos desde 01/01/1970
data = datetime.strptime('13/10/1997', '%d/%m/%Y')
print(data.timestamp())

# convertendo o timestamp em data
data = datetime.fromtimestamp(876715200.0)
print(data)

# adicionando dias á data - usando timedelta
data = datetime.strptime('13/10/1997 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=8)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# adicionando dias e segundos à data - usando timedelta
data = datetime.strptime('13/10/1997 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=8, seconds=60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# calculando segundos com timedelta - 2 horas a mais
data = datetime.strptime('13/10/1997 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# calculando minutos com timedelta - 59 minutos a mais
data = datetime.strptime('13/10/1997 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(seconds=59*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# diferença entre datas
d1 = datetime.strptime('17/10/1995 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('13/10/1997 15:00:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.seconds)  # diferença dos segundos que representam as horas
print(dif.total_seconds())  # segundos totais
print(dif.days)  # diferença de dias

# coparação entre datas
print(d2 > d1)
print(d2 == d1)
print(d2 < d1)