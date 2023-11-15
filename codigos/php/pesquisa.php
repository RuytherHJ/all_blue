


<?php

include_once("cabecalho.php");

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Blue</title>

    <link rel="stylesheet" href="/all_blue/codigos/css/pagina_principal/cabecalho.css">
    <link rel="stylesheet" href="/all_blue/codigos/css/pagina_principal/style_principal.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />

</head>

<body>

<div class="table_produtos">
    <table>

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
        $dados_pesquisados=$_POST['search_bar'];
        $sql = "call all_blue.pesquisando('".$dados_pesquisados."');";
        $result=$conn->query($sql);

        $aux=1;
        $cont=1;
        if ($result->num_rows > 0) {

            
            while($row= $result->fetch_assoc() && $aux<20 ){
                
                echo "<tr>";
                while($cont<=5) {
                    $row= $result->fetch_assoc();

                    if ($row != null){
                        echo "<td>";
                        echo '<div class="imagem">';
                        echo '<a href="'.$row["url_produto"].'">';            
                        echo "<img src=".$row["url_img"]." class=img_produto alt=Monitor>";
                        echo '</div>';
                        echo '<hr>';
                
                        echo '</a>';
                        
                        echo '<div class="nome_produto">'.$row["nome"].'';
                        echo '<h3>R$'.$row["preco"].'</h3>';
                        echo '</div>';
                        echo '</td>';


                    }
                    

                    $cont=$cont+1;
                    $aux=$aux+1;


                }
                echo"</tr>";
                
                $cont=1;
            }

        } else {
            echo "Nenhuma informação encontrada no banco de dados.";
        }
        $conn->close();



    } else {
        echo "Método de requisição inválido.";
    }
?>



    </table>
</div>

</body>

</html>