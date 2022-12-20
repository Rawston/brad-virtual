class Cliente:
    pass

print("Testando o projeto")

from Cliente import Cliente # type: ignore
from Conta import Conta # type: ignore

c1 = Cliente ("joão", "114444-2222")# type: ignore
conta = Conta (c1.nome, 5665,0)# type: ignore

#print(c1)
print(conta.titular, " numero: ", conta.numero, "seu saldo: ", conta.saldo)# type: ignore