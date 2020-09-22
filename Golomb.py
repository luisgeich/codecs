import math
from Codec import *
from utils import *

class Golomb(Codec):

    def __init__(self, filePath, parametroK):
        super(Golomb, self).__init__(filePath)
        self.parametro = parametroK
        self.tipo = "0" # Ver enunciado do trabalho

    def encode(self):
        self.encoded = ""

        try:
            ints = file_to_int(self.file).split(" ")

        except FileNotFoundError:
            print("Caminho do arquivo não encontrado")
            return False
            

        for inteiro in ints:
            binario = self.golomb_code(int(inteiro), self.parametro)
            self.encoded += bin_to_str(binario)

        return self

    def getEncoded(self):
        return self.encoded

    def decode(self):
        print("Decoding file with Golomb", self.file)

    def golomb_code(self, valor, k):
        c = int(math.ceil(math.log(k,2)))
        remin = valor % k
        quo =int(math.floor(valor / k))
        div = int(math.pow(2,c) - k)
        first = ""
        for i in range(quo):
            first = first + "0"

        if (remin < div):
            b = c - 1
            a = "{0:0" + str(b) + "b}"
            bi = a.format(remin)
        else:
            b = c
            a = "{0:0" + str(b) + "b}"
            bi = a.format(remin+div)

        final = first + "1" +str(bi)
        return final
    