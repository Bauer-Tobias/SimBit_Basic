# SimBit_Basic

This project provides a virtual microbit simulator that can be started from the console.
It is based on the official micro:bit simulator found at https://github.com/microbit-foundation/micropython-microbit-v2-simulator.

Developed with python 3.11.1

Before use, install a new venv in the project's directory by calling the following commands in cmd:
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt

Starting the server and opening the simulator window in cmd or Powershell:
.\venv\Scripts\python.exe microVSim.py {absolute path to code file}


German Instructions on use in GuiPy:
Wekrzeuge->Werkzeuge->Werkzeugkonfiguration->Hinzufügen
	Name: Nach Wahl
	Anwendung: {Ordner dieses Projekts}\venv\Scripts\python.exe
	Parameter: microVSim.py $[ActiveDoc]
	Arbeitspfad: {Ordner dieses Projekts}
	Kontext: Aktive Pythondatei
	Befehlszeile: Keine versteckte Befehlszeile
