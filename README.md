# Anti-Duplicator

A script for finding duplicate files in the current directory, as well as in subfolders. At start it is necessary to transfer the path to the checked directory as a parameter.
The program displays the name of the duplicates, their size and the directories in which they are located.
If there are no duplicates in this directory, the program displays the corresponding notification

# Quickstart

Example of running the script at Linux with Python 3.5:
```bash
python3 duplicates.py /home/oeananas/3_bars
duplicates of file: bars.json of size: 446364 bites in directories: ['/home/oeananas/3_bars', '/home/oeananas/3_bars/dup']
duplicates of file: bars.py of size: 1969 bites in directories: ['/home/oeananas/3_bars', '/home/oeananas/3_bars/dup']
duplicates of file: HEAD of size: 189 bites in directories: ['/home/oeananas/3_bars/.git/logs', '/home/oeananas/3_bars/.git/logs/refs/remotes/origin']
```
```bash
python3 duplicates.py /home/oeananas/11_duplicates
duplicates of file: HEAD of size: 196 bites in directories: ['/home/oeananas/11_duplicates/.git/logs', '/home/oeananas/11_duplicates/.git/logs/refs/remotes/origin']
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
