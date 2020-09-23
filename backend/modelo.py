from config import *

class Animal(db.Model):

    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254)) 
    nome_cientifico = db.Column(db.String(254))
    tamanho_medio = db.Column(db.Float)
    peso_medio = db.Column(db.Float)

    def __str__(self):
        return self.nome + ", " + self.nome_cientifico + ", " + \
        str(self.tamanho_medio) + ", " + str(self.peso_medio)

    def json(self):
        return {
          "id" : self.id,
          "nome" : self.nome,
          "nome_cientifico" : self.nome_cientifico,
          "tamanho_medio" : self.tamanho_medio,
          "peso_medio" : self.peso_medio
        }        

if __name__ == "__main__":

    db.create_all()

    animal_1 = Animal(nome = "Cachorro", nome_cientifico = "Canninus Lupus", 
      tamanho_medio = 123.0, peso_medio = 60.2)

    animal_2 = Animal(nome = "Gato", nome_cientifico = "Eu sei", 
      tamanho_medio = 30.0, peso_medio = 30.2)

    animal_3 = Animal(nome = "Zebra", nome_cientifico = "Zebrus Zebras", 
      tamanho_medio = 5.0, peso_medio = 10.2929)

    db.session.add(animal_1)
    db.session.add(animal_2)
    db.session.add(animal_3)
    db.session.commit()

    animais = db.session.query(Animal).all()

    for animal in animais:

      print(animal)
      print(animal.json())