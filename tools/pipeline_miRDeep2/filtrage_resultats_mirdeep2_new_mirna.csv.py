#!/bin/env python

#script pour remplacer la commande : tail -n+27 $input | awk -F '\t' '{if($2>=0 &#124;&#124; $2 =="miRDeep2 score") {print "bta-" $1 "\t" $0}else{exit}}' > $output

import sys
import argparse
import re
import csv

parser = argparse.ArgumentParser(description='test')
parser.add_argument('param1',help='fichier csv sur lequel on utilise la commande')
#parser.add_argument('param2',help='fichier que l\'on souhaite remplir')
args=parser.parse_args()

"""
definition des fonctions
"""

def commande(args):
	#fichier_entrer=open(args.param1,"r")
	fichier_entrer=open(args.param1,"r").readlines()
	#fichier_a_remplir=open(args.param2,'w')
	line_fichier=iter(fichier_entrer)
	n=0
	
	#with open(args.param1,"r") as fichier_entrer:
	for line in line_fichier:
		#print("ligne : "+line)
		if n<13:
			n=n+1
			line_fichier.next()
		else:
			line_words=line.split('\t')
			#print(len(line_words))
			#print("line_words"+str(line_words))
			if len(line_words)!=17:
				break
			elif line_words[1] >= 0 or line_words[1] == "miRDeep2 score":
				#fichier_a_remplir.write("bta-"+line_words[0]+"\t"+line_words[1]+"\t"+line_words[2]+"\t"+line_words[3]+"\t"+line_words[4]+"\t"+line_words[5]+"\t"+line_words[6]+"\t"+line_words[7]+"\t"+line_words[8]+"\t"+line_words[9]+"\t"+line_words[10]+"\t"+line_words[11]+"\t"+line_words[12]+"\t"+line_words[13]+"\t"+line_words[14]+"\t"+line_words[15]+"\t"+line_words[16]+"\n")
				print("bta-"+line_words[0]+"\t"+line_words[0]+"\t"+line_words[1]+"\t"+line_words[2]+"\t"+line_words[3]+"\t"+line_words[4]+"\t"+line_words[5]+"\t"+line_words[6]+"\t"+line_words[7]+"\t"+line_words[8]+"\t"+line_words[9]+"\t"+line_words[10]+"\t"+line_words[11]+"\t"+line_words[12]+"\t"+line_words[13]+"\t"+line_words[14]+"\t"+line_words[15]+"\t"+line_words[16])
			else:
				exit
	#fichier_a_remplir.close()

"""
lancement programme
"""

commande(args)
