from fastapi import APIRouter
from ..models.item import Item
from ml.utils.loader import load_model

router = APIRouter()
model = load_model()

@router.post("/predict/")
def predict(item: Item):
    predictions = model.predict(item.data)
    return {"predictions": predictions}
