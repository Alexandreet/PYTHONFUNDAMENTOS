# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
def addNum(x,y):
    return x + y

def subtNum(x,y):
    return x - y

def multNum(x,y):
    return x * y

def divNum(x,y):
    return x / y

print("\n******************* Python Calculator *******************")

print("\n Selecione o número da operação desejada:")

print("\n 1 - Soma")
print("\n 2 - Subtração")
print("\n 3 - Multiplicação")
print("\n 4 - Divisão")

selectOper = input('Digite sua opção (1/2/3/4):')

primeiroNum = input('Digite o Primeiro Número:')

segundoNum = input('Digite o Segundo Número:')


if int(selectOper) == 1:
    addNum(int(primeiroNum),int(segundoNum))
    print('%s + %s = %s' %(primeiroNum,segundoNum, addNum(int(primeiroNum),int(segundoNum))))

elif int(selectOper) == 2:
    subtNum(int(primeiroNum), int(segundoNum))
    print('%s - %s = %s' %(primeiroNum,segundoNum, subtNum(int(primeiroNum),int(segundoNum))))

elif int(selectOper) == 3:
    multNum(int(primeiroNum), int(segundoNum))
    print('%s * %s = %s' %(primeiroNum,segundoNum, multNum(int(primeiroNum),int(segundoNum))))

elif int(selectOper) == 4:
    divNum(int(primeiroNum), int(segundoNum))
    print('%s ÷ %s = %s' %(primeiroNum,segundoNum, divNum(int(primeiroNum),int(segundoNum))))

else:
    print("Operação Inválida")