


<!DOCTYPE html>
<html lang="pt">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ofertas do Dia</title>

    <link rel="stylesheet" href="ofertas_do_dia.css">
    <link rel="stylesheet" href="/all_blue/codigos/css/menu/ofertas_do_dia.css">
    <link rel="stylesheet" href="/all_blue/codigos/css/pagina_principal/cabecalho.css">
    <link rel="stylesheet" href="/all_blue/codigos/css/pagina_principal/style_principal.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

</head>

<body>
    <!-- Cabeçalho -->
    <header>
        <div class="img-container">
            <img src="/codigos/files/logo_png.png" alt="All Blue" class="logo">
        </div>
        <nav>
            <div class="wrap">
                <div class="search">
                    <input type="text" class="searchTerm" placeholder="O que você procura hoje?">
                    <button type="submit" class="searchButton">
                        <i class="fa fa-search"></i>
                    </button>
                </div>
            </div>

            <div class="dropdown">
                <button class="dropbutton_Menu">Menu</button>
                <div class="drop_options">
                    <a href="/codigos/html/login.html">Login</a>
                    <a href="/codigos/html/cadastro_usuario.html">Cadastro</a>
                    <a href="/codigos/html/fale-conosco.html">Fale conosco</a>
                    <a href="/codigos/html/favoritos.html">Favoritos</a>
                    <a href="/codigos/html/ofertas_do_dia.html">Ofertas do Dia</a>
                </div>
            </div>
            <div class="dropdown">

                <button class="dropbutton_Filtros">Filtrar</button>
                <div class="drop_options">


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
        </nav>

    </header>

    <!-- Ofertas do dia -->
    <main>
        <h1>Ofertas do Dia</h1>
    </main>
    <div class="table_produtos">
        <table class="ofertas_do_dia">
            <tr>
                <td>
                    <?php
                    include 'pegar_bd.php';
                
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
                    ?>
                
                </td>

            </tr>
        </table>

    </div>




        <footer>

        </footer>



</body>

</html>