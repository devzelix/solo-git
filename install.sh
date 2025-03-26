#!/bin/bash

if ! grep -q "https://github.com/devzelix/solo-git.git" .git/config 2>/dev/null
then
    echo -e "\n¡Debes ejecutar este script desde el directorio raíz del repositorio!\n"
    exit 1
fi
if [ ! -f "requeriments.txt" ]
then
    echo -e "\n¡No se encontro el archivo 'requeriments.txt'!, clone nuevamente el repositorio.\n"
    exit 1
fi

if [ ! -d ".venv" ]
then
    echo -e "\nCreando entorno virtual..."
    python3 -m venv .venv
fi
source .venv/bin/activate
echo -e "\nInstalando dependencias..."
pip install -r requeriments.txt 1>/dev/null
deactivate

echo -e "\nInstalando el comando 'solo-git'...\n"
mkdir ~/.solo-git
cp -r ./.venv ~/.solo-git/
cp -r ./src ~/.solo-git/
cp -r ./scripts ~/.solo-git/
chmod +x ~/.solo-git/scripts/solo-git.sh
sudo ln -sf ~/.solo-git/scripts/solo-git.sh /usr/local/bin/solo-git
echo -e "\n¡Instalación completada! Ahora puedes usar el comando 'solo-git' desde cualquier lugar.\n"