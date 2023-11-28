import requests                         #     pip install requests
from bs4 import BeautifulSoup           #     pip install bs4

import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode

banco=mysql.connector.connect(host='localhost', database='all_blue', user='root', password='thiago')

cursor=banco.cursor(buffered=True)

if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'pichau' ")
aux=cursor.fetchone()


id_loja=int(aux[0])

def salvando_no_bd(nome,preco,imagem,prodLink):
    cursor.execute(f"call insere_produtos('{nome}',{preco},{id_loja},'{imagem}','{prodLink}');")
    
    banco.commit()
    

def TUDO_HARDWARE():
    print("COMEÇO HARDWARE")
    url ='https://www.pichau.com.br/hardware'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    
    pagina_final=278

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/hardware?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        hardwares=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        hardware_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(hardwares)):
            
                hardware_nome= hardwares[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                hardware_preco=hardwares[k].find('div', class_='jss81')

                imagem=hardware_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{imagem.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})
                

                

                if hardware_nome!=None and hardware_preco!=None:

                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=hardware_nome.get_text().strip()
                    p=hardware_preco.get_text().strip()[2:]
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)

                if hardware_preco==None:
                    trava=True
                    break
                    

        else:
            print("FIM HARDWARE")
            break

TUDO_HARDWARE()

def TUDO_PERIFERICOS():
    print("COMEÇO PERIFERICOS")
    url ='https://www.pichau.com.br/perifericos'
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    pagina_final=210

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/perifericos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        perifericos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        periferico_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(perifericos)):
            
                periferico_nome= perifericos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                periferico_preco=perifericos[k].find('div', class_='jss81')

                periferico=periferico_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{periferico.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})


                if periferico_nome!=None and periferico_preco!=None:
                    
                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=periferico_nome.get_text().strip()
                    p=periferico_preco.get_text().strip()[2:]

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)

                if periferico_preco==None:
                    trava=True
                    break
                        

        else:
            print("FIM PERIFERICOS")
            break
           
TUDO_PERIFERICOS()

def TUDO_NOTEBOOKS_PORTATEIS():
    print("COMEÇO NOTEBOOKS")
    url ='https://www.pichau.com.br/notebooks'
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    pagina_final=11

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/notebooks?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        notebooks=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        notebook_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(notebooks)):
            
                notebook_nome= notebooks[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                notebook_preco=notebooks[k].find('div', class_='jss81')

                notebook=notebook_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{notebook.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})


                if notebook_nome!=None and notebook_preco!=None:
                    
                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=notebook_nome.get_text().strip()
                    p=notebook_preco.get_text().strip()[2:]

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)
                
                if notebook_preco==None:
                    trava=True
                    break

        else:
            print("FIM NOTEBOOK")
            break

TUDO_NOTEBOOKS_PORTATEIS()

def TUDO_ELETRONICOS():
    print("COMEÇO ELETRONICOS")
    url ='https://www.pichau.com.br/eletronicos'
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    pagina_final=4

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/eletronicos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        eletronicos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        eleronico_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(eletronicos)):
            
                eletronico_nome= eletronicos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                eletronico_preco=eletronicos[k].find('div', class_='jss81')

                eletronico=eleronico_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{eletronico.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})


                if eletronico_nome!=None and eletronico_preco!=None:
                    
                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=eletronico_nome.get_text().strip()
                    p=eletronico_preco.get_text().strip()[2:]

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)
                
                if eletronico_preco==None:
                    trava=True
                    break
              
        else:
            print("FIM ELETRONICOS")
            break

TUDO_ELETRONICOS()

def TUDO_CADEIRAS_MESAS():
    print("COMEÇO CADEIRAS")
    url ='https://www.pichau.com.br/cadeiras'
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    pagina_final=29

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/cadeiras?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        cadeiras=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        cadeira_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(cadeiras)):
            
                cadeira_nome= cadeiras[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                cadeira_preco=cadeiras[k].find('div', class_='jss81')

                cadeira=cadeira_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{cadeira.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})

                if cadeira_nome!=None and cadeira_preco!=None:
                    
                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=cadeira_nome.get_text().strip()
                    p=cadeira_preco.get_text().strip()[2:]

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)
                
                if cadeira_preco==None:
                    trava=True
                    break
                    
        else:
            print("FIM CADEIRAS")
            break
            
TUDO_CADEIRAS_MESAS()

def TUDO_MONITORES():
    print("COMEÇO MONITORES")
    url ='https://www.pichau.com.br/monitores'
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    pagina_final=16

    trava=False

    for pags in range(1,pagina_final):
        url=f'https://www.pichau.com.br/monitores?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        monitores=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        monitor_imagem=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if trava!=True:
            for k in range(len(monitores)):
            
                monitor_nome= monitores[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                monitor_preco=monitores[k].find('div', class_='jss81')

                monitor=monitor_imagem[k]
                
                url_imagem=f"https://www.pichau.com.br{monitor.get('href')}"
                pega_imagem=requests.get(url_imagem,headers=headers)
                soup_imagem=BeautifulSoup(pega_imagem.content, 'html.parser')
                propria_imagem=soup_imagem.find('img',{"style" : "transition:opacity 0ms linear 0ms, visibility 0ms linear 0ms"})

                if monitor_nome!=None and monitor_preco!=None:
                    
                    n=propria_imagem.get('src')
                    l=url_imagem
                    m=monitor_nome.get_text().strip()
                    p=monitor_preco.get_text().strip()[2:]

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n,l)
                
                if monitor_preco==None:
                    trava=True
                    break
                    

        else:
            print("FIM MONITORES")
            break

TUDO_MONITORES