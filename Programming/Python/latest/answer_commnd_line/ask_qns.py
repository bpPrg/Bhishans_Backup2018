#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 04, 2017 Tue
# Last update : 
#
# Imports

def choice():
    # raw_input returns the empty string for "enter"
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    choice = input().lower()
    if choice in yes:
        print('You chose "Yes".') 
        return True
    elif choice in no: 
        print('You chose "No".')
        return False
    else: 
        sys.stdout.write("Please respond with 'yes' or 'no'.")


if __name__ == '__main__':
    choice()
    choice()
