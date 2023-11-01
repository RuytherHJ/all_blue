<?php
$servername = "localhost:3306";
$username = "root";
$password = "root";
$dbname = "all_blue";

// Conectar ao banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar a conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Consulta para obter informações do banco de dados
$sql = "SELECT pd.nome AS nome_produto, pd.preco AS preco_produto, lj.nome AS nome_loja, lj.url_logo AS logo, mc.nome_fabricante AS marca
        FROM Tabela_Produtos pd
        JOIN Tabela_Lojas lj ON pd.id = lj.id
        JOIN Tabela_Marcas mc ON lj.id = mc.id";
$result = $conn->query($sql);


// Fechar a conexão<?php

                
// Exibir informações do banco de dados
if ($result->mysqli_num_rows() > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "Nome do Produto: " . $row["nome_produto"] . "<br>";
        echo "Preço: " . $row["preco"] . "<br>";
        echo "Loja: " . $row["nome_loja"] . "<br>";
        echo "Marca: " . $row["nome_fabricante"] . "<br>";
        
        // Exibir a URL da logo da marca
        echo '<img src="' . $row["logo"] . '" alt="Logo da Marca"><br><br>';
    }
} else {
    echo "Nenhuma informação encontrada no banco de dados.";
}
$conn->close();
?>



