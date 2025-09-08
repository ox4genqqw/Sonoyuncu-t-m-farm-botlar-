import time
import pygetwindow as gw
import pyautogui

def find_sonoyuncu_windows():
    # "SonOyuncu" başlıklı tüm pencereleri listele
    sonoyuncu_windows = [win for win in gw.getWindowsWithTitle("CraftRise")]
    return sonoyuncu_windows

def seconddesk():
    time.sleep(1)
    pyautogui.hotkey('win', 'ctrl', 'left')
    time.sleep(1)  # 1 saniye bekle

def perform_actions_on_window(window):
    # Pencereyi ön plana getir
    window.minimize()
    window.restore()
    window.activate()

    # 1. Esc tuşuna bas
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('5')
    pyautogui.rightClick()
    time.sleep(5)
    # 2. Sağ tıklama yap
    pyautogui.press('1')
    pyautogui.rightClick()
    time.sleep(3)

    # 3. Mouse'u belirtilen koordinatlara getir
    pyautogui.moveTo(820, 369)
    time.sleep(1)

    # 4. Sol tıklama yap
    pyautogui.click()
    time.sleep(10)

    # 5. Sağ tıklama yap
    pyautogui.rightClick()
    time.sleep(3)

def bring_windows_to_front_and_perform_actions():
    # SonOyuncuClient pencerelerini bul
    sonoyuncu_windows = find_sonoyuncu_windows()

    # Eğer pencereler bulunduysa, her birine sırasıyla işlemleri uygula
    if sonoyuncu_windows:
        for window in sonoyuncu_windows:
            perform_actions_on_window(window)
    else:
        print("SonOyuncuClient penceresi bulunamadı.")

if __name__ == "__main__":
    seconddesk()
    time.sleep(50)
    bring_windows_to_front_and_perform_actions()
    seconddesk()
