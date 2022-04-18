<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS LOOP</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        $oper = isset($_GET["nopc"])?$_GET["nopc"]:1;
        /*$c=1;
        do {
            echo "$oper x $c = ".$oper*$c."<br />";
            $c++;	
        }while($c<=10);*/
        for($c=1; $c<=10; $c++ ) {
            echo "$oper x $c = ".$oper*$c."<br />";
        }
    ?>
    <a href="javascript:history.go(-1)">Voltar</a>
</div>
</body>
</html>