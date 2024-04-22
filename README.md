# mxcppfy
A Python script to convert STM32CubeIDE .c files to .cpp files, preserving code written between USER CODE blocks.

## Requirements
Requires Python 3.x

## Usage
Either drop `mxcppfy.py` into your desired folder and run it with just the filename as the argument, or include the absolute path of the directory.
```
python3 mxcppfy.py <filename> [directory]
```
### Arguments
| Name      | Description |
| ----------- | ----------- |
| `<filename>`      | The name of the files you want to merge. Required. |
| `[directory]`  | (Optional) Absolute path of the directory where the .c and .cpp files are located. **Default: .** |

## Upcoming updates
- Better argument testing and general robustness improvements
- Docker container (Compose)
- A web frontend?
