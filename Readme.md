***TO Do in Beta 0.3:***

- MAPA:
    - mapa GUI
    - automatyczna mapa

***Done in Beta 0.3:***

- GUI:
    - predefiniowanie pola roboczego

***TO Do in Beta 0.4:***

- wstempna obsluga zumu ?

***TO Do in Beta next:***

- Refactor!!!!!!!!

- Debug Mode

- Manipulator:
    - wait for manipulator to reach goll befor displeing ROI's (bardziej skompliowane niz powino byc z uwagi na TCIP)

-Bug fixing and searching

-GUI
  -wybur zoomu

**ogulne zalozenia**

- pole robocze (zadefiniowane nie uzywane)
- Natwny zoom tylko na nim dziala oznaczanie roi
- Mapa autpmatyczna dla majacych ses zlzoen zuma i pola roboczego

**Znalezione bledy do rozwionzania**

- No ROIs in labels
  - May be due to no proper manipulator connection
- TCIP Erore - cos bylo robione na sieci


**Refactor Rules**
- one class per file
- one class +optional one inherit file per folder
- one main file per main class
- main class list:
  - Main Window
  - Main Vue
    - Camera
  - ROI
    - ROI Label
  - Manipulator
  - Map