set rom_version=1.1
set rom_name=PMD_BRT_Cutsceneless_v%rom_version%.nds
set temp_rom_name=temp.nds

IF NOT EXIST rom_output mkdir rom_output
del /q rom_output
copy rom_source\source.nds rom_output\%temp_rom_name%
python .\script_import.py .\rom_output\%temp_rom_name%
armips\armips.exe src\asm\pre-boss-cutscenes.asm
ren rom_output\%temp_rom_name% %rom_name%