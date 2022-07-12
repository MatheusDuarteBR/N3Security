from ast import Str
from importlib.machinery import SourceFileLoader

import text_chunk
import base64

#Abre o arquivo de chave publica
keyFile = open('public.txt', 'r')
lines = keyFile.readlines()

#Abre o arquivo de entrada de dados
with open("source.txt") as f:
    srcFile = f.read()

# Divide o public.txt em duas linhas para separaçao
for index, line in enumerate(lines):
    print("Linha {}: {}".format(index, line.strip()))
keyFile.close()

#Le a linha 0 (modulo)
modulusStr = (lines[0])
modulus = int(modulusStr)

#Le a chave publica
keyStr = (lines[1])
key = int(keyStr)

chunkSize = text_chunk.block_size(modulus)

codedTextBytes = base64.b64encode(bytes(srcFile, "utf-8"))
codedText = str(codedTextBytes.decode("utf-8"))

cod = (codedText)
n = (chunkSize)

chunks = [cod[i:i+n] for i in range(0, len(cod), n)]

for chunk in chunks: 
    original_chunk = text_chunk.TextChunk(chunk).int_value()
    encoded_chunk = pow(original_chunk,key, modulus)


#Abre o arquivo de saída de dados
with open('out.txt', 'w') as f:
        for lines in chunks:
            f.write(lines)
            f.write("\n")
