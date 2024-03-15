from pydantic import BaseModel, Field
from typing import  Optional
class Movie(BaseModel):
    id:Optional[int] = None
    title:str = Field(max_length=15, min_length=5)
    overview:str = Field(max_length=50, min_length=15)
    year:int = Field(le=2024, ge=1900)
    rating:float = Field(le=10, ge=1)
    category:str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            'example': {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "descripcion",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }