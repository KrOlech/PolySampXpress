***TO Do in Beta 0.5:***

- zerowanie na pkcie znajdowanym softwrowo
   - na start pkt wybierany recznie.
- manipulator selection interfejs

- Full migration to JsonReadClass

***Done in Beta 0.5:***
- auto Calibration Mode (Need testing)
- Balans Bieli
- logGenie
- file with camera configuration
- new Manipulator
- botom info bar with current manipulator position
- configure work Feald

***TO Do in Beta next:***

- test in code manual

- Debug Mode

- zoom handling
  - Kamera ma ciagły zoom jakies pressety

- obsluga fokusu
  - autofokus

- Bug fixing and searching

- Automatic tests + installation proces

- Main class Refactor

- resolution for Map

- Using CUDA for imiage resize (oneFX for radeon and so on)

- Utiliti Strig Using Python "Static"

- position on the sample on main screen + cursor position

- auto mapwindow coling after program power off

- auto wykrywanie portu com manipulatora

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
  - after refactor do not work even with TCIP
- Strange movement of ROIS after manipulator ordered to move Video in bugs
- No ROI creation working after calibration