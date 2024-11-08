"""
zmodyfikuj make_shirt() z zad. 8.3 tak, aby:
- domyślnie były to duze koszulki,
- domyślnie były to koszulki z nadrukim "I love Python"
- zrób jedną koszulkę L z domyślnym tekstem,
- zrób jedną koszulkę M z domyślnym tekstem,
- zrób jedną koszulkę w dowolnym rozmiarzze z innym tekstem.
"""

print("\nWYBIERZ ROZMIAR I TEKST NA SWOJEJ KOSZULCE:\n")


def main():
    """
    program kolekcjonuje zamówienia na koszulki do wykonania
    :size: to wielkość zamówionej koszulki
    :text: to porządany przez klienta nadruk
    """

    size, text = take_parameters()

    make_shirt(size, text)


def take_parameters():
    """
    zbiera parametry koszulki do zamówienia
    :size: rozmiar koszulki
    :text: napis na koszulce
    :accept: to pytanie czy zamówienie zgodne z oczekiwaniem
    """

    while True:

        size = input("\npodaj rozmiar: ")
        rozmiary = ["S", "M", "L", "XL"]

        if size.upper() not in rozmiary:

            print("dostępne rozmiary to S, M, L, XL.")
            continue

        else:
            break

    text = input("\na teraz, podaj tekst: ")

    # added >>> :

    print(
        f"\nZamówiłeś t-shirt w rozmiarze: {size.upper()}," f'\nZ napisem: "{text}".\n'
    )

    while True:

        accept = input("Czy Twoje zamówienie się zgadza? ")
        answers = ["y", "n"]

        if accept.lower() in answers:

            if accept == "y":
                break

            # TODO: dlaczego dwa razy pyta czy zamówienie się zgadza?

            else:
                take_parameters()

        else:
            print('dostępne odpowiedzi to "y" dla TAK oraz "n" dla NIE :)')
            # continue

    # added <<<

    return size, text


def make_shirt(size, text):
    """wyświetla zamówienie do wykonania"""

    print(
        f"\nProdukujemy t-shirt w rozmiarze: {size.upper()},"
        f'\nZ napisem: "{text}".\n'
    )


def is_order_ok():
    """
    to byłaby funkcja, która robi to samo,
    co `while` w `take_parameters()`
    tj. pyta czy zamówienie jest zgodne z oczekiwaniami klienta
    """
    return


if __name__ == "__main__":
    main()
