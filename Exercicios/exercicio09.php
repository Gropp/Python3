<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS CONDICIONAIS #9</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        $a = isset($_GET["ano"])?$_GET["ano"]:1900;
        $i = date("Y") - $a;
        echo "<p>Você nasceu em $a e tem $i ano(s).</p>";
        if ($i>=18) {
            $v = "ja pode votar";
            $d = "ja pode dirigir";
        }
        else {
            $v = "não pode votar";
            $d = "não pode dirigir";
        }
        echo "<p>Com essa idade, você $v e $d.</p>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>