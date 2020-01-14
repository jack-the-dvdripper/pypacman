#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:47:14 2020

@author: dracula
"""
from pypacman import pacman
import subprocess

pc=pacman()

USER="dracula"
GROUP=["wheel","audio","video"]
SHELL="bash"

if not pc.is_installed(SHELL):
    pc.install(['SHELL'])

# now create the user
try:
    subprocess.run(['useradd','-m','-g','users','-s', SHELL, USER])
    print("Added user" + USER)
except subprocess.CalledProcessError as e:
    print(e)

# next add the created user to additional groups
try:
    subprocess.run(['usermod','-aG', ",".join(GROUP), USER])
except subprocess.CalledProcessError as e:
    print(e)
    