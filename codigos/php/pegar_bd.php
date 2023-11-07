<?php
$servername = "localhost:3306";
$username = "root";
$password = "";
$dbname = "all_blue";

// Conectar ao banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar a conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Consulta para obter informações do banco de dados
$sql = "SELECT pd.nome AS nome_produto, pd.preco AS preco_produto, lj.nome AS nome_loja, pd.url_img AS img
        FROM produtos pd
        JOIN lojas lj ON pd.id = lj.id;";
$result = $conn->query($sql);


// Fechar a conexão<?php

                
// Exibir informações do banco de dados
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "Nome do Produto: " . $row["nome_produto"] . "<br>";
        echo "Preço: " . $row["preco_produto"] . "<br>";
        echo "Loja: " . $row["nome_loja"] . "<br>";
        echo '<img src="'. $row["img"] . '">' ;

        }

} else {
    echo "Nenhuma informação encontrada no banco de dados.";
}
$conn->close();
?>



