from selenium import webdriver

# Inicio
def before_all(context): # Antes de tudo

    #Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/jaiss_f3yllmx/PycharmProjects/fts132_blazedemo/drivers/chrome/96/chromedriver.exe')


    #Maximizar a janela do navegador
    context.driver.maximize_window()

#Fim
def after_all(context): #depois de tudo

    #Desligar / Destruir o objeto do selenium
    context.driver.quit()

    print('Passo 7 - Depois de Tudo')