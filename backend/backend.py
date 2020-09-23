from config import *
from modelo import Animal

@app.route("/")
def padrao():
    return "Rota padrão back-end"

@app.route("/listar_animais")
def listar_animais():

    animais = db.session.query(Animal).all()
    retorno = []

    for animal in animais:
        retorno.append(animal.json())

    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta

@app.route("/incluir_animal", methods=['post'])
def incluir_animal():

    dados = request.get_json()
    novo_animal = Animal(**dados)
    db.session.add(novo_animal)
    db.session.commit()
    return {"resultado":'ok'}#.headers.add("Access-Control-Allow-Origin", "*")

if __name__ == "__main__":
    
    print("test")

    app.run(debug=True)
