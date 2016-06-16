#!/bin/env python

#script pour retirer tous les caractere apres les chiffre de le reference bos_taurus (>1 dklvgfnsdlkgnsl devient >1)

import sys
import argparse
import re

parser = argparse.ArgumentParser(description='test')
parser.add_argument('param1',help='fichier de ref dont on change l\'identifiant')
parser.add_argument('param2',help='fichier que l\'on souhaite remplir')
args=parser.parse_args()

#~ """
#~ initialisation de l'expression reguliere pour rechecher les sequences de Bos taurus
#~ """

#~ expression_id=re.compile(r"^(?P<id>>\w*\-?\w*-?d*\w*-?\w*\d*\.?\d*) .*")

"""
definition des fonctions
"""

def modifieur(args):
	ref=open(args.param1,"r")
	fichier_a_remplir=open(args.param2,'w')
	for line in ref:
		if ">" in line :
			identifiant=line.split(" ")[0]
			fichier_a_remplir.write(identifiant+'\n')
		else:
			fichier_a_remplir.write(line)
	fichier_a_remplir.close()
	ref.close()
			
#~ def modifieur(args):
	#~ ref=open(args.param1,"r")
	#~ fichier_a_remplir=open(args.param2,'w')
	#~ for line in ref:
		#~ if re.search(expression_id,line):
			#~ m=re.search(expression_id,line)
			#~ identifiant=m.group('id')
			#~ fichier_a_remplir.write(identifiant+'\n')
		#~ else:
			#~ fichier_a_remplir.write(line)
	#~ fichier_a_remplir.close()
	#~ ref.close()

"""
lancement programme
"""

modifieur(args)
