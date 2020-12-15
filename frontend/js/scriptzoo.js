$( document ).ready(function() {
	
	$("#conteudoInicial").css("display", "");

	$("#btn_listar_animais").click(function(){
		
		console.log($("#btn_listar_animais").data("id"));

		let id_zoo = $(this).attr('data-id');

		console.log(id_zoo);

		$.ajax({
			url: `http://localhost:5000/listar_animais_por_zoo?id=${id_zoo}`,
			method: 'GET',
			dataType: 'json',
			success: listar_animais,
			error: function() {
				alert("Erro interno ao tentar listar animais!");
			}
		});
		function listar_animais(animais) {

			linhas = ""

			for (var i in animais) {

			  l = `<tr>  
						<td> ${animais[i].nome} </td>
						<td> ${animais[i].nome_cientifico} </td>
						<td> ${animais[i].tamanho} </td>
						<td> ${animais[i].peso} </td>
						<td>
							<a href="#" id="link_remover_animal" data-id=${animais[i].id}>
								Remover
							</a>
						</td>
					</tr>
				`;

			  linhas = linhas + l;
			}

			$("#corpoTabelaAnimais").css("display", "");
			$("#tabelaAnimais").css("display", "");

			$("#corpoTabelaAnimais").html(linhas);

			$("#conteudoInicial").css("display", "none");

			$("#btn_listar_animais").css("display", "none");
			$("#btn_listar_visitantes").css("display", "none");

		}

	});

	$('#btn_listar_visitantes').click(function(){

		console.log($("#btn_listar_visitantes").data("id"));

		let id_zoo = $(this).attr('data-id');

		console.log(id_zoo);

		$.ajax({
			url: `http://localhost:5000/listar_visitantes_por_zoo?id=${id_zoo}`,
			method: 'GET',
			dataType: 'json',
			success: listar_visitantes,
			error: function() {
				alert("Erro interno ao tentar listar visitantes!");
			}
		});
		function listar_visitantes(visitantes) {

			linhas = ""

			for (var i in visitantes) {

				l = `<tr>  
						<td> ${visitantes[i].nome} </td>
						<td> ${visitantes[i].numero_identificacao_universal} </td>
						<td> ${visitantes[i].nivel_de_acesso} </td>
					</tr>
				`;

				linhas = linhas + l;

			}

			$("#corpo_tabela_visitantes").css("display", "");
			$("#tabela_visitantes").css("display", "");

			$("#corpo_tabela_visitantes").html(linhas);

			$("#conteudoInicial").css("display", "none");

			$("#btn_listar_animais").css("display", "none");
			$("#btn_listar_visitantes").css("display", "none");

		}

	});

	$(document).on('click', 'td a', function(event) {

		let id_animal = $(this).attr('data-id');

		$.ajax({
			url: `http://localhost:5000/excluir_animal?id=${id_animal}`,
			method: 'GET',
			success: function(callback){

				if (callback['resultado'] !== "ok"){
					console.log(callback);
				} else {
					
					//alert("Animal excluído com êxito!");
					
					let btn_listar_animais = $('#btn_listar_animais');
					if (typeof btn_listar_animais !== undefined)
						btn_listar_animais[0].click();
					}

			},
			error: function() {
				alert("Erro interno ao tentar excluir animal!");
			}

		});

	});

	$("#btn_incluir_animal").click(function(){

		let nome_animal = $("#nome_animal").val();
		let nome_cientifico = $("#nome_cientifico").val();
		let tamanho = $("#tamanho").val();
		let peso = $("#peso").val();
		let id_zoo = $("#modal_lista_de_zoologicos option:selected").attr('data-id');

		dados = JSON.stringify({nome : nome_animal, nome_cientifico: nome_cientifico, 
			tamanho: tamanho, peso: peso, zoo_id: id_zoo});

		$.ajax({
			url : 'http://localhost:5000/incluir_animal',
			type : 'POST',
			contentType : 'application/json',
			dataType: 'json',
			data: dados,
			success: incluirAnimal,
			error: erroIncluirAnimal
		});
		function incluirAnimal(resposta) {
			
			if (resposta.resultado == "ok") {

				//alert('Animal incluído com êxito');
				
				$("#nome_animal").val("");
				$("#nome_cientifico").val("");
				$("#tamanho").val("");
				$("#peso").val("");

				let btn_listar_animais = $('#btn_listar_animais');

				if (!(typeof btn_listar_animais === "undefined")){

					if (!(typeof btn_listar_animais.attr('data-id') === "undefined")){

						$("#listar_zoos").css("display", "none");

						btn_listar_animais[0].click();
					}
				}

			} else {

				alert('Erro na comunicação com o servidor!');

			}
		}
		function erroIncluirAnimal(resposta) {
			alert("Erro interno ao tentar incluir o animal!");
		}
	});

	$("#link_pagina_inicial").click(function(){

		$("#corpoTabelaAnimais").html("");
		$("#corpo_tabela_visitantes").html("");

		$("#lista_de_zoologicos").html("");
		$("#modal_lista_de_zoologicos").html("");

		$("#conteudoInicial").css("display", "");

		$("#tabelaAnimais").css("display", "none");
		$("#tabela_visitantes").css("display", "none");

		$("#listar_zoos").css("display", "none");

		$("#div_menu_opcoes_listagem").css("display", "none");

	});
	
	$("#link_menu_listar").click(function(){

		$("#lista_de_zoologicos").html("");
		$("#conteudoInicial").css("display", "none");
		$("#tabelaAnimais").css("display", "none");
		$("#tabela_visitantes").css("display", "none");

		$.get('http://127.0.0.1:5000/listar_apenas_zoos', function(data) {

			$("#listar_zoos").css("display", "");

			var ul = document.getElementById("lista_de_zoologicos");

			$.each(data, function(i, v) {
				var li = document.createElement("option");
				var linkText = document.createTextNode(v.nome);
				$(li).attr('data-id', v.id);

				li.appendChild(linkText);
				ul.appendChild(li);
			})

		});

		$("#div_menu_opcoes_listagem").css("display", "none");

	});
	$('#modalInclusao').on('shown.bs.modal', function(){

		$("#modal_lista_de_zoologicos").html("");

		$.get('http://127.0.0.1:5000/listar_apenas_zoos', function(data) {

			$("#modal_lista_de_zoologicos").css("display", "");

			var ul = document.getElementById("modal_lista_de_zoologicos");

			$.each(data, function(i, v) {
				var li = document.createElement("option");
				var linkText = document.createTextNode(v.nome);
				$(li).attr('data-id', v.id);

				li.appendChild(linkText);
				ul.appendChild(li);
			})

		});

	});

	$('#btn_listar').click(function(){

		opcao_escolhida = $("#lista_de_zoologicos option:selected");

		let nome_zoo = opcao_escolhida.html();

		$("#lista_de_zoologicos").html("");
		$("#modal_lista_de_zoologicos").html("");

		$("#listar_zoos").css("display", "none");

		$("#btn_listar_animais").css("display", "");
		$("#btn_listar_visitantes").css("display", "");
		$("#div_menu_opcoes_listagem").css("display", "");
		$("#zoo_titulo").text(nome_zoo);

		$(document.getElementById("btn_listar_animais")).attr('data-id', opcao_escolhida.attr('data-id'));
		$(document.getElementById("btn_listar_visitantes")).attr('data-id', opcao_escolhida.attr('data-id'));

	});

});