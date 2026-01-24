# W1D3 (Piątek) — Pętla for + sprawdzanie hasła bez any()

## Najważniejsze
- `for ch in password:` przechodzi po haśle znak po znaku.
- Flaga = zmienna True/False, np.:
  - `has_digit = False` → jeśli znajdę cyfrę: `has_digit = True`
  - `has_upper = False` → jeśli znajdę dużą literę: `has_upper = True`
- Najpierw zbieram info w pętli, potem robię `if/elif/else` i wypisuję wynik raz.

## Funkcje / operatory
- `ch.isdigit()` → czy znak to cyfra
- `ch.isupper()` → czy znak to duża litera
- `len(password)` → długość hasła
- `" " in password` → czy hasło ma spację
- `not has_space` → brak spacji

## Typowy błąd
Nie drukować “ma/nie ma” w pętli dla każdego znaku — decyzja ma być po pętli.
