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

YOUR_BASE_PATH_HERE = Path("basepath.txt").read_text().strip()
# TODO: very quick and dirty anonymization. put in function later.
#TODO: raw strings best practice y/n?


#################
# FUNCTION LAND #
#################

# TODO refactor this to a helper class when it is not just duct tape.

def dfs_folder_traverse(folder):
    child_folders = [f for f in folder.iterdir() if f.is_dir()]

    for f in child_folders:
        print(f'down one level to {f.name}')
        dfs_folder_traverse(f)
    else:
        numfiles = len([file.name for file in folder.iterdir() if file.is_file()])
        print(f"{numfiles} files in {folder.name} here...")
        return



############
# mainland #
############

base = Path(YOUR_BASE_PATH_HERE)


dfs_folder_traverse(base)
