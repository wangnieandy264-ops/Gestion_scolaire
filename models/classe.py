class Classe :
    def __init__(self,nom,id=None):
        self.id = id
        self.nom = nom
    def __str__(self):
        return f"{self.nom} "