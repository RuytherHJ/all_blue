<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Configuração de conexão com o banco de dados
    $servername = "localhost:3306";
    $username = "root";
    $password = "thiago";
    $dbname = "all_blue";

    // Conecte-se ao banco de dados
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verifique a conexão
    if ($conn->connect_error) {
        die("Falha na conexão com o banco de dados: " . $conn->connect_error);
    }

    // Captura os dados do formulário
    $nome = trim($_POST['user_name']);
    $email = trim($_POST['user_email']);
    $senha = trim($_POST['user_senha']);

    // Inserção dos dados no banco de dados

    $sql = "call all_blue.insere_usuario('$email','".sha1($senha)."', '$nome');";


    if ($conn->query($sql) === TRUE) {


        $_SESSION['nome_logado']=$nome;
        $_SESSION['usuarioLogado'] = true;
        
        $_SESSION['cadastrou']=true;
        
        header('Location: /all_blue/codigos/php/all_blue.php');
        
        exit();

    } else {
        echo "<h1>ERRO AO CADASTRAR!!!</h1>";
        sleep(2);
        header('Location: /all_blue/codigos/php/cadastro_usuario.php');
        exit();
    }

    // Feche a conexão com o banco de dados
    $conn->close();
} else {
    echo "Método de requisição inválido.";
}
?>
