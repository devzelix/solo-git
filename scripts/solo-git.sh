#!/bin/bash

VENV_PATH="$HOME/.solo-git/.venv"

if [ ! -d "$VENV_PATH" ]
then
    echo -e "\n¡El entorno virtual no se encuentra en $VENV_PATH!\n"
    exit 1
fi

source "$VENV_PATH/bin/activate"
python3 "$HOME/.solo-git/src/solo_git.py" "$@"
deactivate