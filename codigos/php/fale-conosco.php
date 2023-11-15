

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fale Conosco</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="/all_blue/codigos/css/menu/menu_itens.css">
</head>
<body>
    <div class="logo-pg">
        <a href="/all_blue/codigos/php/all_blue.php"><img src="/all_blue/codigos/files/logo_png.png" alt="All Blue"></a>
        
    </div>
    <main>
        <!-- Formulário Fale conosco -->
        <div class="container">    
            <form action="">
                <fieldset class="tamanho-contato">
                    <h1>Fale Conosco</h1><span class="material-symbols-outlined"></span><br>
                    <label for="Seu nome">Nome:</label>
                    <input type="text" id="nome" name="user_nome">
                    <label for="Seu e-mail">E-mail:</label>
                    <input type="email" id="email" name="user_email">
                    <label for="mensagem">Mensagem:</label>
                    <textarea id="mensagem" name="user_mensagem"></textarea>
                    <div>
                        <button type="submit">Enviar</button>
                    </div> 
                </fieldset>
            </form>
        </div>
    </main>
   
</body>
</html>    
