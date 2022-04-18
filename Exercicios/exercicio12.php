<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS SWITCH</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        $opcao = isset($_GET["opc"])?$_GET["opc"]:"ER";
        switch ($opcao){
            case "N":
                echo "<p>REGIÃO NORTE</p>";
            break;
            case "NE":
                echo "<p>REGIÃO NORDESTE</p>";
            break;
            case "CO":
                echo "<p>REGIÃO CENTRO-OESTE</p>";
            break;
            case "SE":
                echo "<p>REGIÃO SULDESTE</p>";
            break;
            case "S":
                echo "<p>REGIÃO SUL</p>";
            break;
            default:
                echo "<p>[ERRO] ESTADO INVÁLIDO</p>";
        }    
        echo "<p>VIAJE - CONHEÇA O BRASIL</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>