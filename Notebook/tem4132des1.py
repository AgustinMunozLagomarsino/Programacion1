# Clase base
class Musico:
    def instrumento(self):
        return "Instrumento genérico"

# Subclase Guitarrista que sobrescribe el método instrumento
class Guitarrista(Musico):
    def instrumento(self):
        return "Toca la guitarra"

# Subclase Baterista que sobrescribe el método instrumento
class Baterista(Musico):
    def instrumento(self):
        return "Toca la batería"

# Demostración de polimorfismo
musicos = [Guitarrista(), Baterista()]

for musico in musicos:
    print(musico.instrumento())
