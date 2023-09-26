from dataclasses import dataclass, field
from hashlib import sha256
# from typing import Optional


@dataclass
class Persona:
    nombre: str
    dni: str


@dataclass
class Estudiante(Persona):
    ru: str

    def __hash__(self):
        # self.ru.encode()                      -> representacion unicode en bytes
        # sha256(self.ru.encode())              -> provee una funcion hash de encriptacion
        # sha256(self.ru.encode()).hexdigest()  -> convierte a hexadecimal en str
        # int(sha256(self.ru.encode()).hexdigest(), 16) -> convierte la cadena hexadecimal a int
        return int(sha256(self.ru.encode()).hexdigest(), 16)


@dataclass
class Docente(Persona):
    sueldo: float
    titular: bool


@dataclass
class Auxiliar(Estudiante):
    sueldo: int
    nro_item: int


# 3.9 < Optional[Auxiliar]
@dataclass
class Paralelo:
    sigla: str
    docente: Docente
    auxiliar: Auxiliar | None = None
    estudiantes: list[Estudiante] = field(default_factory=list)
    notas: list[int] = field(default_factory=list)  # campo


@dataclass
class Materia:
    nombre: str
    sigla: str
    paralelos: list[Paralelo] = field(default_factory=list)
