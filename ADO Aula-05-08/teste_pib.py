from ReadFile import ReadFile
import pprint
pp = pprint.PrettyPrinter(indent=2)


# #Instancia da Classe
read = ReadFile()

# #Método que lê um arquivo e retorna uma lista.
pib_txt = read.list_file('pib.txt')
regioes_txt = read.list_file('regioes.txt')
#--------- # --------- # ---------- # ------------

#Método que calcula o PIB TOTAL por Regioes
soma_regioes = read.sum_regioes(regioes_txt,pib_txt)
teste = read.somatoria(soma_regioes)
print('Somatória do PIB por Regiões')
pp.pprint(teste)
print('------------------------')
#--------- # --------- # ---------- # ------------

# Método que calcula porcentagem do PIB por estado
print('Porcentagem do PIB por Estados')
pib_states = read.pib_states(pib_txt)
pp.pprint(pib_states)
#--------- # --------- # ---------- # ------------



