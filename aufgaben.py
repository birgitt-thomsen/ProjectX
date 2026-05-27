"""100 Basis-Aufgaben für die Studierenden.

Jede Funktion ist nur als Stub angelegt und soll von euch implementiert
werden. Nutzt Docstring und Parameternamen als Leitplanke. Schreibt sauberen,
getesteten Code und haltet euch an PEP 8.
"""

from typing import Any, Optional


# Gruppe: patricznr1, ANY1-hub
def aufgabe_001_spiegle_text(text: str) -> str:
    """Gib den Text rückwärts zurück."""
    return text[::-1]


# Gruppe: patricznr1, ANY1-hub
def aufgabe_002_zaehle_vokale(text: str) -> int:
    """Zähle die Anzahl der Vokale im Text (a, e, i, o, u)."""
    vokale = "aeiouAEIOU"
    return sum(1 for char in text if char in vokale)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_003_ist_palindrom(text: str) -> bool:
    """Prüfe, ob der Text ein Palindrom ist (Groß/Klein ignorieren)."""
    clean_text = text.lower()
    return clean_text == clean_text[::-1]


# Gruppe: patricznr1, ANY1-hub
def aufgabe_004_zu_grossbuchstaben(text: str) -> str:
    """Wandle alle Zeichen in Großbuchstaben um."""
    return text.upper()


# Gruppe: patricznr1, ANY1-hub
def aufgabe_005_zu_kleinbuchstaben(text: str) -> str:
    """Wandle alle Zeichen in Kleinbuchstaben um."""
    return text.lower()


# Gruppe: patricznr1, ANY1-hub
def aufgabe_006_capitalize_saetze(text: str) -> str:
    """Setze den ersten Buchstaben jedes Satzes auf Großbuchstaben."""
    if not text:
        return text
    
    result = []
    capitalize_next = True
    
    for char in text:
        if char in '.!?':
            result.append(char)
            capitalize_next = True
        elif char.isalpha() and capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
            if not char.isspace():
                capitalize_next = False
    
    return ''.join(result)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_007_ersetze_zeichen(text: str, alt: str, neu: str) -> str:
    """Ersetze alle Vorkommen von alt durch neu in text."""
    return text.replace(alt, neu)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_008_zaehle_wort(text: str, wort: str) -> int:
    """Zähle, wie oft wort im Text vorkommt (wortgenau)."""
    worte = text.split()
    return worte.count(wort)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_009_kuerze_text(text: str, limit: int) -> str:
    """Schneide den Text nach limit Zeichen ab und füge '...' an, falls nötig."""
    if len(text) <= limit:
        return text
    return text[:limit] + '...'


# Gruppe: patricznr1, ANY1-hub
def aufgabe_010_teile_worte(text: str) -> list[str]:
    """Zerlege einen Satz in Wörter, getrennt nach Leerzeichen."""
    return text.split()


# Gruppe: patricznr1, ANY1-hub
def aufgabe_011_verbinde_worte(worte: list[str], trenner: str = ", ") -> str:
    """Verbinde Wörter mit dem angegebenen Trenner zu einem String."""
    return trenner.join(worte)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_012_laengstes_wort(worte: list[str]) -> Optional[str]:
    """Finde das längste Wort in der Liste, None bei leerer Liste."""
    if not worte:
        return None
    return max(worte, key=len)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_013_zaehle_ziffern(text: str) -> int:
    """Zähle alle Zeichen im Text, die Ziffern sind."""
    return sum(1 for char in text if char.isdigit())


# Gruppe: patricznr1, ANY1-hub
def aufgabe_014_entferne_whitespace(text: str) -> str:
    """Entferne alle Whitespaces (Leerzeichen, Tabs, Zeilenumbrüche)."""
    return ''.join(char for char in text if not char.isspace())


# Gruppe: patricznr1, ANY1-hub
def aufgabe_015_slugify(text: str) -> str:
    """Erzeuge einen einfachen Slug: Kleinbuchstaben, '-' statt Leerzeichen."""
    return text.lower().replace(' ', '-')


# Gruppe: patricznr1, ANY1-hub
def aufgabe_016_summe_liste(zahlen: list[int]) -> int:
    """Summiere alle Zahlen in der Liste."""
    return sum(zahlen)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_017_mittelwert(zahlen: list[float]) -> float:
    """Berechne den arithmetischen Mittelwert der Liste."""
    if not zahlen:
        return 0.0
    return sum(zahlen) / len(zahlen)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_018_max_wert(zahlen: list[int]) -> Optional[int]:
    """Gib den größten Wert zurück, None bei leerer Liste."""
    if not zahlen:
        return None
    return max(zahlen)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_019_min_wert(zahlen: list[int]) -> Optional[int]:
    """Gib den kleinsten Wert zurück, None bei leerer Liste."""
    if not zahlen:
        return None
    return min(zahlen)


# Gruppe: patricznr1, ANY1-hub
def aufgabe_020_sortiere_aufsteigend(zahlen: list[int]) -> list[int]:
    """Gib eine neue Liste mit aufsteigend sortierten Zahlen zurück."""
    return sorted(zahlen)


# Gruppe: it-student, birgitt-thomsen
def aufgabe_021_sortiere_absteigend(zahlen: list[int]) -> list[int]:
    """Gib eine neue Liste mit absteigend sortierten Zahlen zurück."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_022_filter_gerade(zahlen: list[int]) -> list[int]:
    """Filtere alle geraden Zahlen aus der Liste."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_023_filter_ungerade(zahlen: list[int]) -> list[int]:
    """Filtere alle ungeraden Zahlen aus der Liste."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_024_quadrate(zahlen: list[int]) -> list[int]:
    """Gib eine Liste mit Quadraten aller Zahlen zurück."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_025_unique_werte(zahlen: list[int]) -> list[int]:
    """Entferne Duplikate, erhalte die erste Reihenfolge."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_026_finde_index(werte: list[str], wert: str) -> int:
    """Finde den Index von wert, -1 wenn nicht vorhanden."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_027_teilliste(werte: list[int], start: int, ende: int) -> list[
    int]:
    """Gib eine Teilliste von start (inkl.) bis ende (exkl.) zurück."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_028_zaehle_vorkommen(werte: list[str], gesucht: str) -> int:
    """Zähle, wie oft gesucht in der Liste vorkommt."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_029_drehe_liste(werte: list[Any]) -> list[Any]:
    """Drehe die Reihenfolge der Liste um."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_030_flatten(liste_von_listen: list[list[int]]) -> list[int]:
    """Führe eine verschachtelte Liste zu einer flachen Liste zusammen."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_031_merge_lists(a: list[int], b: list[int]) -> list[int]:
    """Mische zwei Listen abwechselnd (falls ungleich lang, Rest anhängen)."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_032_remove_none(werte: list[Optional[int]]) -> list[int]:
    """Entferne alle None-Werte aus der Liste."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_033_chunk_list(werte: list[int], groesse: int) -> list[list[int]]:
    """Zerlege die Liste in Blöcke der Länge groesse."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_034_rotate_left(werte: list[int], schritte: int) -> list[int]:
    """Rotiert die Liste um schritte nach links."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_035_split_even_odd(werte: list[int]) -> tuple[
    list[int], list[int]]:
    """Trenne die Liste in gerade und ungerade Zahlen auf."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_036_dict_keys_sort(data: dict[str, int]) -> list[str]:
    """Gib sortierte Schlüssel eines Dicts zurück."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_037_dict_values_sum(data: dict[str, int]) -> int:
    """Summiere alle Werte in einem Dict."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_038_invert_dict(data: dict[str, str]) -> dict[str, str]:
    """Tausche Schlüssel und Werte (Fehler bei Duplikaten klären)."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_039_merge_dicts(a: dict[str, Any], b: dict[str, Any]) -> dict[
    str, Any]:
    """Führe zwei Dicts zusammen, b überschreibt a bei Konflikten."""
    pass


# Gruppe: it-student, birgitt-thomsen
def aufgabe_040_count_letters(text: str) -> dict[str, int]:
    """Zähle, wie oft jeder Buchstabe im Text vorkommt (case-insensitive)."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_041_group_by_length(worte: list[str]) -> dict[int, list[str]]:
    """Gruppiere Wörter nach ihrer Länge."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_042_word_frequency(worte: list[str]) -> dict[str, int]:
    """Erstelle eine Häufigkeitstabelle für Wörter."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_043_dict_without_keys(
        data: dict[str, int], keys: list[str]
) -> dict[str, int]:
    """Gib ein neues Dict ohne die angegebenen Schlüssel zurück."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_044_find_key_by_value(data: dict[str, int], value: int) -> \
Optional[str]:
    """Finde den ersten Schlüssel, dessen Wert value entspricht."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_045_safe_get(data: dict[str, Any], path: list[str]) -> Optional[
    Any]:
    """Greife sicher auf verschachtelte Dicts zu, None wenn Pfad fehlt."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_046_set_union(a: set[int], b: set[int]) -> set[int]:
    """Vereinigung zweier Sets zurückgeben."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_047_set_intersection(a: set[int], b: set[int]) -> set[int]:
    """Schnittmenge zweier Sets zurückgeben."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_048_set_difference(a: set[int], b: set[int]) -> set[int]:
    """Differenzmenge a - b zurückgeben."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_049_remove_duplicates_preserve_order(werte: list[str]) -> list[
    str]:
    """Entferne doppelte Einträge aus einer Stringliste, Reihenfolge behalten."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_050_has_duplicates(werte: list[Any]) -> bool:
    """Prüfe, ob die Liste doppelte Elemente enthält."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_051_sum_range(n: int) -> int:
    """Berechne die Summe der Zahlen von 1 bis n (inklusive)."""
    sum = 0
    for num in range(1, n + 1):
        sum += num
    return sum


# Gruppe: Appeyron, esterplaza
def aufgabe_052_factorial(n: int) -> int:
    """Berechne n! iterativ oder rekursiv."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_053_fibonacci(n: int) -> list[int]:
    """Gib eine Liste der ersten n Fibonacci-Zahlen zurück."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_054_ist_primzahl(n: int) -> bool:
    """Prüfe, ob n eine Primzahl ist."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_055_primzahlen_bis(limit: int) -> list[int]:
    """Gib alle Primzahlen bis inklusive limit zurück."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_056_ggt(a: int, b: int) -> int:
    """Berechne den größten gemeinsamen Teiler."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_057_kgv(a: int, b: int) -> int:
    """Berechne das kleinste gemeinsame Vielfache."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_058_durchschnitt_gewichtet(
        werte: list[float], gewichte: list[float]
) -> float:
    """Berechne den gewichteten Mittelwert, gleiche Länge vorausgesetzt."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_059_anzahl_true(flags: list[bool]) -> int:
    """Zähle die True-Werte in einer Bool-Liste."""
    pass


# Gruppe: Appeyron, esterplaza
def aufgabe_060_binaer_zu_int(bits: str) -> int:
    """Wandle einen Binärstring in eine Ganzzahl um."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_061_int_zu_binaer(n: int) -> str:
    """Wandle eine Ganzzahl in einen Binärstring ohne Präfix um."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_062_zahlenformat(n: float, nachkommastellen: int) -> str:
    """Formatiere eine Zahl mit fester Anzahl Nachkommastellen."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_063_clamp(wert: float, minimum: float, maximum: float) -> float:
    """Begrenze wert auf den Bereich [minimum, maximum]."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_064_normiere(werte: list[float]) -> list[float]:
    """Skaliere Werte in den Bereich 0..1 (min-max-Normierung)."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_065_skaliere(werte: list[float], faktor: float) -> list[float]:
    """Multipliziere jeden Wert mit faktor."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_066_moving_average(werte: list[float], fenster: int) -> list[
    float]:
    """Berechne gleitende Durchschnitte mit Fenstergröße fenster."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_067_linear_map(
        wert: float, alt_min: float, alt_max: float, neu_min: float,
        neu_max: float
) -> float:
    """Mappe wert linear vom Bereich alt_min..alt_max nach neu_min..neu_max."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_068_countdown(n: int) -> list[int]:
    """Gib eine Liste von n bis 0 zurück."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_069_repeat_text(text: str, anzahl: int) -> str:
    """Wiederhole einen Text anzahl-mal hintereinander."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_070_summenliste(werte: list[int]) -> list[int]:
    """Gib die kumulative Summe der Werte zurück."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_071_zip_to_dict(keys: list[str], values: list[int]) -> dict[
    str, int]:
    """Baue ein Dict aus Schlüsseln und Werten gleicher Länge."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_072_swap_keys_values(data: dict[str, str]) -> dict[str, str]:
    """Tausche Keys und Values, Fehler bei Duplikaten klären."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_073_filter_dict_by_value(
        data: dict[str, int], minimum: int
) -> dict[str, int]:
    """Filtere Einträge, deren Wert mindestens minimum ist."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_074_werte_aufaddieren(datensaetze: list[dict[str, int]]) -> dict[
    str, int]:
    """Summiere Werte gleicher Schlüssel über mehrere Dicts."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_075_dict_diff(a: dict[str, int], b: dict[str, int]) -> dict[
    str, str]:
    """Vergleiche a und b: 'gleich', 'nur_a', 'nur_b', 'anders' pro Schlüssel."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_076_sortiere_tupel_nach_index(
        eintraege: list[tuple[Any, ...]], index: int = 0
) -> list[tuple[Any, ...]]:
    """Sortiere eine Liste von Tupeln nach dem angegebenen Index."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_077_transponiere_matrix(matrix: list[list[int]]) -> list[
    list[int]]:
    """Transponiere eine rechteckige Matrix."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_078_diagonalsumme(matrix: list[list[int]]) -> int:
    """Berechne die Summe der Hauptdiagonale einer quadratischen Matrix."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_079_spaltenmittel(matrix: list[list[float]]) -> list[float]:
    """Berechne den Mittelwert jeder Spalte einer Matrix."""
    pass


# Gruppe: markus-niessen, kollodergrosse
def aufgabe_080_matrix_multiply(
        a: list[list[int]], b: list[list[int]]
) -> list[list[int]]:
    """Multipliziere zwei Matrizen (gültige Dimensionen vorausgesetzt)."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_081_filter_worte_laenge(worte: list[str], minimum: int) -> list[
    str]:
    """Filtere Wörter, deren Länge mindestens minimum beträgt."""
    return [wort for wort in worte if len(wort) >= minimum]


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_082_join_ohne_letztes(worte: list[str]) -> str:
    """Verbinde Wörter mit Komma, ersetze das letzte Komma durch ' und '."""
    if not worte:
        return ""
    if len(worte) == 1:
        return worte[0]

    return ", ".join(worte[:-1]) + " und " + worte[-1]


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_083_count_characters_ignore_case(text: str) -> dict[str, int]:
    """Zähle Zeichenhäufigkeiten ohne zwischen Groß/Klein zu unterscheiden."""
    ergebnis = {}
    for zeichen in text.lower():
        ergebnis[zeichen] = ergebnis.get(zeichen, 0) + 1
    return ergebnis


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_084_vokale_entfernen(text: str) -> str:
    """Entferne alle Vokale aus dem Text."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_085_erste_wiederholung(werte: list[Any]) -> Optional[Any]:
    """Finde das erste Element, das mehr als einmal vorkommt."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_086_ist_sortiert(werte: list[int]) -> bool:
    """Prüfe, ob die Liste nicht-absteigend sortiert ist."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_087_bubble_sort(werte: list[int]) -> list[int]:
    """Sortiere die Liste mit Bubble-Sort und gib eine neue Liste zurück."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_088_binary_search(werte: list[int], ziel: int) -> int:
    """Finde den Index von ziel in sortierter Liste, -1 falls nicht vorhanden."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_089_two_sum(werte: list[int], ziel: int) -> Optional[
    tuple[int, int]]:
    """Finde zwei Indizes, deren Werte zusammen ziel ergeben."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_090_anagramm(text_a: str, text_b: str) -> bool:
    """Prüfe, ob zwei Strings Anagramme sind."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_091_zeichenhaeufigkeit_top(
        text: str, limit: int = 3
) -> list[tuple[str, int]]:
    """Gib die häufigsten Zeichen mitsamt Häufigkeit zurück."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_092_tokenisiere_satz(text: str) -> list[str]:
    """Tokenisiere einen Satz grob nach Leer- und Satzzeichen."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_093_title_case(text: str) -> str:
    """Setze jeden Wortanfang auf Großbuchstaben (Title Case)."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_094_count_substring(text: str, substring: str) -> int:
    """Zähle nicht überlappende Vorkommen eines Substrings."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_095_remove_stopwords(worte: list[str], stopwords: list[str]) -> \
list[str]:
    """Entferne Stopwörter aus einer Wortliste (case-insensitive)."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_096_ersetzungen_kette(text: str, mapping: dict[str, str]) -> str:
    """Führe mehrere Ersetzungen gemäß mapping nacheinander aus."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_097_validiere_email(text: str) -> bool:
    """Prüfe grob, ob ein String wie eine E-Mail-Adresse aussieht."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_098_extract_domain(url: str) -> str:
    """Extrahiere die Domain aus einer URL (ohne Schema/Path/Query)."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_099_parse_kv(text: str) -> dict[str, str]:
    """Parse einen Text wie 'a=1;b=2' in ein Dict."""
    pass


# Gruppe: Airdinsh-Ai, NiBerni, ahmadalshouly
def aufgabe_100_teile_in_abschnitte(text: str, breite: int) -> list[str]:
    """Zerlege einen Text in Abschnitte fester Breite."""
    pass
