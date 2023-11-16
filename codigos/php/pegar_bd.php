<?php
$servername = "localhost:3306";
$username = "root";
$password = "thiago";
$dbname = "all_blue";

// Conectar ao banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar a conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Consulta para obter informações do banco de dados
$sql = "SELECT * FROM produtos_aleatorios";
$result = $conn->query($sql);


// Fechar a conexão<?php

                
// Exibir informações do banco de dados
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "Nome do Produto: " . $row["nome"] . "<br>";
        echo "Preço: " . $row["preco"] . "<br>";
        echo "Loja: " . $row["url_logo"] . "<br>";
        echo '<img src="'. $row["url_img"] . '">' ;

        }

} else {
    echo "Nenhuma informação encontrada no banco de dados.";
}
$conn->close();
?>



