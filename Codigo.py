# Passo a Passo do projeto
# Passo 1: entrar no sistema da empresa

import pyautogui
import time
import pandas as pd
# pyautogui.write -> escrever texto
# pyautogui.press -> apertar 1 teclaMOLO000192  Logitech    Mouse   2   19.95   5.0
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=738, y=361)
# escrever o seu email
pyautogui.write("testeprojeto@outlook.com.br")
pyautogui.press("tab") # passando pro proximo campo
pyautogui.write("suasenha") 
pyautogui.click(x=928, y=521) # clique no botao de login
time.sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # Clicar no campo de código
    pyautogui.click(x=763, y=236)
    # pegar da tabela o valor do campo que quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    # Passar para o proximo campo
    pyautogui.press("tab")
    # Preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # Cadastrar o produto (Botao enviar)
    # Dar scroll para cima 
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo até o fim do cadrasto