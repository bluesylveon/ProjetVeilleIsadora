from priorite import Priorite
class Note:
    # TODO: MaAYBE AJOUTER INDEX?
    def __init__(self, id=0, titre="", contenu="", priorite: Priorite = Priorite.Faible):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.priorite = priorite
        self.is_complete = False

    def get_id(self) -> str:
        return self.id

    def get_titre(self) -> str:
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre

    def get_contenu(self) -> str:
        return self.contenu
    
    def set_contenu(self, contenu):
        self.contenu = contenu

    def get_priorite(self) -> Priorite:
        return self.priorite
    
    def set_priorite(self, priorite):
        self.priorite = priorite

    def get_is_complete(self) -> bool:
        return self.is_complete
    
    def set_is_complete(self, is_complete):
        self.is_complete = is_complete