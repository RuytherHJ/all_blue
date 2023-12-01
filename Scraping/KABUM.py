


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
            
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
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

def TUDO_PERIFERICOS():
    print("COMEÇO PERIFERICOS")
    
    url ="https://www.kabum.com.br/perifericos"
    driver.get(url)
            
    
    pagina_final=510
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/perifericos?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        perifericos=driver.find_elements(By.CLASS_NAME,'cardProdutoListagem')
        perifericos_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        perifericos_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        perifeircos_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        perifericos_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(perifericos)):

                nome=perifericos_nome[k].text.strip()
                preco=perifericos_preco[k].text.strip()[2:]
                imagem=perifeircos_imagens[k].get_property('src')
                prodLink=perifericos_paginas[k].get_property('href')

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
            print("FIM PERIFERICOS")
            break

TUDO_PERIFERICOS()

def TUDO_COMPUTADORES():
    print("COMEÇO COMPUTADORES")
    
    url ="https://www.kabum.com.br/computadores"
    driver.get(url)
            
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/computadores?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        computadores=driver.find_elements(By.CLASS_NAME,'productCard')
        computadores_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        computadores_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        computadores_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        computadores_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(computadores)):

                nome=computadores_nome[k].text.strip()
                preco=computadores_preco[k].text.strip()[2:]
                imagem=computadores_imagens[k].get_property('src')
                prodLink=computadores_paginas[k].get_property('href')

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
            print("FIM COMPUTADORES")
            break

TUDO_COMPUTADORES()


def TUDO_ESPACO_GAMER():
    print("COMEÇO ESPAÇO-GAMER")
    
    url ="https://www.kabum.com.br/espaco-gamer"
    driver.get(url)
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/espaco-gamer?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        espacos=driver.find_elements(By.CLASS_NAME,'productCard')
        espacos_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        espacos_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        espacos_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        espacos_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(espacos)):

                nome=espacos_nome[k].text.strip()
                preco=espacos_preco[k].text.strip()[2:]
                imagem=espacos_imagens[k].get_property('src')
                prodLink=espacos_paginas[k].get_property('href')

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
            print("FIM ESPAÇO-GAMER")
            break

TUDO_ESPACO_GAMER()

def TUDO_GAMER():
    print("COMEÇO GAMER")
    
    url ="https://www.kabum.com.br/gamer"
    driver.get(url)
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/gamer?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        gamers=driver.find_elements(By.CLASS_NAME,'productCard')
        gamers_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        gamers_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        gamers_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        gamers_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(gamers)):

                nome=gamers_nome[k].text.strip()
                preco=gamers_preco[k].text.strip()[2:]
                imagem=gamers_imagens[k].get_property('src')
                prodLink=gamers_paginas[k].get_property('href')

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
            print("FIM GAMER")
            break

TUDO_GAMER()

def TUDO_CELULARES():
    print("COMEÇO CELULARES")
    
    url ="https://www.kabum.com.br/celular-smartphone"
    driver.get(url)
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/celular-smartphone?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        celulares=driver.find_elements(By.CLASS_NAME,'productCard')
        celulares_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        celulares_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        celulares_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        celulares_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(celulares)):

                nome=celulares_nome[k].text.strip()
                preco=celulares_preco[k].text.strip()[2:]
                imagem=celulares_imagens[k].get_property('src')
                prodLink=celulares_paginas[k].get_property('href')

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
            print("FIM CELULARES")
            break

TUDO_CELULARES()

def TUDO_TV():
    print("COMEÇO TV")
    
    url ="https://www.kabum.com.br/tv"
    driver.get(url)
    
    pagina_final=500
    trava=False
    
    for pags in range(1,pagina_final):
        url=f"https://www.kabum.com.br/tv?page_number={pags}&page_size=20&facet_filters=&sort=most_searched"
        driver.get(url)
        tvs=driver.find_elements(By.CLASS_NAME,'productCard')
        tvs_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
        tvs_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
        tvs_imagens=driver.find_elements(By.CLASS_NAME,'imageCard')
        tvs_paginas=driver.find_elements(By.CLASS_NAME,'productLink')

        if trava!=True:
            for k in range(len(tvs)):

                nome=tvs_nome[k].text.strip()
                preco=tvs_preco[k].text.strip()[2:]
                imagem=tvs_imagens[k].get_property('src')
                prodLink=tvs_paginas[k].get_property('href')

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
            print("FIM TV")
            break

TUDO_TV()