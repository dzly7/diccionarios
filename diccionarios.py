def ejercicio_1():
    print("\n--- Ejercicio 1: Agenda telefónica ---")
    agenda = {
        "Ana": "55-1234-5678",
        "Luis": "55-8765-4321",
        "Sofía": "55-1111-2222",
    }
    nombre = "Luis"
    print(f"Teléfono de {nombre}: {agenda.get(nombre, 'No registrado')}")
    print(f"Teléfono de Pedro: {agenda.get('Pedro', 'No registrado')}")


def ejercicio_2():
    print("\n--- Ejercicio 2: Frecuencia de palabras ---")
    texto = "el perro y el gato y el raton"
    frecuencia = {}
    for palabra in texto.split():
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    for palabra, veces in frecuencia.items():
        print(f"{palabra}: {veces}")


def ejercicio_3():
    print("\n--- Ejercicio 3: Alumnos por matrícula ---")
    lista_alumnos = [
        ("2025001", "Carlos Pérez", 9.1),
        ("2025002", "María López", 8.5),
        ("2025003", "Jorge Ruiz", 7.8),
    ]
    indice = {}
    for matricula, nombre, promedio in lista_alumnos:
        indice[matricula] = {"nombre": nombre, "promedio": promedio}

    buscar = "2025002"
    if buscar in indice:
        alumno = indice[buscar]
        print(f"{buscar}: {alumno['nombre']} - Promedio {alumno['promedio']}")
    else:
        print("Matrícula no encontrada")


def ejercicio_4():
    print("\n--- Ejercicio 4: Inventario ---")
    inventario = {"manzana": 50, "pera": 30, "plátano": 20}
    inventario["uva"] = 15
    inventario["pera"] -= 5
    inventario.pop("plátano")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} piezas")


def ejercicio_5():
    print("\n--- Ejercicio 5: Índice invertido ---")
    documentos = {
        1: "python es un lenguaje facil",
        2: "los diccionarios en python son rapidos",
        3: "un arbol es una estructura de datos",
    }
    indice = {}
    for id_doc, texto in documentos.items():
        for palabra in texto.split():
            indice.setdefault(palabra, set()).add(id_doc)

    for buscar in ["python", "es", "java"]:
        print(f"'{buscar}' aparece en documentos: {sorted(indice.get(buscar, []))}")


def ejercicio_6():
    print("\n--- Ejercicio 6: Agrupar por inicial ---")
    palabras = ["casa", "perro", "carro", "pato", "mesa", "coco"]
    grupos = {}
    for p in palabras:
        inicial = p[0]
        if inicial not in grupos:
            grupos[inicial] = []
        grupos[inicial].append(p)
    for letra in sorted(grupos):
        print(f"{letra}: {grupos[letra]}")


def ejercicio_7():
    print("\n--- Ejercicio 7: Dos números que suman un objetivo ---")
    numeros = [2, 7, 11, 15, 4]
    objetivo = 15
    vistos = {}
    for i, num in enumerate(numeros):
        falta = objetivo - num
        if falta in vistos:
            print(f"{falta} + {num} = {objetivo} (posiciones {vistos[falta]} y {i})")
            return
        vistos[num] = i
    print("No hay pareja que sume el objetivo")


def ejercicio_8():
    print("\n--- Ejercicio 8: Primer elemento repetido ---")
    datos = [5, 3, 8, 1, 3, 9, 5]
    vistos = {}
    for d in datos:
        if d in vistos:
            print(f"El primer repetido es: {d}")
            return
        vistos[d] = True
    print("No hay repetidos")


def ejercicio_9():
    print("\n--- Ejercicio 9: Traductor ---")
    traductor = {"hola": "hello", "mundo": "world",
                 "gato": "cat", "perro": "dog", "casa": "house"}
    frase = "hola mundo perro azul"
    traducida = [traductor.get(p, f"[{p}]") for p in frase.split()]
    print(f"Español: {frase}")
    print(f"Inglés:  {' '.join(traducida)}")


class TablaHash:
    def __init__(self, tamano=7):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        return sum(ord(c) for c in str(clave)) % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        casilla = self.tabla[indice]
        for par in casilla:
            if par[0] == clave:
                par[1] = valor
                return
        casilla.append([clave, valor])

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

    def mostrar(self):
        for i, casilla in enumerate(self.tabla):
            print(f"  [{i}] -> {casilla}")


def ejercicio_10():
    print("\n--- Ejercicio 10: Tabla hash con encadenamiento ---")
    th = TablaHash(5)
    for clave, valor in [("ana", 20), ("luis", 22), ("naa", 19),
                         ("pedro", 25), ("sofia", 21)]:
        th.insertar(clave, valor)
    th.mostrar()
    print(f"Buscar 'naa': {th.buscar('naa')}")
    print(f"Buscar 'jose': {th.buscar('jose')}")


if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()
    ejercicio_9()
    ejercicio_10()
