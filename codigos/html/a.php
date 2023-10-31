<?php
                    include '/all_blue/codigos/php/pegar_bd.php';
                
                    // Exibir informações do banco de dados
                    if ($result->num_rows > 0) {
                        while ($row = $result->fetch_assoc()) {
                            echo "Nome do Produto: " . $row["nome_produto"] . "<br>";
                            echo "Preço: " . $row["preco"] . "<br>";
                            echo "Loja: " . $row["nome_loja"] . "<br>";
                            echo "Marca: " . $row["nome_fabricante"] . "<br>";
                            
                            // Exibir a URL da logo da marca
                            echo '<img src="' . $row["logo"] . '" alt="Logo da Marca"><br><br>';
                        }
                    } else {
                        echo "Nenhuma informação encontrada no banco de dados.";
                    }
                    ?>