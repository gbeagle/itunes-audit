'''
The basics:
    1) Run a depth first search on the library. pretty-print it in a way that I do not despise.
    2) Print out the number of files in the bottom folder.
    3) Print the highest track number in the bottom folder.
    4) If those two numbers don't match, mark the folder for auditing and output the potential number of missing tracks.

    Optional enhancement: since we're trawling track numbers anyway, find the first missing track number and return that.

    False positive case: folders where I've only purchased a subset of songs off of the album.
    There's no programmatic way to know what I was thinking at time of purchase, so we'll leave those for visual inspection.
    I have to touch any folder with a potentially missing track anyway, and these should only make up a small fraction.

    '''

# MAJOR TODO
# evaluate path.walk() as an alternative to the relatively naive DFS here

from pathlib import Path
from mutagen.mp4 import MP4

YOUR_BASE_PATH_HERE = Path("basepath.txt").read_text().strip()
# TODO: very quick and dirty anonymization. put in function later.
#TODO: raw strings best practice y/n?


#################
# FUNCTION LAND #
#################

# TODO refactor this to a helper class when it is not just duct tape.

def dfs_folder_traverse(folder):
    child_folders = [child_folder for child_folder in folder.iterdir() if child_folder.is_dir()]
    child_music_files = [file for file in folder.iterdir() if file.suffix in ['.mp3', '.m4a']]

    for f in child_folders:
        print(f'down one level to {f.name}')
        dfs_folder_traverse(f)
    else:
        if child_music_files:
            num_files = len(child_music_files)
            print(f"{num_files} files in {folder.name}...")

            for file in child_music_files:
                m4a_metadata = MP4(file)
                print(m4a_metadata.tags['sonm'])

        return



############
# mainland #
############

base = Path(YOUR_BASE_PATH_HERE)


dfs_folder_traverse(base)
