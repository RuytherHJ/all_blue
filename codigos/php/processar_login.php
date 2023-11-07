<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Configuração de conexão com o banco de dados (substitua com suas próprias credenciais)
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
    $email = $_POST['user_email'];
    $senha = $_POST['user_senha'];

    // Consulta SQL para verificar o usuário e senha
    $sql = "call loga_usuario('$senha', '$email')";
    $result = $conn->query($sql);
   

    if ($result->num_rows == 1) {
        echo "Login bem-sucedido!"; // Usuário autenticado       
        header('Location: /all_blue/codigos/html/all_blue.html');
        exit();

    } else {
        echo "Login falhou. Verifique suas credenciais.";
    }

    // Feche a conexão com o banco de dados
    $conn->close();
} else {
    echo "Método de requisição inválido.";
}
