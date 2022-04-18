<!DOCTYPE html>
<html lang="pt-BR">
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE</title>
</head>
<body>
<div>
	<h1>PHP - curso online</h1>
	<h2>Treinamneto de uso e recursos do PHP</h2>
	<p>Está página tem como objetivo colocar em prática os recursos oferecidos por essa importante ferramenta</p>
</div>
<div>
	<!--
	Nós podemos avançar agora e mostrar a você como alternar entre os modos PHP mesmo que você esteja executando blocos de códigos: Entre IF / THEN / ELSE, por exemplo.
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Alternando PHP/HTML5</h2>";
		if (strpos($_SERVER['HTTP_USER_AGENT'], 'MSIE') !== FALSE) { # abre chaves
	?>
	<!-- HTML EXECUTADO SE O IF FOR VERDADEIRO -->
	<h3>strpos() must have returned non-false</h3>
	<p>You are using Internet Explorer</p>
	<!-- PHP -->
	<?php
		} else { # fecha o if e abre o else
	?>
	<!-- HTML EXECUTADO SE O ELSE FOR VERDADEIRO -->
	<h3>strpos() must have returned false</h3>
	<p>You are not using Internet Explorer</p>
	<!-- PHP -->
	<?php
		} # fecha o else, encerra o bloco!
	?>
</div>
<div>
	<?php #SUPERTAG
		/* 
		echo comando de saida para tela
		$no = (string) "Fernando"; FORÇA A ATRIBUIÇÃO DA VARIAVEL
		*/
		echo "<h2>Concatenação</h2>";
		$nome = (string) "Fernando";
		$idade = 47;
		echo $nome." ".$idade."."."<br/>";
		# echo $nome." tem ".$idade." anos!<br/>";
		echo "$nome tem $idade anos.<br/>";		
	?>
</div>
<div>
	<?php
		/*
		ao chamar a função $_GET[], lembre-se de passa na url o valor -> URL?p=100
		*/
		echo "<h2>Operadores Matemáticos</h2>";
		$preco = 100;
		//$_GET["p"]; FUNCAO QUE RECEBE DA URL O VALOR DA VARIAVEL p -> xxx.php?p=100
		echo "O preço do produto é R$ $preco";
		//$preco = $preco + ($preco*10/100);
		$preco += $preco*10/100;
		echo "<br/>O preço com 10% de aumento será R$ $preco";
		//resetei o valor pois o proximo calculo estava usando o valor acrescido de 10%
		$preco = 100; 
		$preco -= $preco*10/100;
		echo "<br/>O preço com 10% de desconto será R$ " . number_format($preco,2)."<br/>";

		$atual = 2014;

		#$_GET["aa"];
		
		#echo "O ano atual é $atual e o ano anterior é " . $atual--;
		#o comando acima nao da certo, pois antes de tirar um ano, ele mostra o valor da variavel
		
		echo "O ano atual é $atual e o ano anterior é " . --$atual;
	?>
</div>
<div>
	<?php
		echo "<h2>Variaveis referenciadas</h2>";
		echo "recebendo o valor da variavel a - normal <br/>";
		$a = 3;
		$b = $a;
		$b += 5;
		echo "O valor da Variavel a é: $a";
		echo "<br/>O valor da Variavel b é: $b <br/>";
	
		echo "recebendo o valor da referencia da variavel a - Referenciada";
		$a = 3;
		$b = &$a; //O uso do & atribui a $b a referencia de $a e nao o valor contido em $a
		$b += 5;
		echo "<br/>O valor da Variavel a é: $a";
		echo "<br/>O valor da Variavel b é: $b";
	?>
</div>
<div>
	<?php
		echo "<h2>Variaveis Variantes</h2>";
		$site = "cursoemvideo";
		$$site = "cursoPHP";
		echo "Os valores das Variaveis são: <br/> ($)site: $site <br/> ($$)site: $cursoemvideo";
		$x = "abc";
		$$x = "def";
		echo "<br/>Os valores das Variaveis são: <br/> ($)x: $x <br/> ($$)x: $abc";
	?>
</div>
<div>
	<!--
	Operadores relacionais - comparativos. > < >= <= <> != == ===
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Operadores Relacionais comparativos</h2>";
		//recebendo tres valores pela url ?a=5 b=3 op=s
		//www.site.com.br/aula.php?a=5&b=3&op=s
		$n1 = 3; //$_GET["a"];
		$n2 = 5; //$_GET["b"];
		$tipo = "s"; //$_GET["op"];
		echo "Os valores passados foram $n1 e $n2 <br/>";
		$r = ($tipo == "s") ? $n1+$n2 : $n1*$n2;
		echo "O resultado é $r <br/>";
		$num = 3;
		$text = "3";
		$compid = ($num === $text)?"SIM":"NÃO";
		echo "O numero $num é identico ao texto $text? $compid<br/>";
		$compig = ($num == $text)?"SIM":"NÃO";
		echo "O numero $num é igual ao texto $text? $compig";
	?>
</div>
<div>
	<!--
	Operadores relacionais - comparativos. > < >= <= <> != == ===
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Operadores Relacionais comparativos 2</h2>";
		//recebendo tres valores pela url ?a=5 b=3 op=s
		//www.site.com.br/aula.php?a=5&b=3&op=s
		$nota1 = 5; //$_GET["a"];
		$nota2 = 9; //$_GET["b"];
		echo "As notas são $nota1 e $nota2 <br/>";
		$media = ($nota1+$nota2)/2;
		echo "A media é $media <br/>";
		//$resultado = ($media < 7)?"REPROVADO":"APROVADO";
		//echo "O ALUNO FOI $resultado<br/>";
		//podemos economizar codigo e variavel fazendo assim com o operador unario concatena direto no echo
		//como o unario é um operador ele tem que estar entre parenteses ( ? : )
		echo "O ALUNO FOI ".(($media < 7)?"REPROVADO":"APROVADO<br/>");
	?>
</div>
<div>
	<!--
	Operadores logicos && || xor !
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Operadores Logicos</h2>";
		$ano = 2007; //$_GET["ano"];
		$idade = 2020 - $ano;
		echo "<p>Quem nasceu em $ano tem $idade anos de idade.</p>";
		$tipo = ($idade>=18 && $idade<65)?"OBRIGATORIO":"NAO OBRIGATORIO";
		echo "<p>Dessa forma o seu voto é $tipo</p>";
	?>
</div>
<div>
	<!--
	USO DE REPETIDORES!
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Uso do While</h2>";
		$c = 1; //$_GET["ano"];
		echo "<p>Contagem Progressiva</p>";
		while ($c <= 20) {
			echo $c." ";//."<br/>";
			$c++;
		}
		echo "<p>Contagem Regressiva</p>";
		while ($c >= 0) {
			echo $c." ";//."<br/>";
			$c--;
		}
	?>
</div>
<div>
	<!--
	USO DE REPETIDORES!
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Uso do While</h2>";
		$f = 6; //isset($_GET["fatorial"])?$_GET["fatorial"]:1;
		$c = $f;
		$fat = 1;
		echo "<p>Fatorial</p>";
		if ($f == 1) {
			echo "<h2>$f! = $fat</h2>";
		} else {
			do {
				$fat = $fat * $c;
				$c--;
			} while ($c >= 1);
		}
		echo "<h2>$f! = $fat</h2>";
	?>
</div>
<div>
	<!--
	USO DE REPETIDORES!
	-->
	<!-- PHP -->
	<?php
		echo "<h2>Uso do For</h2>";
		//isset($_GET["fatorial"])?$_GET["fatorial"]:1;
		for($i=1;$i<=10;$i++){
			echo "$i ";
		}
		echo "<br/>";
		for($i=10;$i>=1;$i--){
			echo "$i ";
		}
		echo "<br/>";
		for($i=1;$i<=50;$i+=5){
			echo "$i ";
		}
		echo "<br/>";
		for($i=20;$i>=0;$i-=2){
			print "$i ";
		}
		//IMPORTANTE: ECHO E PRINT SAO EQUIVALENTES
		print "<br/>";
		for($i=0;$i<=21;$i+=3){
			print "$i ";
		}
	?>
</div>
<div>
	<!-- IMPORTANTE: vamos fazer o exercicio da tabuada dentro do PHP dentro do php vamos chamar outro php -->
	<h2>Uso do For para criar a lista com PHP e a chama a mesma tabuada usada no arquivo html/JS </h2>
	<form method="get" action="exercicio13.php">
		<select name="nopc">
			<!-- FICOU BEM MAIS FACIL DO QUE FAZER EM HTML/JS -->
			<?php
				for($c=1;$c<=10;$c++){
					print "<option>$c</option>";
				}
			?>
		</select>
	<input type="submit" value="tabuada"/>
</div>
<div>
	<!-- USO DE FUNÇOES	-->
	<!-- PHP -->
	<?php
		echo "<h2>FUNCAO PHP VOID</h2>";
		function soma($a, $b){
			$s=$a+$b;
			echo "<p>O resultado da soma é $s</p>";
		}
		soma(3,4);
		soma(8,2);
		soma(5,8);
		$x = 9;
		$y = 6;
		soma($x,$y);
	?>
</div>
<div>
	<!-- USO DE FUNÇOES	-->
	<!-- PHP -->
	<?php
		echo "<h2>FUNCAO PHP RETURN</h2>";
		function somar($a,$b){
		//	$s=$a+$b;
		//	return $s;
			return $a+$b;
		}
		$r = somar(3,4);
		print "<p>O resultado da soma é $r</p>";
		$r = somar(8,2);
		print "<p>O resultado da soma é $r</p>";
		$r = somar(5,8);
		print "<p>O resultado da soma é $r</p>";
		$x = 9;
		$y = 6;
		$r = somar($x,$y);
		print "<p>O resultado da soma é $r</p>";
	?>
</div>
<div>
	<!-- USO DE FUNÇOES	-->
	<!-- PHP -->
	<?php
		echo "<h2>FUNCAO PHP ARGUMENTOS DINAMICOS</h2>";
		function somavet(){
		//	USA VETOR - a funcao joga em um vetor os argumentos passados
			$p = func_get_args();
		// funcao que nos diz o numero de argumentos da funcao - tamanho do vetor <n-1> pois inica em 0
			$totarg = func_num_args();
			$s = 0;
			for($i=0;$i<$totarg;$i++) {
			//for($i in $p) {
				$s+=$p[$i];
			}
			return $s;
		}
		//IMPORTANTE: chamadas de funcao sem definir o n. dos argumentos!!!
		$res = somavet(3,4,5,6,8);
		print "<p>O resultado da soma é $res</p>";
		$res = somavet(8,2,5,7,2,8,0);
		print "<p>O resultado da soma é $res</p>";
		$res = somavet(5,8);
		print "<p>O resultado da soma é $res</p>";
		$x = 9;
		$y = 6;
		$z = 8;
		$res = somavet($x,$y,$z);
		print "<p>O resultado da soma é $res</p>";
	?>
</div>
<div>
	<!-- USO DE FUNÇOES	-->
	<!-- PHP -->
	<?php
		//IMPORTANTE: PASSAGEM DE ARGUMENTOS POR VALOR
		echo "<h2>FUNCAO PHP POR VALOR</h2>";
		function somavalor($x){
			$x += 2;
			echo "<p>O resultado é $x.</p>";
		}
		$a = 3;
		somavalor($a);
		echo "<p>O valor da variavel a é $a.</p>";
	?>
</div>
<div>
	<!-- USO DE FUNÇOES	-->
	<!-- PHP -->
	<?php
		//IMPORTANTE: PASSAGEM DE ARGUMENTOS POR REFERENCIA &
		echo "<h2>FUNCAO PHP POR REFERENCIA &</h2>";
		function somaref(&$x){
			$x += 2;
			echo "<p>O resultado é $x.</p>";
		}
		$a = 3;
		somaref($a);
		//O VALOR DE a ALTERA DEVIDO A REFERENCIA QUE FOI FEITA PELA FUNCAO. &
		echo "<p>O valor da variavel a é $a.</p>";
	?>
</div>
<div>
	<!-- USO DE FUNÇOES	EXTERNAS -->
	<!-- PHP -->
	<?php
		//IMPORTANTE: CHAMADA DE FUNCOES EXTERNAS
		include "funcoes.php";
		//include_once - testa se o arquivo ja foi carregado antes no codigo
		//require - marca o arquivo carregado como requerido, se nao existir PARA O PROGRAMA DA ERRO!!!!!!!!!!!!!!
		//require_once - tambem garante que o arquivo requerido seja carregado uma vez só durante a execucao deste documento!!!!!!
		echo "<h2>CHAMADA DE FUNCAO EXTERNA</h2>";
		ola();
		mostraValor(3);
		print "<p>final de programa</p>";
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	-->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR STRINGS</h2>";
		$prod = "leite";
		$preco = 3.5;
		print "<h2>echo</h2>";
		echo "O $prod está custando R$ ".number_format($preco,2)."<br/><br/>";
		print "<h2>printf</h2>";
		//%s string %.2 casas f float - formatação!!! das variaveis $prod e $preco
		printf("O %s está custando R$ %.2f",$prod,$preco);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	VETORES -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR VETORES</h2>";
		$vet = [4,3,8];
		$vet2 = [1,2,5,7,4,9,3,5];
		print_r($vet);
		print "<br/>";
		print_r($vet2);
		print "<br/>";
		var_dump($vet);
		print "<br/>";
		var_export($vet2);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR QUEBRA DE LINHA</h2>";
		$txt = "Este é um exemplo de string gigante que nao deve caber em uma unica linha...";
		//o \n quebra a linha no codigo... o false nao corta a palavra, true corta
		$res = wordwrap($txt, 40, "<br/>\n", false);
		print $res."<br/>";
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		mb_internal_encoding('utf-8');
		echo "<h2>MANIPULAR STRLEN() E TRIM()</h2>";
		$txt = "Este é um exemplo de string com várias palavras";
		print $txt."<br/>";
		print "ela tem ".strlen($txt)." letras.<br/>";
		//0 conta as palavras. 1 cria um vetor (jogar em uma variavel), 2 cria um vetor porem ele coloca as palavras nos indices equivalentes a posicao da palavra na string.
		$contpa = str_word_count($txt,0);
		$vet1pa = str_word_count($txt,1);
		$vet2pa = str_word_count($txt,2);
		//o explode tambem gera um array com as palavras, e CORRIGE O PROBLEMA DOS ACENTOS
		$vetexp = explode(" ",$txt);
		print "ela tem ".$contpa." palavras.<br/>";
		print_r($vet1pa);
		print "<br/>";
		print_r($vet2pa);
		print "<br/>";
		print_r($vetexp);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR EXPLODE()</h2>";
		$txt = "Este é um exemplo de string";
		print $txt."<br/>";
		//o explode tambem gera um array separando por espacos (ou algum caracter de interesse colocado entre aspas) com as palavras, e CORRIGE O PROBLEMA DOS ACENTOS
		$vetortxt = explode(" ",$txt);
		print_r($vetortxt);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR STR_SPLIT()</h2>";
		$txt = "Fernando";
		print $txt."<br/>";
		$vetcaracter = str_split($txt);
		print_r($vetcaracter);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR IMPLODE() / JOIN()</h2>";
		$vetsep = ["Fernando","é","legal","!"];
		print_r($vetsep);
		print "<br/>";
		//coloca # como separador, pode por qquer coisa
		$implo = implode("#",$vetsep);
		print $implo."<br/>";
		//a funçao JOIN() funciona igual a implode()
		$jo = join(" ",$vetsep);
		print $jo;
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR CHR() / ORD()</h2>";
		//CHR() - traz o valor do caracter dado um valor numerico
		$cod = chr(67);
		print $cod."<br/>";
		$letra = "C";
		print ord($letra);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR STRTOLOWER()/UPPER</h2>";
		$nome = "feRnAnDo gRoPp";
		print "seu nome é ".strtolower($nome)."<br/>";
		print "seu nome é ".strtoupper($nome)."<br/>";
		print "seu nome é ".ucfirst(strtolower($nome))."<br/>";
		print "seu nome é ".ucwords(strtolower($nome))."<br/>";
		print "seu nome é ".strrev($nome);
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR STRPOS()/STRIPOS()</h2>";
		$nome = "Estou aprendendo php";
		//procurar a posicao da string procurada dentro da string passada. comeca em zero
		//essa funcao é keysensitive
		//vai dar erro pois nao acha em caixa maiuscula - false em php retorna null, true retorna 1
		$pos1 = strpos($nome, "PHP");
		//a funcao stripos - ignora a caixa...
		$pos2 = stripos($nome, "PHP");
		print "resultado1: $pos1 resultado2: $pos2";
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR SUBSTR_COUNT</h2>";
		$nome = "Estou aprendendo php com estudo do PHP";
		//procurar a posicao da string procurada dentro da string passada. comeca em zero
		//essa funcao é keysensitive
		//vai dar erro pois nao acha em caixa maiuscula - false em php retorna null, true retorna 1
		$pos = substr_count($nome, "PHP");
		print "string encontrada: $pos, vezes";
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR SUBSTR()</h2>";
		$site = "Plataforma Sustentavel Nova";
		//string, pos inicio, pos final
		$sub = substr($site, 0, 10);
		//string, posicao - posicao positiva o inicio zero é default D-->E
		//string, posicao - posicao negativa o inicio é o final da string E<--D
		$sub1 = substr($site, -4);
		print "string informada: $site<br/> sub + : $sub<br/> sub - : $sub1";
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		echo "<h2>MANIPULAR STR_PAD()/REPEAT</h2>";
		$strn = "Plataforma";
		//string, tamanho total, preencher com, R/L/BOTH
		$subpad = str_pad($strn,40,"__",STR_PAD_BOTH);
		print("A string informada: $strn<br/>");
		print("E o uso do pad faz isso: $subpad<br/>");
		$txtrep = str_repeat("Php",5);
		print $txtrep."<br/>";
		print(str_repeat("-",100)); 
	?>
</div>
<div>
	<!-- MANIPULAÇÃO DE STRINGS	 -->
	<!-- PHP -->
	<?php
		//FUNCOES PARA MANIPULAR STRINGS
		mb_internal_encoding('utf-8');
		echo "<h2>MANIPULAR STR_REPLACE()</h2>";
		$strnovo = "Plataforma é muito legal";
		//string, tamanho total, preencher com, R/L/BOTH
		//IMPORTANTE: É KEYSENSITIVE
		//IMPORTANTE: ireplace ignora maiusculas e minusculas
		//nao muda nada Muito nao existe na string
		$replaced = str_replace("Muito","PHP",$strnovo);
		//muda pois o irepalce ignora MAIUSCULA/MINUSCULA
		$ireplaced = str_ireplace("plataforma","PHP",$strnovo);
		print "Frase original: $strnovo<br/>";
		print "Frase alterada: $replaced<br/>";
		print "Frase alterada: $ireplaced<br/>";
		print(str_repeat("-",100));
	?>
</div>
<div class="vetor">
	<!-- MANIPULAÇÃO DE VETORES	 -->
	<!-- PHP -->
	<!-- o pre muda a visualizacao do array com print_r -->
	<pre>
	<?php
		//VETORES E MATRIZES
		echo "<h2>VETORES E MATRIZES</h2>";
		$v = array(3,4,6,7);
		$v1 = [1,4,6,3,2,7];
		//imprimir
		print_r($v);
		print "<br/>";
		print_r($v1);
	?>
	</pre>
</div>
<div>
	<!-- MANIPULAÇÃO DE VETORES	 -->
	<!-- PHP -->
	
	<?php
		//VETORES E MATRIZES
		echo "<h2>VETORES E MATRIZES</h2>";
		$vt = [1,4,6,3,2,7];
		//imprimir
		print_r($vt);
		print "<br/>";
		//criando um novo valor - append no vetor atual
		$vt[] = 10;
		print_r($vt);
		print "<br/>";
		//criando um vetor que comeca com 5, vai até 20 de 5 em 5...
		$vr = range(5,20,5);
		print_r($vr);
		print "<br/>";
	?>
	<pre>
		<table border="1"><tr>
	<?php
		//foreach - faz um loop jogando o valor da matriz na variavel $valor a cada repeticao
		foreach($vr as $valor){
			print("<td>$valor ");
		}
	?>
		</table>
	</pre>
</div>
<div class="vetor">
	<?php
		//VETORES E MATRIZES
		echo "<h2>VETORES E MATRIZES</h2>";
		//atribui um indice a um valor
		$vpp = array(1=>"A",3=>"B",6=>"C",8=>"D");
		print_r($vpp);
		print "<br/>";
		$vpp[]="E";
		print_r($vpp);
		print "<br/>";
		//IMPORTANTE: COMO APAGAR UM DADO DO VETOR
		//desalocar/apagar um valor do vetor da memoria
		unset($vpp[9]);
		print_r($vpp);
		print "<br/>";
	?>
	<pre>
	<?php	
		//colocando strings como indices
		//o PHP tem vetores nao HOMOGENEOS entao voce pode misturar em um unico vetor inteiros, strings, floats, boolean,...
		$vpc = array("Nome"=>"Ana","Idade"=>31,"Peso"=>89.5,"Signo"=>"Aries");
		$vpc["fuma"]=true;
		print_r($vpc);
		//usando a funcao foreach para indices strings
		foreach($vpc as $campo => $valor){
			print "O valor de $campo é $valor<br/>";
		}
	?>
	</pre>
</div>
<div class="vetor">
	<!-- MANIPULAÇÃO DE MATRIZES -->
	<!-- PHP -->
	<!-- o pre muda a visualizacao do array com print_r
	nao existe matriz em PHP, aqui sao vetores dentro de vetores -->
	<pre>
	<?php
		//VETORES E MATRIZES
		echo "<h2>VETORES E MATRIZES</h2>";
		//$vm = array(array(),array(),array(),... )
		$vm = [[1,4],[6,3]];
		//imprimir e atribuir matrizes...
		print_r($vm);
		print "<br/>";
		print $vm[0][0];
		print " ";
		print $vm[0][1];
		print " ";
		$vm[0][0] = 2;
		print $vm[0][0];
		print " ";
		$vm[0][1] = $vm[1][0];
		print $vm[0][1];
	?>
	</pre>
</div>
<div class="vetor">
	<!-- MANIPULAÇÃO DE VETORES	 -->
	<!-- PHP -->
	<!-- o pre muda a visualizacao do array com print_r -->
	<!-- <pre> -->
	<?php
		//VETORES E MATRIZES
		echo "<h2>FUNÇOES PARA MOSTRAR VETORES E SEUS CONTEUDOS</h2>";
		//$v = array(3,4,6,7);
		$v = [1,4,6,3,2,7];
		//imprimir vetor
		print_r($v);
		print "<br/>";
		//imprimir dados do vetor
		var_dump($v);
		print "<br/>";
		//imprimir o numero de itens do vetor
		print count($v);
		print "<br/>";
		//por elememto no final
		$v[]=7;
		//pilha
		array_push($v,9);
		print_r($v);
		print "<br/>";
		//eliminar o ultimo elemento do vetor [n]
		//pilha final do vetor LIFO
		array_pop($v);
		print_r($v);
		print "<br/>";
		//por elemento no inicio do vetor - ajusta os indices
		array_unshift($v,12);
		print_r($v);
		print "<br/>";
		//eliminar o primeiro vetor [0] - ajusta os indices
		array_shift($v);
		print_r($v);
		print "<br/>";
		//ordenar o vetor cresc letras e numeros
		sort($v);
		print_r($v);
		print "<br/>";
		//ordenar o vetor decres letras e numeros
		rsort($v);
		print_r($v);
		print "<br/>";
		//ordenar associativa ele ordena o conteudo e leva junto o indice cresc
		asort($v);
		print_r($v);
		print "<br/>";
		//ordenar associativa ele ordena o conteudo e leva junto o indice decresc
		arsort($v);
		print_r($v);
		print "<br/>";
		//ordenar por chaves/indices ordena os indices e nao o conteudo cresc
		ksort($v);
		print_r($v);
		print "<br/>";
		//ordenar por chaves/indices ordena os indices e nao o conteudo decresc
		krsort($v);
		print_r($v);
		print "<br/>";
	?>
	<!-- </pre> -->
</div>
</body>
</html>