import configparser
from configparser import ConfigParser

parser = ConfigParser()
confdict = {}
ini_file='/Users/svenkata/Projects/Parsing-Workshop/exercises/ini_files/example.ini'

modified_ini = False
with open(ini_file, 'r') as f:
    lines = f.readlines()
    if not lines[0].startswith('[') and not lines[0].startswith("#"):
        modified_ini=True

if modified_ini:
    with open(ini_file, 'r+') as f:
        data = f.read()
        f.seek(0)
        f.write("[_]\n" + data)

parser.read(ini_file)
for section in parser.sections():
        confdict.update({section: dict(parser.items(section))})

print(confdict)
