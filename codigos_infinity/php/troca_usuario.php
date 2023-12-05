<?php
session_start();

// Desconectar o usuário - remova todas as variáveis de sessão
$_SESSION = array();

// Se necessário, destrua a sessão
session_destroy();

// Redirecione para a página de login ou qualquer outra página desejada
header('Location: login.php');
exit();
?>