from datetime import datetime


class DatasBr():
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        lst_mes = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes = self.momento_cadastro.month - 1
        return lst_mes[mes].upper()
    
    def semana(self):
        lst_semana = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        semana = self.momento_cadastro.weekday()
        return lst_semana[semana].upper()
    
    def __str__(self) -> str:
        return f'{self.mes_cadastro} {self.semana}'

data = DatasBr()

print(data)