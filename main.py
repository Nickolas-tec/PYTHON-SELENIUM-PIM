
# CARREGAMENTO DE BIBLITOECAS
import time
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# O OBJETO DRIVER RECEBE O WEBDRIVER DO CHROME DO SELENIUM
driver = selenium.webdriver.Chrome()

# NAVEGADOR RECEBE O DRIVER PARA IMPORTAR OS MODULOS
navegador = driver

# O OBJETO URL RECEBE O LINK DO SIDRA - IBGE
url = ('https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/')

# O MODULO SLEEP AGUARDA UM SEGUNDO PARA QUE O SITE CARREGUE TODOS OS COMPONENTES
sleep(1)

# UTILIZANDO O MODULO GET PARA BUSCAR ATRÁVES DA URL O SITE
navegador.get(url)


# AGUARDA ATÉ QUE O ELEMENTO COM A CLASSE "dropdown-toggle" ESTEJA PRESENTE NO DOM E ARMAZENA ELE NA VARIÁVEL
botao_pesquisas = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
)
# EM SEGUIDA, REALIZA O CLIQUE NO ELEMENTO IDENTIFICADO.
botao_pesquisas.click()

# ENCONTRA O ELEMENTO COM A CLASSE "pesquisas-menu-arvore" NO DOM DA PÁGINA E ATRIBUI À VARIÁVEL
pesquisas_menu_arvore = navegador.find_element(By.CLASS_NAME, "pesquisas-menu-arvore")
# LOCALIZA O PRIMEIRO ELEMENTO <UL> DENTRO DO ELEMENTO 'PESQUISAS_MENU_ARVORE' E O ATRIBUI A TAG_UL
tag_ul = pesquisas_menu_arvore.find_element(By.TAG_NAME, "ul")
# ENCONTRA O PRIMEIRO ELEMENTO <LI> DENTRO DO ELEMENTO TAG_UL E O ATRIBUI A TAG_LI
tag_li = tag_ul.find_element(By.TAG_NAME, "li")
# O MUDULO REALIZA O CLIQUE NO PRIMEIRO ITEM DA LISTA <LI> ENCONTRADO
tag_li.click()


# AGUARDA ATÉ QUE O BOTÃO COM O TEXTO "INDÚSTRIA" ESTEJA PRESENTE NO DOM DA PÁGINA.
industria = WebDriverWait(navegador, 10).until(
    # USA O XPATH PARA LOCALIZAR O ELEMENTO <SPAN> QUE CONTÉM O TEXTO ESPECÍFICO "INDÚSTRIA".
    EC.presence_of_element_located((By.XPATH, "//span[text()='Indústria']"))
)
industria.click() 
# ARMAZENA O ELEMENTO ENCONTRADO NA VARIÁVEL industria E REALIZA O CLIQUE PARA INTERAGIR COM O BOTÃO.

# AGUARDA ATÉ QUE O LINK COM O TEXTO "PESQUISA INDUSTRIAL MENSAL - PRODUÇÃO FÍSICA - PIM-PF-BRASIL" ESTEJA PRESENTE NO DOM DA PÁGINA.
pim_pf_brasil = WebDriverWait(navegador, 10).until(
    # USA O XPATH PARA LOCALIZAR O ELEMENTO <A> QUE CONTÉM O TEXTO ESPECÍFICO.
    EC.presence_of_element_located((By.XPATH, "//a[text()='Pesquisa Industrial Mensal - Produção Física - PIM-PF-Brasil']"))
)
# ARMAZENA O ELEMENTO ENCONTRADO NA VARIÁVEL pim_pf_brasil E REALIZA O CLIQUE PARA ACESSAR AS INFORMAÇÕES.
pim_pf_brasil.click()



input("Clique em ENTER para encerrar o navegador...")

#time.sleep(20)
