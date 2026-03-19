# 📊 Automatyzacja analizy danych procesu I-ECAP (Python)

Projekt badawczo-analityczny zrealizowany w ramach pracy magisterskiej. Skrypty w języku Python służące do masowego przetwarzania, filtracji i analizy wielkich zbiorów danych sensorycznych pochodzących z wyciskarki promieniowej ISx.

## 🎯 Opis problemu
Proces I-ECAP (Incremental Equal Channel Angular Pressing) generuje potężne zbiory danych z czujników maszyny. Sygnały rejestrowane w środowisku LabVIEW (siła i przemieszczenie) potrafią wygenerować **ponad 4 miliony rekordów na jedną próbkę**. 
Ręczna obróbka takich plików w programie MS Excel była niemożliwa ze względu na ogromną objętość danych oraz wysoki poziom zaszumienia sygnału.

## 🚀 Rozwiązanie
Stworzyłem autorskie oprogramowanie w Pythonie, które w pełni automatyzuje proces analityczny. Algorytm samodzielnie importuje surowe dane, odszumia sygnał, identyfikuje fazy ruchu maszyny i generuje gotowe raporty z obliczeniami.

### Główne funkcjonalności algorytmu:
* **Czyszczenie i filtracja sygnału:** Zastosowanie algorytmu średniej kroczącej (moving average) za pomocą biblioteki NumPy w celu eliminacji szumów z czujników.
* **Identyfikacja cykli:** Automatyczne wykrywanie punktów zwrotnych (szczytów i dolin) w celu precyzyjnego oddzielenia poszczególnych cykli roboczych od jałowych.
* **Zaawansowane obliczenia numeryczne:** * Wyznaczanie siły maksymalnej ($F_{max}$) oraz siły średniej ($F_{sr}$).
  * Obliczanie wykonanej pracy mechanicznej ($W$) poprzez **całkowanie numeryczne** (metoda Simpsona z biblioteki `SciPy`).
* **Automatyczny eksport:** Generowanie gotowych raportów w formacie `.xlsx` oraz wykresów analitycznych.

## 🛠 Technologie i Biblioteki
* **Język:** Python (IDE: PyCharm)
* **Analiza danych:** `Pandas`, `NumPy`
* **Obliczenia naukowe:** `SciPy` (moduł `scipy.integrate`)
* **Wizualizacja:** `Matplotlib`
* **Akwizycja danych:** National Instruments LabVIEW (źródło pomiarów)

## 📈 Skala projektu badawczego
W rzeczywistości, podczas badań do pracy dyplomowej, moje oprogramowanie posłużyło do masowej analizy potężnej bazy danych. Skrypt bezbłędnie i automatycznie przetworzył:
* **67** plików z potężnymi danymi surowymi
* **61** zrzutów z systemu LabVIEW
* Wygenerował łącznie **116** gotowych plików wynikowych MS Excel.

> **Uwaga:** Ze względu na gigantyczny rozmiar oryginalnych plików pomiarowych, w tym repozytorium zamieszczam wyłącznie **wycinek demonstracyjny** kodu oraz przykładowe próbki danych, potwierdzające poprawne działanie algorytmu.

## 📁 Zawartość repozytorium (Wersja Demo)
* `Program_1_Agregacja.py` - skrypt analizujący do agregacji danych procesowych i wyznaczania statystyk siłowych.
* `Program_2_Obliczanie_Pracy.py` - skrypt do szczegółowej analizy stabilnych cykli i numerycznego obliczania pracy odkształcenia.
* `1cu 1p_skok_49-62.txt` - próbka surowego sygnału z maszyny.
* `1cu1p_skok_1-191 F.xlsx`, `1cu1p_skok_1-191 W.xlsx` - wygenerowane automatycznie raporty.
* `2cu 1p_skok_1-49 jpg.jpg` - widok panelu akwizycji danych na maszynie.

## 📷 Wizualizacja działania

*(W tym miejscu dodaj swoje zrzuty ekranu na GitHubie)*

### Wykres maksymalnej siły w kolejnych cyklach pracy
<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/1685d304-b7f7-4cd9-9d7b-b64b900d5558" />

### Przebieg siły i przemieszczeń w czasie (dla skoków 94–96)
<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/875196ed-d1b9-4701-a61b-84b793c48844" />

### Wykres pracy (dla skoków 94–96)
<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/855ef4c7-084b-4ac5-b2c1-348d8d7ecfe2" />

### Zbiorczy wykres siły maksymalnej dla czwartego przejścia (Schemat C – 180°)
<img width="1385" height="674" alt="image" src="https://github.com/user-attachments/assets/779e0f11-801f-47c9-9aeb-381ee64a400e" />

---
*Projekt zrealizowany w ramach pracy magisterskiej na Politechnice Warszawskiej (Kierunek: Automatyzacja i Robotyzacja Procesów Produkcyjnych).*
