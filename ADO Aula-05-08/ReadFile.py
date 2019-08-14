class ReadFile:

    def list_file(self, arquivo):
        self.arquivo = arquivo
        f = open(self.arquivo, "r")
        aux = []
        lista = []
        for l in f:
            aux.append(l)

        for i in range(len(aux)):
            lista.append(aux[i].strip().split(';'))
        return lista

    def pib_total(self, lista):
        self.lista = lista
        aux = 0
        pib = lista
        for i in range(len(pib)):
            aux += float(pib[i][1])
        return round(aux, 2)

    def sum(self, lista):
        self.lista = lista
        aux = 0
        pib = lista
        for i in range(len(pib)):
            aux += float(pib[i][1])
        return round(aux, 2)

    def pib_states(self, lista):
        self.lista = lista
        read = ReadFile()
        total = read.pib_total(self.lista)
        for i in range(len(self.lista)):
            aux = (float(lista[i][1])/total)*100
            self.lista[i][1] = f'{aux:.2f}% - PIB'

        pib = read.to_dict(self.lista)
        return pib

    def sum_regioes(self, lista_reg, lista_pib):
        self.lista_reg = lista_reg
        self.lista_pib = lista_pib
        read = ReadFile()
        pos = []
        teste = 0
        regioes = self.lista_reg
        for i in range(len(self.lista_reg)):
            if self.lista_reg[i][0] == 'Norte':
                x = 0
                regioes[i].append(x)
            if self.lista_reg[i][0] == 'Nordeste':
                x = 0
                regioes[i].append(x)
            if self.lista_reg[i][0] == 'Sul':
                x = 0
                regioes[i].append(x)
            if self.lista_reg[i][0] == 'Sudeste':
                x = 0
                regioes[i].append(x)
            if self.lista_reg[i][0] == 'Centro-Oeste':
                x = 0
                regioes[i].append(x)
            for j in range(len(self.lista_pib)):
                if self.lista_pib[j][0] == self.lista_reg[i][0]:
                    aux = self.lista_pib[j][1]
                    regioes[i].append(float(aux))

            # print('Regioes Som ', regioes[i])

        return regioes
    def somatoria(self, lista):
        self.lista = lista
        for n in self.lista:
            if n != ['']:
                print(n[1])

    def to_dict(self, lista):
        self.lista = lista
        dic = {k: v for k, v in self.lista}
        return dic
