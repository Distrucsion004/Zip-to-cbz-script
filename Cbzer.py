'''All that's left to do is turn the archiver and the rename into functions and
make them aplicable to whatever folder I put them in.
 Also put them both into one file and export the script.'''
import os
import shutil as st

def archiver(Folder):
    entries = os.listdir(Folder)
    for entry in entries:
        if ('.py'not in entry):
            file = entry
            st.make_archive(file , 'zip',Folder+'\\'+ file)

def renamer(folder):
    cond = '.zip'
    entries = os.listdir(folder)
    for entry in entries:
        if (cond in entry):
            new = entry.replace('.zip', '.cbz')
            os.rename(entry, new)


directory = os.getcwd()
archiver(directory)
renamer(directory)

