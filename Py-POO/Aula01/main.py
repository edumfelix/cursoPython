from pessoa import Pessoa

p1 = Pessoa('Eduardo', 18)
p2 = Pessoa('Luiz', 32)

p1.falar('POO')
p2.falar('Filmes')
p1.comer('Churrasco')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.ano_atual)