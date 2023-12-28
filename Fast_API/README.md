para usar el ambiente virtual:

python3.11 -m venv venv

linux:
source venv/bin/activate

pip install -r requirements.txt

Para ejecutar la aplicacion:

uvicorn nombre_archivo:nombre_aplcacion
uvicorn main:app

cambiar el puerto:
uvicorn main:app --port 5000

actualizar cambios a tiempo real:
uvicorn main:app --port 5000 --reload

permitir que otros dispositivos se conecten a la app:
uvicorn main:app --reload --host 0.0.0.0 --port 5000

Docmentacion:
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

