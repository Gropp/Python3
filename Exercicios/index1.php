<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>Primeiro Exemplo de PHP</title>
	<style type="text/css">
		h2 {
			color: #80a2ff;
			text-shadow: 1px 1px 1px black;
		}
	</style>
</head>
<body>
	<h1>Testando PHP</h1>
	<!-- SUPERTAGs - LINGUAGEM PHP NO MEIO DO HTML -->
	<!-- <?PHP ?> LINGUAGEM PHP SEMPRE ACABA EM ;  -->
	<!-- BLOCOS E COMANDOS PHP PODEM RECEBER TAGS HTML -->
	<!--
	PHP é casesensitive
	Variaveis começam com $
	Toda fim de linha tem ;
	$idade = 3; - inteiro
	$salario = 1825.54; - real
	$nome = "Leonardo"; - caractere
	$casado = false; - logica
	NO PHP NAO PRECISA DECLARAR A VARIAVEL, É POR COERSAO - A VARIAVEL É O QUE ELA É ATRIBUIDA, PODE VARIAR DENTRO DO ESCOPO!
	podemos forcar um tipo
	(int), (integer)
	(real), (float), (double)
	(string)
	NAO EXISTE TIPO LOGICO - O PHP TRATA COMO INTEIRO 1 ou 0

	 -->
	<?php 
		if (strpos($_SERVER['HTTP_USER_AGENT'], 'Chrome') !== FALSE) {
 			   echo "Você está usando o Google Chrome.<br />";
		}
		echo "<h2>Olá,<br/>Mundo!</h2>";
		echo "<p>Informações do Servidor</p><br />";
		echo $_SERVER['HTTP_USER_AGENT'];

		$str = "Mary Had A Little Lamb and She LOVED It So";
		$str = strtoupper($str);
		print "<br />".$str;
		// Prints MARY HAD A LITTLE LAMB AND SHE LOVED IT SO
	?>
</body>
</html>