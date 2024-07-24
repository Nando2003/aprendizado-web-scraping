from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from datetime import date
import os
import pyautogui
from dotenv import load_dotenv

class Emissao_DARJ:
    def __init__(self, cnpj : int):
        self.url = "https://www1.fazenda.rj.gov.br/portaldepagamentos/"
        self.cnpj = cnpj
        self.driver = None
        self.await_time = 10
        self._process()
        
    def _process(self) -> None:
        self.open_browser()
        self.dados_do_pagamento()
        self.itens_de_pagamento()
        self.screenshot()
        self.download_file()
        sleep(5)
        
    def open_browser(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.get(self.url)
        sleep(3)
    
    def dados_do_pagamento(self) -> None:
        select_element = WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[1]/div[1]/select"
            ))
        )
        select = Select(select_element)
        select.select_by_value("1")
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[1]/div[1]/select/option[3]"
            ))
        ).click()
    
    def itens_de_pagamento(self) -> None:
        select_element = WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[1]/select"
            ))
        )
        select = Select(select_element)
        select.select_by_value("3")
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[3]/input[1]"
            ))
        ).send_keys(self.cnpj)
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[3]/input[2]"
            ))
        ).click()
        
        sleep(3)
        today_date = str(date.today())
        today_day = today_date[8:10]
        today_mouth = today_date[5:7]
        today_year = today_date[0:4]
        mouth_year = today_mouth + "/" + today_year
        day_mouth_year = today_day + "/" + mouth_year
                
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[16]/input"
            ))
        ).send_keys(mouth_year)
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[19]/input[2]"
            ))
        ).click()
        sleep(2)
        
        data_vencimento = WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[19]/input[1]"
            ))
        )
        data_vencimento.clear()
        sleep(2)
        
        data_vencimento.send_keys(day_mouth_year)
        sleep(3)
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[1]/div[23]/textarea"
            ))
        ).send_keys("Teste de emissão")
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[2]/div[1]/div[1]/input[1]"
            ))
        ).send_keys("0,01")
        
        sleep(2)
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[2]/div[1]/div[1]/input[2]"
            ))
        ).click()
        
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[2]/div[2]/div/input[1]"
            ))
        ).send_keys("0,01")
        
        sleep(2)
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[2]/fieldset[2]/div[2]/div/input[2]"
            ))
        ).click()
        
        sleep(2)
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/form/fieldset[2]/div[3]/input[1]"
            ))
        ).click()
        
    def screenshot(self) -> None:
        sleep(6)
        
        screenshot_path = "./screenshots"
        
        if os.path.isdir(screenshot_path) is False:
            os.makedirs(screenshot_path)
    
        self.driver.get_screenshot_as_file(f"./screenshots/{self.cnpj}.png")
    
    def download_file(self) -> None:
        download_path = "./download_file"
        
        if os.path.isdir(download_path) is False:
            os.makedirs(download_path)
        
        abs_path = os.path.abspath(download_path)
        
        sleep(3)
        WebDriverWait(self.driver, self.await_time).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/div/div/div/fieldset/form/div[5]/input"
            ))
        ).click()
        
        sleep(2)
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width/2, screen_height/2)
        
        sleep(2)
        download_coord = pyautogui.locateCenterOnScreen(
            image="refer_images/image.png",
            minSearchTime=10
        )
        pyautogui.moveTo(download_coord)
        pyautogui.click()
        abs_path = abs_path + "\\"

        sleep(2)
        pyautogui.press('left')
        pyautogui.write(abs_path)
        pyautogui.press('enter')
        
    def __del__(self) -> None:
        self.driver.close()
        
        
if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    
    CNPJS_STRING = os.environ.get("CNPJS")
    
    if CNPJS_STRING:
        cnpjs = CNPJS_STRING.split(',')
    else:
        cnpjs = []
    
    for cnpj in cnpjs:
        Emissao_DARJ(cnpj=cnpj)
        
    print("PROCESSO FINALIZADO")