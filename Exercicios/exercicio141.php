<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - FORMULÁRIOS LOOP - PRIMO</title>
</head>
<body>
<div>
    <?php
        // como o nome dada a variavel no metodo input era v, (name="v"), no php voce usa o metodo GET para "capturar" essa variavel e utiliza-la dentro do codigo de acordo com a sua necessidade!
        $nprimo = isset($_GET["nps"])?$_GET["nps"]:1;
        //IMPORTANTE: O . é o concatenador do PHP não esquecer, o browser nao da erro!
        print "<p>Analisando os números até o numero: $nprimo.</p>"; 
        while ($nprimo >= 1) {
            $arraymult = [];
            $totmult = 0;
            for($c=1; $c<=$nprimo; $c++ ) {
                // o array começa no zero...
                // alimento o array com os resultados que multiplicam
                $mod = $nprimo % $c;
                if($mod == 0) {
                    $arraymult[$totmult] = $c;
                    $totmult++;
                }
            }
            if($totmult == 2){
                print "O NUMERO: $nprimo - é Primo.<br />";
            }
            /*else{
                print "<p class='respri'>O NUMERO: $nprimo - <span>não é Primo.</span></p>";    
            }*/
            $nprimo--;
        }
    ?>
    <a href="javascript:history.go(-1)" class="botao">Voltar</a>
</div>
</body>
</html>