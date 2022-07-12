# N3Security (Projeto de Criptografia e Descriptografia de um .txt)

MainSrc: https://courses.cs.washington.edu/courses/cse143/01au/homework/hw5/

O Arquivo ('Encrypt.py') pega os dados que estão dentro do (source.txt) e criptografa usando um função (base64) usando a chave pública e o módulo gerado anteriormente com dois números primos aleatórios, e por fim gera um arquivo 'out.txt' com os dados já criptografados na base64.

O arquivo ('Decrypt.py') pega o ('out.txt') que são os números critpografados e faz o caminho de volta da criptografia gerando assim novamente os dados que estavam no ('source.txt').

Dupla : Matheus Y. Duarte & Gabriela Borowiak

Planejamento e operação: Foi organizado e feito em base no pseudo-código que o professor nos proveu. Nesse projeto tive problemas com a lignuagem escolhida (Python) problemas simples de síntaxe e um pouco de lógica de programação. Foi usada a linguagem Python porque é uma linguagem que estou ainda aprendendo e queria melhorar minhas capacidades com esta liguagem.

Teste: Os testes no código foram feitos conforme eu ia programando ele, testando se as variáveis estavam printando oque eu precisava.

O que funciona e o que não funciona? 
R: A parte de Encrypt, está 100% fucional conseguindo criptografar dados que estão no source.txt sem maiores problemas. Já o Decrypt, ele consegue ler o arquivo entrada de dados (out.txt) ele também consegue ler o arquivos da private.txt (chave privada e também o módulo). Porém o retorno que está me dando é conforme a imagem a seguir:
(imagem)

Há algum problema no código que você não conseguiu resolver?
R: Sim, tive um grande problema no código de Decrypt, acredito que seja o "for" que está com algum bug de síntaxe porém não consegui confirmar.

Avalie o projeto: Consegui testar minhas habilidades e também aprender novas funções pogramando esse código, foi de grande importância e valeu a pena demais, mesmo sem saber por onde começar fui fazendo devagar. 
