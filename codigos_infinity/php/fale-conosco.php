

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fale Conosco</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="menu_itens.css">
    <link rel="stylesheet" href="style_principal.css">
</head>
<body>
    <div class="logo-pg">
        <a href="index.php"><img src="logo_png.png" alt="All Blue"></a>
        
    </div>
    <main>
        <!-- Formulário Fale conosco -->
        

        <?php

                include 'processar_faleconosco.php';

                if (array_key_exists('campo_fale_vazio',$_SESSION)){
                    
                    if($_SESSION['campo_fale_vazio']==true){
                        
                        echo('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>'); 
                                echo('<script>Swal.fire({
                                    icon: "error",
                                    title: "Algum dos campos estam vazios!",
                                    showConfirmButton: false,
                                    timer: 1500
                                    });</script>');
                            
                        }

                        $_SESSION['campo_fale_vazio']=false;
                
                }


            ?>




        <div class="container">    
            <form action="processar_faleconosco.php" method="POST">
                <fieldset class="tamanho-contato">
                    <h1>Fale Conosco</h1><span class="material-symbols-outlined"></span><br>
                    <label for="Seu nome">Nome:</label>
                    <input type="text" id="nome" name="user_name">
                    <label for="Seu e-mail">E-mail:</label>
                    <input type="email" id="email" name="user_email">
                    <label for="mensagem">Mensagem:</label>
                    <textarea name="user_mensagem" id="mensagem" ></textarea>
                    <div>
                        <button type="submit">Enviar</button>
                    </div> 
                </fieldset>
            </form>
        </div>
    </main>
   
</body>
</html>    
