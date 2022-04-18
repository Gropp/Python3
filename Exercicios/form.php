<!DOCTYPE>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - VARIAVEIS VARIANTES</title>
</head>
<body>
<div>
	<h1>PHP - curso online</h1>
	<h2>Treinamneto de uso e recursos do PHP</h2>
	<p>Criação de variaveis variantes para recebimento de parametros dinamicos #11</p>
</div>
<div>
	<?php #SUPERTAG
		/* 
		echo comando de saida para tela
		$no = (string) "Fernando"; FORÇA A ATRIBUIÇÃO DA VARIAVEL
		*/
		$i = 1;
		//esse loop vai pegar os dados da URL do v1 ao v5 criados dinamicamente
		//$$v -> num.$i = $_GET["v$i"] com uma variavel referenciavel, conseguimos criar as variaveis v$i dinamicamente e ainda colocar os valores delas nas variaveis num$i!! MUITO INTERESSANTE ESSE RECURSO 
		while ($i <= 5) {
			$v = "num".$i; //$v vai criar as variaveis num1 ate num5
			$url = "v".$i; //$url vai receber o name do form de v1 até v5 criado no PHP que chamou esse!
			$$v = isset($_GET[$url]) ? $_GET[$url] : 0; //testa se os argumentos foram passados, se não passa 0!
			$i++;
		}
		//para mostrar as variaveis de forma direta - neste exemplo, pois se fossem n variaveis num(n) o loop é o correto!
		//echo "$num1 $num2 $num3 $num4 $num5";
		//neste segundo while vamos percorrer as variaveis num$i e mostrar os valores delas com o echo!
		//resetamos o contador
		
		$i = 1;
		while ($i <=5) {
			$v = "num".$i; //o v vai quardar as contagens dos numeros num1 ate num5 que sao os nomes das variaveis que criamos para quardar os valores de v1 ate v5
			echo "Valor $i : ". $$v . "<br/>"; //o $$v vai pegar o conteudo referenciado da variavel num$i da vez!
			$i++;	
		}
	?>
	<a href="javascript:history.go(-1)">Voltar</a>
</div>
</body>
</html>