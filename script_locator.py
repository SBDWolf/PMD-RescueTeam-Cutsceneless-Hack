# given an address to a RRT script location, try to find the same script in the BRT rom

import sys
import binascii

input_brt_rom = r".\rom_source\source.nds"
input_rrt_rom = r".\rom_source\source.gba"

if(len(sys.argv) != 2):
    print("Invalid number of parameters. Usage: script_locator.py {RRT script address}")
    quit()

script_offset = int(sys.argv[1], 16)
   
try:
    with open(input_brt_rom, "rb") as brt_rom:
        brt_romcontents = brt_rom.read()
except IOError:
    print("Could not read the specified file.")
    quit()

with open(input_rrt_rom, "rb") as rrt_rom:
    rrt_rom.seek(script_offset + 16)
    print("Searching for script...")
    search_hex_sequence = b''
    while(True):
        command = rrt_rom.read(16)
        # don't use any command that could contain a pointer, as well as any script-ending command
        #0x32 = MSG_PLAIN, 0x33 = MSG_THOUGHT, 0x34 = MSG_SPEECH, 0x35 = MSG_READING, 0x39 = MSG_FLOATY, 0xd0 = CASE, 0xd1 = DEFAULT, 0xef = END, 0xf0 = CLOSE, 0xf1 = REMOVE
        if(command[0] == 0x32 or command[0] == 0x33 or command[0] == 0x34 or command[0] == 0x35 or command[0] == 0x39 or command[0] == 0xd0 or command[0] == 0xd1 or command[0] == 0xef or command[0] == 0xf0 or command[0] == 0xf1):
            break
        else:
            search_hex_sequence = search_hex_sequence + command

    found_script_offsets = []
    current_found_script_offset = 0
    while(True):
        current_found_script_offset = brt_romcontents.find(search_hex_sequence, current_found_script_offset + 16)
        found_script_offsets.append(current_found_script_offset)
        if current_found_script_offset == -1:
            break

    if found_script_offsets[0] != -1:
        print("Found potential scripts in the BRT rom. List of offsets: ")
        for element in found_script_offsets:
            if (element != -1):
                print(hex(element - 16))
    else:
        print("Couldn't find script in the BRT rom")
        


