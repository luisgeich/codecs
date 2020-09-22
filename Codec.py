class Codec:

    def __init__(self, filePath):
        self.tipo = "" # Tipo da codificação
        self.file = filePath # Caminho do arquivo
        self.encoded = "" # Buffer do resultado da codificação
        self.parametro = 0 # Valor extra a ser inserido na saida
        self.fileSaida = "" # 

        self.fileSaida = self.file.split(".")
        self.fileSaida = self.fileSaida[0]+".cod"

    def encode(self):
        print("Encoding file ", self.file)

    def decode(self):
        print("Decoding file ", self.file)

    def write_encoded(self):
    
        arquivo = open(self.fileSaida, "w")
        arquivo.write(str(self.tipo)+str(self.parametro)+self.encoded)
        arquivo.close()

        return self


        