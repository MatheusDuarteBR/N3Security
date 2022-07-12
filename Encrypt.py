import text_chunk
import base64

#Abre o arquivo de chave publica
keyFile = open('public.txt', 'r')
lines = keyFile.readlines()

#Abre o arquivo de entrada de dados
with open("source.txt") as f:
    srcFile = f.read()

#Le a linha 0 (modulo)
modulusStr = (lines[0])
modulus = int(modulusStr)

#Le a chave publica
keyStr = (lines[1])
key = int(keyStr)

chunkSize = text_chunk.block_size(modulus)

codedText = base64.b64encode(bytes(srcFile.encode())).decode()

chunks = [codedText[i:i+chunkSize] for i in range(0, len(codedText), chunkSize)]

encoded_chunks = []

for chunk in chunks: 
    original_chunk = text_chunk.TextChunk(chunk).int_value()
    encoded_chunk = pow(original_chunk,key, modulus)
    encoded_chunks.append(str(encoded_chunk))

#Abre o arquivo de saída de dados
with open('out.txt', 'w') as f:
        for lines in encoded_chunks:
            f.write(lines)
            f.write('\n')
