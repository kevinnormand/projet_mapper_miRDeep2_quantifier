#!/bin/env python

#script pour remplacer la commande : awk -F '\t' '{if($1 !="bta-tag id"){print $1 "\t" $18}}' $input | perl -pi -e 's/:|\.\./\t/g' | awk -F '\t' '{print $2"\tmiRDeep2\tpredicted_precursor_with_know_bta_mature\t" $3 "\t" $4 "\t.\t" $5 "\t.\t" $1}' > $output

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
				

"""
lancement programme
"""

commande(args)
