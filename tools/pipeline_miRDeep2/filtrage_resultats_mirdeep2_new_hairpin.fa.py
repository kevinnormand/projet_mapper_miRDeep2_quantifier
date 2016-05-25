#!/bin/env python

#script pour remplacer la commande : awk -F '\t' '{if($1 !="bta-provisional id"){print ">" $1 "\n" $17 }}' $input > $output;
import sys
import argparse
import re


parser = argparse.ArgumentParser(description='test')
parser.add_argument('param1',help='fichier csv sur lequel on utilise la commande')
args=parser.parse_args()

"""
definition des fonctions
"""

def commande(args):
	fichier_entrer=open(args.param1,"r").readlines()
	line_fichier=iter(fichier_entrer)
	for line in line_fichier:
			line_fichier.next()
			line_words=line.split('\t')
			if line_words[0] != 'bta-provisional id':
				print(">"+line_words[0]+"\n"+line_words[16])

"""
lancement programme
"""

commande(args)
