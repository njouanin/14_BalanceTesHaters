from datetime import datetime

from pydantic import BaseModel


class Auteur(BaseModel):
    name: str
    href: str


class Publication(BaseModel):
    url: str
    auteur: Auteur
    date_publication: datetime
    texte_publication: str | None = None
    commentaires: list["Commentaire"]


class Commentaire(BaseModel):
    auteur: Auteur
    date_commentaire: datetime | None = None
    texte_commentaire: str
    screenshot: str
    reponses: list["Commentaire"] | None = None
