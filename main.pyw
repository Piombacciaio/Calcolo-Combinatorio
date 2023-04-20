import ctypes, os, sys, webbrowser
from itertools import permutations, product
from math import factorial
from urllib import request
try:
  import PySimpleGUI as PSG
except ImportError:
  import pip
  pip.main(['install', 'PySimpleGUI'])
  import PySimpleGUI as PSG

PSG.theme("LightBlue2")

#INITIAL CHECKS
def run_checks():
  """
  Initial checks to see if all necessary assets are present on the pc and download them if necessary
  """
  if sys.argv[0].endswith(".py"):
    ctypes.windll.kernel32.SetConsoleTitleW(f'Calcolo Combinatorio | made by piombacciaio')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=0, cols=0))

  if not os.path.exists("assets"):
    os.mkdir("assets")
  
  files = ["simple-disp.png","repeated-disp.png", "simple-perm.png", "repeated-perm.png", "simple-comb.png", "repeated-comb.png", "icon.ico"]
  if any(not os.path.exists(f"assets/{item}") for item in files):

    try:

      github = 'https://raw.githubusercontent.com/Piombacciaio/Calcolo-Combinatorio/main/assets/'
      path = "assets"

      for file in files:
        if not os.path.exists(f"{path}/{file}"):
          with request.urlopen(github + file) as response:
            with open(os.path.join(path, file), 'wb') as f:
              f.write(response.read())
              
    except:
      PSG.popup_ok("Missing assets or invalid filenames", "Check assets directory or go to https://github.com/Piombacciaio/Calcolo-Combinatorio to recover original files.", title="Error", button_color="red")
      quit(1)

# ASSETTS
SIMPLE_DISP_IMG = "assets\\simple-disp.png"
REPEATED_DISP_IMG = "assets\\repeated-disp.png"
SIMPLE_PERM_IMG = "assets\\simple-perm.png"
REPEATED_PERM_IMG = "assets\\repeated-perm.png"
SIMPLE_COMB_IMG = "assets\\simple-comb.png"
REPEATED_COMB_IMG = "assets\\repeated-comb.png"
ICON = "assets\\icon.ico"
# LAYOUTS
simple_disp = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-SIMPLE-DISP-LENGHTINPUT-")], 
  [PSG.Text("Classe (k)"), PSG.Push(), PSG.Input("", key="-SIMPLE-DISP-CLASSINPUT-")],
  [PSG.Checkbox("Visualizzare le disposizioni?", key="-SHOW-SIMPLE-DISP-", tooltip="Rende il processo più lento")],
  [PSG.Text("D"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-DISP-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-DISP-CALCULATE-"), PSG.Button("Formula", key="-SIMPLE-DISP-FORMULA-"), PSG.Button("Visualizza disposizioni", key="-SIMPLE-DISP-LIST-", disabled=True)],
]
repeated_disp = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-REPEATED-DISP-LENGHTINPUT-")], 
  [PSG.Text("Classe (k)"), PSG.Push(), PSG.Input("", key="-REPEATED-DISP-CLASSINPUT-")],
  [PSG.Checkbox("Visualizzare le disposizioni?", key="-SHOW-REPEATED-DISP-", tooltip="Rende il processo più lento")],
  [PSG.Text("D'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-DISP-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-DISP-CALCULATE-"), PSG.Button("Formula", key="-REPEATED-DISP-FORMULA-"), PSG.Button("Visualizza disposizioni", key="-REPEATED-DISP-LIST-", disabled=True)],
]
disp_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Disposizione Semplice", layout=simple_disp),
      PSG.Tab("Disposizione con ripetizioni", layout=repeated_disp)
    ]])
  ]
]

simple_perm = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-SIMPLE-PERM-LENGHTINPUT-")], 
  [PSG.Checkbox("Permutazione circolare?", key="-CIRCLE-PERM-")],
  [PSG.Text()],
  [PSG.Text("P"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-PERM-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-PERM-CALCULATE-"), PSG.Button("Formula", key="-SIMPLE-PERM-FORMULA-")],
]
repeated_perm = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-REPEATED-PERM-LENGHTINPUT-")], 
  [PSG.Text("Elementi ripetuti (h,k)"), PSG.Push(), PSG.Input("", key="-REPEATED-PERM-REPSINPUT-", tooltip="Separa gli elementi ripetuti con una virgola")],
  [PSG.Text(), PSG.VPush()],
  [PSG.Text("P'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-PERM-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-PERM-CALCULATE-"), PSG.Button("Formula", key="-REPEATED-PERM-FORMULA-")],
]
perm_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Permutazione Semplice", layout=simple_perm),
      PSG.Tab("Permutazione con ripetizioni", layout=repeated_perm)
    ]])
  ]
]

simple_comb = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-SIMPLE-COMB-LENGHTINPUT-")], 
  [PSG.Text("Classe (k)"), PSG.Push(), PSG.Input("", key="-SIMPLE-COMB-CLASSINPUT-")],
  [PSG.Text(), PSG.VPush()],
  [PSG.Text("C"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-COMB-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-COMB-CALCULATE-"), PSG.Button("Formula", key="-SIMPLE-COMB-FORMULA-")],
]
repeated_comb = [
  [PSG.Text("Numero elementi (n)"), PSG.Push(), PSG.Input("", key="-REPEATED-COMB-LENGHTINPUT-")], 
  [PSG.Text("Classe (k)"), PSG.Push(), PSG.Input("", key="-REPEATED-COMB-CLASSINPUT-")],
  [PSG.Text(), PSG.VPush()],
  [PSG.Text("C'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-COMB-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-COMB-CALCULATE-"), PSG.Button("Formula", key="-REPEATED-COMB-FORMULA-")],
]
comb_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Combinazione Semplice", layout=simple_comb),
      PSG.Tab("Combinazione con ripetizioni", layout=repeated_comb)
    ]])
  ]
]

def_text = """
DISPOSIZIONI

- Disposizioni Semplici

Le disposizioni semplici di n elementi distinti di classe k (con 0 < k <= n) sono tutti i gruppi di k elementi scelti fra gli n, che differiscono per almeno un elemento o per l'ordine con cui gli elementi sono collocati
    
- Disposizioni con Ripetizione

Le disposizioni con ripetizione di n elementi distinti di classe k (con k numero naturale qualunque non nullo) sono tutti i gruppi di k elementi, anche ripetuti, scelti fra gli n, che differiscono per almeno un elemento o per il loro ordine
    
PERMUTAZIONI

- Permutazioni Semplici

Le permutazioni semplici di n elementi distinti sono tutti i gruppi formati dagli n elementi, che differiscono per il loro ordine

- Permutazioni Circolari

La permutazione circolare è una permutazione di elementi diversi tra loro in cui non è possibile distinguere tra il primo e l'ultimo elemento; in altri termini una permutazione circolare è il risultato di uno scambio dell'ordine di elementi distinti disposti in modo circolare

- Permutazioni con Ripetizione

Le permutazioni con ripetizione di n elementi, di cui h, k, … ripetuti, sono tutti i gruppi formati dagli n elementi, che differiscono per l'ordine in cui si presentano gli elementi distinti e la posizione che occupano gli elementi ripetuti
    
COMBINAZIONI

- Combinazioni Semplici

Le combinazioni semplici di n elementi distinti di classe k (con 0 < k <= n) sono tutti i gruppi di k elementi [scelti all'interno di n] che differsicono per almeno un elemento ma non per l'ordine
    
- Combinazioni con Ripetizione
    
Le combinazioni con ripetizione di n elementi distinti di classe k [numero naturale non nullo] sono tutti i gruppi di k elementi che si possono formare nei quali:
    - ogni elemento può essere ripetuto fino a k volte
    - non interessa l'ordine con cui gli elementi si presentano
    - è diverso il numero di volte col quale un elemento compare"""
defs_tab = [
  [PSG.Multiline(def_text, disabled=True, expand_x=True, expand_y=True)]
]
default_view = [
  [PSG.TabGroup([[
      PSG.Tab("Disposizioni", layout=disp_tab),
      PSG.Tab("Permutazioni", layout=perm_tab),
      PSG.Tab("Combinazioni", layout=comb_tab),
      PSG.Tab("Definizioni", layout=defs_tab)
    ]])
  ],
  [PSG.Button("Source", key="-VIEW-SOURCE-")]
]

# FUNCTIONS
def calculate_simple_disp(n:int, k:int, return_list:bool=False):
  """Le disposizioni semplici di n elementi distinti di classe k (con 0 < k <= n)
  sono tutti i gruppi di k elementi scelti fra gli n, che differiscono per almeno un
  elemento o per l'ordine con cui gli elementi sono collocati"""
  if k <= n:
    if return_list:
      simple_disp = permutations(range(n), k)
      return list(simple_disp)
    else:
      simple_disp = factorial(n) / factorial(n-k)
      return simple_disp
  else:
    PSG.popup_error("La classe dell'insieme non può essere maggiore del numero di elementi che compongono l'insieme stesso", title="", icon=ICON)

def calculate_repeated_disp(n:int, k:int, return_list:bool=False):
  """Le disposizioni con ripetizione di n elementi distinti di classe k (con k numero 
  naturale qualunque non nullo) sono tutti i gruppi di k elementi, anche ripetuti,
  scelti fra gli n, che differiscono per almeno un elemento o per il loro ordine"""
  if return_list:
    rep_disp = [p for p in product(range(n), repeat=k)]
    return rep_disp
  else:
    rep_disp = n**k
    return rep_disp

def calculate_simple_perm(n:int):
  """Le permutazioni semplici di n elementi distinti sono tutti i gruppi formati
  dagli n elementi, che differiscono per il loro ordine"""
  return factorial(n)

def calculate_circular_perm(n:int):
  """Una permutazione è una permutazione di elementi diversi tra loro in cui non 
  è possibile distinguere tra il primo e l'ultimo elemento; in altri termini una 
  permutazione circolare è il risultato di uno scambio dell'ordine di elementi 
  distinti disposti in modo circolare."""
  return factorial(n-1)

def calculate_repeated_perm(n:int, k:list):
  """Le permutazioni con ripetizione di n elementi, di cui h, k, … ripetuti, sono
  tutti i gruppi formati dagli n elementi, che differiscono per l'ordine in cui si pre-
  sentano gli elementi distinti e la posizione che occupano gli elementi ripetuti"""
  denom = 1
  if sum(k) <= n:
    for x in k:
      denom = denom * factorial(x)
    perm = factorial(n) / denom
    return perm
  else:
    PSG.popup_error("Non possono esserci più elementi ripetuti degli elementi che compongono l'insieme stesso", title="", icon=ICON)

def calculate_simple_comb(n:int, k:int):
  """Le combinazioni semplici di n elementi distinti di classe k (con 0 < k <= n)
  sono tutti i gruppi di k elementi [scelti all'interno di n] che differsicono per
  almeno un elemento ma non per l'ordine"""
  if k <= n:
    comb = factorial(n) / (factorial(k) * factorial(n-k))
    return comb
  else:
    PSG.popup_error("La classe dell'insieme non può essere maggiore del numero di elementi che compongono l'insieme stesso", title="", icon=ICON)

def calculate_repeated_comb(n:int, k:int):
  """
  Le combinazioni con ripetizione di n elementi distinti di classe k [numero naturale non nullo] sono tutti
  i gruppi di k elementi che si possono formare, nei quali:
  - ogni elemento può essere ripetuto fino a k volte
  - non interessa l'ordine con cui gli elementi si presentano
  - è diverso il numero di volte col quale un elemento compare
  """
  n = n + k - 1
  return calculate_simple_comb(n, k)

def main():
  """Script basato sulle formule per il calcolo combinatorio trovate nel capitolo 26 del libro Zanichelli Matematica.verde 4B"""

  window = PSG.Window("Calcolo combinatorio", default_view, icon=ICON)

  while True:
    
    try:
      
      events, values = window.read()

      if events == PSG.WIN_CLOSED: break

      #SIMPLE DISP
      if events == "-SIMPLE-DISP-CALCULATE-":

        n = int(values["-SIMPLE-DISP-LENGHTINPUT-"])
        k = int(values["-SIMPLE-DISP-CLASSINPUT-"])
        return_list = values["-SHOW-SIMPLE-DISP-"]

        global simple_disp
        simple_disp = calculate_simple_disp(n, k, return_list)

        window["-SIMPLE-DISP-OUTPUT-"].update(len(simple_disp) if type(simple_disp) == list else int(simple_disp))
        window["-SIMPLE-DISP-LIST-"].update(disabled=False) if return_list else window["-SIMPLE-DISP-LIST-"].update(disabled=True)
      
      if events == "-SIMPLE-DISP-LIST-":
        PSG.popup_scrolled(simple_disp, title="Disposizioni", icon=ICON)
      
      #REPEATED DISP
      if events == "-REPEATED-DISP-CALCULATE-":

        n = int(values["-REPEATED-DISP-LENGHTINPUT-"])
        k = int(values["-REPEATED-DISP-CLASSINPUT-"])
        return_list = values["-SHOW-REPEATED-DISP-"]

        global rep_disp
        rep_disp = calculate_repeated_disp(n, k, return_list)

        window["-REPEATED-DISP-OUTPUT-"].update(len(rep_disp) if type(rep_disp) == list else int(rep_disp))
        window["-REPEATED-DISP-LIST-"].update(disabled=False) if return_list else window["-REPEATED-DISP-LIST-"].update(disabled=True)

      if events == "-REPEATED-DISP-LIST-":
        PSG.popup_scrolled(rep_disp, title="Disposizioni", icon=ICON)

      #SIMPLE PERM
      if events == "-SIMPLE-PERM-CALCULATE-":
        n = int(values["-SIMPLE-PERM-LENGHTINPUT-"])
        circular = values["-CIRCLE-PERM-"]
        global simple_perm
        if circular:
          simple_perm = calculate_circular_perm(n)
        else:
          simple_perm = calculate_simple_perm(n)

        window["-SIMPLE-PERM-OUTPUT-"].update(simple_perm)
      
      #REPEATED PERM
      if events == "-REPEATED-PERM-CALCULATE-":
        n = int(values["-REPEATED-PERM-LENGHTINPUT-"])
        k = [int(item) for item in values["-REPEATED-PERM-REPSINPUT-"].split(",")]

        global rep_perm
        rep_perm = int(calculate_repeated_perm(n, k))

        window["-REPEATED-PERM-OUTPUT-"].update(rep_perm)

      #SIMPLE COMB
      if events == "-SIMPLE-COMB-CALCULATE-":
        n = int(values["-SIMPLE-COMB-LENGHTINPUT-"])
        k = int(values["-SIMPLE-COMB-CLASSINPUT-"])

        global simple_comb
        simple_comb = int(calculate_simple_comb(n, k))

        window["-SIMPLE-COMB-OUTPUT-"].update(simple_comb)

      #REPEATED COMB
      if events == "-REPEATED-COMB-CALCULATE-":
        n = int(values["-REPEATED-COMB-LENGHTINPUT-"])
        k = int(values["-REPEATED-COMB-CLASSINPUT-"])

        global rep_comb
        rep_comb = int(calculate_repeated_comb(n, k))

        window["-REPEATED-COMB-OUTPUT-"].update(rep_comb)

      #SHOW FORMULAS
      if events == "-SIMPLE-DISP-FORMULA-":
        PSG.PopupOK(image=SIMPLE_DISP_IMG)

      if events == "-REPEATED-DISP-FORMULA-":
        PSG.PopupOK(image=REPEATED_DISP_IMG)

      if events == "-SIMPLE-PERM-FORMULA-":
        PSG.PopupOK(image=SIMPLE_PERM_IMG)

      if events == "-REPEATED-PERM-FORMULA-":
        PSG.PopupOK(image=REPEATED_PERM_IMG)

      if events == "-SIMPLE-COMB-FORMULA-":
        PSG.PopupOK(image=SIMPLE_COMB_IMG)

      if events == "-REPEATED-COMB-FORMULA-":
        PSG.PopupOK(image=REPEATED_COMB_IMG)
  
      #OPEN SOURCE PAGE
      if events == "-VIEW-SOURCE-":
        webbrowser.open_new_tab("https://github.com/Piombacciaio/Calcolo-Combinatorio")

    except ValueError:
      PSG.popup_error("Inserire valori numerici validi per la classe e il numero di oggetti", title="", icon=ICON)

    except Exception as e:
      PSG.popup_error("Inviare il Traceback ad Andrea Piombo per assistenza", e, title="", icon=ICON)

if __name__ == '__main__': 
  run_checks()
  main()