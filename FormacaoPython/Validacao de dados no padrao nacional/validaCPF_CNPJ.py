from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):

        if len(documento) == 11:
            return DOC_CPF(documento)
        
        elif len(documento) == 14:
            return DOC_CNPJ(documento)
        
        else:
            raise ValueError("Quantidade de digitos do CPF ou CNPJ invalida. ")

#-------Classe CPF------------------------------------
class DOC_CPF:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF invalido')

    def valida_cpf(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formata_cpf(self, documento):
        mascara = CPF()
        return mascara.mask(documento)
    
    def __str__(self):
        return self.formata_cpf(self.cpf)

#-------Classe CNPJ------------------------------------
class DOC_CNPJ:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ invalido')
        
    def valida_cnpj(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata_cnpj(self, documento):
        mascara = CNPJ()
        return mascara.mask(documento)
    
    def __str__(self):
        return self.formata_cnpj(self.cnpj)




