import base64

from text_chunk import TextChunk

with open("private.txt", "r") as key_files: 
        module = int(key_files.readline())
        key = int(key_files.readline())

with open("out.txt", "r") as crypted_text:
    source_file = [int(line) for line in crypted_text.readlines()]

original_encoded_text = ""

for line in source_file:
    original_chunk = pow(line, key, module)
    base64_encoded_chunk = str(TextChunk(original_chunk))
    original_encoded_text += base64_encoded_chunk

original_text = base64.b64decode(original_encoded_text).decode()

with open('final.txt', 'w') as f:
    f.write(original_text)
    f.write('\n')