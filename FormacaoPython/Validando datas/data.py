from datetime import datetime, timedelta


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
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada
    
    def data_cadastro(self):
        data_cadastro = (datetime.today() + timedelta(days=30, minutes=55, seconds=10)) - self.momento_cadastro
        return data_cadastro

    def tempo_de_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro


    def __str__(self) -> str:
        return self.format_data()
    

data = DatasBr()

print(data.mes_cadastro())

print(data.semana())