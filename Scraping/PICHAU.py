
import requests                         #     pip install requests
from bs4 import BeautifulSoup           #     pip install bs4

import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode

import re



banco=mysql.connector.connect(host='localhost', database='all_blue', user='root', password='thiago')

cursor=banco.cursor()

if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'pichau' ")
aux=cursor.fetchone()

id_loja=int(aux[0])

ajuda=18







def salvando_no_bd(nome,preco):
    cursor.execute(f"call insere_produtos( '{nome}' , {preco} , {id_loja} , {ajuda} );")
    
    banco.commit()
    

def TUDO_HARDWARE():
    
    url ='https://www.pichau.com.br/hardware'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    hardwares=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(hardwares)):
            
            hardware_nome= hardwares[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            hardware_preco=hardwares[k].find('div', class_='jss81')


            if hardware_nome!=None and hardware_preco!=None:
                m=hardware_nome.get_text().strip()
                p=hardware_preco.get_text().strip()[2:]
                
                
                m=str(m)
                
                p = p.replace(',', '.')
                p = p.replace('\xa01', '.')
                if p
                p = float(p)

                
                
                
                salvando_no_bd(m,p)
                    



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 278"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/hardware?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        hardwares=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        
        with open('dados_hardwares.csv','a',newline='',encoding='UTF-8')  as envia:

            if len(hardwares)!=0:
                for k in range(len(hardwares)):
                
                    hardware_nome= hardwares[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                    hardware_preco=hardwares[k].find('div', class_='jss81')

                    if hardware_nome!=None and hardware_preco!=None:
                        m=hardware_nome.get_text().strip()

                        p=hardware_preco.get_text().strip()[2:]
                        p=float(p)
                        salvando_no_bd(m,p)
            else:
                pags=pagina_final


def TUDO_PERIFERICOS():

    url ='https://www.pichau.com.br/perifericos'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    perifericos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(perifericos)):
            
            periferico_nome= perifericos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            periferico_preco=perifericos[k].find('div', class_='jss81')

            if periferico_nome!=None and periferico_preco!=None:
                m=periferico_nome.get_text().strip()

                p=periferico_preco.get_text().strip()[2:]
                salvando_no_bd(m,p)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 208"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/perifericos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        perifericos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        

        if len(perifericos)!=0:
            for k in range(len(perifericos)):
            
                periferico_nome= perifericos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                periferico_preco=perifericos[k].find('div', class_='jss81')

                if periferico_nome!=None and periferico_preco!=None:
                    m=periferico_nome.get_text().strip()

                    p=periferico_preco.get_text().strip()[2:]

                    salvando_no_bd(m,p)
        else:
            pags=pagina_final

def TUDO_NOTEBOOKS_PORTATEIS():

    url ='https://www.pichau.com.br/notebooks'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    notebooks=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(notebooks)):
            
            notebook_nome= notebooks[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            notebook_preco=notebooks[k].find('div', class_='jss81')

            if notebook_nome!=None and notebook_preco!=None:
                m=notebook_nome.get_text().strip()

                p=notebook_preco.get_text().strip()[2:]

                salvando_no_bd(m,p)


    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 11"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/notebooks?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        notebooks=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        

        if len(notebooks)!=0:
            for k in range(len(notebooks)):
            
                notebook_nome= notebooks[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                notebook_preco=notebooks[k].find('div', class_='jss81')

                if notebook_nome!=None and notebook_preco!=None:
                    m=notebook_nome.get_text().strip()

                    p=notebook_preco.get_text().strip()[2:]

                    salvando_no_bd(m,p)
        else:
            pags=pagina_final


def TUDO_ELETRONICOS():

    url ='https://www.pichau.com.br/eletronicos'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    eletronicos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(eletronicos)):
            
            eletronico_nome= eletronicos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            eletronico_preco=eletronicos[k].find('div', class_='jss81')

            if eletronico_nome!=None and eletronico_preco!=None:
                m=eletronico_nome.get_text().strip()

                p=eletronico_preco.get_text().strip()[2:]

                salvando_no_bd(m,p)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 4"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/eletronicos?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        eletronicos=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        

        if len(eletronicos)!=0:
            for k in range(len(eletronicos)):
            
                eletronico_nome= eletronicos[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                eletronico_preco=eletronicos[k].find('div', class_='jss81')

                if eletronico_nome!=None and eletronico_preco!=None:
                    m=eletronico_nome.get_text().strip()

                    p=eletronico_preco.get_text().strip()[2:]

                    salvando_no_bd(m,p)
        else:
            pags=pagina_final


def TUDO_CADEIRAS_MESAS():

    url ='https://www.pichau.com.br/cadeiras'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    cadeiras=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(cadeiras)):
            
            cadeira_nome= cadeiras[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            cadeira_preco=cadeiras[k].find('div', class_='jss81')

            if cadeira_nome!=None and cadeira_preco!=None:
                m=cadeira_nome.get_text().strip()

                p=cadeira_preco.get_text().strip()[2:]

                salvando_no_bd(m,p)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 29"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/cadeiras?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        cadeiras=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        

        if len(cadeiras)!=0:
            for k in range(len(cadeiras)):
            
                cadeira_nome= cadeiras[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                cadeira_preco=cadeiras[k].find('div', class_='jss81')

                if cadeira_nome!=None and cadeira_preco!=None:
                    m=cadeira_nome.get_text().strip()

                    p=cadeira_preco.get_text().strip()[2:]

                    salvando_no_bd(m,p)
                
        else:
            break
            
        




def TUDO_MONITORES():

    url ='https://www.pichau.com.br/monitores'

    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

    site=requests.get(url, headers=headers)
    soup=BeautifulSoup(site.content, 'html.parser')
    monitores=soup.find_all("div",{"class":"MuiCardContent-root jss64"})

    for k in range(len(monitores)):
            
            monitor_nome= monitores[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

            monitor_preco=monitores[k].find('div', class_='jss81')

            if monitor_nome!=None and monitor_preco!=None:
                m=monitor_nome.get_text().strip()

                p=monitor_preco.get_text().strip()[2:]

                salvando_no_bd(m,p)



    pagina_final=int(soup.find('button',attrs={"aria-label" : "Go to page 16"}).get_text())



    for pags in range(2,pagina_final):

        url=f'https://www.pichau.com.br/monitores?page={pags}'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        monitores=soup.find_all("div",{"class":"MuiCardContent-root jss64"})
        

        if len(monitores)!=0:
            for k in range(len(monitores)):
            
                monitor_nome= monitores[k].find('h2',class_='MuiTypography-root jss78 jss79 MuiTypography-h6')  

                monitor_preco=monitores[k].find('div', class_='jss81')

                if monitor_nome!=None and monitor_preco!=None:
                    m=monitor_nome.get_text().strip()

                    p=monitor_preco.get_text().strip()[2:]

                    salvando_no_bd(m,p)
        else:
            pags=pagina_final



TUDO_HARDWARE()



