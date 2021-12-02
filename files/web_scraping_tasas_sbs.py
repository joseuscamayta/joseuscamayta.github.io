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
    for i in range(0,44):
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

fechas_cc=['07/06/2011'
,'01/09/2011'
,'19/12/2011'
,'06/03/2012'
,'24/05/2012'
,'09/08/2012'
, '06/11/2012',
'10/01/2013',
'16/04/2013',
'19/07/2013',
'12/11/2013',
'23/01/2014',
'02/04/2014',
'09/07/2014',
'15/09/2014',
'05/11/2014',
'08/01/2015',
'09/04/2015',
'02/07/2015',
'02/09/2015',
'04/12/2015',
'16/03/2016',
'22/06/2016',
'29/09/2016',
'29/11/2016',
'06/02/2017',
'11/05/2017',
'26/09/2017',
'13/12/2017',
'20/03/2018',
'06/06/2018',
'05/09/2018',
'13/11/2018',
'07/01/2019',
'01/04/2019',
'13/06/2019',
'01/10/2019',
'06/01/2020',
'03/04/2020',
'14/07/2020',
'01/10/2020',
'12/01/2021',
'15/04/2021',
'09/07/2021']

fechas_cc[2]

range(0,44)