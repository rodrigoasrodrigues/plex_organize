'''
Creates hard links for subtitles as .por (Portuguese) for files .pob (Brazilian Portuguese) 
Plex does not understand .pob files as Portuguese subtitles, so we need to create links for them.
Bazarr does not understand .por as pt-br so we keep .pob for it
to save space, we create hard links
'''

import os

def move(file, matching_file):
    # move file
    try:
        os.rename(file, matching_file)
        print(f'Moved file: {file} to {matching_file}')
    except Exception as e:
        print(f'Error moving file: {e}')
        

def main():
    # Get current directory
    current_dir = '/volume2/Media'

    # Get all files in current directory and subdirectories
    files_pob = []
    files_pt_br = []
    for root, dirs, filenames in os.walk(current_dir):
        for filename in filenames:
            if filename.endswith('.pob.srt'):
                files_pob.append(os.path.join(root, filename))
            elif filename.endswith('.pt-br.srt'):
                files_pt_br.append(os.path.join(root, filename))
    

    # Create symbolic links for subtitles
    for file in files_pob:
        matching_file = file.replace('.pob', '.pt-br')
        if matching_file not in files_pt_br:
            move(file, matching_file)


if __name__ == '__main__':
    main()