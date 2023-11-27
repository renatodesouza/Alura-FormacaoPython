import requests

class CEP:
    def __init__(self, cep):
        cep = str(cep)

        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Valor do CEP incorreto")
        
    def valida_cep(self, cep):
        
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):
        return  f'{self.cep[:5]}-{self.cep[5:]}'
    
    def __str__(self) -> str:
        return self.formata_cep()   
    
    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)

        
        r = requests.get(url)

        dados = r.json()

        return (
            dados['logradouro'],
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )