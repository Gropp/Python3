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
        $valor = $_GET["v"];
        echo "<p>Você digitou o valor $valor </p>";
        $rq = sqrt($valor);
        echo "<p>A raiz quadrada deste numero é igual a ".number_format($rq,2)."</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>