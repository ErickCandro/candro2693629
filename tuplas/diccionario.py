dic={
    "amarillo":"yellow",
    "Azul":"Blue",
    "Verde":"Green",
    "Cafe":"brown",
    "Morado":"Purple",
    "Naranja":"Orange",
    "Negro":"Black",
    "Blanco":"White",
    "Rosado":"Pink",
    "rojo":"Red",
}
color=["yellow","Azul","Verde","Cafe","Morado","Naranja","Negro","Blanco","Rosado","rojo"]

for colores in color:
    if colores in dic:
        print(colores, "->", dic[colores])
    else:
        print(colores,"el color no se encuentra")     