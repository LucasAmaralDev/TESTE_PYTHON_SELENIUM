#Necessario
#pip install selenium
#pip install selenium-stealth

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from Driver.agents import selecionar_user_agent_aleatorio
from Driver.consumir_agents_txt import escolher_agente
from Driver.setarProxy import configurarProxt
from time import sleep
import platform

sistema_operacional = platform.system()

timeout = 8




class DriverBot:
    def __init__(self,marcadorPasta = '', dataProxy = '', headless = False ):

        # Se dataproxy n for vazio proxy é True caso seja proxy é false
        if dataProxy == '':
            proxy = False
        else:
            proxy = True

        # Configurações do navegador
        self.options = Options()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-user-media-security=true")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)

        # Configurações de Proxy
        if proxy == False:
            pass
        else:
            configurarProxt(dataProxy)
            self.options.add_extension('proxy_auth_plugin.zip')

        # Add extensao do facebook
        self.options.add_extension('autofb.zip')

        # Configuracoes de userAgent
        self.agent = selecionar_user_agent_aleatorio()

        if marcadorPasta != '':
            # Configuracoes do Path do perfil de navegador
            self.options.add_argument(f"user-data-dir=./Perfis/{marcadorPasta}")

        # Invocando o driver
        self.driver = webdriver.Chrome(options=self.options)
        sleep(1)

        # Configurando o stealth
        addst = True
        if addst == True:
            stealth(
                self.driver,
                user_agent = self.agent,
                languages = ["pt-BR", "pt"],
                vendor = "Google Inc.",
                platform = "Win32",
                webgl_vendor = "Intel Inc.",
                renderer= "Intel Iris OpenGL Engine",
                fix_hairline = False,
                run_on_insecure_origins = False,
            )

        # Configurando o tamanho da janela
        self.driver.set_window_size(1366, 768)

        # Configurando o tempo maximo de aguardo da pagina ser carregada
        self.driver.set_page_load_timeout(timeout)

        


         