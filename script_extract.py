import json
import binascii

MAX_LOOP_SIZE = 3000

def getCommandName(command_id):
    match command_id:
        case "02":
            return "WARPTO_DIRECT"
        case "04":
            return "WARPTO_MAP"
        case "0c":
            return "LOAD_MAP"
        case "0d":
            return "CALL"
        case "2d":
            return "LOAD"
        case "2e":
            return "KAOMADO"
        case "30":
            return "MSG_EXIT"
        case "32":
            return "MSG_PLAIN"
        case "33":
            return "MSG_THOUGHT"
        case "34":
            return "MSG_SPEECH"
        case "35":
            return "MSG_READING"
        case "39":
            return "MSG_FLOATY"
        case "3c":
            return "REWARD"
        case "3d":
            return "RENAME"
        case "3e":
            return "RENAME_TEAM"
        case "42":
            return "STOP_SONG"
        case "44":
            return "PLAY_SONG"
        case "45":
            return "FADE_IN"
        case "48":
            return "FADE_OUT"
        case "4c":
            return "PLAY_SOUND"
        case "4d":
            return "STOP_SOUND"
        case "54":
            return "SET_ANIM"
        case "58":
            return "WARP_TO"
        case "62":
            return "MOVE_NOROTATE"
        case "68":
            return "CHANGE_Z"
        case "6a":
            return "MOVE"
        case "6b":
            return "MOVETO_GRID"
        case "7a":
            return "MOVETO_DIRECT"
        case "86":
            return "MOVE_CAMERA_TO_WAYPOINT"
        case "8b":
            return "FACE_DIR"
        case "91":
            return "ROTATE"
        case "c0":
            return "LOAD_EVENT_FLAG"
        case "c1":
            return "LOAD_EVENT_FLAG_CALC"
        case "c2":
            return "LOAD_TWO_EVENT_FLAGS_CALC"
        case "c3":
            return "CHOOSE_RANDOM_VALUE"
        case "c4":
            return "LOAD_FIRST_EVENT_FLAG_BYTE"
        case "c5":
            return "LOAD_SECOND_EVENT_FLAG_BYTE"
        case "cc":
            return "TEST_EQUALS"
        case "cd":
            return "TEST_CONDITION"
        case "ce":
            return "TEST_CONDITION_CUSTOM"
        case "cf":
            return "VARY_MSG"
        case "d0":
            return "CASE"
        case "d1":
            return "DEFAULT"
        case "d5":
            return "QUESTION"
        case "d8":
            return "VARY_QUESTION"
        case "d9":
            return "OPTION"
        case "db":
            return "SLEEP"
        case "e2":
            return "WAIT_SEND"
        case "e3":
            return "WAIT_FLAG"
        case "e4":
            return "SET_FLAG"
        case "e7":
            return "GOTO_LABEL"
        case "e8":
            return "EXECUTE"
        case "e9":
            return "MSG_END"
        case "ee":
            return "RETURN"
        case "ef":
            return "END"
        case "f0":
            return "CLOSE"
        case "f1":
            return "REMOVE"
        case "f4":
            return "LABEL"
        case "f6":
            return "START_THREAD"
        case _:
            return "UNKNOWN_" + command_id
        


input_rom = r".\rom_source\source.nds"

input_script_list = r".\script_list.json"
with open(input_script_list, "r") as scripts:
    script_data = json.load(scripts)

script_index = 0
for script in script_data['scripts']:

    script_title = script['title']
    script_offset = int(script['offset'], 16)

    output_script_file = r".\script_extract_output\\" + "{:03d}".format(script_index) + " - " + script_title + ".txt"
    script_index = script_index + 1

    with open(input_rom, "rb") as f:
        with open(output_script_file, "w") as o:
            f.seek(script_offset)
            
            i = 0
            while(i < MAX_LOOP_SIZE): # setting a maximum loop size just in case for whatever reason a script-ending command isn't reached
                command_id = str(binascii.hexlify(f.read(1)))[2:-1]
                command_name = getCommandName(command_id)
                f.seek(-1, 1)   # go one byte back to prepare for reading the entire command
                command_binary_data = str(binascii.hexlify(f.read(16)))[2:-1]
                o.write(command_binary_data + "| " + command_name + "\n" )
                if (command_id == "ef" or command_id == "f0" or command_id == "f1"):
                    break
                i = i + 1