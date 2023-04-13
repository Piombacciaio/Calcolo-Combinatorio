import PySimpleGUI as PSG, webbrowser
from itertools import permutations, product
from math import factorial
PSG.theme("DarkBlack")

# LAYOUTS
simple_disp = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-SIMPLE-DISP-LENGHTINPUT-")], 
  [PSG.Text("Classe"), PSG.Push(), PSG.Input("", key="-SIMPLE-DISP-CLASSINPUT-")],
  [PSG.Text("D"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-DISP-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-DISP-CALCULATE-"), PSG.Button("Visualizza disposizioni", key="-SIMPLE-DISP-LIST-", disabled=True)],
]
repeated_disp = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-REPEATED-DISP-LENGHTINPUT-")], 
  [PSG.Text("Classe"), PSG.Push(), PSG.Input("", key="-REPEATED-DISP-CLASSINPUT-")],
  [PSG.Text("D'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-DISP-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-DISP-CALCULATE-"), PSG.Button("Visualizza disposizioni", key="-REPEATED-DISP-LIST-", disabled=True)],
]
disp_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Disposizione Semplice", layout=simple_disp),
      PSG.Tab("Disposizione con ripetizioni", layout=repeated_disp)
    ]])
  ]
]

simple_perm = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-SIMPLE-PERM-LENGHTINPUT-")], 
  [PSG.Text()],
  [PSG.Text("P"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-PERM-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-PERM-CALCULATE-")],
]
repeated_perm = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-REPEATED-PERM-LENGHTINPUT-")], 
  [PSG.Text("Elementi ripetuti"), PSG.Push(), PSG.Input("", key="-REPEATED-PERM-REPSINPUT-", tooltip="Separa gli elementi ripetuti con una virgola")],
  [PSG.Text("P'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-PERM-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-PERM-CALCULATE-")],
]
perm_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Permutazione Semplice", layout=simple_perm),
      PSG.Tab("Permutazione con ripetizioni", layout=repeated_perm)
    ]])
  ]
]

simple_comb = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-SIMPLE-COMB-LENGHTINPUT-")], 
  [PSG.Text("Classe"), PSG.Push(), PSG.Input("", key="-SIMPLE-COMB-CLASSINPUT-")],
  [PSG.Text("C"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-SIMPLE-COMB-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-SIMPLE-COMB-CALCULATE-")],
]
repeated_comb = [
  [PSG.Text("Numero elementi"), PSG.Input("", key="-REPEATED-COMB-LENGHTINPUT-")], 
  [PSG.Text("Classe"), PSG.Push(), PSG.Input("", key="-REPEATED-COMB-CLASSINPUT-")],
  [PSG.Text("C'"), PSG.Push(), PSG.Input("", size = (55, 5), disabled=True, key="-REPEATED-COMB-OUTPUT-", text_color="black")],
  [PSG.Button("Calcola", key="-REPEATED-COMB-CALCULATE-")],
]
comb_tab = [
  [PSG.TabGroup([[
      PSG.Tab("Combinazione Semplice", layout=simple_comb),
      PSG.Tab("Combinazione con ripetizioni", layout=repeated_comb)
    ]])
  ]
]

default_view = [
  [PSG.TabGroup([[
      PSG.Tab("Disposizioni", layout=disp_tab),
      PSG.Tab("Permutazioni", layout=perm_tab),
      PSG.Tab("Combinazioni", layout=comb_tab)
    ]])
  ],
  [PSG.Button("Source", key="-VIEW-SOURCE-")]
]

def calculate_simple_disp(n:int, k:int):
  """Le disposizioni semplici di n elementi distinti di classe k (con 0 < k <= n)
  sono tutti i gruppi di k elementi scelti fra gli n, che differiscono per almeno un
  elemento o per l'ordine con cui gli elementi sono collocati"""
  simple_disp = permutations(range(n), k)
  return list(simple_disp)

def calculate_repeated_disp(n:int, k:int):
  """Le disposizioni con ripetizione di n elementi distinti di classe k (con k numero 
  naturale qualunque non nullo) sono tutti i gruppi di k elementi, anche ripetuti,
  scelti fra gli n, che differiscono per almeno un elemento o per il loro ordine"""
  rep_disp = [p for p in product(range(n), repeat=k)]
  return rep_disp

def calculate_simple_perm(n:int):
  """Le permutazioni semplici di n elementi distinti sono tutti i gruppi formati
  dagli n elementi, che differiscono per il loro ordine"""
  return factorial(n)

def calculate_repeated_perm(n:int, k:list):
  """Le permutazioni con ripetizione di n elementi, di cui h, k, … ripetuti, sono
  tutti i gruppi formati dagli n elementi, che differiscono per l'ordine in cui si pre-
  sentano gli elementi distinti e la posizione che occupano gli elementi ripetut"""
  denom = 1
  if sum(k) <= n:
    for x in k:
      denom = denom * factorial(x)
    perm = factorial(n) / denom
    return perm
  else:
    PSG.popup_error("Non possono esserci più elementi ripetuti degli elementi che compongono l'insieme stesso", title="")

def calculate_simple_comb(n:int, k:int):
  """Le combinazioni semplici di n elementi distinti di classe k (con 0 < k <= n)
  sono tutti i gruppi di k elementi [scelti all'interno di n] che differsicono per
  almeno un elemento ma non per l'ordine"""
  if k <= n:
    comb = factorial(n) / (factorial(k) * factorial(n-k))
    return comb
  else:
    PSG.popup_error("La classe dell'insieme non può essere maggiore del numero di elementi che compongono l'insieme stesso", title="")

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

  window = PSG.Window("Calcolo combinatorio", default_view)

  while True:
    
    try:
      
      events, values = window.read()

      if events == PSG.WIN_CLOSED: break

      #SIMPLE DISP
      if events == "-SIMPLE-DISP-CALCULATE-":

        n = int(values["-SIMPLE-DISP-LENGHTINPUT-"])
        k = int(values["-SIMPLE-DISP-CLASSINPUT-"])

        global simple_disp
        simple_disp = calculate_simple_disp(n, k)

        window["-SIMPLE-DISP-OUTPUT-"].update(len(simple_disp))
        window["-SIMPLE-DISP-LIST-"].update(disabled=False)
      
      if events == "-SIMPLE-DISP-LIST-":
        PSG.popup_scrolled(simple_disp, title="Permutazioni")
      
      #REPEATED DISP
      if events == "-REPEATED-DISP-CALCULATE-":

        n = int(values["-REPEATED-DISP-LENGHTINPUT-"])
        k = int(values["-REPEATED-DISP-CLASSINPUT-"])

        global rep_disp
        rep_disp = calculate_repeated_disp(n, k)

        window["-REPEATED-DISP-OUTPUT-"].update(len(rep_disp))
        window["-REPEATED-DISP-LIST-"].update(disabled=False)

      if events == "-REPEATED-DISP-LIST-":
        PSG.popup_scrolled(rep_disp, title="Permutazioni")

      #SIMPLE PERM
      if events == "-SIMPLE-PERM-CALCULATE-":
        n = int(values["-SIMPLE-PERM-LENGHTINPUT-"])

        global simple_perm
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

      if events == "-VIEW-SOURCE-":
        webbrowser.open_new_tab("https://github.com/Piombacciaio/Calcolo-Combinatorio")

    except ValueError:
      PSG.popup_error("Inserire valori numerici validi per la classe e il numero di oggetti", title="")

    except Exception as e:
      PSG.popup_error("Inviare il Traceback ad Andrea Piombo per assistenza", e, title="")

if __name__ == '__main__': main()