from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy import ARRAY, String


class RecipeList(Base):
    __tablename__ = "RecipeList"

    id = Column(Integer, nullable=False, primary_key=True)
    items = Column(ARRAY(String), nullable=False)
   
