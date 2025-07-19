from modelo_webdriver import Webdriver
from leitor_dados import ler_dados_csv
from navegacao import acessar_pagina, fazer_login, fill_job_posting , new_job_posting, processamento_aplicantes

driver = Webdriver().criar_webdriver()
dados = ler_dados_csv()
acessar_pagina(driver)
fazer_login(driver, "jane007", "TheBestHR123")


for _, linha in dados.iterrows():
    
    new_job_posting(driver)
    fill_job_posting(driver, linha)

processamento_aplicantes(driver)

driver.close()