<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS IF ANINHADOS</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        $nota1 = isset($_GET["n1"])?$_GET["n1"]:0;
        $nota2 = isset($_GET["n2"])?$_GET["n2"]:0;
        $media = ($nota1 + $nota2)/2;
        echo "<p>A média entre $nota1 e $nota2 é $media.</p>";
        if ($media >= 0 && $media < 5) {
            $resultado = "[REPROVADO]";
        }
        elseif ($media >= 5 && $media < 7) {
                $resultado = "[RECUPERAÇÃO]";  
            }
            else {
                    $resultado = "[APROVADO]";     
                }
        echo "<p>Você está $resultado.</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>