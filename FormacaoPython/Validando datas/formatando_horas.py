from datetime import datetime
from datetime import time


#O datetime.now() retorna a data e a hora atual do sistema
hora_atual = datetime.now()

print(hora_atual)

hora_formatada = hora_atual.strftime('%H:%M:%S')


print(hora_formatada)