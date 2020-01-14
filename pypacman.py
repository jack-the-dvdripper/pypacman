#!/usr/bin/env python3

import subprocess
import os
import logging

class pacman(object):

    def __init__(self):
        self.path="/usr/bin/pacman"
        self.config="/etc/pacman.conf"
        
        try:
            subprocess.check_call([self.path,'-V'],stdout=subprocess.DEVNULL)
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
            installed = subprocess.getoutput([self.path + ' -Qq'])
            return(installed.split('\n'))
        except subprocess.CalledProcessError as e:
            print (e)
    
    def list_explicit_installed(self):
        try:
            installed = subprocess.getoutput([self.path + ' -Qenq'])
            return(installed.split('\n'))
        except subprocess.CalledProcessError as e:
            print (e)
    
    def autoremove(self):
        packages = subprocess.getoutput([self.path + ' -Qdtq'])
        if packages:
            self.remove(packages.split('\n'))
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

class pacstrap:
    def __init__(self):
        self.path="/usr/bin/pacstrap"
        self.logger = logging.getlogger('pacstrap-logger')
        self.root = "/mnt"
        try:
            subprocess.check_call([self.path,'-h'],stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print (e)
        
    def pacstrap(self,packages:list):
        try:
            subprocess.call([self.path,self.root] + packages)
        except subprocess.CalledProcessError as e:
            print (e)
    
    def pacstrap_auto(self):
        packages=['base','base-devel','linux','nano','dhcpcd','wifi-menu','linux-firmware',
                  'device-mapper', 'inetutils', 'man-db', 'sysfsutils', 'texinfo', 'usbutils',
                  'xfsprogs','bash-completion','wpa_supplicant','dialog','netctl']
        self.pacstrap(packages)



