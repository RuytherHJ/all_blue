
<?php

echo('

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cadastro usuário</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <link rel="stylesheet" href="/all_blue/codigos/css/menu/menu_itens.css">
        <script src="/all_blue/codigos/JavaScript/TelaDeCadastro.js" defer></script>
    </head>

    <body>


        <div class="logo-pg">
            <a href="/all_blue/codigos/php/all_blue.php"><img src="/all_blue/codigos/files/logo_png.png" alt="All Blue"></a>
        </div>
            <main>
                <!-- Formulário Cadastro -->
                <div class="container">
                    <form action="/all_blue/codigos/php/processar_cadastro.php" method="POST"> 
                        <fieldset class="tamanho-cadastro">
                            <h1>Criar conta</h1><span class="material-symbols-outlined"></span><br>
                            <label for="nome">Nome:</label>
                            <input type="text" id="nome" name="user_name">
                            <label for="email">E-mail:</label>
                            <input type="email" id="email" name="user_email">
                            <label for="senha">Crie uma senha:</label>
                            <input type="password" id="senha" name="user_senha" minlength="8" onkeyup="senha_errada()">
                            <label for="confirmasenha">Confirme sua senha:</label>
                            <input type="password" id="confirmasenha" name="user_senhaconfirma" minlength="8" onkeyup="senha_errada()">

                            <div>
                                <button type="submit">Continuar com e-mail</button>
                            </div>
                            <hr>
                            
                            <!-- Direciona login -->
                            <p>Já possui um cadastro? </p>
                            <p><a href="/all_blue/codigos/php/login.php">Fazer Login</a></p>
                        </fieldset>



                    </form>

                </div>
            </main>
        
    </body>

    </html>');


?>