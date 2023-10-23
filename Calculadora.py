import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(1)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(9, 1063)
tempoEspera.sleep(1)

#Clicando na posição
posicaoMouse.click(9, 1063)

#Escrever na barra de pesquisa
posicaoMouse.typewrite('calculadora')
tempoEspera.sleep(1)

#Entrando na calculadora
posicaoMouse.click(168, 471)
tempoEspera.sleep(2)


#Tentativa de calculo 9-6=
#posicaoMouse.click(294, 373)
#tempoEspera.sleep(2)
#posicaoMouse.click(329, 440)
#tempoEspera.sleep(2)
#posicaoMouse.click(295, 404)
#tempoEspera.sleep(2)
#posicaoMouse.click(365, 470)


#print(posicaoMouse.position())