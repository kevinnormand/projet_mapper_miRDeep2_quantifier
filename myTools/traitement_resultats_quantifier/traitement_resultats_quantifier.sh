#!/bin/bash

####filtering results of quantifier####

#filtering#
echo "nom du fichier des resultats de quantifier : ${1}">log.txt	#indicate the name of file used in first parameter in a file called log
echo "nom du fichier miRBase.mrd utilisé : ${2}">>log.txt	#indicate the name of file used in second parameter in the file called log
echo "nom du fichier des matures et news mappés : ${3}">>log.txt	#indicate the name of file used in third parameter in the file called log
echo "non de l'espece etudiee : ${4}">>log.txt #indicate the word used in parameter for specie researched in the file called log
echo "voulez-vous appliquer un filtre : ${5}">>log.txt #indicate if you applied a filter in the file called log
echo "nombre de condition : ${6}">>log.txt #indicate the number of condition used in the pipeline
echo "valeur du filtre : ${7}">>log.txt	#indicate the value of filter at apply

if [ $5 = "no" ]	#attention space important	check if option filter is false
then
	cmd0="parse_miRDeep2_output.pl --mature_arf ${3} --structure_file ${2} --expression_file ${1} > miRNAs_expressed_all_samples.pre_unique_espece.csv"	#command used if there is not filter, assigns mature miRNAs to a set of precursors, and report the quantification of the best two mature (3p & 5p predicted from their position on the precursor) observed for each precursor.
fi

if [ $5 = "yes" ]	#attention space important	check if option filter is true
then
	cmd1="perl -p -e 's/(\d+)\.(\d{2})/\1\,\2/g' ${1} > sortie_inter"	
	echo "execution de la commande suivante :">>log.txt 
	echo $cmd1>>log.txt	#display the command used in the file called log
	(eval "$cmd1") 2>>log.txt #execute the command 1
	
	condition="awk -F '\t' '\$5>=${7}"	#initialize the condition for the filter
	i=2
	#echo "i : ${i}">>log.txt
	while [ $i -le ${6} ]
	do
		n=$(( $i+4 ))	#use to know the column in file ${1}
		#echo "n : ${n}">>log.txt
		condition=${condition}" || \$${n}>=${7}"	#add informations for the condition
		i=$(( $i+1 ))	#incrementing of number to arrive at number of condition
		#echo "nouveau i : ${i}">>log.txt
	done
	echo "condition : ${condition}">>log.txt	#display the condition used in the file called log
	cmd2=${condition}"' sortie_inter > sortie_inter2"	#finish the command
	echo "execution de la commande suivante :">>log.txt
	echo $cmd2>>log.txt	#display the command used in the file called log
	(eval "$cmd2") 2>>log.txt #execute the command 2
	cmd0="parse_miRDeep2_output.pl --mature_arf ${3} --structure_file ${2} --expression_file sortie_inter2 > miRNAs_expressed_all_samples.pre_unique_espece.csv"	#command used if there is not filter, assigns mature miRNAs to a set of precursors, and report the quantification of the best two mature (3p & 5p predicted from their position on the precursor) observed for each precursor.
	
fi

echo "execution de la commande suivante :">>log.txt
echo $cmd0>>log.txt	#display the command used in the file called log

(eval "$cmd0") 2>>tableau_recapitulatif #execute the command 0 in a summary table

#add header line to results files#
cmd3="head -n 1 miRNAs_expressed_all_samples.pre_unique_espece.csv > head_miRNAs_expressed_all_samples.pre_unique_espece.csv"	#recover the first line in the file miRNAs_expressed_all_samples.pre_unique_espece.csv in the file head_miRNAs_expressed_all_samples.pre_unique_espece.csv
cmd4="perl -p -e 's/\#//' head_miRNAs_expressed_all_samples.pre_unique_espece.csv > miRNAs_expressed_all_samples.pre_unique.matureSEQ_unique.espece.csv" #modify the first line and create the file miRNAs_expressed_all_samples.pre_unique.matureSEQ_unique.espece.csv
cmd5="perl -p -e 's/\#//' head_miRNAs_expressed_all_samples.pre_unique_espece.csv > miRNAs_expressed_all_samples.pre_unique.matureID_unique.espece.csv"	#modify the first line and create the file miRNAs_expressed_all_samples.pre_unique.matureID_unique.espece.csv

echo "execution de la commande suivante :">>log.txt
echo $cmd3>>log.txt	#display the command used in the file called log
echo "execution de la commande suivante :">>log.txt
echo $cmd4>>log.txt	#display the command used in the file called log
echo "execution de la commande suivante :">>log.txt
echo $cmd5>>log.txt	#display the command used in the file called log

(eval "$cmd3") 2>> log.txt	#execute the command 3
(eval "$cmd4") 2>> log.txt	#execute the command 4
(eval "$cmd5") 2>> log.txt	#execute the command 5

#mature sequence unique#
n=5+${6}*2+1	#use to know the number of the last column

cmd6="grep -v 'read_count' miRNAs_expressed_all_samples.pre_unique_espece.csv | awk -F '\t' '{if(\$2 > count[\$${n}]){infos[\$${n}] = \$0;count[\$${n}]=\$2}} END {for  (var in infos){print infos[var]}}' >> miRNAs_expressed_all_samples.pre_unique.matureSEQ_unique.espece.csv"	#recuperate mirna and add sequences of matures mirna

echo "execution de la commande suivante :">>log.txt
echo $cmd6>>log.txt	#display the command used in the file called log

(eval "$cmd6") 2>> log.txt	#execute the command 6

#mature id unique#
cmd7="grep -v 'read_count' miRNAs_expressed_all_samples.pre_unique_espece.csv | perl -p -e 's/(\d+)\,(\d{2})/\1\.\2/g' | awk -F '\t' '{if(\$2 > count[\$1]){infos[\$1] = \$0;count[\$1]=\$2}} END {for (var in infos){print infos[var]}}' >> miRNAs_expressed_all_samples.pre_unique.matureID_unique.espece.csv"

echo "execution de la commande suivante :">>log.txt
echo $cmd7>>log.txt	#display the command used in the file called log

(eval "$cmd7") 2>> log.txt	#execute the command 7
