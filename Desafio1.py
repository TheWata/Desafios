anterior = 0
atual = 1
resultado = 0
entrada = int(input('Digite um numero: '))
pertence = 0
while anterior<=entrada:
    if resultado == entrada:
        pertence = 1
        break
    resultado = atual + anterior
    anterior = atual
    atual = resultado
if pertence == 1:
    print("O numero ", entrada, " pertence a sequencia de fibonacci")
else:
    print("O numero ", entrada, " não pertence a sequencia de fibonacci")


