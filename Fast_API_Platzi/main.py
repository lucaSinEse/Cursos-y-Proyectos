from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'
app.version = "0.0.1"

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

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "overviewwwwwwwwww",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "overviewwwwwwwwww",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World!</h1>')


@app.get('/movies', tags=['movies'], response_class=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie_by_id(id:int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get('/movies/', tags=['movies'], response_class=List[Movie])
def get_movie_by_category(category:str = Query(min_length=5, max_length=15))-> List[Movie]:
    
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'], response_model=dict)
def create_movie(movie:Movie) -> dict:
    movies.append(movie.model_dump())
    return JSONResponse(content={"message": "Se registro la película"})

@app.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id:int, movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            
            return JSONResponse(content={"message": "Se modificó la película"})


@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id:int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se eliminó la película"})