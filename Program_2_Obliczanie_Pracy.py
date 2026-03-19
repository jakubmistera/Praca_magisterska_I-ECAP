import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw()

# Wybór pliku wejściowego
input_file = askopenfilename(title="Wybierz plik z danymi", filetypes=[("All files", "*.*")])
if not input_file:
    print("Nie wybrano pliku.")
    exit()

# Wczytanie danych
try:
    df = pd.read_csv(input_file, sep='\t', header=1, decimal=',', engine='python', encoding='cp1250')
except Exception as e:
    print("Błąd przy wczytywaniu pliku:", e)
    exit()

# Nazwy kolumn
skok_col = 'popychacz-droga - Sfs [mm]'
sila_col = 'stempel-siła - Fp [kN]'

# Konwersja kolumn na liczby
df[skok_col] = pd.to_numeric(df[skok_col], errors='coerce')
df[sila_col] = pd.to_numeric(df[sila_col], errors='coerce')
df = df.dropna(subset=[skok_col, sila_col])

# Filtrowanie danych (0–191 mm)
df = df[(df[skok_col] >= 0) & (df[skok_col] <= 192)]

if df.empty:
    print("Nie ma danych w tym zakresie skoków.")
    exit()

# Znalezienie najmniejszej siły w całym pliku
min_force = df[sila_col].min()

# Grupowanie po zaokrąglonym skoku i wybór maksymalnej siły w każdej grupie
df['skok_bin'] = df[skok_col].round()
df_max = df.loc[df.groupby('skok_bin')[sila_col].idxmax()].copy()
df_max = df_max[[skok_col, sila_col]].sort_values(by=skok_col)

# Dodanie kolumny z obliczoną siłą (odjęcie minimalnej wartości)
df_max['obliczone stempel-siła - Fp [kN]'] = df_max[sila_col] - min_force

# Dodanie kolumny czasu (kolejne liczby całkowite)
df_max['Numer cyklu - n'] = range(len(df_max))

# ---- OBLICZENIA DODATKOWE ----

# Fmax i czas jego wystąpienia
Fmax = df_max['obliczone stempel-siła - Fp [kN]'].max()
czas_Fmax = df_max.loc[df_max['obliczone stempel-siła - Fp [kN]'].idxmax(), 'Numer cyklu - n']

# Średnia siła dla wartości > 36 kN
df_srednie = df_max[df_max['obliczone stempel-siła - Fp [kN]'] > 37]
if not df_srednie.empty:
    Fsr = df_srednie['obliczone stempel-siła - Fp [kN]'].mean()
    czas_Fsr_start = df_srednie.iloc[0]['Numer cyklu - n']
else:
    Fsr = 0
    czas_Fsr_start = None

# ---- ZAPIS DO EXCELA ----

# Stworzenie dodatkowych wierszy dla kolumn E i F
df_summary = pd.DataFrame({
    'E': ['Fmax [kN]', Fmax, 'podczas cyklu', czas_Fmax],
    'F': ['Fśr [kN]', Fsr, 'od cyklu', czas_Fsr_start]
})

# Zapis z użyciem ExcelWriter, żeby dopisać dane obok
output_file = asksaveasfilename(
    title="Zapisz wynik jako Excel",
    defaultextension=".xlsx",
    filetypes=[("Excel files", "*.xlsx")]
)
if not output_file:
    print("Nie wybrano pliku wyjściowego.")
    exit()

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_max.to_excel(writer, index=False, startcol=0, startrow=0)  # dane główne (A–D)
    df_summary.to_excel(writer, index=False, header=False, startcol=4, startrow=0)  # dane E1–F4

print(f"✅ Wynik zapisano do: {output_file}")
print(f"📈 Fmax = {Fmax:.2f} kN podczas cyklu {czas_Fmax}")
print(f"📊 Fśr = {Fsr:.2f} kN od cyklu {czas_Fsr_start}")
