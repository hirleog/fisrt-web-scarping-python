import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# criando instancia do Navegador Chrome
service = Service()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=service, options=options)

url="https://books.toscrape.com/"
driver.get(url)
# FIM instancia



# PEGANDO elemento pela tag HTML dentro do site e printando a lista na tela

# essa linha está pegando a tag 'a' da 54º posição até a 94º posição indo de duas em duas tags 'a'
titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
titleList = [title.get_attribute('title') for title in titleElements]
# print(titleElements)

# FIM PEGANDO elemento pela tag HTML



# CLICANDO NO LIVRO SELECIONADO NO SITE
# titleElements[0].click()
# classElement = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace('available)', ''))
# print(classElement)
# driver.back()


# fazendo um loop para pegar o titulo a quantidade de stock todos os items na pagina
stockList = []
for element in titleElements:
    try:
        element.click()

        # Extrair informações de estoque
        try:
            qtdStock = driver.find_element(By.CLASS_NAME, 'instock.availability').text
            qtdStock = int(qtdStock.replace('In stock (', '').replace('available)', '').strip())
            stockList.append(qtdStock)
        except Exception as e:
            print(f"Erro ao extrair estoque: {e}")
            stockList.append(0)  # Adicione 0 se não conseguir obter o valor

        driver.back()

    except Exception as e:
        print(f"Erro ao clicar no elemento: {e}")
        continue

# print(stockList)
# FIM DO LOOP


# inserindo a lista de titulos e as qnt de estoque em uma tabela
disctDF = {'title': titleList, 'stock': qtdStock}
table = pd.DataFrame(disctDF)
print(table)
