class Cliente:
    def __init__(self, nome, fone):
      self._nome = nome
      self._telefone = fone
      
      #Método get      
    def get_nome(self):
      return self._nome
    
      #Método set
    def set_nome(self, nome):
      self._nome = nome  
      
                    