import pyautogui
import time
import random
import numpy as np
import pygetwindow as gw
import pyperclip

# posicao = pyautogui.position()
# print(posicao)

mensagens = ['Bom dia vó!', 'Bom dia vó!!', 'Bom diaa Dinda!', 'Bom dia Vó!, bjs']
msg_aleatorio = random.choice(mensagens)


# print(msg_aleatorio)

tecla = 'ENTER'
contato = 'DINDA'

tempo = 0.5

x_vscode = 1249
y_vscode = 3

x_whatzap = 200;
y_whatzap = 0

x_barra_pesquisa = 176
y_barra_pesquisa = 185

x_contato = 631
y_contato = 738

x_barra_mensagem = 555
y_barra_mensagem = 736
w_barra_mensagem = 462
h_barra_mensagem = 42

horario = [6]
minutos = [22, 42, 56]
m_aleatorio = random.choice(minutos)

def sai_do_vscode(x, y):
    pyautogui.moveTo(x, y, tempo) 
    pyautogui.click(x, y)


def vai_para_whatzap(x, y):
    pyautogui.moveTo(x, y, tempo)
    pyautogui.click(x,y)

def clica_barra_de_pesquisa(x , y):
    pyautogui.moveTo(x, y, tempo)
    pyautogui.click(x,y)

def procura_contato(t, cntt):
    pyautogui.typewrite(t)
    pyautogui.press(cntt)

def envia_mensagem(x, y, msg):
     pyautogui.moveTo(x, y, tempo)
     pyautogui.click(x,y)
     time.sleep(3)
     pyperclip.copy(msg)
     pyautogui.hotkey('ctrl','v')
     return True

def verifica_envio_mensagem():

    time.sleep(3)
    window = gw.getActiveWindowTitle()
    screenshot_anterior = pyautogui.screenshot()
    while True:
        screenshot_atual = pyautogui.screenshot()

        if verifica_mudanca_img(screenshot_anterior, screenshot_atual):
            print(f"Mensagem enviada as: "+str(horario[0])+':'+str(m_aleatorio))
            return True
        else:
            print('Mensagem não enviada')
    
        time.sleep(2)
        screenshot_anterior = screenshot_atual
  

        
def verifica_mudanca_img(screenshot_anterior, screenshot_atual):
    np_anterior = np.array(screenshot_anterior)
    np_atual = np.array(screenshot_atual)
    dif = np.subtract(np_atual, np_anterior)
    if np.any(dif != 0):
        return True
    else:
        return False




while True: 
    horario_enviar = int(time.strftime("%H", time.localtime()))
    minutos_enviar = int(time.strftime("%M", time.localtime()))

    if horario_enviar in horario and minutos_enviar >= m_aleatorio :
        sai_do_vscode(x_vscode, y_vscode)
        vai_para_whatzap(x_whatzap, y_whatzap)
        clica_barra_de_pesquisa(x_barra_pesquisa, y_barra_pesquisa)
        procura_contato(contato, tecla)
        envia_mensagem(x_contato, y_contato, msg_aleatorio)
        print(verifica_envio_mensagem())  
        break


  