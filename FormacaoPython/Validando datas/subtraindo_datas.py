from datetime import datetime, timedelta


hoje = datetime.today()

amanha = datetime.today() - timedelta(days=2, minutes=10, seconds=32)

diferenca = amanha - hoje



print(hoje)

print(amanha)

print(diferenca)