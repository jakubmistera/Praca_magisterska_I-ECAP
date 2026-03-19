Temat
Analiza parametrów technologicznych procesu I-ECAP

Opis problemu:
Proces I-ECAP generuje potężne zbiory danych z czujników maszyny ISx (ponad 4 mln rekordów na próbkę). Ręczna obróbka w Excelu była niemożliwa ze względu na szum i objętość.

Rozwiązanie:
Stworzyłem skrypt w Pythonie, który automatycznie importuje dane, filtruje sygnał, identyfikuje pojedyncze cykle robocze maszyny
i oblicza kluczowe parametry: siłę maksymalną, siłę średnią oraz całkuje numerycznie pracę mechaniczną.

Technologie: Python, Pandas, NumPy, Matplotlib.

W rzeczywistości, podczas badań do pracy dyplomowej, moje oprogramowanie posłużyło do masowej analizy znacznie większej bazy danych:
automatycznie przetworzyło 67 plików z danymi surowymi 
oraz 61 zrzutów z LabVIEW,
generując łącznie 116 plików wynikowych w formacie MS Excel. 
Ze względu na ogromny rozmiar plików (ponad 4 miliony rekordów na próbkę), na GitHubie zamieszczam wyłącznie wycinek demonstracyjny potwierdzający poprawne działanie algorytmu.

Screenshots:

<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/1685d304-b7f7-4cd9-9d7b-b64b900d5558" />

<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/875196ed-d1b9-4701-a61b-84b793c48844" />

<img width="947" height="558" alt="image" src="https://github.com/user-attachments/assets/855ef4c7-084b-4ac5-b2c1-348d8d7ecfe2" />
