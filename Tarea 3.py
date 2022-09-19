listaEstudiantes = []


class Estudiantes(object):
    def __init__(self, _cedula, _nombre, _apellido, _edad, _n1, _n2, _n3):
        self.cedula = _cedula
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.n1 = _n1
        self.n2 = _n2
        self.n3 = _n3
        self.notaFinal = (_n1 + _n2 + _n3) / 3
        self.historial = []

    def entregarDatos(self):
        print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.cedula, self.nombre, self.apellido, self.notaFinal))

    def editarNotas(self, _n1, _n2, _n3):
        self.n1 = _n1
        self.n2 = _n2
        self.n3 = _n3
        self.notaFinal = (_n1 + _n2 + _n3) / 3
        print("Registro Exitoso!")

    def incluirEvento(self, _n1, _n2, _n3):
        return ("modificacion: Nota_1: {} Nota_2: {} Nota_3: {}".format(_n1, _n2, _n3))

    def entregaHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))


def registrarEstudiante():
    print("Registro de Estudiantes\n")
    cedula = int(input("Ingrese el numero de cedula: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese su edad: "))
    n1 = float(input("Ingrese nota 1: "))
    n2 = float(input("Ingrese nota 2: "))
    n3 = float(input("Ingrese nota 3: "))
    objAlumno = Estudiantes(cedula, nombre, apellido, edad, n1, n2, n3)
    listaEstudiantes.append(objAlumno)


def listadoEstudiantes():
    print("Listado de Estudiantes\n")
    for objAlumno in listaEstudiantes:
        objAlumno.entregarDatos()


def buscarEstudiante():
    print("Buscar Estudiante\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            objAlumno.entregarDatos()


def modificarNotas():
    print("Modificar Notas\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            n1 = float(input("Ingrese su nota 1: "))
            n2 = float(input("Ingrese su nota 2: "))
            n3 = float(input("Ingrese su nota 3: "))
            objAlumno.editarNotas(n1, n2, n3)
            objAlumno.entregarDatos()
            recepcionMensaje = objAlumno.incluirEvento(n1, n2, n3)
            objAlumno.historial.append(recepcionMensaje)


def consultarHistorial():
    print("Consulta de Historial\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            for recepcionMensaje in objAlumno.historial:
                print("Evento: {}".format(recepcionMensaje))


def salir():
    print("usted a escogido la opcion salir...!\n")
    print("GRACIAS")
    exit()


def main():
    while True:
        print("\n")
        print("|---------------------------------|")
        print("|--|      Bienvenidos usuarios    |--|")
        print("|--|                Menu          |--|")
        print("|---------------------------------|")
        print("")
        print("Seleccione una de las siguientes opciones presentes:");
        print("1.- Registrar Estudiante")
        print("2.- Mostrar Estudiantes")
        print("3.- Buscar Estudiante")
        print("4.- Modificar notas")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
        elif opcion == 3:
            buscarEstudiante()
        elif opcion == 4:
            modificarNotas()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            salir()


if __name__ == '__main__':
    main();