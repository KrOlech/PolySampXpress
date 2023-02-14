***TO Do in Beta 0.4:***

- in code To DO resolve
- alternatywne metody tworzenia ROI:
  - klikanie Naroznikow
  - oznacanie pktow
  - Stworznie siatki pktow mesz radom full radom

- zerowanie na pkcie znajdowanym softwrowo
  - na start pkt wybierany recznie.

- test in code manual

- Map 2.0
  - alternative hiden option for curent map

***Done in Beta 0.4:***
- Map 2.0
  - simple map

***TO Do in Beta next:***

- logGenie
- Debug Mode

- zoom handling
  - Kamera ma ciagły zoom jakies pressety

- obsluga fokusu
  - autofokus
  
- Silniki krokowe brak encodingu musi byc po strnie softweru

- Bug fixing and searching

- Automatic tests + installation proces
- 
- Main class Refactor

- resolution for Map

- Using CUDA for imiage resize (oneFX for radeon and so one)

- Utiliti Strig Using Python "Static"

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
  - after refactor do not work even with TCIP
- Work fild window need 2 clicks if not conectet by TCIP
- Strange movement of ROIS after manipulator ordered to move Video in bugs
- map 1.1 may not work full ok 

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
