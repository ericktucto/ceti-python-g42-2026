import requests

def main() -> None:
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    datos = r.json()
    print(datos)
    print("Hola a todos!")
