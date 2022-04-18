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
        $numero = isset($_GET["num"])?$_GET["num"]:0;
        $opcao = isset($_GET["opc"])?$_GET["opc"]:1;
        switch ($opcao){
            case 1:
                $res = $numero*2;
                $tipo = "dobro";
            break;
            case 2:
                $res = $numero*$numero*$numero;
                $tipo = "cubo";
            break;
            case 3:
                $res = sqrt($numero); //$numero ^ (1/2);
                $tipo = "raiz²";
            break;
            default:
                echo "<p>[ERRO]</p>";
        }    
        echo "<p>O(A) $tipo do número $numero é $res.</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>