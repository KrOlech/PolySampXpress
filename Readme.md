![Tests](https://github.com/KrOlech/Magisterka/actions/workflows/python-app.yml/badge.svg)

***TO Do in Beta 0.6:***
- Main class Refactor
  - Utiliti Strig Using Python "Static"

- position off the cursor on main screen

- optymalisation

- Labels in save file

- Rois in labels (fix)

- Manipulator not resiving comands from interfejs corectli after centring or randomli during usage

***Done in Beta 0.6:***

- Center On ROI


***TO Do in Beta next:***

- test in code

- Debug Mode

- zoom handling
  - Kamera ma ciagły zoom jakies pressety

- obsluga fokusu
  - autofokus

- Using CUDA for imiage resize (oneFX for radeon and so on)

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
- Manipulator not resiving comands from interfejs corectli after centring or randomli during usage