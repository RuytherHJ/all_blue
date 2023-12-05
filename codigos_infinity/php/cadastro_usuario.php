

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro usuário</title>
    <link rel="stylesheet" href="style_principal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11.10.0/dist/sweetalert2.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="menu_itens.css">
    <script src="TelaDeCadastro.js" defer></script>
</head>

<body>


    <div class="logo-pg">
        <a href="index.php"><img src="logo_png.png" alt="All Blue"></a>
    </div>
        <main>




            <?php

                include 'processar_cadastro.php';

                if (array_key_exists('erro_de_cadastro',$_SESSION) && array_key_exists('senhas_diferentes',$_SESSION) && isset($_SESSION['campo_vazio'])){

                    if($_SESSION['erro_de_cadastro']==true){

                        echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
                                echo('<script>Swal.fire({
                                    icon: "error",
                                    title: "Esse email já está sendo utilizado!",
                                    showConfirmButton: false,
                                    timer: 1500
                                    });</script>');

                        $_SESSION['erro_de_cadastro']=false;
                    
                    
                    }elseif($_SESSION['senhas_diferentes']==true){

                        echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
                        echo('<script>Swal.fire({
                            icon: "error",
                            title: "Oops...",
                            text: "Você inseriu senhas diferentes, por favor, certifique-se o que você digitou!",
                            
                        });</script>')   ;
                        $_SESSION['senhas_diferentes']=false;

                    }
                    
                    elseif($_SESSION['campo_vazio']==true){
                        
                        echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
                                echo('<script>Swal.fire({
                                    icon: "error",
                                    title: "Algum dos campos estam vazios!",
                                    showConfirmButton: false,
                                    timer: 1500
                                    });</script>');
                            
                        }

                        $_SESSION['campo_vazio']=false;



                
                }


            ?>


        


            <!-- Formulário Cadastro -->
            <div class="container">
                <form action="processar_cadastro.php" method="POST"> 
                    <fieldset class="tamanho-cadastro">
                        <h1>Criar conta</h1><span class="material-symbols-outlined"></span><br>
                        <label for="nome">Nome:</label>
                        <input type="text" id="nome" name="user_name">
                        <label for="email">E-mail:</label>
                        <input type="email" id="email" name="user_email">
                        <label for="senha">Crie uma senha:</label>
                        <input type="password" id="senha" name="user_senha" minlength="8">
                        <label for="confirmasenha">Confirme sua senha:</label>
                        <input type="password" id="confirmasenha" name="user_senhaconfirma" minlength="8">

                        <div>
                            <button type="submit">Continuar com e-mail</button>
                        </div>
                        <hr>
                        
                        <!-- Direciona login -->
                        <p>Já possui um cadastro? </p>
                        <p><a href="login.php">Fazer Login</a></p>
                    </fieldset>



                </form>

            </div>
        </main>
    
</body>

</html>