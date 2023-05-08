![Tests](https://github.com/KrOlech/Magisterka/actions/workflows/python-app.yml/badge.svg)

***TO Do in Beta 0.5:***


***Done in Beta 0.5:***
- Full migration to JsonReadClass
- auto Calibration Mode (Need testing)
- Balans Bieli
- logGenie
- file with camera configuration
- new Manipulator
- botom info bar with current manipulator position
- configure work Feald
- manipulator selection interfejs
- manipulatr GoTo and HomeAxis interfejs
- Automatic tests start no proper tests implemented
- end mesage info uses difrent taskbar
- Zapis Roi
- auto mapwindow closing after program power off

***TO Do in Beta next:***

- test in code

- Debug Mode

- zoom handling
  - Kamera ma ciagły zoom jakies pressety

- obsluga fokusu
  - autofokus

- Bug fixing and searching

- Main class Refactor

- resolution for Map

- Using CUDA for imiage resize (oneFX for radeon and so on)

- Utiliti Strig Using Python "Static"

- position off the cursor on main screen

- auto wykrywanie portu com manipulatora

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
  - after refactor do not work even with TCIP
- Strange movement of ROIS after manipulator ordered to move Video in bugs
- Strage Map creation need difrent offset than the roi
- Last ROI stays during Map Creation (propabli residum from last created ROI)
- dialog window not corectli resize (unse but mey need in future)