from Golomb import *
from utils import *

coder = Golomb("arquivos/teste.txt", 4)
coder.encode().write_encoded()
