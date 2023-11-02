


from selenium import webdriver                              #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import re

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
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'kabum'")
aux=cursor.fetchone()


id_loja=int(aux[0])



def salvando_no_bd(nome,preco,imagem,prodLink):
    cursor.execute(f"call insere_produtos('{nome}',{preco},{id_loja},'{imagem}','{prodLink}');")
    
    banco.commit()
    

def TUDO_HARDWARE():
    print("COMEÇO HARDWARE")
    
    url ="https://www.kabum.com.br/hardware"
    driver.get(url)

    
    
    hardwares=driver.find_elements(By.CLASS_NAME,'productCard')
    hardwares_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
    hardwares_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
    hardwares_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
    hardwares_paginas=driver.find_elements(By.CLASS_NAME,'productLink')


    for k in range(len(hardwares)):

            nome=hardwares_nome[k].text.strip()
            preco=hardwares_preco[k].text.strip()[2:]
            imagem=hardwares_imagens[k].get_property('src')
            prodLink=hardwares_paginas[k].get_property('href')

            if nome!=None and preco!=None and imagem!=None:
                n=imagem
                m=nome
                p=preco

                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:
                    p = p.replace('.', '').replace(',', '.')
                
                p = float(p)

                salvando_no_bd(m,p,n,prodLink)
            
    
    pagina_final=int(driver.find_element(By.XPATH,"//*[@aria-label='Page 429']").text)
    trava=False
    
    for pags in range(2,pagina_final):
        url=f"https://www.kabum.com.br/hardware?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        hardwares=driver.find_elements(By.CLASS_NAME,'productCard')
        hardwares_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        hardwares_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        hardwares_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        hardwares_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
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
                    elif '-'in preco:
                        trava=True
                        break

                    else:
                        p = p.replace('.', '').replace(',', '.')

                    p = float(p)
                    salvando_no_bd(m,p,n,prodLink)
                    


                if preco==None:
                        trava=True
                        break
                    

        else:
            print("FIM HARDWARE")
            break

TUDO_HARDWARE()

