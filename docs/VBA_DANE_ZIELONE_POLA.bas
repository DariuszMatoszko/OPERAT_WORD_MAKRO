Attribute VB_Name = "VBA_DANE_ZIELONE_POLA"
Option Explicit

' Wstaw kod zdarzeń do ThisDocument

Private Const KOLOR_SZARY As Long = RGB(217, 217, 217)
Private Const KOLOR_ZIELONY As Long = RGB(0, 176, 80)

' --- Zdarzenia do umieszczenia w ThisDocument ---
Public Sub Document_Open()
    ResetujKolumneNazwNaSzaro
End Sub

Public Sub Document_ContentChange(ByVal Range As Range)
    PodswietlZmianeWKolumnieWartosci Range
End Sub

' --- Logika wspólna ---
Public Sub ResetujKolumneNazwNaSzaro()
    Dim tbl As Table
    Dim i As Long

    If ActiveDocument.Tables.Count = 0 Then Exit Sub
    Set tbl = ActiveDocument.Tables(1)
    If tbl.Columns.Count < 2 Then Exit Sub

    For i = 1 To tbl.Rows.Count
        tbl.Cell(i, 1).Shading.BackgroundPatternColor = KOLOR_SZARY
    Next i
End Sub

Public Sub PodswietlZmianeWKolumnieWartosci(ByVal ChangedRange As Range)
    Dim tbl As Table
    Dim komorka As Cell

    If ActiveDocument.Tables.Count = 0 Then Exit Sub
    Set tbl = ActiveDocument.Tables(1)
    If tbl.Columns.Count < 2 Then Exit Sub

    If ChangedRange.Tables.Count = 0 Then Exit Sub
    If Not (ChangedRange.Tables(1) Is tbl) Then Exit Sub

    For Each komorka In ChangedRange.Cells
        If komorka.ColumnIndex = 2 Then
            tbl.Cell(komorka.RowIndex, 1).Shading.BackgroundPatternColor = KOLOR_ZIELONY
        End If
    Next komorka
End Sub
