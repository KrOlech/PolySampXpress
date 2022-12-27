***TO Do in Beta 0.3:***

- MAPA:
    - automatyczna mapa
    - Refactor
- ***Done in Beta 0.3:***
- MAPA:
    - mapa GUI
- GUI:
    - predefiniowanie pola roboczego
- Manipulator:
    - wait for manipulator to reach goll befor displeing ROI's(hard coded wait

***TO Do in Beta 0.4:***

- ?

***TO Do in Beta next:***

- Debug Mode

- zoom handling

-Bug fixing and searching

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
- TCIP Error - Someone wos messing with internet
- Work fild window need 2 clicks if not conectet by TCIP


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
