def aufgabe_100_teile_in_abschnitte(text: str, breite: int) -> list[str]:
    """Zerlege einen Text in Abschnitte fester Breite."""

    return [text[i:i + breite] for i in range(0, len(text), breite)]


print(aufgabe_100_teile_in_abschnitte("Hallo, Welt!", 2))
