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

    def to_dict(self, lista):
        self.lista = lista
        dic = {k:v for k,v in self.lista}
        return dic
    
    