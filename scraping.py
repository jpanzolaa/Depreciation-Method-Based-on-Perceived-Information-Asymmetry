from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

url = 'https://carros.tucarro.com.co/electrico/_NoIndex_True'
driver = webdriver.Chrome()

datos_productos = []

for k in range(15):
    
    driver.get(url)

    links = driver.find_elements(By.XPATH, "//div[@class='ui-search-item__group ui-search-item__group--title']//a[1]")
    links = [link.get_attribute("href") for link in links]

    modelos = driver.find_elements(By.XPATH, "//li[@class='ui-search-card-attributes__attribute'][1]")
    modelos = [modelo.text for modelo in modelos]

    kiloms= driver.find_elements(By.XPATH, "//li[@class='ui-search-card-attributes__attribute'][2]")
    kiloms = [kilom.text for kilom in kiloms]

    ubis = driver.find_elements(By.XPATH, "//span[@class='ui-search-item__group__element ui-search-item__location'][1]")
    ubis = [ubi.text for ubi in ubis]


    for i in range(len(links)):

        driver.get(links[i])

        titulo = driver.find_element(By.TAG_NAME, "h1").text

        precio = driver.find_element(By.XPATH, "//span[@class='andes-money-amount__fraction']").text

        modelo = modelos[i]

        kilom = kiloms[i]

        ubi = ubis[i]
        
        sleep(2)

        datos_1 = driver.find_elements(By.XPATH, "//p//span[@class='ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--REGULAR']")
        datos_1 = [dato_1.text for dato_1 in datos_1]

        datos_2 = driver.find_elements(By.XPATH, "//p//span[@class='ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD']")
        datos_2 = [dato_2.text for dato_2 in datos_2]

        datos_adicionales = [datos_1[j] + datos_2[j] for j in range(len(datos_1))]

        producto = {
        "Nombre del carro": titulo,
        "Precio": precio,
        "Modelo": modelo,
        "Kilometraje": kilom,
        "Ubicación": ubi,
        "Información adicional": datos_adicionales
        }

        datos_productos.append(producto)
        print('Carro: ', i)
        print(datos_adicionales)
        print(k + 1)

        url = f'https://carros.mercadolibre.com.co/electrico/_Desde_{(k+1)*49-k}_NoIndex_True'
    

df = pd.DataFrame(datos_productos)
df.to_csv("PRODUCTOS.csv", index=False)
driver.close