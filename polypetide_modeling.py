# Created by Zichen Yang on 11th sep
# Verion 1
# Verion 0.0 Protype
# Version 1.0 we fix some know issue
# Version 1.1 fix generated file can't open without pymol

from pyrosetta import *
from pyrosetta import init
from pyrosetta.io import pose_from_sequence
from pyrosetta.rosetta.protocols.relax import FastRelax
import os

str = 'b\nEND'
str = str.encode()
init('-ex1 -ex2')
scorefxn = pyrosetta.create_score_function('ref2015')
fastrelax = FastRelax()
fastrelax.set_scorefxn(scorefxn)
fastrelax.set_default_movemap()

isExists = os.path.exists('./Output')
if not isExists:
    path = './Output'
    os.mkdir(path)
    print("core.io: {0} output: Output Path has been created")
else:
    print("core.io: {0} output: Output Path arelady exists")

print("core.io: {0} Where is you seq file?")
input = input()
with open(input, 'r+', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        pose = pose_from_sequence(line)
        fastrelax.apply(pose)
        pose = pose.dump_pdb("./Output/%s.pdb" % line)
        with open("./Output/%s.pdb" % line, 'rb+') as File:
            AlL_line = File.readlines()
            last_line = line[-1]
            for i in range(len(last_line)+2):
                File.seek(-1, os.SEEK_END)
                File.truncate()
            File = File.write(str)
        print("core.io: {0} output: %s.pdb created successfully " % line)
