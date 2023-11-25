import re


class RG():
    def __init__(self, rg):
        if self.valida_rg:
            self.rg = rg
        else:
            raise ValueError("Numero nao é valido")
        
    def valida_rg(self, rg):
        padrao = "[0-9]{2}[0-9]{3}[0-9]{3}[0-9]{1}"
        resposta = re.findall(padrao, rg)
        return resposta
    
    def formata_rg(self):
        padrao = "([0-9]{2})([0-9]{3})([0-9]{3})([0-9])"
        resposta = re.search(padrao, self.rg)
        rg_formatado = f'{resposta.group(1)}.{resposta.group(2)}.{resposta.group(3)}-{resposta.group(4)}'

        return rg_formatado
    
    def __str__(self) -> str:
        return self.formata_rg()
    
