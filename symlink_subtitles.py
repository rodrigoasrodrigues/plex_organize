'''
Creates symbolic links for subtitles as .por (Portuguese) for files .pob (Brazilian Portuguese) 
Plex does not understand .pob files as Portuguese subtitles, so we need to create symbolic links for them.
'''

import os

def create_symlink(file_path):
    # Create symbolic link
    try:
        link_name = file_path.replace('.pob', '.por')
        os.symlink(file_path, link_name)
        print(f'Symlink created: {link_name}')
    except FileExistsError:
        print(f'File already exists: {file_path.replace(".pob", ".por")}')
    except Exception as e:
        print(f'Error creating symlink: {e}')

def main():
    # Get current directory
    current_dir = '/volume2/Media'

    # Get all files in current directory and subdirectories
    files_pob = []
    files_por = []
    for root, dirs, filenames in os.walk(current_dir):
        for filename in filenames:
            if filename.endswith('.pob.srt'):
                files_pob.append(os.path.join(root, filename))
            elif filename.endswith('.por.srt'):
                files_por.append(os.path.join(root, filename))
    

    # Create symbolic links for subtitles
    for file in files_pob:
        matching_file = file.replace('.pob', '.por')
        if matching_file not in files_por:
            create_symlink(file)


if __name__ == '__main__':
    main()