from config import *
from modelo import Zoo, Animal, Visitante

@app.route("/")
def padrao():
	return "Rota padrão back-end"

@app.route("/listar_animais_todos_zoos")
def listar_animais():

	animais = db.session.query(Animal).all()
	retorno = []

	for animal in animais:
		retorno.append(animal.json())

	resposta = jsonify(retorno)
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/listar_animais_por_zoo", methods=['GET'])
def listar_animais_por_zoo():

	id_zoo = int(request.args.get("id"))

	animais = db.session.query(Animal).all()

	retorno = []

	for animal in animais:

		if (animal.zoo_id == id_zoo):

			retorno.append(animal.json())

	resposta = jsonify(retorno)
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/listar_zoos")
def listar_zoos():

	zoos = db.session.query(Zoo).all()
	retorno = []

	for zoo in zoos:
		retorno.append(zoo.json_completo())

	resposta = jsonify(retorno)
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/listar_apenas_zoos")
def listar_apenas_zoos():

	zoos = db.session.query(Zoo).all()
	retorno = []

	for zoo in zoos:
		retorno.append(zoo.json())

	resposta = jsonify(retorno)
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/listar_visitantes_por_zoo", methods=['GET'])
def listar_visitantes_por_zoo():

	id_zoo = int(request.args.get("id"))

	visitantes = db.session.query(Visitante).all()

	retorno = []

	for visitante in visitantes:

		if (visitante.zoo_id == id_zoo):

			retorno.append(visitante.json())

	resposta = jsonify(retorno)
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/incluir_animal", methods=['POST'])
def incluir_animal():

	dados = request.get_json()

	novo_animal = Animal(**dados)
	db.session.add(novo_animal)
	db.session.commit()

	return {
				"resultado":'ok'
			}

@app.route("/excluir_animal", methods=['GET'])
def excluir_animal():

	resposta = jsonify(
						{
							"resultado": "ok",
							"detalhes": "ok"
						}
					)

	try:
		
		id = int(request.args.get("id"))

		animal = db.session.query(Animal).get(id)
		
		if (animal is not None):

			db.session.delete(animal)
			db.session.commit()

		else:

			resposta = jsonify(
								{
									"resultado": "erro",
								 	"detalhes": "Informação sobre o animal não encontrada."
								}
							)

	except Exception as e:

		resposta = jsonify(
							{
								"resultado": "erro",
								"detalhes": str(e)
							}
						)

	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

if __name__ == "__main__":
	
	app.run(debug=True)