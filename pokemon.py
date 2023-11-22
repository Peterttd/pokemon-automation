import cv2
import numpy as np
import pyautogui
import time
import pygetwindow as gw
import keyboard
#Pokemon - Fire Red Version (U) (V1.1) - VisualBoyAdvance-M 2.1.6

def run():
    pyautogui.keyDown("space")
    time.sleep(0.3)
    pyautogui.keyDown("l")
    pyautogui.keyUp("l")
    time.sleep(0.3)

    pyautogui.keyDown("d")
    pyautogui.keyUp("d")
    time.sleep(0.1)

    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(0.1)

    pyautogui.keyDown("l")
    pyautogui.keyUp("l")
    time.sleep(0.1)

    pyautogui.keyDown("l")
    pyautogui.keyUp("l")
    pyautogui.keyUp("space")
    
window_name = "PokеMМO"

pokemon_template_file = "pigey.png"
appeared_file = "appeared.png"
mat_file = "mat.png"
level_file = "level.png"

threshold = 0.8

window = gw.getWindowsWithTitle(window_name)

if len(window) == 1:

    tempo_total_execucao = 20
    encontrado = False
    tempo_inicial = time.time()
    pkn_certo = False


    while (time.time() - tempo_inicial) < tempo_total_execucao:
        if keyboard.is_pressed('q'):
            print("Tecla 'q' pressionada. O código será encerrado.")
            break

        window[0].activate()
        window_rect = window[0]._rect

        screenshot = pyautogui.screenshot(region=(window_rect.left, window_rect.top, window_rect.width, window_rect.height))

        screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        pokemon_template_gray = cv2.imread(pokemon_template_file, cv2.IMREAD_GRAYSCALE)
        appeared_gray = cv2.imread(appeared_file, cv2.IMREAD_GRAYSCALE)
        mat_gray = cv2.imread(mat_file, cv2.IMREAD_GRAYSCALE)
        level_gray = cv2.imread(level_file, cv2.IMREAD_GRAYSCALE)

        output_file = "screenshot.png"
        cv2.imwrite(output_file, screenshot_gray)

        result = cv2.matchTemplate(screenshot_gray, pokemon_template_gray, cv2.TM_CCOEFF_NORMED)
        resultpkn = cv2.matchTemplate(screenshot_gray, appeared_gray, cv2.TM_CCOEFF_NORMED)
        resultmat = cv2.matchTemplate(screenshot_gray, mat_gray, cv2.TM_CCOEFF_NORMED)
        resultlevel = cv2.matchTemplate(screenshot_gray, level_gray, cv2.TM_CCOEFF_NORMED)

        _, max_val, _, _ = cv2.minMaxLoc(result)
        _, max_valpkn, _, _ = cv2.minMaxLoc(resultpkn)
        _, max_valmat, _, _ = cv2.minMaxLoc(resultmat)
        _, max_vallevel, _, _ = cv2.minMaxLoc(resultlevel)
   
        if max_val > threshold:
            print("Pokémon encontrado.")
            pkn_certo = True
            run()
        else:
            print("Pokémon não encontrado.")
            pkn_certo = False

        if max_valpkn > threshold:
            encontrado = True
            print("qlqr um")
        else:
            encontrado = False
            print("funcionando")

        if max_vallevel > threshold:
            print("upou")
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            time.sleep(0.1)
        else:
            print("n upou")

        while encontrado == True and pkn_certo == False:
            screenshot = pyautogui.screenshot(region=(window_rect.left, window_rect.top, window_rect.width, window_rect.height))
            screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

            resultmat = cv2.matchTemplate(screenshot_gray, mat_gray, cv2.TM_CCOEFF_NORMED)
            cv2.imwrite(output_file, screenshot_gray)

            _, max_valmat, _, _ = cv2.minMaxLoc(resultmat)

            if max_valmat > threshold:
                encontrado = False
                print("mat")
            else:
                encontrado = True
                print("nmat")

            pyautogui.keyDown("space")
            pyautogui.keyDown("l")
            pyautogui.keyUp("l")
            pyautogui.keyUp("space")

        if encontrado == False:
            pyautogui.keyDown("a")
            time.sleep(0.6)
            pyautogui.keyUp("a")
            pyautogui.keyDown("d")
            time.sleep(0.4)
            pyautogui.keyUp("d")

else:
    print(f"Janela '{window_name}' não encontrada.")