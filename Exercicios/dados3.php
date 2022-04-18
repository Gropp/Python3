<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
    <title>PHP CURSO ONLINE - FORMULÁRIOS SELECT</title>
    <?php
        //colocamos esse GET no HEAD pois ele ira interferir direto no CSS desta página
        $txt = isset($_GET["t"])?$_GET["t"]:"VALOR PADRÃO";
        $tam = isset($_GET["tam"])?$_GET["tam"]:"12pt";
        $cor = isset($_GET["cor"])?$_GET["cor"]:"#000000";
    ?>
    <style>
        /* AO CHAMAR UMA VARIAVEL DO PHP TEM QUE ESTAR EM UMA INSTANCIA PHP - É IMPORTANTE NO ECHO VC INCLUIR O ; DEPOIS DA VARIAVEL, POIS ESSE ; É DO PHP E O ULTIMO ; É DO CSS!!!!!!!!! */
        span.texto {
            font-size: <?php echo $tam; ?>;
            color: <?php echo $cor; ?>;
        }
    </style>
</head>
<body>
<div>
    <?php
        echo "<span class='texto'>$txt</span><br/>";
    ?>
    <a href="formulario.html">Voltar</a>
</div>
</body>
</html>