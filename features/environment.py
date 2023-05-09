from selenium import webdriver

# Inicio
def before_all(context): # Antes de tudo
    #Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/jaiss_f3yllmx/PycharmProjects/fts132_blazedemo/drivers/chrome/96/chromedriver.exe')
    context.driver.maximize_window()

    print('Passo A - antes de tudo')
#Fim
def after_all(context): #depois de tudo

    #Desligar / Destruir o objeto do selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')
#BLOCO EXECUTADO AI FINAL DE CADA step
def after_step(context, step):
    print()

