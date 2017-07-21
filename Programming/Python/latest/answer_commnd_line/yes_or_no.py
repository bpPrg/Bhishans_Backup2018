#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 04, 2017 Tue
# Last update : 
#
# Imports
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        print('You entered y')
        return True
    if reply[0] == 'n':
        print('You entered n')
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")
        


question = lambda q: input(q).lower().strip()[0] == "y" or question(q)

if __name__ == '__main__':
    #yes_or_no('Enter yes or no: ')
    question("Enter yes or no")
