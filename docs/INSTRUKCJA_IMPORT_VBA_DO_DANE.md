# Import VBA do templates\DANE.docm

1. Otwórz `templates\DANE.docm` w Microsoft Word.
2. Wciśnij `ALT+F11`, aby otworzyć edytor VBA.
3. W panelu projektu wybierz `Normal`/`DANE.docm`, aby go uaktywnić.
4. Wybierz **File > Import File...** i wskaż `docs\VBA_DANE_ZIELONE_POLA.bas`.
5. Otwórz obiekt **ThisDocument** w projekcie `DANE.docm`.
6. Skopiuj procedury `Document_Open` oraz `Document_ContentChange` z zaimportowanego modułu do **ThisDocument** (tam muszą się znajdować zdarzenia).
7. Pozostałe procedury (`ResetujKolumneNazwNaSzaro`, `PodswietlZmianeWKolumnieWartosci`) mogą zostać w module.
8. Zapisz dokument jako `DANE.docm`.
9. Zamknij i ponownie otwórz dokument, aby sprawdzić reset i podświetlanie.
