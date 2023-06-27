

import os

def file_walker(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file != "__init__.py" and file[-4:] != ".pyc" and file[-3:] == ".py":
                file_paths.append(file_path)
    return file_paths

# Usage example:
folder_path = r"C:\Users\Auris 5600\Magisterka\src"
paths = file_walker(folder_path)


with open("fileLocations.txt","w") as f:
    for path in paths:
        path = path[path.find("src"):]
        row = r"\newpage\lstinputlisting[language=Python, caption={Slider osi Z.},label={lst:pmv_example}, mathescape=true]{" + path + "}\n"
        f.write(row)


