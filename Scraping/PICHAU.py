
import requests                         #     pip install requests
from bs4 import BeautifulSoup           #     pip install bs4

import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode



banco=mysql.connector.connect(host='localhost', database='all_blue', user='root')

cursor=banco.cursor(buffered=True)

if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'pichau' ")
aux=cursor.fetchone()


id_loja=int(aux[0])


def salvando_no_bd(nome,preco,id_fa):
    cursor.execute(f"call insere_produtos( '{nome}' , {preco} , {id_loja} , {id_fa} );")
    
    banco.commit()
    
    

def sem_registro(nomMarca):
    cursor.execute(f"call insere_fabricante( '{nomMarca}');")
    
    banco.commit()


def busca_id_fabricante(nomMarca):
    
    cursor.execute(f"SELECT id FROM fabricante WHERE nome_fabricante like '%{nomMarca}%'")
    var=cursor.fetchone()
    envia=int(var[0])
    return envia

def TUDO_HARDWARE():
    print("COMEÇO HARDWARE")
    url ='https://www.pichau.com.br/hardware'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    hardwares=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    hardware_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})



    for k in range(len(hardwares)):
            
            hardware_nome= hardwares[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            hardware_preco=hardwares[k].find('div', class_='jss81')

            marca=hardware_marca[k]
            
            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and hardware_nome!=None and hardware_preco!=None:
                n=propria_marca.get_text().strip()
            
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                m=hardware_nome.get_text().strip()
                p=hardware_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                
                
                salvando_no_bd(m,p,n)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 278"}).get_text())
    


    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/hardware?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        hardwares=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        hardware_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(hardwares)!=0:
            for k in range(len(hardwares)):
            
                hardware_nome= hardwares[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                hardware_preco=hardwares[k].find('div', class_='jss81')

                marca=hardware_marca[k]
        
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                

                if propria_marca!=None and hardware_nome!=None and hardware_preco!=None:
                    n=propria_marca.get_text().strip()
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    m=hardware_nome.get_text().strip()
                    p=hardware_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                    
                    
                    salvando_no_bd(m,p,n)


        else:
            print("FIM HARDWARE")
            break



TUDO_HARDWARE()

def TUDO_PERIFERICOS():
    print("COMEÇO PERIFERICOS")
    url ='https://www.pichau.com.br/perifericos'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    perifericos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
    periferico_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

    for k in range(len(perifericos)):
            
            periferico_nome= perifericos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            periferico_preco=perifericos[k].find('div', class_='jss81')

            marca=periferico_marca[k]
            
            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and periferico_nome!=None and periferico_preco!=None:
                n=propria_marca.get_text().strip()
                
                
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                
                
                
                m=periferico_nome.get_text().strip()
                p=periferico_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                
                
                salvando_no_bd(m,p,n)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 208"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/perifericos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        perifericos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        periferico_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(perifericos)!=0:
            for k in range(len(perifericos)):
            
                periferico_nome= perifericos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                periferico_preco=perifericos[k].find('div', class_='jss81')

                marca=periferico_marca[k]
            
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                if propria_marca!=None and periferico_nome!=None and periferico_preco!=None:
                    n=propria_marca.get_text().strip()
                    
                    
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    m=periferico_nome.get_text().strip()
                    p=periferico_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                    salvando_no_bd(m,p,n)
        else:
            print("FIM PERIFERICOS")
            break


TUDO_PERIFERICOS()

def TUDO_NOTEBOOKS_PORTATEIS():
    print("COMEÇO NOTEBOOKS")
    url ='https://www.pichau.com.br/notebooks'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    notebooks=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
    notebooks_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

    for k in range(len(notebooks)):
            
            notebook_nome= notebooks[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            notebook_preco=notebooks[k].find('div', class_='jss81')


            marca=notebooks_marca[k]

            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and notebook_nome!=None and notebook_preco!=None:
                n=propria_marca.get_text().strip()
                
                
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                m=notebook_nome.get_text().strip()
                p=notebook_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                salvando_no_bd(m,p,n)
            

            


    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 11"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/notebooks?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        notebooks=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        notebooks_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(notebooks)!=0:
            for k in range(len(notebooks)):
            
                notebook_nome= notebooks[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                notebook_preco=notebooks[k].find('div', class_='jss81')

                marca=notebooks_marca[k]

                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                if propria_marca!=None and notebook_nome!=None and notebook_preco!=None:
                    n=propria_marca.get_text().strip()
                    
                    
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    m=notebook_nome.get_text().strip()
                    p=notebook_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                    
                    
                    salvando_no_bd(m,p,n)
        else:
            print("FIM NOTEBOOKS")
            break


TUDO_NOTEBOOKS_PORTATEIS()


def TUDO_ELETRONICOS():
    print("COMEÇO ELETRONICOS")
    url ='https://www.pichau.com.br/eletronicos'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    eletronicos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    eletronicos_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})


    for k in range(len(eletronicos)):
            
            eletronico_nome= eletronicos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            eletronico_preco=eletronicos[k].find('div', class_='jss81')

            marca=eletronicos_marca[k]
            
            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and eletronico_nome!=None and eletronico_preco!=None:
                n=propria_marca.get_text().strip()
                
                
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                m=eletronico_nome.get_text().strip()
                p=eletronico_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                
                
                salvando_no_bd(m,p,n)
            




    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 4"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/eletronicos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        eletronicos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        eletronicos_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(eletronicos)!=0:
            for k in range(len(eletronicos)):
            
                eletronico_nome= eletronicos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                eletronico_preco=eletronicos[k].find('div', class_='jss81')

                marca=eletronicos_marca[k]
            
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                if propria_marca!=None and eletronico_nome!=None and eletronico_preco!=None:
                    n=propria_marca.get_text().strip()
                    
                    
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    
                    m=eletronico_nome.get_text().strip()
                    p=eletronico_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                    
                    
                    salvando_no_bd(m,p,n)
                    

        else:
            print("FIM ELETRONICOS")
            break



TUDO_ELETRONICOS()

def TUDO_CADEIRAS_MESAS():
    print("COMEÇO CADEIRAS")
    url ='https://www.pichau.com.br/cadeiras'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    cadeiras=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    cadeiras_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

    for k in range(len(cadeiras)):
            
            cadeira_nome= cadeiras[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            cadeira_preco=cadeiras[k].find('div', class_='jss81')

            marca=cadeiras_marca[k]
            
            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and cadeira_nome!=None and cadeira_preco!=None:
                n=propria_marca.get_text().strip()
                
                
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                m=cadeira_nome.get_text().strip()
                p=cadeira_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                salvando_no_bd(m,p,n)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 29"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/cadeiras?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        cadeiras=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        cadeiras_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(cadeiras)!=0:
            for k in range(len(cadeiras)):
            
                cadeira_nome= cadeiras[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                cadeira_preco=cadeiras[k].find('div', class_='jss81')

                marca=cadeiras_marca[k]
            
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                if propria_marca!=None and cadeira_nome!=None and cadeira_preco!=None:
                    n=propria_marca.get_text().strip()
                    
                    
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    
                    m=cadeira_nome.get_text().strip()
                    p=cadeira_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                        
                        
                    salvando_no_bd(m,p,n)
                
        else:
            print("FIM CADEIRAS")
            break
            
        

TUDO_CADEIRAS_MESAS()


def TUDO_MONITORES():
    print("COMEÇO MONITORES")
    url ='https://www.pichau.com.br/monitores'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    monitores=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    monitores_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

    for k in range(len(monitores)):
            
            monitor_nome= monitores[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            monitor_preco=monitores[k].find('div', class_='jss81')

            marca=monitores_marca[k]
            
            url_marca=f"https://www.pichau.com.br{marca.get('href')}"
            pega_marca=requests.get(url_marca,headers=headers)
            soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
            propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

            

            if propria_marca!=None and monitor_nome!=None and monitor_preco!=None:
                n=propria_marca.get_text().strip()
                sem_registro(n)
                n=busca_id_fabricante(n)
                
                m=monitor_nome.get_text().strip()
                p=monitor_preco.get_text().strip()[2:]

                m=str(m)
                
                if '\xa0' in p :
                    p=p.replace('\xa0','')
                    p = p.replace(',', '.')  # substitui a vírgula por um ponto
                    last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                    p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                    
                else:

                    p=p.replace(',','.')

                p = float(p)

                
                
                salvando_no_bd(m,p,n)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 16"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/monitores?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        monitores=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        monitores_marca=soup.find_all('a',attrs={"data-cy" : "list-product"})

        if len(monitores)!=0:
            for k in range(len(monitores)):
            
                monitor_nome= monitores[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                monitor_preco=monitores[k].find('div', class_='jss81')
               
                marca=monitores_marca[k]
            
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})


                if propria_marca!=None and monitor_nome!=None and monitor_preco!=None:
                    n=propria_marca.get_text().strip()
                   
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    
                    m=monitor_nome.get_text().strip()
                    p=monitor_preco.get_text().strip()[2:]

                    m=str(m)
                    
                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:

                        p=p.replace(',','.')

                    p = float(p)

                    
                    
                    salvando_no_bd(m,p,n)
        else:
            print("FIM MONITORES")
            break

TUDO_MONITORES()