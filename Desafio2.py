entrada = str(input('Digite algo'))
qnt = 0
for char in entrada:
    if char == 'A' or char == 'a':
        qnt +=1
print('a quantidade de A ou a na frase é de: ',qnt)