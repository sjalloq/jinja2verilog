#!/usr/bin/env python

import inspect
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates')
)


class Module(object):
    def __init__(self, name):
        self.template = env.get_template('test.vt')
        self.name = name
        self.registers = 'hello'
        
    def render(self):
        print(self.template.render(m=self.__dict__))

    
class Register(object):
    def __init__(self, name,
                 msb='0',
                 lsb='0',
                 clock='clk',
                 clockedge='posedge',
                 reset='reset_n',
                 resetedge='negedge',
                 resetpol='!',
                 resetval='0'):
        
        self.template  = env.get_template('register.vt')
        self.name      = name
        self.msb       = msb
        self.lsb       = lsb
        self.clock     = clock
        self.clockedge = clockedge
        self.reset     = reset
        self.resetedge = resetedge
        self.resetpol  = resetpol
        self.resetval  = resetval
               
    def render(self):
        print(self.template.render(self.__dict__))


#r = Register('data', '7', '0')
#r.render()

m = Module('topmod')
m.render()
