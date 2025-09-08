import pyautogui
import time
import os



def leftdereges():
    time.sleep(2)  # 2 saniye bekleme süresi
    # Fareyi sağa doğru küçük adımlarla hareket ettir (x ekseninde 240 piksel)
    pyautogui.moveRel(240, 0, duration=0.2)  # x ekseninde 240 piksel sağa hareket ettir
coordinates = {
    "sancak": (816, 513),
    "yakamoz": (857, 519),
    "avrasya": (884, 517),
    "pruva": (919, 519),
    "velena": (960, 517),
    "flador": (994, 517),
    "astra": (1071, 517)
}

def renderingoa():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(13.8)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(13.8)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(13.8)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(13.8)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()


def ananızıskikim():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.4)
    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(1.1)
    # 'W' tuşunu bırak
    pyautogui.keyUp('w') 
    pyautogui.keyDown('d')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(1.1)
    # 'W' tuşunu bırak
    pyautogui.keyUp('d') 
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.1)
    # 'W' tuşunu bırak
    pyautogui.keyUp('w') 
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(1.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    pyautogui.keyDown('d')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(5.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('d')
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    
def renderinger():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.2)
    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.1)
    # 'W' tuşunu bırak
    pyautogui.keyUp('w') 
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def renderingo():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.5)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.35)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.4)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def renderforilkermira():
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(20.1)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(20.1)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(19.9)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(19.7)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def renderforout():
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(19.7)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(19.7)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(19.7)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(19.7)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()


# Örnek olarak her adın koordinatlarını yazdıralım
for name, (x, y) in coordinates.items():
    print(f"{name}: x={x}, y={y}")

def yemekye():
    # Sağ tıklama yap
    pyautogui.mouseDown(button='right')
    
    # 3 saniye bekle (sağ tıklamayı basılı tut)
    time.sleep(3)
    
    # Sağ tıklamayı bırak
    pyautogui.mouseUp(button='right')

def hata():
    time.sleep(3)
    pyautogui.moveTo(963, 575)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(699, 125)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1001, 655)
    time.sleep(1)
    pyautogui.click()
    time.sleep(15)
    pyautogui.moveTo(955, 312)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(2)
    pyautogui.moveTo(599, 343)
    pyautogui.click()
    time.sleep(10)
    pyautogui.press('t')
    time.sleep(0.5)
    pyautogui.write('/spawn')
    pyautogui.press('enter')
    time.sleep(12)
    pyautogui.press('1')

def renderinge():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def velenasymox8113():
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(13.9)
  
    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(13.9)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()


def spawnproccess():
# Bir süre bekleyin, ardından T tuşuna basılacak
    time.sleep(2)  # 2 saniye bekleme süresi, zamanlamak için kullanılır

# 'T' tuşuna basarak sohbet kutusunu aç
    pyautogui.press('t')

# Biraz bekleyin, çünkü bazen tuşlar arasında kısa bir zaman farkı gerekir
    time.sleep(0.5)

# '/spawn' komutunu yaz
    pyautogui.write('/spawn')

# Biraz bekleyin, komut yazılsın
    time.sleep(0.5)

# 'Enter' tuşuna basarak komutu çalıştır
    pyautogui.press('enter')


# 2 saniye bekleyin, ardından fare hareketini başlatın
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(4.75)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    time.sleep(2)
    pyautogui.keyDown('shift')
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')
    time.sleep(0.5)
    pyautogui.click(button='right')
    time.sleep(0.7)

def renringoa():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(13.8)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def leftdereges():
    time.sleep(2)  # 2 saniye bekleme süresi
    # Fareyi sağa doğru küçük adımlarla hareket ettir (x ekseninde 240 piksel)
    pyautogui.moveRel(240, 0, duration=0.2)  # x ekseninde 240 piksel sağa hareket ettir
def rendering():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()

def pruvaqweqwerender():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(13.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(13.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(13.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(13.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    
def renderingoza():
        # Enter tuşuna bas
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.1)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
 
def velenasymox81():
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 1
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 2
    time.sleep(14.2)
  
    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et 3
    time.sleep(13.9)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    time.sleep(1)
    pyautogui.keyDown('w')

    # 5 saniye boyunca basılı tutmaya devam et
    time.sleep(14.2)

    # 'W' tuşunu bırak
    pyautogui.keyUp('w')
    leftdereges()
    
def sancakagit():
    spawnproccess()
    pyautogui.moveTo(coordinates["sancak"][0], coordinates["sancak"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm2')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    renderforout()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm3')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()


def yakamozgit():
    spawnproccess()
    pyautogui.moveTo(coordinates["yakamoz"][0], coordinates["yakamoz"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    renderforout()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm2')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm3')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()


def avrasyagit():
    spawnproccess()
    pyautogui.moveTo(coordinates["avrasya"][0], coordinates["avrasya"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm2')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm3')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()

def pruvagit():
    spawnproccess()
    pyautogui.moveTo(coordinates["pruva"][0], coordinates["pruva"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()

def velenagit():
    spawnproccess()
    pyautogui.moveTo(coordinates["velena"][0], coordinates["velena"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)   
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm2')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    renringoa()
    time.sleep(1)
    time.sleep(1)   
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm3')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    renderforilkermira()
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()

def fladorgit():
    spawnproccess()
    pyautogui.moveTo(coordinates["flador"][0], coordinates["flador"][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()

def astragit():
    spawnproccess()
    pyautogui.moveTo(coordinates["astra"][0], coordinates["astra"][1])
    time.sleep(1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/home farm')
    pyautogui.press('enter')
    yemekye()
    time.sleep(12)
    rendering()
    time.sleep(1)
    time.sleep(1)
    pyautogui.press('t')
    pyautogui.write('/spawn')
    yemekye()
    pyautogui.press('enter')
    time.sleep(12)
    hata()
    
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(2)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(2)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(2)
pyautogui.hotkey('ctrl', 'win', 'right')
time.sleep(2)
pyautogui.hotkey('ctrl', 'win', 'right')
time.sleep(2)
pyautogui.press('esc')
avrasyagit()
pruvagit()
fladorgit()
astragit()
time.sleep(2)
time.sleep(1)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(1)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(1)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(1)
pyautogui.hotkey('ctrl', 'win', 'left')
time.sleep(1) #14.04.2025 son güncelleme tarihi