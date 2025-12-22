import sys
from PyDictionary import PyDictionary
import messagebox
import tkinter
import pyttsx3

dictionary = PyDictionary()
mGui = tkinter.Tk()

ment = tkinter.StringVar()

mGui.geometry('509x300+0+0')

mGui.title("Dictionary")
# ==============================================================Dictionary=============================================================================================
mFrame = tkinter.Frame(mGui, width=709, height=600, bg="powder blue", relief="ridge", bd=10)
mFrame.pack()


mLabel = tkinter.Label(mGui, font=("arial", 25, "bold"),
               text="DICTIONARY", fg="steel blue", bd=10, anchor="w")
mLabel.place(x=130, y=0)


def TextToSpeech():
    mtext = ment.get()

    engine = pyttsx3.init()
    engine.say(mtext)
    engine.runAndWait()


def Meaning():
    mtext = ment.get()
    mOutput.delete(0.0, tkinter.END)
    Word = (dictionary.meaning(mtext))
    mOutput.insert(tkinter.END, Word)


def Synonym():
    mtext = ment.get()
    mOutput.delete(0.0, tkinter.END)
    Word = (dictionary.synonym(mtext))
    mOutput.insert(tkinter.END, Word)
    mlabel2=tkinter.Label(mGui,text=Word).pack()


def Antonym():
    mtext = ment.get()
    mOutput.delete(0.0, tkinter.END)
    Word = (dictionary.antonym(mtext))
    mOutput.insert(tkinter.END, Word)
    mlabel2=tkinter.Label(mGui,text=Word).pack()


def Translate(L="hi"):
    L = var.get()
    mtext = ment.get()
    Language = L
    mOutput.delete(0.0, tkinter.END)
    Word = (dictionary.translate(mtext, Language))
    mOutput.insert(tkinter.END, Word)
    mlabel2=tkinter.Label(mGui,text=Word).pack()
# =====================================================================================================================================================================


def mHistory():
    f = open(creds, 'a')
    f.write(mEntry.get())
    f.write('\t')
    f.write(mbutton1)
    f.write('\n')
    f.close()
    d = open('tempfile.txt')
    str = d.read()
    messagebox.showinfo(title="History", message=str)


def mExit():
    mQuit = messagebox.askokcancel(title="Exit", message="Are You Sure?")
    if mQuit > 0:
        mGui.destroy()
        return


creds = 'tempfile.txt'
a = open(creds, 'w')
a.close()


menubar = tkinter.Menu(mGui)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Search History", command=mHistory)
filemenu.add_command(label="Exit", command=mExit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menubar, tearoff=1)
#editmenu.add_command(label="Translate Into",command=ChangeLanguage)
# menubar.add_cascade(label="Edit",menu=editmenu)

mGui.config(menu=menubar)

mEntry = tkinter.Entry(mFrame, font=("arial", 20, "bold"), bg="powder blue",
               bd=10, textvariable=ment, insertwidth=2, justify="center")
mEntry.place(x=85, y=60)

mbutton0 = tkinter.Button(mGui, font=("arial", 12, "bold"), text="|<))", bd=10,
                  justify="center", command=TextToSpeech, bg="powder blue").place(x=410, y=60)


mbutton1 = tkinter.Button(mGui, font=("arial", 16, "bold"), text="Meaning", bd=10,
                  justify="center", command=Meaning, bg="powder blue").place(x=0, y=120)

mbutton2 = tkinter.Button(mGui, font=("arial", 16, "bold"), text="Synonym", bd=10,
                  justify="center", command=Synonym, bg="powder blue").place(x=121, y=120)

mbutton3 = tkinter.Button(mGui, font=("arial", 16, "bold"), text="Antonym", bd=10,
                  justify="center", command=Antonym, bg="powder blue").place(x=251, y=120)

data = {'German': 'de', 'Icelandic': 'is', 'Italian': 'it', 'English (Australia)': 'en-au', 'English (United Kingdom)': 'en-uk',
        'Chinese (Mandarin/Taiwan)': 'zh-tw', 'Dutch': 'nl', 'Korean': 'ko', 'Danish': 'da', 'Indonesian': 'id', 'Latin': 'la',
        'Hungarian': 'hu', 'Macedonian': 'mk', 'French': 'fr', 'Catalan': 'ca', 'Armenian': 'hy', 'Afrikaans': 'af', 'Bengali': 'bn',
        'Finnish': 'fi', 'Chinese (Mandarin/China)': 'zh-cn', 'Albanian': 'sq', 'Greek': 'el', 'Latvian': 'lv', 'English': 'en',
        'Arabic': 'ar', 'Croatian': 'hr', 'Chinese (Cantonese)': 'zh-yue', 'Chinese': 'zh', 'Czech': 'cs', 'Khmer (Cambodian)': 'km',
        'Japanese': 'ja', 'English (United States)': 'en-us', 'Esperanto': 'eo', 'Hindi': 'hi'}


var = tkinter.StringVar(mGui)
var.set("Select any Language")
p = tkinter.OptionMenu(mGui, var, *data, command=Translate)
p.place(x=378, y=0)


mbutton4 = tkinter.Button(mGui, font=("arial", 16, "bold"), text="Translate", bd=10,
                  justify="center", command=Translate, bg="powder blue").place(x=378, y=120)


mOutput = tkinter.Text(mGui, width=63, height=7, wrap=tkinter.WORD, background="white")
mOutput.place(y=180)
mScrollbar = tkinter.Scrollbar(mGui)
mScrollbar.place(x=491, y=180)
mOutput.configure(yscrollcommand=mScrollbar.set)
mScrollbar.configure(command=mOutput.yview)
# ===============================================================Run The Program=====================================================================================
mGui.mainloop()
