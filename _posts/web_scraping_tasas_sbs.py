# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 07:40:12 2021

@author: JOSE
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

website='https://www.sbs.gob.pe/app/pp/CurvaSoberana/Curvas_Consulta_Historica.asp'
path='C:/Users/JOSE/Downloads/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)


fechas_cc=['30/11/2005', '15/08/2006']
fechas_cc[1]


    fechas_cc=['15/08/2006','30/11/2005']

def extraer_tasas():
    driver = webdriver.Chrome(path)
    for i in range(0,2):
        driver = webdriver.Chrome(path)
        driver.get(website)

        dropdown= Select(driver.find_element_by_id('as_tip_curva'))
        dropdown.select_by_visible_text('Curva Soberana Soles')

        dropdown= Select(driver.find_element_by_id('as_fec_cons'))
        dropdown.select_by_visible_text(fechas_cc[i])

        boton_consultar=driver.find_element_by_xpath("//*[@id='Consultar']")
        boton_consultar.click()
        
        
        time.sleep(10)
        
        driver.close()
    

extraer_tasas()
