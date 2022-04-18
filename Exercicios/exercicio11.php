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
        $diaSem = isset($_GET["sem"])?$_GET["sem"]:0;
        switch ($diaSem){
            case 2:
            case 3:
            case 4:
            case 5:
            case 6;
                echo "<p>Levanta!!!</p>";
                echo "<p>Hoje tem Aula! :(</p>";
            break;
            case 7:
            case 8;
                echo "<p>Pode Dormir!!!</p>";
                echo "<p>Chegou o Fim de Semana! :)</p>";
            break;
            default:
                echo "<p>[ERRO] Dia da Semana Inválido!</p>";
        }    
    ?>
    <!-- funcao de javascript para o historico voltar uma pagina -->
    <a href="javascript:history.go(-1)">Voltar</a>
</div>
</body>
</html>