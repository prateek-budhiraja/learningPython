import random
import os

pth='/home/prateek/Pictures/college'

os.chdir(pth)

filename=random.choice(os.listdir())
os.system('xdg-open '+filename)
