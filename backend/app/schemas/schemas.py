from pydantic import BaseModel, EmailStr

class ListIng(BaseModel):
    items: list[str]
class RecipeResponse(BaseModel):
    recipe: str