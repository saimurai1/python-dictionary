import sys
import messagebox
import tkinter
import tkinter.ttk as ttk
import pyttsx3
from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()
root = tkinter.Tk()

ment_dict = tkinter.StringVar()
ment_trans = tkinter.StringVar()
ment_tts = tkinter.StringVar()

root.geometry('600x500+0+0')

root.title("Dictionary")

def TextToSpeech():
    mtext = ment_tts.get().strip()
    if not mtext:
        messagebox.showwarning("Warning", "Please enter some text to speak.")
        return
    try:
        engine = pyttsx3.init()
        engine.say(mtext)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Text-to-Speech failed: {str(e)}")


def Meaning(L="en"):
    mtext = ment_dict.get()
    mOutput_dict.delete(0.0, tkinter.END)
    Word = (dictionary.meaning(L, mtext))
    if Word:
        if isinstance(Word, tuple) and len(Word) == 2:
            lang, meanings = Word
            formatted_word = "\n".join([f"{k}: {', '.join(v)}" for k, v in meanings.items()])
        else:
            formatted_word = str(Word)
    else:
        formatted_word = "No meaning found."
    mOutput_dict.insert(tkinter.END, formatted_word)


def Synonym(L="en"):
    mtext = ment_dict.get()
    mOutput_dict.delete(0.0, tkinter.END)
    Word = (dictionary.synonym(L, mtext))
    if Word:
        if isinstance(Word, tuple) and len(Word) == 2:
            lang, synonyms = Word
            formatted_word = "\n".join([f"{k}: {', '.join(v)}" for k, v in synonyms.items()])
        else:
            formatted_word = str(Word)
    else:
        formatted_word = "No synonyms found."
    mOutput_dict.insert(tkinter.END, formatted_word)

def Antonym(L="en"):
    mtext = ment_dict.get()
    mOutput_dict.delete(0.0, tkinter.END)
    Word = (dictionary.antonym(L, mtext))
    if Word:
        if isinstance(Word, tuple) and len(Word) == 2:
            lang, antonyms = Word
            formatted_word = "\n".join([f"{k}: {', '.join(v)}" for k, v in antonyms.items()])
        else:
            formatted_word = str(Word)
    else:
        formatted_word = "No antonyms found."
    mOutput_dict.insert(tkinter.END, formatted_word)

def Translate(L="hi"):
    L = var.get()
    mtext = ment_trans.get()
    Language = data.get(L, L)  # Get the language code from the dict
    mOutput_trans.delete(0.0, tkinter.END)
    try:
        Word = (dictionary.translate(Language, mtext))
        if Word:
            if isinstance(Word, tuple) and len(Word) == 2:
                lang, translation = Word
                formatted_word = str(translation)
            else:
                formatted_word = str(Word)
        else:
            formatted_word = "No translation found."
    except Exception as e:
        formatted_word = f"Translation error: {str(e)}"
    mOutput_trans.insert(tkinter.END, formatted_word)


def mHistory():
    f = open(creds, 'a')
    f.write(ment_dict.get())
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
        root.destroy()
        return


creds = 'tempfile.txt'
a = open(creds, 'w')
a.close()


menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Search History", command=mHistory)
filemenu.add_command(label="Exit", command=mExit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menubar, tearoff=1)
#editmenu.add_command(label="Translate Into",command=ChangeLanguage)
# menubar.add_cascade(label="Edit",menu=editmenu)

root.config(menu=menubar)

# Create notebook for tabs
notebook = ttk.Notebook(root)
tab_dict = ttk.Frame(notebook)
tab_trans = ttk.Frame(notebook)
tab_tts = ttk.Frame(notebook)
notebook.add(tab_dict, text="Dictionary")
notebook.add(tab_trans, text="Translation")
notebook.add(tab_tts, text="Text to Speech")
notebook.pack(expand=1, fill="both")

# Dictionary Tab
mFrame = tkinter.Frame(tab_dict, bg="powder blue", relief="ridge", bd=10)
mFrame.pack(pady=10)

mEntry_dict = tkinter.Entry(mFrame, font=("arial", 24, "bold"), bg="powder blue",
               bd=10, textvariable=ment_dict, insertwidth=2, justify="center", width=60)
mEntry_dict.pack(pady=15)

button_frame = tkinter.Frame(mFrame, bg="powder blue")
button_frame.pack(pady=10)

mbutton1 = tkinter.Button(button_frame, font=("arial", 16, "bold"), text="Meaning", bd=10,
                  justify="center", command=Meaning, bg="powder blue")
mbutton1.pack(side=tkinter.LEFT, padx=5)

mbutton2 = tkinter.Button(button_frame, font=("arial", 16, "bold"), text="Synonym", bd=10,
                  justify="center", command=Synonym, bg="powder blue")
mbutton2.pack(side=tkinter.LEFT, padx=5)

mbutton3 = tkinter.Button(button_frame, font=("arial", 16, "bold"), text="Antonym", bd=10,
                  justify="center", command=Antonym, bg="powder blue")
mbutton3.pack(side=tkinter.LEFT, padx=5)

mOutput_dict = tkinter.Text(mFrame, width=63, height=7, wrap=tkinter.WORD, background="white")
mOutput_dict.pack(pady=10)
mScrollbar_dict = tkinter.Scrollbar(mFrame)
mScrollbar_dict.pack(side=tkinter.RIGHT, fill=tkinter.Y)
mOutput_dict.configure(yscrollcommand=mScrollbar_dict.set)
mScrollbar_dict.configure(command=mOutput_dict.yview)

# Translation Tab
mFrame_trans = tkinter.Frame(tab_trans, bg="powder blue", relief="ridge", bd=10)
mFrame_trans.pack(pady=10)

mEntry_trans = tkinter.Entry(mFrame_trans, font=("arial", 24, "bold"), bg="powder blue",
               bd=10, textvariable=ment_trans, insertwidth=2, justify="center", width=60)
mEntry_trans.pack(pady=15)

data = {'Japanese': 'ja', 'English (United States)': 'en-us', 'Esperanto': 'eo', 'Hindi': 'hi', 'Spanish': 'es', 'Portuguese': 'pt',
        'Russian': 'ru', 'Polish': 'pl', 'Romanian': 'ro', 'Turkish': 'tr', 'Marathi': 'mr', 'Malay': 'ms', 'Tamil': 'ta',
        'Javanese': 'jv', 'Ukrainian': 'uk'}

var = tkinter.StringVar(root)
var.set("Select any Language")
p = tkinter.OptionMenu(mFrame_trans, var, *data)
p.pack(pady=10)

mbutton4 = tkinter.Button(mFrame_trans, font=("arial", 16, "bold"), text="Translate", bd=10,
                  justify="center", command=Translate, bg="powder blue")
mbutton4.pack(pady=10)

mOutput_trans = tkinter.Text(mFrame_trans, width=63, height=7, wrap=tkinter.WORD, background="white")
mOutput_trans.pack(pady=10)
mScrollbar_trans = tkinter.Scrollbar(mFrame_trans)
mScrollbar_trans.pack(side=tkinter.RIGHT, fill=tkinter.Y)
mOutput_trans.configure(yscrollcommand=mScrollbar_trans.set)
mScrollbar_trans.configure(command=mOutput_trans.yview)

# Text to Speech Tab
mFrame_tts = tkinter.Frame(tab_tts, bg="powder blue", relief="ridge", bd=10)
mFrame_tts.pack(pady=10)

mLabel_tts = tkinter.Label(mFrame_tts, font=("arial", 25, "bold"),
               text="TEXT TO SPEECH", fg="steel blue", bd=10, anchor="w")
mLabel_tts.pack()

mEntry_tts = tkinter.Entry(mFrame_tts, font=("arial", 24, "bold"), bg="powder blue",
               bd=10, textvariable=ment_tts, insertwidth=2, justify="center", width=60)
mEntry_tts.pack(pady=15)

mbutton_tts = tkinter.Button(mFrame_tts, font=("arial", 16, "bold"), text="Speak", bd=10,
                  justify="center", command=TextToSpeech, bg="powder blue")
mbutton_tts.pack(pady=10)
mtext = ment_tts.get().strip()
if not mtext:
    messagebox.showwarning("Warning", "Please enter some text to speak.")
try:
    engine = pyttsx3.init()
    engine.say(mtext)
    engine.runAndWait()
except Exception as e:
    messagebox.showerror("Error", f"Text-to-Speech failed: {str(e)}")


def Meaning(L="en"):
    mtext = ment.get()
    mOutput_dict.delete(0.0, tkinter.END)
    Word = (dictionary.meaning(L, mtext))
    if Word:
        if isinstance(Word, tuple) and len(Word) == 2:
            lang, meanings = Word
            formatted_word = "\n".join([f"{k}: {', '.join(v)}" for k, v in meanings.items()])
        else:
            formatted_word = str(Word)
    else:
        formatted_word = "No meaning found."
    mOutput_dict.insert(tkinter.END, formatted_word)


# ===============================================================Run The Program=====================================================================================
root.mainloop()
