

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cabecalho</title>
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
                <a href="/all_blue/codigos/php/all_blue.php">
                <img src="/all_blue/codigos/files/logo_png.png" alt="All Blue" class="logo">
                </a>
            </div>
            <!-- Barra de pesquisa -->
            <div class="wrap">
            
                <form class="search" action="/all_blue/codigos/php/pesquisa.php" method="POST"> 

                    <input type="text" class="searchTerm" name="search_bar" placeholder="O que você procura hoje?">
                    <button type="submit" class="searchButton">
                        <i class="fa fa-search"></i>
                    </button>

                </form>
                
            </div>
            
            <div class="dropdown">
                <button class="dropbutton"><span class="material-symbols-outlined" id="icon_options"> 
                account_circle</span> Olá, Ruyther!</button>
                
                <div class="drop_options">
                    <form action="/all_blue/codigos/php/logout.php" method="post" >
                        <a href="">Sair</a>
                    </form>    
                    <a href="/all_blue/codigos/php/login.php">Trocar usuário</a>
                </div>
             </div>

            <!-- Dropdown menu  -->
            <div>

                <div class="position">
                    <!-- Opções do menu -->
                    <span class="material-symbols-outlined" id="icon">
                        contact_support
                        </span>
                    <a href="/all_blue/codigos/php/fale-conosco.php">Fale conosco</a>
                    <span class="material-symbols-outlined" id="icon">
                        favorite
                        </span>
                    <a href="/all_blue/codigos/php/favoritos.php">Favoritos</a>
                    <span class="material-symbols-outlined" id="icon">
                        shopping_bag
                        </span>
                    <a href="/all_blue/codigos/php/ofertas_do_dia.php">Ofertas do Dia</a>
                </div>
            </div>

        

            <!--Dropdown filtro de marca/preço  -->

        </nav>
    </header>

    
</body>

</html>






