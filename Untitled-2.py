'''
x = int(input("Digite um numero inteiro maior que 0: "))
fat = x
while (x > 1):
    fat = fat * (x - 1)
    x = x - 1
print("Seu numero fatoriado: ", fat)
'''

'''
def calculo(x, y, z):
    adicao = x + y + z
    return adicao

def main():
    a = int(input("Digite um numero: "))
    b = int(input("Digite um numero: "))
    c = int(input("Digite um numero: ")) 

    result = calculo(a, b, c)
    result = result / 3
    print("A media dos 3 numeros é: ", result)
main()
'''

def potencia(base, indice):
    potenciacao = base ** indice
    return potenciacao

def main():
    base = int(input("Digite a base: "))
    indice = int(input("Digite o indice: "))
    
    result = potencia(base, indice)
    print("O valor da Potencia é: ", result)
main()










