<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="_css/estilo.css">
	<title>PHP CURSO ONLINE - Exemplo de PHP com HTML5</title>
	<style>
		p {
			margin-top: -10px;
		}
	</style>
</head>
<body>
	<div>
		<p>Formulário</p>
		<form method="get" action="form.php">
			<?php
			$c = 1;
			while ($c <= 5) {
				echo "Valor $c: <input type='number' name='v$c' max='100' min='0' value='0'/><br/>";
				$c++;
			}		
			?>
			<input type="submit" value="Enviar"/>
		</form>	
	</div>
</body>
</html>