

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
     <div class="cabeçalho">
        <header>
            <nav>
                <div class="logo-container">
                    <a href="index.php">
                    <img src="logo_png.png" alt="All Blue" class="logo">
                    </a>
                </div>
                <!-- Barra de pesquisa -->
                <div class="wrap">
                
                    <form class="search" action="pesquisa.php" method="GET"> 

                        <input type="text" class="searchTerm" name="search_bar" placeholder="O que você procura hoje?">
                        <button type="submit" class="searchButton">
                            <i class="fa fa-search"></i>
                        </button>

                    </form>
        
                </div>

                <!-- Itens de menu -->
                <div>

                    <div class="position">
                        <span class="material-symbols-outlined" id="icon"> 
                            account_circle
                            </span>
                        <a href="login.php">Login</a>
                        <span class="material-symbols-outlined" id= "icon">
                            person_add
                            </span>
                        <a href="cadastro_usuario.php">Cadastro</a>
                        <span class="material-symbols-outlined" id="icon">
                            contact_support
                            </span>
                        <a href="fale-conosco.php">Fale conosco</a>
                    </div>
                </div>

             

            </nav>
        </header>
     </div>
     

    
</body>

</html>






