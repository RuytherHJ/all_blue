


from selenium import webdriver                              #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode

banco=mysql.connector.connect(host='localhost', database='all_blue', user='root',password='thiago')

cursor=banco.cursor(buffered=True)

service=Service()
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)


if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'itxgamer'")
aux=cursor.fetchone()


id_loja=int(aux[0])



def salvando_no_bd(nome,preco,imagem,prodLink):
    cursor.execute(f"call insere_produtos('{nome}',{preco},{id_loja},'{imagem}','{prodLink}');")
    
    banco.commit()
    

def TUDO_HARDWARE():
    print("COMEÇO HARDWARE")
    
    pagina_final=39


    for pags in range(1,pagina_final):
    
        url =f"https://www.itxgamer.com.br/hardware?page={pags}"
        driver.get(url)
        
        hardwares=driver.find_elements(By.CLASS_NAME,'product-card')
        hardwares_nome=driver.find_elements(By.CLASS_NAME,'product-title')
        hardwares_preco=driver.find_elements(By.CLASS_NAME,'pix')
        hardwares_imagens=driver.find_elements(By.CLASS_NAME,'img-fluid')
        hardwares_paginas=driver.find_elements(By.CLASS_NAME,'product-link')
        metade = len(hardwares) // 2
        del hardwares[:metade]
        del hardwares_nome[:metade]
        del hardwares_preco[:metade]
        del hardwares_imagens[:47]
        del hardwares_paginas[:metade]
            
        for k in range(len(hardwares)):

                nome=hardwares_nome[k].text.strip()
                preco=hardwares_preco[k].text.strip()[2:]
                imagem=hardwares_imagens[k].get_attribute('src')
                prodLink=hardwares_paginas[k].get_attribute('href')

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

                    if 'no pix' in p:
                        p=p.replace('no pix','')
                        p=p.strip()
                    
                    if '\n' in p:
                        last_dot = p.rfind('\n') 
                        p=p[:last_dot]

                    
                    p = float(p)

                    salvando_no_bd(m,p,n,prodLink)

                if preco==None:
                    print("FIM HARDWARE")
                    break

TUDO_HARDWARE()
