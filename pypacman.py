#!/usr/bin/env python3

import subprocess

class pacman:

    def __init__(self):
        self.path="/usr/bin/pacman"
        self.config="/etc/pacman.conf"
        
        try:
            subprocess.check_call([self.path,'-V'])
        except subprocess.CalledProcessError as e:
            print (e)

    def install(self , packages:list):
        try:
            subprocess.call([self.path,'-S'] + packages)
        except subprocess.CalledProcessError as e:
            print(e)

    def upgrade(self):
        try:
            subprocess.call([self.path,'-Syu']) 
        except subprocess.CalledProcessError as e:
            print (e)

    def update(self):
        try:
            subprocess.run([self.path,'-Sy'])
        except subprocess.CalledProcessError as e:
            print (e)
    
    def remove(self, packages:list):
        try:
            subprocess.run([self.path,'-Rns'] + packages)
        except subprocess.CalledProcessError as e:
            print (e)
    
    def search(self, search:str):
        try:
            subprocess.run([self.path,'-Ss', search])
        except subprocess.CalledProcessError as e:
            print (e)
    
    def list_installed(self):
        try:
            installed = subprocess.check_output([self.path,'-Qq'],encoding="utf-8")
            return(installed.rstrip('\n').split('\n'))
        except subprocess.CalledProcessError as e:
            print (e)
    
    def list_explicit_installed(self):
        try:
            installed = subprocess.check_output([self.path,'-Qenq'],encoding="utf-8")
            return(installed.rstrip('\n').split('\n'))
        except subprocess.CalledProcessError as e:
            print (e)
    
    def autoremove(self):
        packages = subprocess.check_output(['pacman','-Qdtq'],encoding="utf-8")
        if packages:
            self.remove(packages.rstrip('\n').split('\n'))
        else:
            print ('No packages to remove')
    
    def is_installed(self, package:str):
        try:
            packages = self.list_installed()
            if package in packages:
                return True
            else:
                return False
        except:
            print('An error occurred')

			
	
