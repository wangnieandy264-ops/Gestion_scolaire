class AnneeSscolaire:
    def __init__(self,libelle,id=None,active=False):
        self.libelle = libelle
        self.id = id
        self.active = active
    def __str__(self):
        return f"{self.libelle} "
