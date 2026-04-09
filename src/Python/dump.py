from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling

d = JsonHandling.readFileRow(r"C:\Users\Zenbook\Documents\27-3-2026\P2\all.json")

cp = {}

for k, v in d.items():
    cp[k] = {}
    cp[k]['name'] = v['name']
    cp[k]['Fokus'] = v['Fokus']
    cp[k]['Fokus um'] = v['Fokus']*2.5

JsonHandling.simpleSaveFile(r"C:\Users\Zenbook\Documents\27-3-2026\P2\okrojony.json",cp)