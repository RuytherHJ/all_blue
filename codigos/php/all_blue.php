<?php 
// Inclua o código de processamento de login
include 'processar_login.php';


// Debug: Verificar o conteúdo da $_SESSION
 //echo "Conteúdo da variável de sessão:";
 //var_dump($_SESSION);

// Verificar se o usuário está logado
$usuarioLogado = (isset($_SESSION['usuarioLogado']) && $_SESSION['usuarioLogado'] === true);

if ($usuarioLogado) {
    require_once("cabecalho_logado.php");
    if($_SESSION['cadastrou']==true){

        echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
                echo('<script>Swal.fire({
                    icon: "success",
                    title: "Usuário cadastrado com sucesso!",
                    showConfirmButton: false,
                    timer: 1500
                    });</script>')   ;
    
    
    }
} else {
    require_once("cabecalho.php");
}

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Blue</title>

    <link rel="stylesheet" href="/ALL_BLUE/codigos/css/pagina_principal/style_principal.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />

</head>

<body>
    <div class="table_produtos">
    <table>

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
        $sql = "SELECT * FROM produtos_aleatorios";
        $result = $conn->query($sql);

                        
        // Exibir informações do banco de dados
        $aux=1;
        $cont=1;

        if ($result->num_rows > 0) {

            
            while($row= $result->fetch_assoc() && $aux<20 ){
                
                echo "<tr>";
                while($cont<=5){
                    $row= $result->fetch_assoc();
                    echo "<td>";
                    echo '<div class="produto">';
                    echo '<div class="imagem">';
                    echo '<a href="' . $row["url_produto"] . '" target="_blank"">';
                    echo "<img src=" . $row["url_img"] . " class=img_produto alt=Monitor>";
                    echo '</a>';
                    echo '</div>';
                    echo '<hr>';
                    echo '<div class="nome_produto"><p>' . substr($row["nome"], 0, 100). '...</p></div>';
                    echo '<div class="preço">';
                    echo '<h3>R$' . $row["preco"] . '</h3>';
                    echo '</div>';
                    echo '</div>';
                    echo '<div class="detalhes-produto">';
                    
                    // Limitar a descrição a 150 caracteres
                    
                    echo '</div>';
                    echo '</td>';
                    $cont = $cont + 1;
                    $aux = $aux + 1;
                }
                echo"</tr>";
                
                $cont=1;
            }

        } else {
            echo "Nenhuma informação encontrada no banco de dados.";
        }
        $conn->close();

       
        ?>
       

    
    </table>
    </div>

    <?php
         require_once 'rodape.php';
    ?>


</body>

</html>



