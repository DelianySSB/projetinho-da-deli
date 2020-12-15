from config import *

class Zoo(db.Model):

	zoo_id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(254))
	visitantes = db.relationship(
		"Visitante", backref="visitante", lazy='dynamic'
	)
	animais = db.relationship(
		"Animal", backref="animal", lazy='dynamic'
	)

	def __str__(self):
		
		return f"{self.nome}, {[str(visitante) for visitante in self.visitantes]}, {[str(animal) for animal in self.animais]}"

	def json(self):

		return {

		  "id" : self.zoo_id,
		  "nome" : self.nome

		}

	def json_completo(self):

		return {

		  "id": self.zoo_id,
		  "nome": self.nome,
		  "visitantes": [visitante.json() for visitante in self.visitantes],
		  "animais": [visitante.json() for visitante in self.animais]

		}

class Animal(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(254)) 
	nome_cientifico = db.Column(db.String(254))

	# em centímetros
	tamanho = db.Column(db.Float)

	# em quilogramas
	peso = db.Column(db.Float)

	zoo_id = db.Column(db.Integer, db.ForeignKey("zoo.zoo_id"))
	zoo = db.relationship('Zoo')

	def __str__(self):

		return f"{self.nome}, {self.nome_cientifico}, {str(self.tamanho)}, {str(self.peso)}"

	def json(self):

		return {

		  "id": self.id,
		  "nome": self.nome,
		  "nome_cientifico": self.nome_cientifico,
		  "tamanho": self.tamanho,
		  "peso": self.peso

		}

class Visitante(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(254))
	numero_identificacao_universal = db.Column(db.Integer, nullable=False);
	nivel_de_acesso = db.Column(db.Integer, nullable=False);

	zoo_id = db.Column(db.Integer, db.ForeignKey("zoo.zoo_id"))
	zoo = db.relationship('Zoo')

	def __str__(self):
		
		br = '\n'
		return f"UID: {str(self.numero_identificacao_universal)} | Nome: {self.nome} | Nível de Acesso: {str(self.nivel_de_acesso)}"

	def json(self):

		return {

		  "id": self.id,
		  "nome": self.nome,
		  "numero_identificacao_universal": self.numero_identificacao_universal,
		  "nivel_de_acesso": self.nivel_de_acesso

		}


if __name__ == "__main__":

	if exists(arquivobd):

		rmfile(arquivobd)

	db.create_all()

	# Zoo 1

	zoo_pomerode = Zoo(nome = "Zoo Pomerode")

	visitante_0_1 = Visitante(nome = "José Fernando", numero_identificacao_universal = 1, nivel_de_acesso = 2)
	visitante_0_2 = Visitante(nome = "Kléber Machado", numero_identificacao_universal = 2, nivel_de_acesso = 1)

	zoo_pomerode.visitantes.extend(
		[
			visitante_0_1,
			visitante_0_2
		]
	)

	animal_0_1 = Animal(nome = "Zebra", nome_cientifico = "Equus Quagga", tamanho = 140, peso = 350.12)
	animal_0_2 = Animal(nome = "Gato", nome_cientifico = "Felis Catus", tamanho = 24.50, peso = 4.5)
	animal_0_3 = Animal(nome = "Cachorro", nome_cientifico = "Canis Lupus Familiaris", tamanho = 53, peso = 35.25)

	zoo_pomerode.animais.extend(
		[
			animal_0_1,
			animal_0_2,
			animal_0_3
		]

	)

	db.session.add(zoo_pomerode)

	db.session.add_all([visitante_0_1, visitante_0_2, animal_0_1, animal_0_2, animal_0_3])

	db.session.commit()

	# Zoo 2

	zoo_balneario = Zoo(nome = "Zoo Balneário Camboriú")

	visitante_1_1 = Visitante(nome = "Valdomiro Santiago", numero_identificacao_universal = 1, nivel_de_acesso = 2)
	visitante_1_2 = Visitante(nome = "Vilmar de Noite", numero_identificacao_universal = 2, nivel_de_acesso = 1)

	zoo_balneario.visitantes.extend(
		[
			visitante_1_1,
			visitante_1_2
		]
	)

	animal_1_1 = Animal(nome = "Zebra", nome_cientifico = "Equus Quagga", tamanho = 140, peso = 350.12)
	animal_1_2 = Animal(nome = "Gato", nome_cientifico = "Felis Catus", tamanho = 24.50, peso = 4.5)
	animal_1_3 = Animal(nome = "Cachorro", nome_cientifico = "Canis Lupus Familiaris", tamanho = 53, peso = 35.25)

	zoo_balneario.animais.extend(
		[
			animal_1_1,
			animal_1_2,
			animal_1_3
		]

	)

	db.session.add(zoo_balneario)

	db.session.add_all([visitante_1_1, visitante_1_2, animal_1_1, animal_1_2, animal_1_3])

	db.session.commit()

	print(zoo_pomerode.json())
	print(end='\n\n\n')
	print(zoo_balneario.json())
	print(end='\n\n\n')

	id_zoo = 1
	zoo = db.session.query(Zoo).get(id_zoo)
	print(zoo)