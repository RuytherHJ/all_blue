


from selenium import webdriver                              #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode

import time


banco=mysql.connector.connect(host='localhost', database='all_blue', user='root',password='thiago')

cursor=banco.cursor(buffered=True)

service=Service()
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)


if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'shopinfo'")
aux=cursor.fetchone()


id_loja=int(aux[0])



def salvando_no_bd(nome,preco,imagem,prodLink):
    cursor.execute(f"call insere_produtos('{nome}',{preco},{id_loja},'{imagem}','{prodLink}');")
    
    banco.commit()
    

def TUDO_HARDWARE():
    print("COMEÇO HARDWARE")
    
    url ="https://www.shopinfo.com.br/hardware"
    driver.get(url)


    time.sleep(10)
    botao=driver.find_element(By.CLASS_NAME,'ver-mais-produtos')

    

    while botao!=None:
         
        botao.click()


        time.sleep(20)

        botao=driver.find_element(By.CLASS_NAME,'ver-mais-produtos')
         


    
    
    hardwares=driver.find_elements(By.CLASS_NAME,'6de5eca9-43ec-4f0b-9a7e-32a5bf4a14b7')
    hardwares_nome=driver.find_elements(By.CLASS_NAME,'product-name')
    hardwares_preco=driver.find_elements(By.CLASS_NAME,'value ')
    hardwares_imagens=driver.find_elements(By.XPATH,"//*[@width='185']")
    hardwares_paginas=driver.find_elements(By.CLASS_NAME,'shelf-common__link')


    for k in range(len(hardwares)):

            nome=hardwares_nome[k].text.strip()
            preco=hardwares_preco[k].text.strip()[2:]
            imagem=hardwares_imagens[k].get_property('src')
            prodLink=hardwares_paginas[k].get_property('href')

            if nome!=None and preco!=None and imagem!=None:
                n=imagem
                m=nome
                p=preco
                m=m.replace("'",'')
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:
                    p = p.replace('.', '').replace(',', '.')
                
                p = float(p)

                salvando_no_bd(m,p,n,prodLink)
            
    


    print("FIM HARDWARE")
            

TUDO_HARDWARE()