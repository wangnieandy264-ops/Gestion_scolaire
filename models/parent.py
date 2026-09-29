class Parent:
    def __init__(self, nom,telephone=None,email=None,adresse=None):
        self.nom = nom
        self.telephone = telephone
        self.email = email
        self.adresse = adresse
    def __str__(self):
        return self.nom