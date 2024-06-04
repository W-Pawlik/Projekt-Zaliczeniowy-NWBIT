# Projekt-Zaliczeniowy-NWBIT
Projekt zaliczeniowy przedmiotu Narzędzia w Branży IT- Program do konwersji formató plików napisany w języku Python.
Obsługuje konwersję między formatami XML, JSON i YAML.

## Funkcje
* Program automatycznie rozpoznaje formaty plików wejściowych i wyjściowych na podstawie rozszerzeń plików.
* Zapewnia walidację składni JSON, YAML i XML podczas wczytywania i zapisywania.
* Automatycznie buduje plik wykonywalny `.exe` za pomocą GitHub Actions.

## Użycie
Sposób użycia: 
```
main.exe pathFile1.x pathFile2.y
```
gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).

## Zależności
Projekt wymaga takich pakietów Pythona jak:
* json
* pyyaml
* xmltodict
* xml.dom.minidom
* xml.etree.ElementTree
* pyinstaller

## GitHub Actions
Projekt jest skonfigurowany z wykorzystaniem GitHub Actions do automatycznego budowania pliku '.exe'
Workflow jest zdefiniowany w pliku .github/workflows/build.yml i zawiera następujące kroki:
* Pobierz repozytorium.
* Skonfiguruj środowisko Pythona.
* Zainstaluj zależności.
* Uruchom skrypt installResources.ps1.
* Zbuduj plik wykonywalny za pomocą pyinstaller.
* Prześlij zbudowany plik .exe jako artefakt.

## Autor
Wojciech Pawlik
