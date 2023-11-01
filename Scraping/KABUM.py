


from selenium import webdriver                              #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import re

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
    
    url ="https://www.kabum.com.br/hardware"
    driver.get(url)

    
    
    hardwares=driver.find_elements(By.CLASS_NAME,'productCard')
    hardwares_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
    hardwares_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
    hardwares_marca=driver.find_elements(By.CLASS_NAME,'productLink')

    for k in range(len(hardwares)):
            url ="https://www.kabum.com.br/hardware"
            driver.get(url)
            hardwares_nome=driver.find_elements(By.CLASS_NAME,'nameCard')
            hardwares_preco=driver.find_elements(By.CLASS_NAME,'priceCard')
            hardwares_marca=driver.find_elements(By.CLASS_NAME,'productLink')


            nome=hardwares_nome[k].text.strip()
            preco=hardwares_preco[k].text.strip()[2:]
            pega_marca=hardwares_marca[k].get_property('href')

            driver.get(pega_marca)

            marca = driver.find_element(By.ID, 'secaoInformacoesTecnicas')
            
            marca=marca.find_elements(By.TAG_NAME,'p')

            
            n=marca[1].text.strip()
            n=n.replace('- Marca:','').strip()
            print(n)

            if len(n)<20:

                if n!=None and nome!=None and preco!=None:
                    
                    sem_registro(n)
                    n=busca_id_fabricante(n)
                    m=nome
                    p=preco

                    if '\xa0' in p :
                        p=p.replace('\xa0','')
                        p = p.replace(',', '.')  # substitui a vírgula por um ponto
                        last_dot = p.rfind('.')  # encontra a última ocorrência do ponto
                        p = p[:last_dot].replace('.', '') + p[last_dot:]  # substitui os pontos antes da última ocorrência
                        
                    else:
                        p=p.replace(',','.')

                    p = float(p)
                    salvando_no_bd(m,p,n)
            

    pagina_final=int(soup.find('a',{"aria-label" : "Page 434"}).get_text())

    trava=False

    for pags in range(2,pagina_final):
        url=f'https://www.kabum.com.br/hardware?page_number={pags}&page_size=20&facet_filters=&sort=most_searched'
        site=requests.get(url, headers=headers)
        soup=BeautifulSoup(site.content, 'html.parser')
        hardwares=soup.find_all("div",{"class":"sc-93fa31de-7 gopyRO productCard"})
        hardware_marca=soup.find_all('a',{"class":"sc-93fa31de-10 eilolk productLink"})

        if trava!=True:
            for k in range(len(hardwares)):
            
                hardware_nome= hardwares[k].find('span',{'class':'sc-d79c9c3f-0 nlmfp sc-93fa31de-16 bBOYrL nameCard6'})  
                hardware_preco=hardwares[k].find('span', {'class':'sc-6889e656-2 bYcXfg priceCard'})
                marca=hardware_marca[k]
                
                url_marca=f"https://www.kabum.com.br/{marca.get('href')}"
                pega_marca=requests.get(url_marca,headers=headers)
                soup_marca=BeautifulSoup(pega_marca.content, 'html.parser')
                propria_marca=soup_marca.find_all('p')

                n=None
                for cont in range(len(propria_marca)):
                    if 'Marca' in propria_marca[cont].text:
                        n=propria_marca[cont].get_text().strip()
                        n=n.replace('- Marca:','')
                        n=n.strip()
                        break


                

                if n!=None and hardware_nome!=None and hardware_preco!=None:
                    
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
                    

        else:
            print("FIM HARDWARE")
            break

TUDO_HARDWARE()

