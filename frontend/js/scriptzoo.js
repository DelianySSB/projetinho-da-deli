$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("invisible");

    $("#link_listar_animais").click(function(){
        
        $.ajax({
            url: 'http://localhost:5000/listar_animais',
            method: 'GET',
            dataType: 'json',
            success: listar_animais,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_animais(animais) {

            linhas = ""

            for (var i in animais) {

              l = "<tr>" + 
              "<td>" + animais[i].nome + "</th>" + 
              "<td>" + animais[i].nome_cientifico + "</td>" + 
              "<td>" + animais[i].tamanho_medio + "</td>" + 
              "<td>" + animais[i].peso_medio + "</td>" +
              "</tr>";

              linhas = linhas + l;
            }

            $("#corpoTabelaAnimais").html(linhas);

            $("#conteudoInicial").addClass("invisible");
            $("#tabelaAnimais").addClass("invisible");

            $("#tabelaAnimais").removeClass("invisible");
        }

    });

    $("#btn_incluir_animal").click(function(){

        nome_animal = $("#nome_animal").val();
        nome_cientifico = $("#nome_cientifico").val();
        tamanho_medio = $("#tamanho_medio").val();
        peso_medio = $("#peso_medio").val();

        dados = JSON.stringify({nome : nome_animal, nome_cientifico: nome_cientifico, 
            tamanho_medio: tamanho_medio, peso_medio: peso_medio});

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

                alert('Animal incluído com sucesso');
                
                $("#nome_animal").val("");
                $("#nome_cientifico").val("");
                $("#tamanho_medio").val("");
                $("#peso_medio").val("");

            } else {

                alert('Erro na comunicação');

            }
        }
        function erroIncluirAnimal(resposta) {
            alert("Deu ruim na chamada ao back-end");
        }
    });

    $("#link_pagina_inicial").click(function(){

        $("#corpoTabelaAnimais").html("");

        $("#conteudoInicial").addClass("invisible");
        $("#conteudoInicial").removeClass("invisible");

        $("#tabelaAnimais").addClass("invisible");

    });
    
  });