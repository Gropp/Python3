<?php
#Define a página atual pela URL
$pagina = "home";
if(isset($_GET['pagina'])){
    $pagina = $_GET['pagina'];
}
#Carrega o cabeçalho
require 'header.php';
#Carrega a pagina escolhida pelo usuario
switch($pagina){
    case 'equipe':
        include 'equipe.php';
    break;
    default:
        include 'home.php';
    break;
}
#Carrega o rodape
require 'footer.php';
?>