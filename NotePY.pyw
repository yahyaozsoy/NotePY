import json, os, sys
from tkinter.filedialog import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, colorchooser
from textblob import TextBlob
import requests

def setup():
    global pref
    global lang
    global data
    global langJSON
    global currentLANGS
    
    data = {
        # This settings defines what is default. So, if you don't know what are you doing don't change anything
        "colorPri": "white",
        "colorSec": "#F2F2F2",
        "font": "Arial",
        "fontSize": 15,
        "fontColor": "black",
        "Language": "English.json"
    }

    langJSON = {
        # WARNING! Spell Checker didn't work with lang files
        # It is officially set to work with English files    
        "new": "New",
        "open": "Open",
        "save": "Save",
        "spellChecker": "Spell Checker",
        "exit": "Exit",
        "options": "Options",
        "optionsTitle": "Options Menu",
        "selectPri": "Select a primary color",
        "selectSec": "Select a secondary color",
        "fontT": "Font Type",
        "fontS": "Font Size",
        "fontC": "Font Color",
        "selectFontC": "Select a font color",
        "saveFont": "Save font changes",
        "setDefault": "Set Default",
        "saveTheme": "Save Theme",
        "chooseTheme": "Choose Theme",
        "sideNote": "If you can't see\n what are you looking for,\n you can change the setting\nthrough 'preferences.json'",
        "warning!": "Warning!",
        "warnSetDef": "Are you sure you want to revert all the changes?",
        "warnSpellC": "This action is WIP\nIf you really want to try, save it before clicking yes",
        "warnNew": "Are you sure you want to open a new file?\nThis action may cause unrevertable changes",
        "warnOpen": "Are you sure you want to open file?\nThis action may cause the destruction of your words",
        "warnExit": "Are you sure you want to exit?",
        "warnLang": "Don't forget even though you change language,\n spell checker will just work for English",
        "warnOpenTheme": "Are you sure you want to change your theme?\nYou may lose your current theme(if you did not saved it)",
        "language": "Language",
        "langTitle": "Language Settings",
        "selectLang": "Select a language",
        "langSave": "Save"
    }

    if not os.path.exists('savedPrefs'):
        os.makedirs('savedPrefs')
        
    if not os.path.exists('langs'):
        os.makedirs('langs')

    if not os.path.isfile(".\preferences.json") and not os.access(".\preferences.json", os.R_OK):
        with open(os.path.join(".\preferences.json"), "w") as p:
            json.dump(data, p)

    if not os.path.isfile(".\langs\English.json") and not os.access(".\langs\English.json", os.R_OK):
        with open(os.path.join(".\langs\English.json"), "w") as p:
            json.dump(langJSON, p)
            
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
        if not os.path.isfile(".\pictures\gear.png"):
            gear1 = "https://i.hizliresim.com/9fag7y1.png"
            r1 = requests.get(gear1)
            with open(".\pictures\gear.png", "wb") as f:
                f.write(r1.content)
        if not os.path.isfile(".\pictures\earth.png"):
            globe1 = "https://i.hizliresim.com/9ohwovw.png"
            r2 = requests.get(globe1)
            with open(".\pictures\earth.png", "wb") as f:
                f.write(r2.content)
        if not os.path.isfile(".\pictures\disclaimer.txt"):
            with open(os.path.join(".\pictures\disclaimer.txt"), "w") as f2:
                f2.write("Gear image is taken from 'https://iconarchive.com/show/noto-emoji-objects-icons-by-google/62971-gear-icon.html'\nGlobe image is taken from 'https://images.emojiterra.com/google/android-pie/512px/1f30d.png'")
            

    with open("preferences.json", "r") as read_it:
        pref = json.load(read_it)

    currentLANGS = pref["Language"]

    with open(f".\langs\{currentLANGS}", "r") as read_it:
        lang = json.load(read_it)
        
    main()

def setDefault():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnSetDef"],icon = 'warning')
    if MsgBox == 'yes': 
        with open("preferences.json", "w") as p:
            json.dump(data, p)
        restart()

def restart():
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        os.execv(sys.executable, ['python'] + sys.argv)

def priColor():
    _priColor = colorchooser.askcolor(title="Select a primary color")
    
    if _priColor and str(_priColor) != "(None, None)":
        pref["colorPri"] = _priColor[1]
        a_file = open("preferences.json", "w")
        json.dump(pref, a_file)
        a_file.close()
        print(str(_priColor))

def secColor():
    _secColor = colorchooser.askcolor(title="Select a secondary color")
    
    if _secColor and str(_secColor) != "(None, None)":
        pref["colorSec"] = _secColor[1]
        b_file = open("preferences.json", "w")
        json.dump(pref, b_file)
        b_file.close()    
    
def spellCheck():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnSpellC"],icon = 'warning')
    if MsgBox == 'yes':
        _text = str(entry.get(1.0, tk.END))
        spellChecker = TextBlob(_text)
        entry.delete(1.0, tk.END)
        entry.insert(1.0, str(spellChecker.correct()))

def newFile():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnNew"],icon = 'warning')
    if MsgBox == 'yes':
       entry.delete(1.0, tk.END)
    
def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('Text Files', '.txt')], defaultextension=".txt")
    if new_file == None: return
    
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnOpen"],icon = 'warning')
    if MsgBox == 'yes':
        file = askopenfile(mode = 'r', filetype = [('Text Files', '*.txt')], defaultextension=".txt")
        if file != None: content = file.read()
        
        entry.insert(tk.INSERT, content)
    
def exitFile():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnExit"],icon = 'warning')
    if MsgBox == 'yes': canvas.destroy()

def fontColorChooser():
    global _fontColorChooser
    _fontColorChooser = colorchooser.askcolor(title="Select a font color")

def saveFChange():
    _fontEND = str(f.get())
    _fontSize = int(e_fontSize.get(1.0, tk.END))
    
    if str(_fontColorChooser) != "" and str(_fontColorChooser) != "(None, None)": 
        pref["fontColor"] = _fontColorChooser[1]
    if f.get() and _fontEND != "":
        pref["font"] = _fontEND
    if e_fontSize.get(1.0, tk.END) and str(e_fontSize.get(1.0, tk.END)) != "" :
        pref["fontSize"] = _fontSize
    
    print(f"_fontEND:{_fontEND}\n _fontColorChooser:{_fontColorChooser}\n _fontSize:{_fontSize}")
    
    c_file = open("preferences.json", "w")
    json.dump(pref, c_file)
    c_file.close()
    restart()

def savePrefs():
    new_file = asksaveasfile(mode = 'w', filetype = [('JSON files', '.json')], defaultextension=".json", title="Save Theme")
    if new_file is None: return
    
    with open('preferences.json','r') as firstfile:
        for line in firstfile:
            new_file.write(line)
    new_file.close()
    
def openPrefs():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnOpenTheme"],icon = 'warning')
    if MsgBox == 'yes':
        file = askopenfile(mode = 'r', filetype = [('JSON files', '*.json')], defaultextension=".json", title="Choose Theme")
        # if file != None: content = file.read()
        
        if file and file is not None: 
            with open('preferences.json', 'w') as firstfile:
                for line in file:
                    firstfile.write(line)
        restart()
            
def optionsWindow():
    global e_font
    global e_fontSize
    global e_fontColor
    global window
    global f
    
    window = tk.Toplevel()
        
    window.geometry("740x390")
    window.title(lang["optionsTitle"])
    window.config(bg = pref["colorPri"])

    center = tk.Frame(window, bg=pref["colorPri"])
    center.pack(padx = 10, pady= 10, anchor='c')
    
    b_colorPri = Button(window, text = lang["selectPri"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = priColor)
    b_colorPri.grid(in_= center, padx = 10, pady = 5, row = 0, column = 0)
    
    b_colorSec = Button(window, text = lang["selectSec"], fg = pref["fontColor"], bg = pref["colorSec"], font = (pref["font"], 12), command = secColor)
    b_colorSec.grid(in_= center, pady = 5, row = 0, column = 1, padx = 20)
    
    txt_f = Label(window, text= lang["fontT"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12))
    txt_f.grid(in_= center, padx = 10, pady = 5, row = 1, column = 0)

    f = tk.StringVar() 
    e_font = ttk.Combobox(window, font = (pref["font"], 12), width="20", height="5", textvariable = f)
    e_font['values'] = ('Arial',
                        'Arial Black',
                        'Comic Sans MS',
                        'Geogia',
                        'Helvetica',
                        'Sans-Serif',
                        'Serif',
                        'Times New Roman',
                        'Roboto',
                        )
    e_font.grid(in_= center, padx = 10, pady = 5, row = 1, column = 1)
    e_font.current(0)
    
    txt_fS = Label(window, text = lang["fontS"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12))
    txt_fS.grid(in_= center, padx = 10, pady = 5, row = 2, column = 0)
    
    e_fontSize = tk.Text(window, fg = pref["fontColor"], bg = pref["colorSec"], font = (pref["font"], 12), width="20", height="1")
    e_fontSize.grid(in_= center, padx = 10, pady = 5, row = 2, column = 1)
    
    txt_small = Label(window, text = lang["sideNote"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 8), width= 25)
    txt_small.grid(in_= center, padx = 0, pady = 5, row = 2, column = 2)

    txt_fC = Label(window, text = lang["fontC"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12))
    txt_fC.grid(in_= center, padx = 10, pady = 5, row = 3, column = 0)
    
    e_fontColor = Button(window, text = lang["selectFontC"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = fontColorChooser)
    e_fontColor.grid(in_= center, padx = 10, pady = 5, row = 3, column = 1)
    
    b_fontSave = Button(window, fg = pref["fontColor"], bg = pref["colorPri"], text= lang["saveFont"], font = (pref["font"], 12), command = saveFChange)
    b_fontSave.grid(in_= center, padx = 10, pady = 5, row = 4, column = 1)
    
    b_prefsave = Button(window, fg = pref["fontColor"], bg = pref["colorPri"], text= lang["saveTheme"], font = (pref["font"], 12), command = savePrefs)
    b_prefsave.grid(in_= center, padx = 10, pady = 5, row = 5, column = 0)
    
    b_prefopen = Button(window, fg = pref["fontColor"], bg = pref["colorPri"], text= lang["chooseTheme"], font = (pref["font"], 12), command = openPrefs)
    b_prefopen.grid(in_= center, padx = 10, pady = 5, row = 5, column = 2)
    
    b_setDefault = Button(window, text = lang["setDefault"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = setDefault)
    b_setDefault.grid(in_= center, padx = 10, pady = 5, row = 4, column = 2)

def saveLang():
    MsgBox = tk.messagebox.askquestion (lang["warning!"], lang["warnLang"],icon = 'warning')
    if MsgBox == 'yes':
        currentLANGS = f"{langs.get()}.json"
        pref["Language"] = currentLANGS
        
        lang_file = open("preferences.json", "w")
        json.dump(pref, lang_file)
        lang_file.close()
        
        restart()

def langWindow():
    global langs
    
    lWindow = tk.Toplevel()
    
    lWindow.geometry("350x150")
    lWindow.title(lang["langTitle"])
    lWindow.config(bg = pref["colorPri"])
    
    txt_langSel = Label(lWindow, text= lang["selectLang"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12))
    txt_langSel.pack(padx = 10, pady = 10)
    
    langs = tk.StringVar() 
    languageSelector = ttk.Combobox(lWindow, font = (pref["font"], 12), width="20", height="5", textvariable = langs)
    languageSelector['values'] = ("English",
                        # "Türkçe",
                        # "Azərbaycan Dili",
                        # "Deutsch",
                        # "Русский язык",
                        # "Español",
                        # "Português",
                        # "Italiao",
                        # "日本語",
                        # "한국",
                        # "中文",
                        )
    languageSelector.pack(padx= 10, pady= 5)
    if pref["Language"] == "English.json":
        currentLang = 0
    elif pref["Language"] == "Türkçe.json":
        currentLang = 1
    elif pref["Language"] == "Azərbaycan Dili.json":
        currentLang = 2
    elif pref["Language"] == "Deutsch.json":
        currentLang = 3
    elif pref["Language"] == "Русский язык.json":
        currentLang = 4
    elif pref["Language"] == "Español.json":
        currentLang = 5
    elif pref["Language"] == "Português.json":
        currentLang = 6
    elif pref["Language"] == "Italiao.json":
        currentLang = 7
    elif pref["Language"] == "日本語.json":
        currentLang = 8
    elif pref["Language"] == "한국.json":
        currentLang = 9
    elif pref["Language"] == "中文.json":
        currentLang = 10
    languageSelector.current(currentLang)
    
    submit_button = Button(lWindow, text = lang["langSave"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = saveLang)
    submit_button.pack(padx = 10, pady = 5)

def main():
    global entry
    global canvas
    
    canvas = tk.Tk()
    canvas.geometry("800x800")
    canvas.title("NotePY")
    canvas.config(bg = pref["colorPri"])

    combostyle = ttk.Style()

    combostyle.theme_create('combostyle', parent='alt',
                            settings = {'TCombobox':
                                        {'configure':
                                        {'selectbackground': pref["colorSec"],
                                            'fieldbackground': pref["colorSec"],
                                            'background': pref["colorSec"],
                                            'foreground': pref["fontColor"]
                                        }}}
                            )
    # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
    combostyle.theme_use('combostyle') 

    gear = PhotoImage(file = ".\pictures\gear.png")
    globe = PhotoImage(file = ".\pictures\earth.png") 

    top = tk.Frame(canvas, bg=pref["colorPri"])
    top.pack(padx = 10, pady= 5, anchor='nw')

    b1 = tk.Button(canvas, text=lang["new"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = newFile)
    b1.pack(padx = 5, in_= top, side = tk.LEFT)

    b2 = tk.Button(canvas, text=lang["open"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = openFile)
    b2.pack(padx = 5, in_= top, side = tk.LEFT)

    b3 = tk.Button(canvas, text=lang["save"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = saveFile)
    b3.pack(padx = 5, in_= top, side = tk.LEFT)

    b4 = tk.Button(canvas, text=lang["spellChecker"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = spellCheck)
    b4.pack(padx = 5, in_= top, side = tk.LEFT)

    b6 = tk.Button(canvas, text=lang["exit"], fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = exitFile)
    b6.pack(padx = 5, in_= top, side = tk.RIGHT)

    b5 = tk.Button(canvas, text=lang["options"], image= gear,fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = optionsWindow)
    b5.pack(padx = 5, in_= top, side = tk.RIGHT)

    langButton = tk.Button(canvas, text=lang["language"], image= globe,fg = pref["fontColor"], bg = pref["colorPri"], font = (pref["font"], 12), command = langWindow)
    langButton.pack(padx = 5, in_= top, side = tk.RIGHT)

    entry = tk.Text(canvas, wrap = tk.WORD, fg = pref["fontColor"], bg = pref["colorSec"], font = (pref["font"], pref["fontSize"]), undo= True)
    entry.pack(padx = 10, pady = 5, expand = tk.TRUE, fill = tk.BOTH)
    entry.bind('<Control-z>', entry.edit_undo)
    entry.bind('<Control-y>', entry.edit_redo)

    canvas.mainloop()

setup()