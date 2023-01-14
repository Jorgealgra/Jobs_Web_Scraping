# Imports
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pyshorteners


class GetJobs:

    def __init__(self, url):
        self.url = url

    def scraping_jobs(self, n_jobs):
        try:
            # Accedemos al puglin de googlechrome
            s = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=s)
            browser.maximize_window()
            browser.get(self.url)
            # Necesario para esta web
            time.sleep(3)
        except:  # Crear clase de excepciones 

            print("Webdriver Error")
        try:
            # Aceptamos Cookies de google
            xpath = '//*[@id="L2AGLb"]/div'
            element = browser.find_element(By.XPATH, xpath)
            element.click()
            time.sleep(3)

        except:
            print("Cookies Link Error")

        # Accedemos a los puestos de trabajo
        #link_text = '100 o más puestos de trabajo adicionales'
        xpath = '//*[@id="rso"]/div[1]/div/div/div/g-card[2]/div/div/div[2]/a/span[2]'
        element = browser.find_element(By.XPATH, xpath)
        #element = browser.find_element(By.LINK_TEXT, link_text)
        element.click()
        time.sleep(3)

        # Seleccionamos la opción de 'todos los trabajos'
        xpath = '//*[@id="choice_box_root"]/div[2]/div[1]/div[1]/div[7]/span'
        element = browser.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(3)

        # Creamos una lista con los distintos XPath / El primer empleo no se graba
        xPathList = []

        for j in range(1, 11):
            for i in range(2, 11):
                xpath = '// *[ @ id = "VoQFxe"] / div[' + str(j) + '] / div / ul / li[' + str(
                    i) + '] / div / div[2] / div[2] / div / div'
                xPathList.append(xpath)

        # Añadir parámetro de 1 100

        job_number_count = 0
        job_url_list = []
        final = []

        for xpath in xPathList:
            if job_number_count == n_jobs:
                print("Web Scraping has finished")
                browser.close()
                browser.quit()
                return final
            else:
                try:

                    # Obtenemos otra información
                    element = browser.find_element(By.XPATH, xpath)
                    element.click()

                    # Obtenemos Urls
                    url = browser.current_url
                    elements = browser.find_elements(By.XPATH, '//a[@href]')
                    apply_job_url = elements[76].get_attribute('href')

                    # Recortamos las url:
                    shortener = pyshorteners.Shortener()
                    short_url_g = shortener.dagd.short(url)
                    short_apply_job_url = shortener.dagd.short(apply_job_url)

                    # Guardamos la información
                    job_information = element.text + '\n' + short_url_g + '\n' + short_apply_job_url

                    time.sleep(2)
                    job_number_count += 1

                    # Listamos la información
                    job_information_list = job_information.split('\n')
                    if len(job_information_list) == 8:
                        job_information_list.insert(0, '?')


                    time.sleep(2)

                    # get Final list
                    final.append(job_information_list)



                except:
                    print("Link Fail")
                    job_url_list.append("No exists")

        return final
