from validaCPF_CNPJ import Documento
from validate_docbr import CNPJ, CPF

#cpf_um = Cpf("15316264754")
#print(cpf_um)

cnpj = CNPJ()
cnpj = cnpj.generate()

cpf = CPF()

cpf = cpf.generate()


cnpj = Documento.cria_documento(cnpj)
cpf = Documento.cria_documento(cpf)

print(cnpj)
print(cpf)