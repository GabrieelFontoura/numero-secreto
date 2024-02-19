import pyautogui
from time import sleep



# - clicar e digitar meu usuario
pyautogui.click(1010,539, duration=1)
pyautogui.write('gabriel')

# - clicar e digitar a senha
pyautogui.click(1008,568, duration=1)
pyautogui.write('123')
# - clicar em entrar
pyautogui.click(865,598, duration=1)

# # - extrair cada produto e registrar
with open('produtos.txt', 'r') as arquivo:
     for linha in arquivo:
         produto = linha.split(',')[0]
         quantidade = linha.split(',')[1]
         preço = linha.split(',')[2]
         # -clicar em produto e registrar
         pyautogui.click(702,529, duration=1)
         pyautogui.write(produto)
         # - clicar em qtdd e registrar123
         pyautogui.click(697,553, duration=1)
         pyautogui.write(quantidade)
         # - clicar em preço e registrar
         pyautogui.click(706,580, duration=1)
         pyautogui.write(preço)
         # - clicar em registrar
         pyautogui.click(583,739, duration=1)
