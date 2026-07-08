from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.models.model  import RecipeList
from app.core.ai import get_recipe_from_chef_claude



app = FastAPI()
origins = [
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/getrecipe", status_code=status.HTTP_202_ACCEPTED)
def get_recipe(array: schemas.ListIng, db: Session = Depends(get_db)):
    recipe = get_recipe_from_chef_claude(array.items)
    return {"recipe": recipe}
    