


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



def TUDO_PERIFERICOS():


    pagina_final=11


    for pags in range(1,pagina_final):
    
        url =f"https://www.itxgamer.com.br/perifericos?page={pags}"
        driver.get(url)
        
        perifericos=driver.find_elements(By.CLASS_NAME,'product-card')
        perifericos_nome=driver.find_elements(By.CLASS_NAME,'product-title')
        perifericos_preco=driver.find_elements(By.CLASS_NAME,'pix')
        perifericos_imagens=driver.find_elements(By.CLASS_NAME,'img-fluid')
        perifericos_paginas=driver.find_elements(By.CLASS_NAME,'product-link')
        metade = len(perifericos) // 2
        del perifericos[:metade]
        del perifericos_nome[:metade]
        del perifericos_preco[:metade]
        del perifericos_imagens[:47]
        del perifericos_paginas[:metade]
            
        for k in range(len(perifericos)):

                nome=perifericos_nome[k].text.strip()
                preco=perifericos_preco[k].text.strip()[2:]
                imagem=perifericos_imagens[k].get_attribute('src')
                prodLink=perifericos_paginas[k].get_attribute('href')

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


        else:
            print("FIM PERIFERICOS")
            break
           

TUDO_PERIFERICOS()

def TUDO_NOTEBOOKS_PORTATEIS():
    print("COMEÇO NOTEBOOKS")
    pagina_final=1


    for pags in range(1,pagina_final):
    
        url =f"https://www.itxgamer.com.br/notebook?page={pags}"
        driver.get(url)
        
        notebooks=driver.find_elements(By.CLASS_NAME,'product-card')
        notebooks_nome=driver.find_elements(By.CLASS_NAME,'product-title')
        notebooks_preco=driver.find_elements(By.CLASS_NAME,'pix')
        notebooks_imagens=driver.find_elements(By.CLASS_NAME,'img-fluid')
        notebooks_paginas=driver.find_elements(By.CLASS_NAME,'product-link')
        metade = len(notebooks) // 2
        del notebooks[:metade]
        del notebooks_nome[:metade]
        del notebooks_preco[:metade]
        del notebooks_imagens[:47]
        del notebooks_paginas[:metade]
            
        for k in range(len(notebooks)):

                nome=notebooks_nome[k].text.strip()
                preco=notebooks_preco[k].text.strip()[2:]
                imagem=notebooks_imagens[k].get_attribute('src')
                prodLink=notebooks_paginas[k].get_attribute('href')

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

        else:
            print("FIM NOTEBOOK")
            break

TUDO_NOTEBOOKS_PORTATEIS()


def TUDO_CADEIRAS_MESAS():
    print("COMEÇO CADEIRAS")
    pagina_final=3


    for pags in range(1,pagina_final):
    
        url =f"https://www.itxgamer.com.br/cadeiras?page={pags}"
        driver.get(url)
        
        cadeiras=driver.find_elements(By.CLASS_NAME,'product-card')
        cadeiras_nome=driver.find_elements(By.CLASS_NAME,'product-title')
        cadeiras_preco=driver.find_elements(By.CLASS_NAME,'pix')
        cadeiras_imagens=driver.find_elements(By.CLASS_NAME,'img-fluid')
        cadeiras_paginas=driver.find_elements(By.CLASS_NAME,'product-link')
        metade = len(cadeiras) // 2
        del cadeiras[:metade]
        del cadeiras_nome[:metade]
        del cadeiras_preco[:metade]
        del cadeiras_imagens[:47]
        del cadeiras_paginas[:metade]
            
        for k in range(len(cadeiras)):

                nome=cadeiras_nome[k].text.strip()
                preco=cadeiras_preco[k].text.strip()[2:]
                imagem=cadeiras_imagens[k].get_attribute('src')
                prodLink=cadeiras_imagens[k].get_attribute('href')

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

                    
        else:
            print("FIM CADEIRAS")
            break
            
TUDO_CADEIRAS_MESAS()
