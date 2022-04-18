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
        $primo = isset($_GET["np"])?$_GET["np"]:1;
        //IMPORTANTE: O . é o concatenador do PHP não esquecer, o browser nao da erro!
        print "<p>Analisando o número: $primo.</p>";
        $arraymult = [];
        $totmult = 0;
        for($c=1; $c<=$primo; $c++ ) {
        // o array começa no zero...
        // alimento o array com os resultados que multiplicam
            $mod = $primo % $c;
            if($mod == 0) {
                $arraymult[$totmult] = $c;
                $totmult++;
            }
        }
        print "<p>Total de multiplos => $totmult.</p>";
        print "<p>Os Multiplos são: ";
        for($p=0;$p<$totmult;$p++){
            print "$arraymult[$p] ";
        }
        //esse print abaixo fecha o <p> do print antes do for...
        print ".</p>";
        if($totmult == 2){
            print "<p class='respri'>Resultado: $primo - <span>é Primo.</span></p>";
        }else{
            print "<p class='respri'>Resultado: $primo - <span>não é Primo.</span></p>";    
        }
    ?>
    <a href="javascript:history.go(-1)" class="botao">Voltar</a>
</div>
</body>
</html>