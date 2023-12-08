import sys
import json

if(len(sys.argv) != 2):
    print("Invalid number of parameters. Usage: script_import.py {path_to_rom}")
    quit()

target_rom = sys.argv[1]

input_script_list = r".\script_list.json"
with open(input_script_list, "r") as scripts:
    script_data = json.load(scripts)

script_index = 0
for script in script_data['scripts']:

    script_title = script['title']
    script_offset = int(script['offset'], 16)

    input_script_file = r".\src\scripts\\" + "{:03d}".format(script_index) + " - " + script_title + ".txt"
    script_index = script_index + 1

    with open(target_rom, "r+b") as rom:
        rom.seek(script_offset)
        with open(input_script_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                command_bytes = bytes.fromhex(line.split("|")[0])
                rom.write(command_bytes)

