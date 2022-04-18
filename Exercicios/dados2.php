<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        //para evitar erro ao carregar diretamente o php, uma vez que ele busca do formulario.php os dados, usamos o metodo isset - que seria algo como um teste do parametro a ser recebido, junto com ele usamos um operador unario para tratar o resultado deste teste    
        
        $nome = isset($_GET["nome"])?$_GET["nome"]:"[NÃO INFORMADO]";
        $ano = isset($_GET["ano"])?$_GET["ano"]:0;
        $sexo = isset($_GET["sexo"])?$_GET["sexo"]:"[N/A]";
        //Y mostra o ano com quatro digitos 2020
        //y mostra o ano com a forma reduzida 20
        $idade = date("Y") - $ano;
        echo "<p>$nome tem $idade anos e é $sexo</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>