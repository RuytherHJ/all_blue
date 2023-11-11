
<?php


    echo('<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login de Usuário</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            <link rel="stylesheet" href="/all_blue/codigos/css/menu/menu_itens.css">
        </head>
        <body>

            <div class="logo-pg">
                <a href="/all_blue/codigos/html/all_blue.html"><img src="/all_blue/codigos/files/logo_png.png" alt="All Blue"></a>
                
            </div>
            <main>
                <!-- Formulário Login -->
                <div class="container">    
                    <form action="/all_blue/codigos/php/processar_login.php" method="POST"> 
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
                            <p>Não possui um cadastro? </p> <p><a href="/all_blue/codigos/html/cadastro_usuario.html">Criar conta</a></p>
                        </fieldset>

                    </form>
                </div>
            </main>
            
        </body>
        </html>');


?>
