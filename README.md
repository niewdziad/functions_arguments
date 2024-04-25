# functions_arguments
#
def gen_mul_table(width=10, height=10, sep_width=3, print_header=False, print_footer=True):
Tutaj definiujemy funkcję gen_mul_table z pięcioma argumentami: width, height, sep_width, print_header, print_footer. Domyślne wartości są ustawione na 10, 10, 3, False i True odpowiednio.
Sprawdzenie warunku dla nagłówka:

if print_header:
    header = f"Multiplication Table {width} x {height}\n"
else:
    header = ""
Sprawdzamy, czy użytkownik chce wydrukować nagłówek (print_header). Jeśli tak, tworzymy nagłówek zawierający informacje o rozmiarach tabeli (width x height). W przeciwnym razie nagłówek pozostaje pusty.
Inicjalizacja tabeli:

table = header
Inicjalizujemy zmienną table wartością nagłówka, która jest pusta lub zawiera informacje o tabeli.
Pętla dla wierszy:

for i in range(1, height + 1):
Rozpoczynamy pętlę for, iterującą po numerach wierszy od 1 do height.
Pętla dla kolumn:

row = ""
for j in range(1, width + 1):
Wewnątrz pętli dla każdego wiersza, rozpoczynamy pętlę for, iterującą po numerach kolumn od 1 do width.
Obliczenie iloczynu:

cell = str(i * j)
Obliczamy iloczyn i * j, aby uzyskać wartość komórki w tabeli mnożenia.
Formatowanie wartości komórki:

cell = cell.ljust(sep_width)
Formatujemy wartość komórki tak, aby miała określoną szerokość (sep_width), zgodnie z wyznaczonym miejscem w kolumnie.
Dodanie wartości komórki do wiersza:

row += cell
Dodajemy sformatowaną wartość komórki do aktualnego wiersza row.
Dodanie nowej linii po każdej kolumnie:

row += " "
Dodajemy spację po wartości komórki, aby oddzielić kolumny.
Dodanie wiersza do tabeli:

table += row.strip() + "\n"
Po zakończeniu pętli dla każdej kolumny, usuwamy dodatkową spację z prawej strony wiersza (strip()) i dodajemy nową linię.
Dodanie stopki:

if print_footer:
    table += "-" * (width * (sep_width + 1)) + "\n"
Jeśli użytkownik chce wydrukować stopkę (print_footer), tworzymy linię stopki, która składa się z - powtórzonych width * (sep_width + 1) razy.
Zwrócenie gotowej tabeli:

return table
Zwracamy gotową tabelę mnożenia.
Testowanie funkcji:

print(gen_mul_table(5, 5, sep_width=3, print_footer=False))
Testujemy funkcję, wywołując ją z określonymi argumentami i wyświetlamy wynik.