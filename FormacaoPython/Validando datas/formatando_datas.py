from datetime import datetime



#Exibe a data atual do sistema
data_atual = datetime.today()

print(data_atual)

#Exibe o mês atual, obs: o mês e representado por numero
mes_atual = data_atual.month

print(mes_atual)

#Exibe a semana atual com base na data atual do sistema
#OBS: tambem representada por numero

semana_atual = data_atual.weekday()

print(semana_atual)

#Exibe o dia atual

dia_atual = data_atual.day

print(dia_atual)

#Exibe o mes atual com base na data atual do sistema

ano_atual = data_atual.year

print(ano_atual)
print("----------------------------Datas formatadas------------------------")

print(dia_atual, mes_atual, ano_atual)

print("----Formatando as datas------")

#Utilizando o metdod strftime para formatar
# (%d) -> para o dia | (%m) -> para o mês | (%Y) -> para o ano com os dois ultimos digitos
# (%Y) -> para retirnar o ano com quatro digitos utilize Y em caixa alta
data_formatada = data_atual.strftime('%d/%m/%y')

data_formatada_dois = data_atual.strftime('%d/%m/%Y')

print(data_formatada)

print(data_formatada_dois)

#Retorna os dias da semana por extenso

dia_da_semana = data_atual.strftime("%A")

print(dia_da_semana)