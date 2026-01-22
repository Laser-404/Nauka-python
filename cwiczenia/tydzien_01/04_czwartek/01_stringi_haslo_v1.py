print("=== Password ===")
password = input("Podaj hasło: ").strip()

is_long_enough = len(password) >= 8
has_upper = any(ch.isupper() for ch in password)
has_space = " " in password

if is_long_enough == False:
    print("Hasło jest za krótkie.")
else:
    if has_upper == False:
        print("Hasło musi zawierać przynajmniej jedną wielką literę.")
    else:
        if has_space:
            print("Hasło nie może zawierać spacji.")
        else:
            print("Hasło jest poprawne.")