

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cabecalho</title>
    <link rel="stylesheet" href="cabecalho.css">
    <link rel="stylesheet" href="style_principal.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />

</head>
<body>

     <!-- Cabeçalho -->
     <header>
        
            <div class="logo-container">
                <a href="index.php">
                <img src="logo_png.png" alt="All Blue" class="logo">
                </a>
            </div>
            <!-- Barra de pesquisa -->
            <div class="wrap">
            
                <form class="search" action="pesquisa.php" method="POST"> 

                    <input type="text" class="searchTerm" name="search_bar" placeholder="O que você procura hoje?">
                    <button type="submit" class="searchButton">
                        <i class="fa fa-search"></i>
                    </button>

                </form>
                
            </div>
            

            <!-- Dropdown menu  -->
            <div class="position">
                <!-- Opções do menu -->
                <span class="material-symbols-outlined" id="icon">
                    contact_support
                    </span>
                <a href="fale-conosco.php">Fale conosco</a>
            </div>
            
            <div class="dropdown">
                <button class="dropbutton"><span class="material-symbols-outlined" id="icon_options"> 
                account_circle</span> Olá, 

                <?php
                $nome = ($_SESSION['nome_logado']);
                echo($nome);
                ?>
    
            </button>
                
                <div class="drop_options">
                    <a href="logout.php">Sair</a>
                    <a href="troca_usuario.php">Trocar usuário</a>
                </div>
            </div>
            
           

        
    </header>

    
</body>

</html>






