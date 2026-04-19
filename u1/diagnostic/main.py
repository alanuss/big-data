"""
crear un program que permita ingresar el nombre, el rut, el departamento (informática, contabilidad, RRHH) y sueldo de los n trabajadores de una empresa. Posteriormente calcule e imprima lo siguiente:
    - Cantidad de trabjadores por departamento
    - Los datos de el o los trabajadores del departamento de informática con mayor sueldo
    - Los datos de él o los trabajadores con el menor suelo en la empresa
"""


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []

    def addPersona(self, persona):
        self.personas.append(persona)

    def getPersonas(self):
        return self.personas

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre


class Persona:
    def __init__(self, nombre: str, rut: str, departamento: str, sueldo: float):
        self.nombre = nombre
        self.rut = rut
        self.departamento = departamento
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre} \nRut: {self.rut} \nDepartamento: {self.departamento} \nSueldo: {self.sueldo}"

    def getNombre(self):
        return self.nombre

    def getRut(self):
        return self.rut

    def getDepartamento(self):
        return self.departamento

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRut(self, rut):
        self.rut = rut

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getSueldo(self):
        return self.sueldo

    def setSueldo(self, sueldo):
        self.sueldo = sueldo


DEPARTAMENTOS = {
    "informatica": Departamento("informatica"),
    "contabilidad": Departamento("contabilidad"),
    "RRHH": Departamento("RRHH"),
}


n_trabajadores = int(input("Ingrese el numero de trabajadores de la empresa: "))
for n in range(n_trabajadores):
    print(f"Ingrese los datos del trabajador {n + 1}")
    nombre = input("Nombre: ")
    rut = input("Rut: ")
    departamento = input("Departamento: ")
    sueldo = float(input("Sueldo: "))

    persona = Persona(nombre, rut, departamento, sueldo)
    departamento_entity = DEPARTAMENTOS[departamento]

    departamento_entity.addPersona(persona)


for key, value in DEPARTAMENTOS.items():
    print(
        f"Cantidad de personas en el departamento de {key}: ",
        len(value.getPersonas()),
    )

personas_informatica = DEPARTAMENTOS.get("informatica").getPersonas()
sorted_personas_informatica = sorted(
    personas_informatica,
    key=lambda persona: persona.getSueldo(),
)
