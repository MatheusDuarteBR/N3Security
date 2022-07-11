from doctest import debug_src
from importlib.machinery import SourceFileLoader

import text_chunk
import base64

keyFileName = open('private.txt','r')
srcFileName = open('out.txt','r')
dstFileName = open('public.txt','r')

#Abre o arquivo da chave privada
keyFile = open('private.txt', 'r')
lines = keyFile.readlines()

#Abre o arquivo de saída
with open("out.txt") as f:
    srcFile = f.read()

for index, line in enumerate(lines):
    print("Linha {}: {}".format(index, line.strip()))
keyFile.close()

#load modulus
modulusStr = (lines[0])
modulus = int(modulusStr)

#load key
keyStr = (lines[1])
key = int(keyStr)

originalEncodedText = ""

with open('out.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]

for line in int_list:
   encoded_chunk = int(line)
   original_chunk = pow(encoded_chunk, key, modulus)
   print(original_chunk)
   print(type(original_chunk))

   base64eEncodedChunk = str(text_chunk.TextChunk(original_chunk))
   print(base64eEncodedChunk)
   
   originalEncodedText += base64eEncodedChunk
   print(originalEncodedText)

decoded_string = base64.b64decode(bytes(originalEncodedText, "utf-8")).decode("utf-8", "ignore")

print(decoded_string)