class Estado:
    def __init__(self,estado,sigla): 
        self.nome_estado = estado
        self.sigla = sigla
        self.pais = 'Brasil'
        self.qt_estado = 0

    def retornaAtributos(self):
        return f'--> {self.nome_estado:<40}{self.sigla:<3}- total de Casos: {self.qt_estado:>5}'

    def getNomeEstado(self):
        return self.nome_estado
    
    def getSigla(self):
        return self.sigla
        
    def atualizarCasos(self,tcasos):
        #pegar de todas cidades do estado escolhido
        self.qt_estado = tcasos
    

class Cidade:
    def __init__(self,nome,casos,estado):
        self.nome_cidade = nome
        self.qt_casos = casos
        self.estado = estado 

    def getCasos(self):
        return self.qt_casos
    
    def retornaAtributos(self):
        return f'--> {self.nome_cidade:<40}- Casos Registrados: {self.qt_casos:>5}'

    def getCidade(self):
        return self.nome_cidade
    
    def getEstado(self):
        return self.estado
    
    def atualizaCasos(self,casos):
        self.qt_casos += casos


