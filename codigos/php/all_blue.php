



    
<?php 

echo('<!DOCTYPE html>
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
    <!-- Cabeçalho -->
    <header>
        <nav>
            <div class="logo-container">
                <img src="/all_blue/codigos/files/logo_png.png" alt="All Blue" class="logo">
            </div>
            <!-- Barra de pesquisa -->
            <div class="wrap">
                <div class="search">
                    <input type="text" class="searchTerm" placeholder="O que você procura hoje?">
                    <button type="submit" class="searchButton">
                        <i class="fa fa-search"></i>
                    </button>
                </div>
            </div>

            <!-- Dropdown menu  -->
            <div>

                <div class="position">
                    <!-- Opções do menu -->
                    <span class="material-symbols-outlined" id="icon"> 
                        account_circle
                        </span>
                    <a href="/all_blue/codigos/html/login.html">Login</a>
                    <a href="/all_blue/codigos/html/cadastro_usuario.html">Cadastro</a>
                    <span class="material-symbols-outlined" id="icon">
                        contact_support
                        </span>
                    <a href="/all_blue/codigos/html/fale-conosco.html">Fale conosco</a>
                    <span class="material-symbols-outlined" id="icon">
                        favorite
                        </span>
                    <a href="favoritos.html">Favoritos</a>
                    <span class="material-symbols-outlined" id="icon">
                        shopping_bag
                        </span>
                    <a href="ofertas_do_dia.html">Ofertas do Dia</a>
                </div>
            </div>

            <!--Dropdown filtro de marca/preço  -->

        </nav>
    </header>
    <div class="dropdown">
       <button class="dropbutton_Filtros">Filtrar  <span class="material-symbols-outlined">tune</span></button> 
        <div class="drop_options">
            <!-- Opções do filtro -->
            <h1>Marcas</h1>
            <input type="checkbox" id="amd">
            <label for="amd">AMD</label><br>

            <input type="checkbox" id="intel">
            <label for="intel">INTEL</label><br>

            <input type="checkbox" id="gforce">
            <label for="gforce">GFORCE</label><br>

            <input type="checkbox" id="logitech">
            <label for="logitech">LOGITECH</label><br>

            <input type="checkbox" id="nvidia">
            <label for="nvidia">NVIDIA</label><br>

            <h1>Preços</h1>
            <input type="range">
        </div>
    </div>
    <div class="table_produtos">
    <table>');

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


// Fechar a conexão<?php




                
// Exibir informações do banco de dados

$cont=1;

if ($result->num_rows > 0) {

    
    while($row= $result->fetch_assoc()){
        echo "<tr>";
        while($cont<=5){
            echo "<td>";
            echo '<div class="imagem">';
            echo '<a href="'.$row["url_produto"].'">';            
            echo "<img src=".$row["url_img"]." class=img_produto alt=Monitor>";
            echo '</div>';
            echo '<hr>';
            echo '</div>';        
            echo '</a>';
            echo '</div>';
            echo '<div class="nome_produto">'.$row["nome"].'';
            echo '<h3>R$'.$row["preco"].'</h3>';
            echo '</td>';

            $cont=$cont+1;
            $row= $result->fetch_assoc();


        }
        echo"</tr>";
        
        $cont=1;
    }
    

    
    

} else {
    echo "Nenhuma informação encontrada no banco de dados.";
}
$conn->close();

echo('
    </div>
    </table>

    </body>
    
    </html>');

?>

