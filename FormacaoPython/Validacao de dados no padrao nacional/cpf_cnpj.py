from validate_docbr import CPF, CNPJ

class CpfCnpj():
    def __init__(self, documento):
        documento = str(documento)

        if self.valida_documento(documento):
            self.documento = documento
        else:
            raise ValueError('CPF/CNPJ invalido')
        
    def valida_documento(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        elif len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError('CNPJ ou CPF invalidos')

    def formata_documento(self):
        if len(self.documento) == 11:
            mascara = CPF()
            return mascara.mask(self.documento)
        else:
            mascara = CNPJ()
            return mascara.mask(self.documento)
    
    def __str__(self):
        return self.formata_documento()




