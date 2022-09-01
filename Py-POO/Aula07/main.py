from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Eduardo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
