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
            if self.lista_reg[i][0] == '' :
                x = None
                regioes[i].append(x)
            for j in range(len(self.lista_pib)):
                if self.lista_pib[j][0] == self.lista_reg[i][0]:
                    aux = self.lista_pib[j][1]
                    regioes[i].append(float(aux))

            # print('Regioes Som ', regioes[i])

        return regioes
    def somatoria(self, lista):
        pega = []
        vai = []
        aux = 0
        test = []
        a = []
        self.lista = lista
        for i in range(len(self.lista)):
            if self.lista[i][1] == None or self.lista[i][1] != 0:
                vai.append(self.lista[i][1])
        # print('ss ',vai)
        for k in range(len(vai)):
            print(k)
            if vai[k] == None:
                pega.append(k)
        for n in pega:
            aux = sum([j for j in vai[:n] if isinstance(j, int) or isinstance(j, float)])
            test.append(aux)
                
        for s in range(len(test)):
            print('num ',s)
            if s == 0:
                a.append(test[s])
            elif s == len(test) - 1:
                a.append(test[s] - test[s-1])
            else:
                a.append(test[s] - test[s+1])


        return a
        

               

    def to_dict(self, lista):
        self.lista = lista
        dic = {k: v for k, v in self.lista}
        return dic