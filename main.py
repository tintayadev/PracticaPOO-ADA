from random import random
import pickle
from clases import Estudiante, Docente, Materia, Paralelo
from collections import defaultdict


def adicionar_materia_a_archivo(materia: Materia, filename="materias.dat"):
    with open(filename, "a+b") as f:
        pickle.dump(materia, f)  # dump -> botar, arrojar


def estudiante_en_dos_materias(filename="materias.dat"):
    repetidos = defaultdict(int)
    with open(filename, "rb") as f:
        while True:
            try:
                materia: Materia = pickle.load(f)
                for paralelo in materia.paralelos:
                    for estudiante in paralelo.estudiantes:
                        repetidos[estudiante] += 1
            except EOFError:  # End of file error, final de archivo
                break
    # print(repetidos)
    for estudiante, conteo in repetidos.items():
        if conteo == 2:
            print(estudiante)


def agregar_auxiliar(materia: Materia, sigla_paralelo: str, filename="materias.dat"):
    pass


def main():
    estudiantes = [
        Estudiante(nombre=f"E{i}", dni=f"{i}" * 3, ru=f"{i}" * 4)
        for i in range(1, 7)
    ]

    docentes = [
        Docente(
            nombre=f"D{i}", dni=f"{i}", sueldo=round(random() * 10000, 2),
            titular=True
        )
        for i in range(8, 11)
    ]

    paralelo_1 = Paralelo(
        sigla="p1",
        docente=docentes[0],
        estudiantes=estudiantes[:2],
        notas=[50, 20]
    )
    paralelo_2 = Paralelo(
        sigla="p2",
        docente=docentes[1],
        estudiantes=estudiantes[2:4],
        notas=[60, 100]
    )
    paralelo_3 = Paralelo(
        sigla="p3",
        docente=docentes[2],
        estudiantes=estudiantes[4:] + [estudiantes[0]],
        notas=[40, 30, 10],
    )

    m1 = Materia(nombre="M1", sigla="M1", paralelos=[paralelo_1, paralelo_2])
    m2 = Materia(nombre="M2", sigla="M2", paralelos=[paralelo_3])

    # Adicionar todas las materias al archivo
    # adicionar_materia_a_archivo(m1)
    # adicionar_materia_a_archivo(m2)
    # Mostrar los estudiantes que están en en ambas materias
    estudiante_en_dos_materias()



if __name__ == "__main__":
    main()
