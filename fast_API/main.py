from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi primera aplicacion con FastAPI"
app.version = "2.0.0"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "accion"
    },
    {
        "id": 2,
        "title": "Avengers",
        "overview": "iron man y compañia hacen cosas",
        "year": "2011",
        "rating": 8.0,
        "category": "aventura"
    }
]

@app.get('/', tags=["Home"])
def home():
    return HTMLResponse("<h1>Hello world</h1>")

@app.get('/movies', tags=["Movies"])
def home():
    return movies

#Parametro de ruta (valor)
@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id:int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []

#Parametro query (clave y valor)
@app.get('/movies/', tags=["Movies"])
def get_movie_by_category(category:str):
    for movie in movies:
        if movie["category"] == category :
            return movie
    return []

#Metodo Post
@app.post('/movies', tags=["Movies"])
def create_movie(
    id:int = Body(),
    title:str = Body(),
    overview:str = Body(),
    year:int = Body(),
    rating:float = Body(),
    category:str = Body()
):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies

#Metodo Put
@app.put('/movies/{id}', tags=["Movies"])
def update_movie(
    id:int,
    title:str = Body(),
    overview:str = Body(),
    year:int = Body(),
    rating:float = Body(),
    category:str = Body()
):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
    return movies

#Metodo Delete
@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(
    id:int
):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies