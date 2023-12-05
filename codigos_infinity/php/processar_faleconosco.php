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
    $mensagem=$_POST['user_mensagem'];

    // Inserção dos dados no banco de dados

    $sql = "call all_blue.registra_mensagem('$nome','$email', '$mensagem');";




    if(strlen($email)>0 && strlen($nome)>0){
        
            if ($conn->query($sql) === TRUE) {
    
                $_SESSION['enviou_mensagem'] = true;
                $_SESSION['campo_fale_vazio']=false;
                
                header('Location: index.php');
                
                exit();
        
            }
                
    }else{
        
        $_SESSION['campo_fale_vazio']=true;
        $_SESSION['enviou_mensagem'] = false;
        header('Location: fale-conosco.php');
        exit();

    }
    

    // Feche a conexão com o banco de dados
    $conn->close();
} else {

   
}
?>