#Passo a passo do projeto 

#1. Abrir o sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.7 #pausa entre todos os comandos

#Abrir o navegador
pyautogui.press("win")  

pyautogui.write("opera")
pyautogui.press("enter")
#Entrar no site do sistema 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #pausa para somente uma parte da automaçao

#2. Fazer Login
pyautogui.click(x=799, y=494)
pyautogui.write("juliatestando@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#3. Abrir/importar a base de dados de prodututos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#4. Cadastrar um produto


for linha in tabela.index: 

    codigo = str(tabela.loc[linha,"codigo"])

    #clicar no campo do codigo do produto
    pyautogui.click(x=935, y=334)

    #preencher o codigo
    pyautogui.write(codigo)

    #passar pro proximo campo
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))

    #passar pro proximo campo
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))

    #passar pro proximo campo
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    #passar pro proximo campo
    pyautogui.press("tab")

    #preco
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    #passar pro proximo campo
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    #passar pro proximo campo
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
     pyautogui.write(obs)

    #passar pro proximo campo
    pyautogui.press("tab")
    #apertar o botao
    pyautogui.press("enter")
    pyautogui.scroll(5000)


#5. Repetir tudo até acabar a lista de produtos 