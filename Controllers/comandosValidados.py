from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def clicar_tagname_texto(driver, tagname, texto):
    contador = 0
    while contador < 10:
        try:
            elemento_target = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elemento_target:
                if elemento.text == texto:
                    elemento.click()
                    return True
            break
        except:
            pass
        sleep(1)
        contador += 1
    return False


def encontrar_tagname_texto(driver, tagname, texto):
    contador = 0
    while contador < 10:
        try:
            elemento_target = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elemento_target:
                if elemento.text == texto:
                    return True
            break
        except:
            pass
        sleep(1)
        contador += 1
    return False


def clicar_tagname_texto_class(driver, tagname, texto, classe):
    contador = 0
    while contador < 10:
        try:
            elemento_target = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elemento_target:
                if elemento.text == texto and elemento.get_attribute("class") == classe:
                    elemento.click()
                    return True
        except:
            pass
        sleep(1)
        contador += 1
    return False

def sendkeys_tagname_texto_class(driver, tagname, texto, classe):
    contador = 0
    while contador < 10:
        try:
            elemento_target = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elemento_target:
                try:
                    if elemento.get_attribute("class") == classe:
                        elemento.send_keys(texto)
                        return True
                except:pass
        except:
            pass
        sleep(1)
        contador += 1
    return False

def encontrar_tagname_texto_class(driver, tagname, texto, classe):
    contador = 0
    while contador < 10:
        try:
            elemento_target = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elemento_target:
                if elemento.text == texto and elemento.get_attribute("class") == classe:
                    return True
        except:
            pass
        sleep(1)
        contador += 1
    return False

        