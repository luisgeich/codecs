from Golomb import *
from utils import *

print("TESTE");

coder = Golomb("arquivos/teste.txt", 4)
coder.encode().write_encoded()
