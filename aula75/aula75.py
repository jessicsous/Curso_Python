'''
Ùltimo dia do mês em ano bissexto
Na aula anterior  foi utilizado 'mdays' de 'calendar'
(que pega a quantidade de dias do mês) para pegar o ultimo dia do mês.
Isso pode não funcionar m ano bissexto.

pod tabém utilizar a função 'monthrange' de 'calendar' para pegar o número
do dia da semana (entre 0-6) e último dia do mês (entre 28-31), exemplo:
'''

from datetime import datetime
from calendar import monthrange

# Retorna uma tupla contendo o número do dia da semana (0-6)
# e último dia de fevereiro d 2020
print(monthrange(2020, 2))

# Saída - (5, 29)
# o 5 significa que é sábado
# o 29 significa que este é o último dia do mês

'''
O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6)
Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:
'''

# dia_semana, ultimo_dia = monthrange
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)
print(dia_semana)

'''
Pode também criar uma lista, assim como mdays, contendo todos os últimos dias de meses
do ano atual: 
'''

ultimos_dias_de_meses_do_ano_atual = [monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)]

print(ultimos_dias_de_meses_do_ano_atual)