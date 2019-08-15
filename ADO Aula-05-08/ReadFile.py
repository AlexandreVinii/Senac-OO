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
        regioes = self.lista_reg
        for i in range(len(self.lista_pib)):
            for j in range(len(self.lista_reg)):
                if self.lista_pib[i][0] == self.lista_reg[j][0]:
                    aux = self.lista_pib[i][1]
                    regioes[j].append(aux)
        norte = read.sum(regioes[1:8])
        nordeste = read.sum(regioes[10:19])
        sudeste = read.sum(regioes[21:25])
        sul = read.sum(regioes[27:30])
        centro_oeste = read.sum(regioes[32:])
        dicionario = {
            'Norte': norte,
            'Nordeste': nordeste,
            'Sudeste': sudeste,
            'Sul': sul,
            'Centro-Oeste': centro_oeste
        }
        return dicionario
    """
                    
    dala 
    """
    def to_dict(self, lista):
        self.lista = lista
        dic = {k: v for k, v in self.lista}
        return dic
