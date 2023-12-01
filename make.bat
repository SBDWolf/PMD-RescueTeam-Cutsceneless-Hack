set rom_version=1.0
set rom_name=PMD_BRT_Cutsceneless_v%rom_version%.nds

IF NOT EXIST rom_output mkdir rom_output
del /q rom_output
copy rom_source\source.nds rom_output\%rom_name%
python .\script_import.py .\rom_output\%rom_name%