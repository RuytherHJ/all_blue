<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Configuração de conexão com o banco de dados
    $servername = "localhost:3306";
    $username = "root";
    $password = "";
    $dbname = "all_blue";

    // Conecte-se ao banco de dados
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verifique a conexão
    if ($conn->connect_error) {
        die("Falha na conexão com o banco de dados: " . $conn->connect_error);
    }

    // Captura os dados do formulário
    $nome = trim($_POST['user_name']);
    $email = filter_var($_POST['user_email'], FILTER_SANITIZE_EMAIL);
    $senha = trim($_POST['user_senha']);
    $confirmadora=trim($_POST['user_senhaconfirma']);

    // Inserção dos dados no banco de dados

    $sql = "call all_blue.insere_usuario('$email','".sha1($senha)."', '$nome');";




    if($senha!=$confirmadora){

        $_SESSION['campo_vazio']=false;
        $_SESSION['senhas_diferentes']=true;
        $_SESSION['erro_de_cadastro']=false;

        header('Location: /all_blue/codigos/php/cadastro_usuario.php');
        exit();





    }elseif(strlen($senha)>0 && strlen($email)>0 && strlen($nome)>0 && strlen($confirmadora)>0){
        
            if ($conn->query($sql) === TRUE) {
    
    
                $_SESSION['nome_logado']=$nome;
                $_SESSION['usuarioLogado'] = true;
                
                $_SESSION['cadastrou']=true;
                
                header('Location: /all_blue/codigos/php/all_blue.php');
                
                exit();
        
            } else {
                
                $_SESSION['campo_vazio']=false;
                $_SESSION['senhas_diferentes']=false;
                $_SESSION['erro_de_cadastro']=true;
    
                header('Location: /all_blue/codigos/php/cadastro_usuario.php');
                exit();
            }

    }else{
        $_SESSION['senhas_diferentes']=false;
        $_SESSION['erro_de_cadastro']=false;
        $_SESSION['campo_vazio']=true;
        header('Location: /all_blue/codigos/php/cadastro_usuario.php');
        exit();

    }
    

    // Feche a conexão com o banco de dados
    $conn->close();
} else {

   
}
?>
