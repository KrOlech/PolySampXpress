***TO Do in Beta 0.3:***

- MAPA:
    - automatyczna mapa


- ***Done in Beta 0.3:***
  
  - Refactor
  - MAPA:
      - mapa GUI
  - GUI:
      - predefiniowanie pola roboczego
  - Manipulator:
      - wait for manipulator to reach goll befor displeing ROI's(hard coded wait

***TO Do in Beta 0.4:***

- logGenie
- Debug Mode
- in code To DO resolve

***TO Do in Beta next:***

- zoom handling
  - Kamera ma ciagły zoom jakies pressety
- obsluga fokusu
  - autofokus
-Silniki krokowe brak encodingu musi byc po strnie softweru

- alternatywne metody tworzenia ROI klikanie Naroznikow
- oznacanie pktow
- Stworznie siatki pktow mesz radom full radom

- zerowanie na pkcie znajdowanym softwrowo

-Bug fixing and searching

-Automatic tests + installation proces

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
  - after refactor do not work even with TCIP
- TCIP Error - Someone wos messing with internet
- Work fild window need 2 clicks if not conectet by TCIP
- Strange movement of ROIS after manipulator ordered to move Video in bugs
- Two map butons on main window

**Refactor Rules**
- one class per file
- one class + optional one inherit file per folder
- one main file per main class
- main class list:
  - Main Window
  - Main Vue
    - Camera
  - ROI
    - ROI Label
  - Manipulator
  - Map
