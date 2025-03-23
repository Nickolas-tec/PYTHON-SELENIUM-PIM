

#####################################################################################################################
# CARREGAMENTO DE BIBLITOECAS E MODULOS
import time
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#####################################################################################################################

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


#####################################################################################################################

# ESTE TRECHO SELECIONA O FILTRO DE PESQUISAS

# AGUARDA ATÉ QUE O ELEMENTO COM A CLASSE "dropdown-toggle" ESTEJA PRESENTE NO DOM E ARMAZENA ELE NA VARIÁVEL
botao_pesquisas = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
)
# EM SEGUIDA, REALIZA O CLIQUE NO ELEMENTO IDENTIFICADO.
botao_pesquisas.click()

#####################################################################################################################

# ESTE TRECHO SELECIONA O TOPICO INDICADORES

# ENCONTRA O ELEMENTO COM A CLASSE "pesquisas-menu-arvore" NO DOM DA PÁGINA E ATRIBUI À VARIÁVEL
pesquisas_menu_arvore = navegador.find_element(By.CLASS_NAME, "pesquisas-menu-arvore")
# LOCALIZA O PRIMEIRO ELEMENTO <UL> DENTRO DO ELEMENTO 'PESQUISAS_MENU_ARVORE' E O ATRIBUI A TAG_UL
tag_ul = pesquisas_menu_arvore.find_element(By.TAG_NAME, "ul")
# ENCONTRA O PRIMEIRO ELEMENTO <LI> DENTRO DO ELEMENTO TAG_UL E O ATRIBUI A TAG_LI
tag_li = tag_ul.find_element(By.TAG_NAME, "li")
# O MUDULO REALIZA O CLIQUE NO PRIMEIRO ITEM DA LISTA <LI> ENCONTRADO
tag_li.click()

#####################################################################################################################

# ESTE TRECHO SELECIONA O TOPICO INDUSTRIA

# AGUARDA ATÉ QUE O BOTÃO COM O TEXTO "INDÚSTRIA" ESTEJA PRESENTE NO DOM DA PÁGINA.
industria = WebDriverWait(navegador, 10).until(
    # USA O XPATH PARA LOCALIZAR O ELEMENTO <SPAN> QUE CONTÉM O TEXTO ESPECÍFICO "INDÚSTRIA".
    EC.presence_of_element_located((By.XPATH, "//span[text()='Indústria']"))
)
industria.click() 
# ARMAZENA O ELEMENTO ENCONTRADO NA VARIÁVEL industria E REALIZA O CLIQUE PARA INTERAGIR COM O BOTÃO.

#####################################################################################################################

# AQUI E SELECIONADO A PESQUISA INDUSTRIAL MENSAL - PIM - PF BRASIL

# AGUARDA ATÉ QUE O LINK COM O TEXTO "PESQUISA INDUSTRIAL MENSAL - PRODUÇÃO FÍSICA - PIM-PF-BRASIL" ESTEJA PRESENTE NO DOM DA PÁGINA.
pim_pf_brasil = WebDriverWait(navegador, 10).until(
    # USA O XPATH PARA LOCALIZAR O ELEMENTO <A> QUE CONTÉM O TEXTO ESPECÍFICO.
    EC.presence_of_element_located((By.XPATH, "//a[text()='Pesquisa Industrial Mensal - Produção Física - PIM-PF-Brasil']"))
)
# ARMAZENA O ELEMENTO ENCONTRADO NA VARIÁVEL pim_pf_brasil E REALIZA O CLIQUE PARA ACESSAR AS INFORMAÇÕES.
pim_pf_brasil.click()

#####################################################################################################################

# ESTE TRECHO ENCONTRA E SELECIONA A TABELA 8887
tabela = navegador.find_element(By.CLASS_NAME, "tabela-8887")
tabela_element = tabela.find_elements(By.TAG_NAME, "td")

# ATRAVES DO XPATH E ENCONTRADO O BOTÃO PARA SELEÇÃO DA TABELA
botao_tabela = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tab-tabelas"]/section/div[1]/table/tbody/tr[5]/td[3]/a'))
)

botao_tabela.click()

#####################################################################################################################

# ESTE TRECHO REALIZA A MARCAÇÃO NA TABELA VARIÁVEL DE TODAS AS VARIÁVEIS 

# LOCALIZANDO O BOTÃO PELO ATRIBUTO 'DATA-CMD'
button = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cmd="marcarTudo"]'))
)

# GARANTINDO QUE O BOTÃO ESTEJA VISÍVEL ANTES DO CLIQUE
navegador.execute_script("arguments[0].scrollIntoView(true);", button)

# CLICANDO NO BOTÃO E SELECIONANDO TODAS AS OPÇÕES
try:
    button.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O MÉTODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button)



#####################################################################################################################

# ESTE TRECHO REALIZA A MARCAÇÃO NA TABELA GRANDES CATEGORIAS ECONÔMICAS APENAS DE 1 BENS DE CAPITAL

# LOCALIZANDO O BOTÃO PELO FULL XPATH
button_2 = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div[4]/div[3]/div/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button'))
)
try:
    button_2.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O METODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button_2)


#####################################################################################################################

# ESTE TRECHO REALIZA A MARCAÇÃO NA TABELA GRANDES CATEGORIAS ECONÔMICAS APENAS 2 BENS INTERMEDIÁRIOS
button_2_1 = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div[4]/div[3]/div/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button'))
)
try:
    button_2_1.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O METODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button_2_1)



#####################################################################################################################

# ESTE TRECHO REALIZA A MARCAÇÃO NA TABELA GRANDES CATEGORIAS ECONÔMICAS APENAS 3 BENS DE CONSUMO
button_2_2 = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div[4]/div[3]/div/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[4]/div/div/div/button'))
)
try:
    button_2_2.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O METODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button_2_2)



#####################################################################################################################

# ESTE TRECHO REALIZA A MARCAÇÃO NA TABELA GRANDES CATEGORIAS ECONÔMICAS APENAS 9 BENS NÃO ESPECIFICADOS ANTERIORMENTE
button_2_3 = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div[4]/div[3]/div/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[13]/div/div/div/button'))
)
try:
    button_2_3.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O METODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button_2_3)


#####################################################################################################################

button_2_4 = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div[4]/div[4]/div/div[2]/div[3]/div/div[1]/div[1]/div/button[1]'))
)
try:
    button_2_4.click()
except:
    # FORÇANDO O CLIQUE VIA JS CASO O METODO DIRETO VENHA A FALHAR
    navegador.execute_script("arguments[0].click();", button_2_4)


#####################################################################################################################


input("Clique em ENTER para encerrar o navegador...")

