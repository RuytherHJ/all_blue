
import requests                         #     pip install requests
from bs4 import BeautifulSoup           #     pip install bs4

import mysql.connector                 #   pip install mysql-connector-python               
from mysql.connector import errorcode


banco=mysql.connector.connect(host='localhost', database='all_blue', user='root', password='thiago')

cursor=banco.cursor(buffered=True)

if banco.is_connected():
    print('FOI')
    

cursor.execute("SELECT id FROM lojas WHERE nome like 'terabyteshop' ")
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
    ultimo_elemento=0
    trava=False
    cont=0
    while trava !=True:

        url ='https://www.terabyteshop.com.br/hardware'

        headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.3"}

        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        hardwares=soup.find_all("div",{"class":"pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5"})
        print(hardwares)
        hardware_marca=soup.find_all('a',attrs={"class" : "commerce_columns_item_image"})
        print(len(hardware_marca))

        



        for k in range(ultimo_elemento,len(hardwares)):
                
                hardware_nome= hardwares[k].find('h2')  

                hardware_preco=hardwares[k].find('div', class_='prod-new-price')

                marca=hardware_marca[k]
                
                url_marca=f"https://www.pichau.com.br{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find('td',attrs={"class" : "value-field Marca"})

                cont=cont+1

                if propria_marca!=None and hardware_nome!=None and hardware_preco!=None:
                    
                    n=propria_marca.get_text().strip()
                    sem_registro(n)
                    n=busca_id_fabricante(n)
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
                    salvando_no_bd(m,p,n)
                
                if hardware_preco==None:
                    trava=True
                    break

        ultimo_elemento=cont
    
    print("FIM HARDWARE")
    

TUDO_HARDWARE()