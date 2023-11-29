# PMD-RescueTeam-Cutsceneless-Hack
A Hack of Pokémon Mystery Dungeon: Blue Rescue Team that removes cutscenes while keeping gameplay as intact as possible.

[WIP]

## Files in this repo
- The ./rom_source folder should the RRT rom and the BRT rom to be present under the names source.gba and source.nds respectively. Most of the other scripts will use either of the two roms, or both.
- **script_list.json** contains the list of scripts in the BRT rom. A title and offset is specified for each entry. The title will be used for the file names for each script, while the offsets is where each script is expected to be extracted from and compiled to.
- **extract_scripts.bat** calls **script_extract.py**. It takes script_list.json and extracts each script into a ./script_extract_output folder. This folder will contain the unmodified scripts as they appear in the BRT rom.
- **make.bat** calls **script_import.py**. It takes each script in the ./src folder and it will place it in the BRT rom, according to the offsets and script order specified in script_list.json. The resulting rom will be in the ./rom_output folder.
These are all essentially glorified hex editing tools made ad hoc for this specific project. When importing a script into the BRT rom, the raw hex data on the left of a script is blindly taken and put directly in the rom. This isn't a very robust system :)
