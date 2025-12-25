from balanceteshaters.routers.ml_model import Publication
from fastapi import APIRouter
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7",
)
router = APIRouter()

labels = [
    "Haineux",
    "Neutre",
    "Positif",
    "Négatif",
    "Toxique",
    "Agressif",
    "Homophobie",
    "Grossophobie",
    "Sexisme",
    "Racisme",
    "Antisémitisme",
    "Islamophobie",
]


@router.post("/publication")
def ml_publication(publication: Publication):
    results = []
    for commentaire in publication.commentaires:
        result = classifier(commentaire.texte_commentaire, candidate_labels=labels)
        results.append({"commentaire": commentaire.texte_commentaire, "result": result})
    print(results)
    return {"result": results}
