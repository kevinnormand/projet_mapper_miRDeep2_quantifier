#!/bin/env python

#program to create the file of configuration for Mapper

import sys
import argparse
import re

arg_voulu=sys.argv[1:] #recuperate name of files
n=1

fichier = open(arg_voulu[0], "r")
for line in fichier:
	if len(line.split('"'))==3: #because there is other line exemple blank line
		if n<10 :
			print line.split('"')[1]+" A0"+str(n) #write name of file in file of configuration with a prefix
			n=n+1
		elif n>=10 : 
			print line.split('"')[1]+" A"+str(n)
			n=n+1
		
fichier.close()
