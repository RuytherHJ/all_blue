<?php
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
    $nome = $_POST['user_name'];
    $email = $_POST['user_email'];
    $senha = $_POST['user_senha'];

    // Inserção dos dados no banco de dados
    $sql = "call insere_usuario('$email','$senha','$nome')";

    if ($conn->query($sql) === TRUE) {
        echo "Cadastro realizado com sucesso!";
        time(5);
        header('Location: /all_blue/codigos/html/all_blue.html');
        exit();

    } else {
        echo "<h1>Esse email já está sendo usado!!!</h1>";
        sleep(2);
        header('Location: /all_blue/codigos/html/cadastro_usuario.html');
        exit();
    }

    // Feche a conexão com o banco de dados
    $conn->close();
} else {
    echo "Método de requisição inválido.";
}
?>
