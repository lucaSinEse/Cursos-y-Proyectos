from fastapi import FastAPI, Body, HTTPException, Path, Query, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Coroutine, Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="credenciales son invalidas")

class User(BaseModel):
    email:str
    password:str

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

@app.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=404, content=[])

@app.get('/movies', tags=['movies'],response_model= List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)


@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie_by_id(id:int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=404, content=[])


@app.get('/movies/', tags=['movies'], response_model=Movie )
def get_movie_by_category(category:str = Query(min_length=5, max_length=15))-> List[Movie]:
    
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie:Movie) -> dict:
    movies.append(movie.model_dump())
    return JSONResponse(status_code=201, content={"message": "Se registro la película"})

@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id:int, movie:Movie) -> dict:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            
            return JSONResponse(status_code=200, content={"message": "Se modificó la película"})


@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id:int)-> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"message": "Se eliminó la película"})