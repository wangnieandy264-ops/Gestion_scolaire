class Eleve :
    def __init__(self,nom,prenom,matricule,id,date_naissance=None,parent_id=None,) :
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.date_naissance = date_naissance
        self.id = id
        self.parent_id = parent_id

    def nom_complet(self) :
        return f"{self.nom} {self.prenom}"
    def __str__(self):
        return f"{self.matricule} {self.nom_compelt()}"