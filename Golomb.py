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

        self.decoded = "";

        try:
            binarios = file_to_bin(self.file).split(" ")

        except FileNotFoundError:
            print("Caminho do arquivo não encontrado")
            return False

        for binario in binarios:
            inteiro = self.golomb_decode(binario, self.parametro)
            print(bin_to_str(bin(inteiro)))
            self.decoded += bin_to_str(bin(inteiro))

        return self
    

    def getDecoded(self):
            return self.decoded;

    
    def golomb_code(self, valor, k):
        c = int(math.ceil(math.log(k,2)))
        remin = valor % k
        quo = int(math.floor(valor / k))
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
    
    def golomb_decode(self, coded, b):
    
        def decode(x):
            num=0
            for i in range(len(x)):
                num+=(int(x[len(x)-1-i])*(math.pow(2,i)))
            return num

        l = 1;
        b = int(b)
        x = list(coded)
        i = math.floor(math.log(b,2))
        d = math.pow(2,i+1)-b
        p2 = 0

        while(p2 < len(x)):
            t = 0;
            k = i;
            q = 0;
            r = [];
            flag = 0;
            for p in range(p2,len(x)):
                if(x[p]=='0' and flag==0):
                    t+=1;
                    continue;
                if(x[p]=='1' and flag==0):
                    q=t;
                    flag=1;
                    continue;
                r.append(x[p]);
                k-=1;
                if(k==0):
                    rnum=decode(r);
                    if(rnum<d):
                        p2=p+1;
                        break;
                if(k==-1):
                    rnum=decode(r);
                    rnum=rnum-d;
                    p2=p+1;
                    break;
            ans=q*b+rnum;
            return (int(ans));
            l = 0;
    