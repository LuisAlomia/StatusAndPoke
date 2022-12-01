from flask import Flask
import requests
import psutil
import platform

app = Flask(__name__)

# Enpoint
URL_POKEAPI = 'https://pokeapi.co/api/v2/pokemon/pikachu'


@app.route("/")
def main():
    return {"poke": "http://127.0.0.1:5000/api/v1/poke",
            "status": "http://127.0.0.1:5000/api/v1/status"}

# Regresa una lista con el nombre de las habilidades del pokemon


@app.get("/api/v1/poke")
def poke():
    try:
        response = requests.get(URL_POKEAPI)
        response = response.json()

        ability_name = []

        response = response["abilities"]

        for value in response:
            ability_name.append(value["ability"]["name"])

        resp = {"abilities_name": ability_name,
                "back": "http://127.0.0.1:5000/"}

        if ability_name.__len__() > 0:
            return resp, 200
        else:
            return {"message": "there are no skills"}

    except Exception as e:
        return {"message": "server error"}, 500

# Esta ruta proporsiona info sobre el servidor y PC


@app.get("/api/v1/status")
def status():

    response = [{"status server": "200 OK",
                "ram": F"{round(psutil.virtual_memory()[0]/1000000000)} G",
                 "operating system": platform.system()},
                {"back": "http://127.0.0.1:5000/"}]

    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
