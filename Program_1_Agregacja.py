import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import numpy as np

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
droga_col = 'stempel- droga - Sp [mm]'

# Konwersja kolumn na liczby
df[skok_col] = pd.to_numeric(df[skok_col], errors='coerce')
df[sila_col] = pd.to_numeric(df[sila_col], errors='coerce')
df[droga_col] = pd.to_numeric(df[droga_col], errors='coerce')
df = df.dropna(subset=[skok_col, sila_col, droga_col])

# Filtr skoków 94–96 mm
df_filtered = df[(df[skok_col] >= 94) & (df[skok_col] <= 97)].copy()

if df_filtered.empty:
    print("Nie ma danych w zakresie skoków 94–97.")
    exit()

# Znalezienie najmniejszej siły w całym pliku
min_force = df[sila_col].min()

# Dodanie kolumny z obliczoną siłą
df_filtered['obliczone stempel-siła - Fp [kN]'] = df_filtered[sila_col] - min_force

# Sortowanie po skoku
df_filtered = df_filtered[[droga_col, sila_col, 'obliczone stempel-siła - Fp [kN]', skok_col]].sort_values(by=skok_col)

# Dodanie kolumny czasu – każda próbka to kolejna wielokrotność 1/1612,903226
dt = 1 / 1612.903226
df_filtered['Czas - t [s]'] = [(i + 1) * dt for i in range(len(df_filtered))]

# --- OBLICZENIE PRACY ---
# Konwersja: siła [kN] → [N], droga [mm] → [m]
force_N = df_filtered['obliczone stempel-siła - Fp [kN]'].values * 1000
distance_m = df_filtered[droga_col].values / 1000

# Suma modułów każdego małego trapezu
work_segments = np.abs((force_N[:-1] + force_N[1:]) / 2 * (distance_m[1:] - distance_m[:-1]))
work_J = np.sum(work_segments)
work_kJ = work_J / 1000

print(f"💡 Obliczona praca: {work_J:.4f} J ({work_kJ:.4f} kJ)")

# --- ZAPIS DO EXCELA ---
# Przygotowanie danych do zapisu
output_file = asksaveasfilename(
    title="Zapisz wynik jako Excel",
    defaultextension=".xlsx",
    filetypes=[("Excel files", "*.xlsx")]
)
if not output_file:
    print("Nie wybrano pliku wyjściowego.")
    exit()

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_filtered.to_excel(writer, index=False, startcol=0, startrow=0)
    # Zapis praca w F1–F2
    df_summary = pd.DataFrame({
        'F': ['Praca [J]', round(work_J, 4)]
    })
    df_summary.to_excel(writer, index=False, header=False, startcol=5, startrow=0)

print(f"✅ Wynik zapisano do: {output_file}")
