#!/usr/bin/python

#program to remove informations after the first space

import sys
import argparse
import re

parser = argparse.ArgumentParser(description='test')	#allows for arguments
parser.add_argument('param1',help='reference file where identifier is changed')
parser.add_argument('param2',help='file that one whish fill')
args=parser.parse_args()

"""
definition of functions
"""

def modifieur(args):
	ref=open(args.param1,"r")	#open first argument
	fichier_a_remplir=open(args.param2,'w')	#open second argument
	for line in ref:
		if ">" in line :
			identifiant=line.split(" ")[0]	#retrieve the first element ot the table create by split
			fichier_a_remplir.write(identifiant+'\n')
		else:
			fichier_a_remplir.write(line)
	fichier_a_remplir.close()
	ref.close()

"""
launching programs
"""

modifieur(args)
