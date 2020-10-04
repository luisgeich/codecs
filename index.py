from Golomb import *

print("Bem vindo! Selecione a ação que deseja executar:")
print("1 - Codificar, 2 - Decodificar, 3 - Sair")

while True:
    acao = int(input(">> "))
    if acao != 1 and acao != 2 and acao != 3:
        print("Operação inválida")
    else:
        break 

if(acao == 1):

    print("Informe o Coder desejado:")
    print("0 - Golomb")
    print("1 - Elias-Gamma")
    print("2 - Fibonacci")
    print("3 - Unária")
    print("4 - Delta")
    print("5 - Sair")

    while True:
        codCoder = int(input(">> "))
        if(codCoder < 0 or codCoder > 5):
            print("Coder inválido")
        else:
            break

    if(codCoder != 5):

        path = input("Insira o caminho do arquivo: ")

        if(codCoder == 0):
            coder = Golomb(path, 4)

        elif(codCoder == 1):
            print("Ainda não implementado")
            #coder = EliasGama()

        elif(codCoder == 2):
            print("Ainda não implementado")
            #coder = Fibonacci()

        elif(codCoder == 3):
            print("Ainda não implementado")
            #coder = Unaria()

        elif(codCoder == 4):
            print("Ainda não implementado")
            #coder = Delta()

        if(coder.encode() != False):
            coder.write_encoded()
            print("\nCodificado com sucesso, arquivo de saida: ", coder.fileSaida, "\n")
        else:
            print("\nERRO ao codificar")
    else:
        print("Fim!")

elif(acao == 2):

    path = input("Insira o caminho do arquivo .cod: ")
    try:
        arquivo = open(path,"r")
        linha = arquivo.readline()
        
        if(int(linha[0]) == 0):
            coder = Golomb(path, int(linha[1]))
        
        elif(int(linha[0]) == 1):
            coder = EliasGama(path)
        
        elif(int(linha[0]) == 2):
            coder = Fibonacci(path)
        
        elif(int(linha[0]) == 3):
            coder = Unaria(path)

        elif(int(linha[0]) == 4):
            coder = Delta(path)
        
        if(coder != None):
            if(coder.decode() != False):
                print("Decodificado: ", coder.getDecoded())
            else:
                print("\nERRO ao decodificar")
        else:
            print("Coder não pode ser identificado. Verfique se o arquivo foi codificado corretamente")

    except FileNotFoundError:
        print("Arquivo não encontrado")

else:
    print("Fim!")