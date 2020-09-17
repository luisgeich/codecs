class Codec:

    def __init__(self, filePath):
        self.file = filePath

    def encode(self):
        print("Encoding file ", self.file)

    def decode(self):
        print("Decoding file ", self.file)
        