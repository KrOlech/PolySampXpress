***TO Do in Beta 0.3:***

- MAPA:
    - mapa GUI
    - automatyczna mapa

- Manipulator:
    - wait for manipulator to reach goll befor displeing ROI's

- ***Done in Beta 0.3:***

- GUI:
    - predefiniowanie pola roboczego

***TO Do in Beta 0.4:***

- ?

***TO Do in Beta next:***

- Refactor!!!!!!!!

- Debug Mode

- zoom handling

-Bug fixing and searching

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
- TCIP Error - Someone wos messing with internet


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