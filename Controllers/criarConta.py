from Driver.invokeChrome import DriverBot
from time import sleep
from selenium.webdriver.common.by import By
from Controllers.comandosValidados import *




def criar_conta(marcadorPasta):
    bot = DriverBot(dataProxy="", marcadorPasta=marcadorPasta)

    driver = bot.driver
    # abrir uma nova aba
    driver.execute_script("window.open('');")

    # Selecionar a aba antiga
    driver.switch_to.window(driver.window_handles[0])

    driver.get("https://codeanywhere.com/signup")
    sleep(1)
    # Inserir nome
    input_nome = driver.find_element(By.NAME, "firstname")
    input_nome.send_keys("Juliano")
    # Inserir sobrenome
    input_sobrenome = driver.find_element(By.NAME, "lastname")
    input_sobrenome.send_keys("Santos")

    # Trocar para a segunda aba
    driver.switch_to.window(driver.window_handles[1])

    # Acessar site de email temporario
    driver.get("https://tmail.social/")
    sleep(3)

    # Capturar email
    email = driver.find_element(By.ID, "email_id").text

    # Trocar para a primeira aba
    driver.switch_to.window(driver.window_handles[0])

    # Inserir email
    input_email = driver.find_element(By.NAME, "email")
    input_email.send_keys(email)
    # Inserir senha
    input_senha = driver.find_element(By.NAME, "password")
    input_senha.send_keys("@Luc97ari")
    input_senha.send_keys("\n")
    sleep(3)

    # Trocar para a segunda aba
    driver.switch_to.window(driver.window_handles[1])

    # tentar ate conseguir encontrar novo email
    driver.refresh()
    sleep(4)

    # Procurar div com o texto "Welcome to Codeanywhere: Verify your account" e a class "w-1/2 md:w-8/12"
    procurar_email = encontrar_tagname_texto_class(
        driver,
        "div",
        "Welcome to Codeanywhere: Verify your account",
        "w-1/2 md:w-8/12",
    )
    if procurar_email == False:
        return False
    
    # Clicar na div que tem esse xpath "/html/body/div[1]/main/div/div[1]/div/div/div[1]/div[2]/div"
    abrir_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div/div[1]/div[2]/div').click()
    sleep(2)

    # Entrar no iframe 
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    # Coletar o link de confirmacao de email
    link_confirmacao = driver.find_element(By.XPATH, '/html/body').text
    link_confirmacao = link_confirmacao.split('https://')[1]
    link_confirmacao = link_confirmacao.split('\n')[0]
    link_confirmacao = 'https://' + link_confirmacao
    driver.get(link_confirmacao)
    sleep(3)

    # Fechar segunda aba
    driver.close()

    # Selecionar a primeira aba
    driver.switch_to.window(driver.window_handles[0])


    # entrar no dashboard
    driver.get("https://dashboard.codeanywhere.com/")
    sleep(1)

    # Clicar na div com o texto "New Container" e que tambem possua a class "create__option tab-focus"
    clicar_new_container = clicar_tagname_texto_class(driver, "div", "New Container", "create__option tab-focus")
    if clicar_new_container == False:
        return False
    sleep(2)


    # Clicar na div com o texto ".NET Core" e que tambem possua a class "template__card "
    clicar_dotnet_core = clicar_tagname_texto_class(driver, "div", ".NET Core", "template__card ")
    if clicar_dotnet_core == False:
        return False
    sleep(2)


    # Clicar no button com o texto "Create"
    clicar_create = clicar_tagname_texto(driver, "button", "Create")
    if clicar_create == False:
        return False
    sleep(5)

    # Tentar ate conseguir fechar a segunda aba do navegador
    while True:
        try:
            # Fechar a segunda aba
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            break
        except:
            pass
        sleep(1)

    # Voltar para a primeira aba
    driver.switch_to.window(driver.window_handles[0])

    # Tentar ate conseguir acessar a pagina "https://dashboard.codeanywhere.com/containers" e clicar em uma div com o texto "Open IDE" que tenha o atributo class sendo "button button--type-success button--type-block card-button tab-focus"
    while True:
        try:
            driver.get("https://dashboard.codeanywhere.com/containers")
            sleep(3)

            # clicar na "div" com o texto "Open IDE" e classe "button button--type-success button--type-block card-button tab-focus"
            clicarOpenIDE = clicar_tagname_texto_class(
                driver,
                "div",
                "Open IDE",
                "button button--type-success button--type-block card-button tab-focus",
            )
            if clicarOpenIDE == True:
                break

            
        except:
            pass

    # Nesse momento existem 2 abas. fechar apenas a primeira aba
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    sleep(0.4)

    # Selecionar a nova primeira aba
    driver.switch_to.window(driver.window_handles[0])

    while True:
        try:

            # Clicar na div com a classe "project-row" que contenha o texto "Create a new Project\nCreate a Project and start working from scratch."
            click_div_create = clicar_tagname_texto_class(
                driver,
                "div",
                "Create a new Project\nCreate a Project and start working from scratch.",
                "project-row",
            )
            if click_div_create == True:
                break

        except:
            pass
        
        try:
            url = driver.current_url
            driver.get(url)
        except:
            pass


    sleep(5)

    # DAR O NOME "MAIN" PARA O PROJETO
    # Inserir nome do projeto no input com id  "ca-projects--dialog-input-new"
    input_nome_projeto = driver.find_element(By.ID, "ca-projects--dialog-input-new")
    input_nome_projeto.send_keys("MAIN")
    input_nome_projeto.send_keys("\n")
    sleep(2)

    # Clicar no button com a class "theia-button secondary" e o texto "No"
    click_button_no = clicar_tagname_texto_class(
        driver, "button", "No", "theia-button secondary"
    )
    if click_button_no == False:
        return False

    # Clicar no button com a class "theia-button secondary" e o texto "Close"
    click_button_close = clicar_tagname_texto_class(
        driver, "button", "Close", "theia-button secondary"
    )
    sleep(4)

    #inserir "Texto" na "Textarea" com a class "xterm-helper-textarea" 
    inserir_texto = sendkeys_tagname_texto_class(
        driver, 
        "textarea", 
        "screen\n", 
        "xterm-helper-textarea")
    sleep(2)

    inserir_texto = sendkeys_tagname_texto_class(
        driver, 
        "textarea", 
        "\n", 
        "xterm-helper-textarea")
    sleep(1)
    

    while True:
        try:
            #trocar para a primeira aba
            driver.switch_to.window(driver.window_handles[0])

            variavel = driver.current_url

            sleep(580)
        
        except:
            break