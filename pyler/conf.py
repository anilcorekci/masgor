#!/usr/bin/env python
#! coding:utf-8 -*-

import configparser

class config(configparser.RawConfigParser):
    def __init__(self,confile):
        configparser.RawConfigParser.__init__(self)
        self.path = confile
        self.readfp(open(self.path))

    @property
    def dict_(self):
        return self._sections['tercihler.cfg']

    def yaz(self,file): 
        with open(self.path, 'w') as configfile:
            self.write(configfile)

    def set_conf(self,file,key,name): 
        try:
            self.add_section(file)
        except:pass
        if self._get(file,key) == name:
            return 
        self.set(file,key,name)
        self.yaz(file)

    def _get(self,file,key):
        try:
            val = self.get(file,key)
        except:
            return False
        else:return val
