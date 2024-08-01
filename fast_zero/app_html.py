from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title> Nosso Olá Mundo!</title>
        </head>
        <doby>
            <h1> Olá Mundo! </h1>
            <h2> Minha primeira página!</h2
        </doby>
    </html>"""
