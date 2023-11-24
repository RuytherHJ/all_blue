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
} else {
    require_once("cabecalho.php");
}


?>


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
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />


</head>

<body>

    <!-- Ofertas do dia -->
    <main>
        <h1>Ofertas do Dia</h1>
    </main>
    <div class="table_produtos">
        <table class="ofertas_do_dia">
            <tr>
                <td>
                    <a href=""><img src="/all_blue/codigos/files/teclado.jpg" class="img_produto" alt="Teclado"></a>
                    <br>
                    Teclado Gamer Knup KP-2060
                    <h3>78,99</h3>
                </td>
                <td>
                    <a href=""><img src="/all_blue/codigos/files/cadiera_gamer.webp" class="img_produto" alt=""></a>
                    Cadeira Gamer Husky Gaming Blizzard RGB, Preto, Luz RGB, Com Almofadas, Reclinável - HBL-RGB
                    <br>
                    <h3>788,99</h3>
                </td>
                <td>
                    <a href=""><img src="/all_blue/codigos/files/monitor.jpg" class="img_produto" alt="Monitor"></a>
                    Monitor Gamer LG 21.5 LED Full HD, 75Hz, 5ms, HDMI, FreeSync - 22MP410-B
                    <br>
                    <h3>680,90</h3>
                </td>
                <td>
                    <a href=""><img src="/all_blue/codigos/files/teclado.jpg" class="img_produto" alt="Teclado"></a>
                    Teclado Gamer Knup KP-2060
                    <br>
                    <h3>78,99</h3>
                </td>

            </tr>
        </table>

    </div>




        <footer>

        </footer>



</body>

</html>
 
 
 
 



?>
