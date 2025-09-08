import pyautogui
import time
import pytesseract
import threading

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def seconddesk():
    time.sleep(1)
    pyautogui.hotkey('win', 'ctrl', 'left')
    time.sleep(1)  # 1 saniye bekle

def maindesk():
    pyautogui.hotkey('win', 'ctrl', 'right')
    time.sleep(1)

# Alt+Tab işlemini farm sayısına göre arttır
def alt_tab(times):
    pyautogui.keyDown('alt')  # Alt tuşunu basılı tut
    for _ in range(times):     # Belirtilen kadar Tab tuşuna bas
        pyautogui.press('tab')  
        time.sleep(0.5)         # Kısa bir bekleme süresi
    pyautogui.keyUp('alt')     # Alt tuşunu bırak

def click_key(key_coordinates):
    time.sleep(0.5)
    pyautogui.moveTo(*key_coordinates)
    pyautogui.click(button='left')

def run_code():
    left, top, width, height = 979, 406, 55, 20
    region = (left, top, width, height)

    try:
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot).strip()
        
        if text:
            print(f'Okunan metin: {text}')
            handle_input(text)
        else:
            print('Hiçbir metin okunamadı.')

    except Exception as e:
        print(f'Hata oluştu: {e}')

def handle_input(text):
    digits = [int(char) for char in text if char.isdigit()]
    key_coordinates = {
        0: (955, 633),
        1: (910, 501),
        2: (956, 501),
        3: (1001, 501),
        4: (908, 542),
        5: (954, 546),
        6: (1001, 545),
        7: (914, 590),
        8: (954, 590),
        9: (1003, 591),
    }

    for digit in digits:
        if digit in key_coordinates:
            click_key(key_coordinates[digit])
            time.sleep(0.5)
        else:
            print(f"Geçersiz sayı: {digit}.")

def farmısat():
    for coords in [(814, 375), (886, 375)]:
        pyautogui.moveTo(*coords)
        time.sleep(1)
        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.click(button='right')
        time.sleep(1)
        pyautogui.keyUp('shift')

def confirm():
    time.sleep(0.5)
    pyautogui.moveTo(999, 634)
    pyautogui.click(button='left')

def gorevynt():
    image_path = "resimler/gorev.png"
    location = pyautogui.locateOnScreen(image_path, confidence=0.99)
    pyautogui.moveTo(location)
    pyautogui.leftClick()

def startprocess(farm_count):
    for i in range(1, farm_count + 1):  # Farm sayısına göre döngü
        print(f"{i}. farm işlemi başlıyor...")

        pyautogui.moveTo(814, 375)
        pyautogui.click(button='left')
        time.sleep(1)
        
        run_code()  # Farm işlemi
        
        time.sleep(1)
        confirm()   # Confirm işlemi
        time.sleep(1)
        farmısat()  # Sat işlemi
        
        alt_tab(i - 1)  # Farm numarasına göre Alt+Tab sayısını arttır
        
        time.sleep(1)  # Her farm işlemi arasında bekleme süresi

# Başlatmadan önce kullanıcıdan kaç farm olduğunu seçmesini iste
farm_count = 28

time.sleep(10)

# Döngüye başla
def repeat_task():
    while True:
        startprocess(farm_count)  # Farm işlemleri başlat
        
        print("İşlem tamamlandı. 7 dakika sonra tekrar başlatılacak...")
        time.sleep(420)  # 7 dakika bekle (420 saniye)
        startprocess(farm_count)  # Farm işlemleri başlat

        print("İşlem tamamlandı. 15 dakika sonra tekrar başlatılacak...")
        time.sleep(900)  # 15 dakika bekle (900 saniye)
        startprocess(farm_count)  # Farm işlemleri başlat
        print("İşlem tamamlandı. 10 dakika sonra tekrar başlatılacak...")
        time.sleep(600)  # 10 dakika bekle (600 saniye)

# Ayrı bir iş parçacığında işlemi başlat
def start_repeating_task():
    threading.Thread(target=repeat_task).start()

# Başlatma fonksiyonunu çağır
seconddesk()
time.sleep(1)
seconddesk()
time.sleep(1)
maindesk()
time.sleep(1)
start_repeating_task()
