from src.bingo import carton
from jinja2 import Template

template = Template(open('src/plantilla.j2').read())
file = open("bingo.html", "w")
file.write(template.render(matriz = carton()))
file.close()