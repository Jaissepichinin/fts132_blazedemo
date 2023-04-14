import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#precisa sempre importar a classe environment (onde estao o before and after)
from features import environment

#método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            #pode ser incluida outras acoes
        )

@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')
    time.sleep(15)  #espera bruta - sempre remover - alfinete


@when(u'seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):

    #mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    #cria um objeto para permitir selecionar as opcoes do combo
    objeto_origem = Select(combo_origem)

    #Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):

    #mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'toPort')

    #cria um objeto para permitir selecionar as opcoes do combo
    objeto_origem = Select(combo_origem)

    #Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(destino)
    # objeto_origem.select_by_value(origem)


    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico em "Find Flights"')
def step_impl(context):
    print('Passo 4- When clico em Find Flights')


@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    print('Passo 5 - direcionou para a pagina de selecao de voos')


@when(u'seleciono o primeiro voo')
def step_impl(context):
    print('Passo 6 - selecionou o primeiro voo')


@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    print('Passo 7 - direcionou para a pagina de pagamento')


@when(u'preencho os dados de pagamento')
def step_impl(context):
    print('Passo 8 - Preencheu os dados para pagamento')


@when(u'clico no botao Purchase Flight')
def step_impl(context):
    print('Passo 9 -clico no botao Purchase Flight')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print('Passo 10 - Then sou direcionado para a pagina de confirmacao')


@when(u'seleciono de "São Paolo" para "Rome"')
def step_impl(context):
    print('Passo 2c- Selecionou a cidade de origem e destino')
