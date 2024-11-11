# Clase base para todos los empleados de la biblioteca
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def descripcion(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: ${self.salario}"

# Clase Administrador que representa un rol adicional mediante composición
class Administrador:
    def gestionar_recursos(self):
        return "Gestionando recursos de la biblioteca."

# Clase Mantenimiento que representa un rol adicional mediante composición
class Mantenimiento:
    def realizar_mantenimiento(self):
        return "Realizando mantenimiento de las instalaciones."

# Subclase Gerente que hereda de Empleado y puede tener habilidades administrativas
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, administrador=None):
        super().__init__(nombre, edad, salario)
        self.administrador = administrador  # Composición con Administrador

    def descripcion(self):
        descripcion = super().descripcion() + " (Gerente)"
        if self.administrador:
            descripcion += " - Rol adicional: Administrador"
        return descripcion

# Subclase Tecnico que hereda de Empleado y puede tener habilidades de mantenimiento
class Tecnico(Empleado):
    def __init__(self, nombre, edad, salario, mantenimiento=None):
        super().__init__(nombre, edad, salario)
        self.mantenimiento = mantenimiento  # Composición con Mantenimiento

    def descripcion(self):
        descripcion = super().descripcion() + " (Técnico)"
        if self.mantenimiento:
            descripcion += " - Rol adicional: Mantenimiento"
        return descripcion

# Clase Voluntario, que también es un tipo de empleado pero sin salario fijo
class Voluntario(Empleado):
    def __init__(self, nombre, edad, horas_voluntariado):
        super().__init__(nombre, edad, salario=0)
        self.horas_voluntariado = horas_voluntariado

    def descripcion(self):
        return (f"Voluntario: {self.nombre}, Edad: {self.edad}, "
                f"Horas de voluntariado: {self.horas_voluntariado}")

# Ejemplo de uso
# Creación de instancias de roles adicionales
admin = Administrador()
mantenimiento = Mantenimiento()

# Creación de empleados con roles adicionales
gerente = Gerente("Ana López", 40, 55000, administrador=admin)
tecnico = Tecnico("Carlos Díaz", 35, 40000, mantenimiento=mantenimiento)
voluntario = Voluntario("María Pérez", 25, 120)

# Imprimir descripción de cada empleado
print(gerente.descripcion())
print(tecnico.descripcion())
print(voluntario.descripcion())

# Mostrar habilidades adicionales si existen
if gerente.administrador:
    print(gerente.administrador.gestionar_recursos())

if tecnico.mantenimiento:
    print(tecnico.mantenimiento.realizar_mantenimiento())
