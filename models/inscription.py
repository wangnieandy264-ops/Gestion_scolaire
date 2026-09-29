class Inscription :
    def __init__(self,id=None,eleve_id=None,annees_scolaires_id=None,classes_id=None,transport=False):
        self.id = id
        self.eleve_id = eleve_id
        self.annees_scolaires_id= annees_scolaires_id
        self.classes_id = classes_id
        self.transport = transport
    def __str__(self):
        return f"{self.eleve_id}-{self.annees_scolaires_id}-{self.classes_id}-Transport:{self.transport}"