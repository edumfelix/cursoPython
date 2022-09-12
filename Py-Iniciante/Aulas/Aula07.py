"""
# Manipulando strings
* String indices
* Fatiamento de strings[inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...

Essas funções podem ser usadas diretamente em cada tipo.
Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos [012345678]
text = 'Python_s2'
for c in range(len(text)):
    print(text[c])

# negativos -[987654321] Fatiamento
url = 'www.google.com.br/'
print(url[:-1])

###
nova_string = text[0::2]
print(nova_string)
