#!/bin/bash
#
#SDF2CSV


echo 'Initializing Application...'

#Installing prerequisites
echo 'Installing the must-have prerequisites...'
echo 'Upgrading pip...'
pip install --upgrade pip
echo 'Installing flask'
pip install flask
echo 'Installing RDkit'
python -m pip install rdkit-pypi
echo 'Installing pandas'
pip install pandas

#obtaining path to program
script_path="$(dirname -- $0)"
if [ -h $0 ]; then
	link="$(readlink $0)"
	script_path="$(dirname -- $link)"
fi

#starting the program
cd "$script_path"
python app.py

#echo "$script_path"
#SDF2CSV_HOME=$script_path

#opening web application
echo 'Starting web application now'
xdg-open http://127.0.0.1:5000/

