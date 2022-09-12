# Criando, lendo, escrevendo e apagando arquivos
import os

# Criando arquivo
file = open('test.txt', 'w+')
file.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus tempor nibh ac commodo pharetra.
Maecenas vel porttitor mauris. Proin in interdum est.
Donec facilisis efficitur fermentum. Proin sed laoreet turpis, non pellentesque libero.
Maecenas at nisl iaculis, iaculis mauris ac, eleifend tortor.
In pulvinar tortor vitae bibendum dignissim.
''')

file.seek(0, 0)
print('Lendo arquivo...\n')
print(file.read())

file.close()

# apagando arquivo
os.remove('test.txt')
