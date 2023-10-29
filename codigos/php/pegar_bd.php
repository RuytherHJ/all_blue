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
$sql = "SELECT pd.nome AS nome_produto, pd.preco AS preco_produto, lj.nome AS nome_loja, lj.url_logo AS logo, mc.nome_fabricante AS marca
        FROM Tabela_Produtos pd
        JOIN Tabela_Lojas lj ON pd.id = lj.id
        JOIN Tabela_Marcas mc ON lj.id = mc.id";
$result = $conn->query($sql);

// Fechar a conexão
$conn->close();
?>
