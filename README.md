# Fake IoT Device Simulator

Ovaj projekat generise lazne podatke sa IoT uredjaja za potrebe simulacije i analiza.
Podaci se mogu cuvati u CSV/JSON formatima ili slati preko MQTT protokola.

## Struktura projekta
- **src/**: Sadrzi sve Python skripte.
-**data/**: Folder za generisane podatke.
**config/**: Konfiguracioni fajl sa postavkama projekta.

## Kako pokrenuti projekat
1. Instaliraj zavisnosti:
```
pip install -r requirements.txt
```
2. Pokreni glavni fajl:
```
python main.py
```