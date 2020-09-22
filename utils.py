import binascii

def file_to_int(caminho):
    
    saida = ""
    arquivo = open(caminho,"r")
    
    for linha in arquivo:
        for caracter in linha:
            binario = str_to_bin(caracter)
            inteiro = bin_to_int(binario)
            saida += str(inteiro) + " "

    arquivo.close()
    saida = saida[:-1]

    return saida

def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::]
    return binario

def bin_to_str(binario):
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  # 0x101100110
        k += 1
    return string

def bin_to_int(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal

