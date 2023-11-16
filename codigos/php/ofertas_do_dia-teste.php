


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
    <?php

    require_once("cabecalho.php");

    ?>

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