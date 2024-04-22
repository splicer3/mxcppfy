import os
import sys


def merge_files(filename_, directory_='.'):
    # Construct file paths
    cpp_file = os.path.join(directory_, filename_ + '.cpp')
    cpp_bak_file = os.path.join(directory_, filename_ + '.cpp.bak')
    c_file = os.path.join(directory_, filename_ + '.c')

    # Rename .cpp to .cpp.bak
    os.rename(cpp_file, cpp_bak_file)

    # Create new .cpp file
    with open(c_file, 'r') as c_file_obj, open(cpp_bak_file, 'r') as cpp_bak_file_obj, open(cpp_file,
                                                                                            'w') as cpp_file_obj:
        # Flag to set when we're either copying from the .cpp or we're ignoring the .c file
        copying_cpp = False
        for line in c_file_obj:
            # If we reach the start of a USER CODE block we need to switch to the .cpp file
            if '/* USER CODE BEGIN' in line:
                # Capturing the USER CODE block identifier
                block_name = line.split('/* USER CODE BEGIN ')[1].split(' */')[0]
                for cpp_bak_line in cpp_bak_file_obj:
                    # Checking the block name is essential to avoid duplicates
                    if f'/* USER CODE BEGIN {block_name}' in cpp_bak_line:
                        # The .cpp copy officially starts, right from the next two lines
                        copying_cpp = True
                    if copying_cpp:
                        cpp_file_obj.write(cpp_bak_line)
                        # Note that the break happens AFTER writing the USER CODE END to the file
                        if f'/* USER CODE END {block_name}' in cpp_bak_line:
                            break
                # We can skip lines until we evenntually get to the right block name
                pass
            elif copying_cpp:
                # If we reach the end of a USER CODE section we can resume copying from the .c file
                if f'/* USER CODE END' in line:
                    copying_cpp = False
            else:
                # Standard copy from .c
                cpp_file_obj.write(line)


# Command line arguments check
if len(sys.argv) < 2:
    print("Usage: python merge_files.py filename [directory]")
    sys.exit(1)

filename = sys.argv[1]
# Defaults to current wd
directory = sys.argv[2] if len(sys.argv) > 2 else '.'

merge_files(filename, directory)

print("Files merged!")
