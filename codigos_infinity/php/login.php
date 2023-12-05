<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login de Usuário</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11.10.0/dist/sweetalert2.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="menu_itens.css">
    <link rel="stylesheet" href="style_principal.css">
</head>
<body>

    <div class="logo-pg">
        <a href="index.php"><img src="logo_png.png" alt="All Blue"></a>
        
    </div>
    
    <main>
        <!-- Formulário Login -->

        <?php
        include 'processar_login.php';

        $senha_correta = (isset($_SESSION['senha_correta']) && $_SESSION['senha_correta'] === true);

        if ($senha_correta!=False) {
            
            echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
            echo('<script>Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Email e/ou Senha incorretos, por favor tente novamente!",
                
              });</script>')   ;
            
                       
        } 

        ?>
        <div class="container">    
            <form action="processar_login.php" method="POST"> 
                <fieldset class="tamanho-login">
                    <h1>Login</h1><span class="material-symbols-outlined"></span><br>
                    <label for="email">E-mail:</label>
                    <input type="email" id="email" name="user_email">
                    <label for="senha">Senha:</label>
                    <input type="password" id="senha" name="user_senha" minlength="8">
                    <div>
                        <button type="submit">Entrar</button>
                    </div>
                    <hr>
                    <!-- Direciona para o cadastro -->
                    <p>Não possui um cadastro? </p> <p><a href="cadastro_usuario.php">Criar conta</a></p>
                </fieldset>

            </form>
        </div>
    </main>
    
</body>
</html>