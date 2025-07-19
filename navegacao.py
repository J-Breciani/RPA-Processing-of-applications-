from modelo_webdriver import Webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


def acessar_pagina(driver): # Navega para o site
    driver.get('https://rpaexercise.aisingapore.org/login')
    
def fazer_login(driver, login, senha): # Faz login utilizando as informações recebidas de login e senha e clica no botão de confirmar
    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="outlined-search"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
    driver.find_element(By.XPATH, '//*[@id="login"]').click()
    
def new_job_posting(driver): # Clica para fazer um novo job posting
    driver.find_element(By.XPATH, '//*[@id="newJobPosting"]').click()

def fill_job_posting(driver, linha_dados):
    sleep(2)
    # Rseponde o componente de Job Title
    driver.find_element(By.XPATH, '//*[@id="jobTitle"]').send_keys(linha_dados['jobTitle'])
    
    # Responde o componente de Job Description
    driver.find_element(By.XPATH, '//*[@id="jobDescription"]').send_keys(linha_dados['jobDescription'])
    
    # Seleciona a combobox correta para Hiring Department
    hiring_department = driver.find_element(By.XPATH, '//*[@id="hiringDepartment"]')
    hp_combobox = Select(hiring_department)
    hp_combobox.select_by_visible_text(linha_dados['hiringDepartment'])
    
    # Seleciona a comobbox correta para Education Level
    education_level = driver.find_element(By.XPATH, '//*[@id="educationLevel"]')
    ed_combobox = Select(education_level)
    ed_combobox.select_by_visible_text(linha_dados['educationLevel'])
    
    # Responde a data de início e data de fim
    driver.find_element(By.XPATH, '//*[@id="postingStartDate"]').send_keys(linha_dados['postingStartDate'])
    driver.find_element(By.XPATH, '//*[@id="postingEndDate"]').send_keys(linha_dados['postingEndDate'])
    
    # Responde se é remoto ou não
    if linha_dados['remote'] == "No":
        driver.find_element(By.XPATH, '//label[.//span[text()="No"]]').click()
    
    # Responde o Job Type
    opcoes_jobType = linha_dados['jobType'].split('/')
    for opcao in opcoes_jobType:
        xpath_label = f'//label[.//span[text()="{opcao}"]]/span[1]'
        driver.find_element(By.XPATH, xpath_label).click()
        
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    
def processamento_aplicantes(driver):
    botoes_visualizar = driver.find_elements(By.XPATH, '//button[.//span[text()="View Applicant List"]]')
    for i in range(len(botoes_visualizar)):
        # Recarrega os botões (pois a página muda a cada clique)
        botoes = driver.find_elements(By.XPATH, '//button[.//span[text()="View Applicant List"]]')
        botoes[i].click()
        sleep(2)
        
        education_level = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[10]/p').text
        tabela = driver.find_element(By.XPATH, '//table//tbody')
        linhas = tabela.find_elements(By.TAG_NAME, 'tr')
        for linha in linhas:
            try:
                applicant_education = linha.find_element(By.XPATH, f'.//td[text()="{education_level}"]')

                score = int(linha.find_element(By.XPATH, './td[5]').text) # ESTÁ RETORNANDO 'DOWNLOAD'!!!
            
                if score > 70:
                    linha.find_element(By.XPATH, './/span[text()="Approve"]/..').click()
                else:
                     linha.find_element(By.XPATH, './/span[text()="Reject"]/..').click()
            except:
                 linha.find_element(By.XPATH, './/span[text()="Reject"]/..').click()
        
        if i < (len(botoes_visualizar) - 1):
            driver.find_element(By.XPATH,'//span[text()= "Back to list"]').click()