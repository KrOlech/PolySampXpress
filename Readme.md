![Tests](https://github.com/KrOlech/Magisterka/actions/workflows/python-app.yml/badge.svg)
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

**Unsolved Errors**

- No ROIs in labels
  - May be due to no proper manipulator connection
  - Works ok with TCIP manipulator
  - after refactor do not work even with TCIP
- Strange movement of ROIS after manipulator ordered to move Video in bugs
- dialog window not corectli resize (unse but mey need in future)