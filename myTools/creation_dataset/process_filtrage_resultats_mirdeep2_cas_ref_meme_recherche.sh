#!/bin/bash

###################creation new_mirna.csv######################
echo "creation de new_mirna.csv">log.txt	#indicate the beginning of the creation of new_mirna.csv in a file called log
echo "creation de la condition a partir des entrees utilisateurs">>log.txt

echo "nom du fichier des resultats de mirdeep2 : ${1}">>log.txt	#indicate the name of file used in first parameter in the file called log
echo "espece recherchee : ${2}">>log.txt	#indicate the word used in parameter for specie researched in the file called log
echo "score selectionné pour la recherche de new mirna : ${3}">>log.txt	#indicate the score use in parameter to create new_mirna.csv in the file called log
echo "option choisie pour le filtre sur les randfold significatif : ${4}">>log.txt	#indicate the option randfold chosen by user in the file called log
echo "option choisie pour le filtre sur les exemple de mirna avec la meme seed region : ${5}">>log.txt	#indicate the option example with mirna in miRBase chosen in the file called log

condition='($2>='${3}'';	#initialize the beginning of the condition to researche mirna with un score higher than the one chosen

if [ $4 = "yes" ] #attention space important	check if option randfold is true
then
	condition=${condition}' && $9 =="yes"'	#if option randfold is true, implements the condition by asking it to verify if "yes" in the column significatively randfold
fi
if [ $5 = "yes" ] #attention space important	check if option example with mirna in miRBase is true
then
	condition=${condition}' && $11 =="-"'	#if option example is true,  implements the condition by asking it to verify if there is an example of mirna in miRBase
fi

condition=${condition}') || $2=="miRDeep2 score"' #finish the condition with operator "OR" to select column titles where the title is "miRDeep2 score"

echo "condition : ${condition}">>log.txt	#view the contents of the condition in a file called log

cmd="tail -n +27 $1 > fichier_apres_tail"	#command to recuperate the file without the board in "fichier_apres_tail"
cmd2="awk -F '\t' '{if(${condition}) {print \"${2}-\" \$1 \"\t\" \$0}else if(\$9 ==\"\"){exit}else{next}}' fichier_apres_tail > new_mirna.csv;" 	#command to recuperate lines of "fichier_apres_tail" which respect "condition" in "new_mirna.csv"

echo "execution de la commande suivante :">>log.txt
echo $cmd>>log.txt	#display the command used in the file called log
echo "execution de la commande suivante :">>log.txt
echo $cmd2>>log.txt	#display the command used in the file called log

(eval "$cmd") 2>>log.txt	#execute the command
(eval "$cmd2") 2>>log.txt	#execute the command 2

echo "new_mirna.csv OK">>log.txt	#display "new_mirna.csv OK" to show the end of the creation of new_mirna.csv in the file called log
echo "">>log.txt	#display a blank space in the file called log

######################creation new_mirna.fa######################
echo "creation de new_mirna.fa">>log.txt	#indicate the beginning of the creation of new_mirna.fa in the file called log

echo "rappel de l'espece recherche : ${2}">>log.txt	#display the specie research in the file called log

cmd3="awk -F '\t' '{if(\$1 !=\"${2}-provisional id\"){print \">\" \$1 \"_mt\n\" \$15 }}' new_mirna.csv > new_mirna.fa"	#command to recuperate mirna where "_mt" is present in the identifier of file new_mirna.csv in the file new_mirna.fa
cmd4="awk -F '\t' '{if(\$1 !=\"${2}-provisional id\"){print \">\" \$1 \"_st\n\" \$16 }}' new_mirna.csv >> new_mirna.fa"	#command to recuperate mirna where "_st" is present in the identifier of file new_mirna.csv in the file new_mirna.fa

echo "execution des commandes suivantes : ">>log.txt
echo $cmd3>>log.txt	#display the command used in the file called log
echo $cmd4>>log.txt

(eval "$cmd3") 2>>log.txt	#execute the command 3
(eval "$cmd4") 2>>log.txt	#execute the command 4

echo "new_mirna.fa OK">>log.txt	#display "new_mirna.fa OK" to show the end of the creation of new_mirna.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log

#####################creation new_hairpin.fa#########################
echo "creation de new_hairpin.fa">>log.txt	#indicate the beginning of the creation of new_hairpin.fa in the file called log

echo "rappel de l'espece recherchee : ${2}">>log.txt	#display the specie research in the file called log

cmd5="awk -F '\t' '{if(\$1 !=\"${2}-provisional id\"){print \">\" \$1 \"\n\" \$17 }}' new_mirna.csv > new_hairpin.fa"	#command to recuperate precursors'mirna of file new_mirna.csv in file new_hairpin.fa

echo "execution de la commande suivante : ">>log.txt
echo $cmd5>>log.txt		#display the command used in the file called log

(eval "$cmd5") 2>>log.txt	#execute the command 5

echo "new_hairpin.fa OK">>log.txt	#display "new_hairpin.fa OK" to show the end of the creation of new_hairpin.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log

###################creation new_predicted_precursors.gff###########
echo "creation de new_predicted_precursors.gff">>log.txt	#indicate the beginning of the creation of new_predicted_precursors.gff in the file called log

echo "rappel de l'espece recherchee : ${2} ">>log.txt	#display the specie research in the file called log

cmd6="awk -F '\t' '{if(\$1 !=\"${2}-provisional id\"){print \$1 \"\t\" \$18}}' new_mirna.csv | perl -p -e 's/:|\.\./\t/g' | awk -F '\t' '{print \$2 \"\tmiRDeep2\tnew_predicted_precursor\t\" \$3 \"\t\" \$4 \"\t.\t\" \$5 \"\t.\t\" \$1}' > news_predicted_precursors.gff"	#command to recuperate positions of precursors on the genome of file new_mirna.csv in file news_predicted_precursors.gff

echo "execution de la commande suivante : ">>log.txt
echo $cmd6>>log.txt	#display the command used in the file called log

(eval "$cmd6") 2>>log.txt	#execute the command 6

echo "new_predicted_precursors.gff OK">>log.txt	#display "new_predicted_precursors.gff OK" to show the end of the creation of new_predicted_precursors.gff in the file called log
echo "">>log.txt	#display a blank space in the file called log

###################creation de know_espece_mirna.csv##########################
echo "creation de know_${2}_mirna.csv">>log.txt	#indicate the beginning of the creation of know_espece_mirna.csv in the file called log

echo "rappel du nom du fichier des resultats de mirdeep2 : ${1}">>log.txt	#display the name of result's file of mirdeep2 in the file called log
echo "rappel de l'espece recherchee : ${2}">>log.txt	#display the specie research in the file called log
echo "score selectionne pour la recherche de mirna connu : ${6}">>log.txt	#display the score used to create the file know_espece_mirna.csv in the file called log

cmd7="cat ${1} | awk -F '\t' '{if(\$1 == \"mature miRBase miRNAs detected by miRDeep2\"){state=\"ok\"}else{if(state==\"ok\" && \$2 > ${6} ){print \"${2}-\" \$1 \"\t\" \$0}else{if(state==\"ok\"){exit}}}}' > know_${2}_mirna.csv"	#command to recuperate mirna know of file of mirdeep2 in the file know_${2}_mirna.csv, cat is not necessarly but used to have the standard output of file for awk

echo "execution de la commande suivante : ">>log.txt
echo $cmd7>>log.txt	#display the command used in the file called log

(eval "$cmd7") 2>>log.txt	#execute the command 7

echo "know_${2}_mirna.csv OK">>log.txt	#display "know_${2}_mirna.csv OK" to show the end of the creation of know_espece_mirna.csv in the file called log
echo "">>log.txt	#display a blank space in the file called log

#################creation predicted_know_mirna.fa################################
echo "creation de predicted_know_mirna.fa">>log.txt	#indicate the beginning of the creation of predicted_know_mirna.fa in the file called log

cmd8="awk -F '\t' '{if(\$1 !=\"${2}-tag id\"){print \">\" \$1 \"_mt\n\" \$15 }}' know_${2}_mirna.csv > predicted_know_mirna.fa"	#command to recuperate mirna where "_mt" is present in the identifier of file know_${2}_mirna.csv in the file predicted_know_mirna.fa
cmd9="awk -F '\t' '{if(\$1 !=\"${2}-tag id\"){print \">\" \$1 \"_st\n\" \$16 }}' know_${2}_mirna.csv >> predicted_know_mirna.fa"	#command to recuperate mirna where "_st" is present in the identifier of file know_${2}_mirna.csv in the file predicted_know_mirna.fa

echo "execution des commandes suivantes : ">>log.txt
echo $cmd8>>log.txt	#display the command used in the file called log
echo $cmd9>>log.txt

(eval "$cmd8") 2>>log.txt	#execute the command 8
(eval "$cmd9") 2>>log.txt	#execute the command 9

echo "predicted_know_mirna.fa OK">>log.txt	#display "predicted_know_mirna.fa OK" to show the end of the creation of predicted_know_mirna.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log

#################creation npp_with_know_espece_mirna.gff###########################
echo "creation de npp_with_know_${2}_mirna.gff">>log.txt	#indicate the beginning of the creation of npp_with_know_espece_mirna.gff in the file called log

cmd10="awk -F '\t' '{if(\$1 !=\"${2}-tag id\"){print \$1 \"\t\" \$18}}' know_${2}_mirna.csv | perl -p -e 's/:|\.\./\t/g' | awk -F '\t' '{print \$2\"\tmiRDeep2\tpredicted_precursor_with_know_${2}_mature\t\" \$3 \"\t\" \$4 \"\t.\t\" \$5 \"\t.\t\" \$1}' > npp_with_know_${2}_mirna.gff"	#command to recuperate positions of precursors on the genome of file know_${2}_mirna.csv in file npp_with_know_${2}_mirna.gff

echo "execution de la commande suivante : ">>log.txt
echo $cmd10>>log.txt	#display the command used in the file called log

(eval "$cmd10") 2>>log.txt	#execute the command 10

echo "npp_with_know_${2}_mirna.gff OK">>log.txt	#display "npp_with_know_${2}_mirna.gff OK" to show the end of the creation of npp_with_know_espece_mirna.gff in the file called log
echo "">>log.txt	#display a blank space in the file called log

#################traitement de mature.fa####################
echo "traitement du fichier mature.fa">>log.txt	#indicate the beginning of the creation of mature.fa in the file called log

cmd11="modification_identifier.py ${7} mature_sans_espace.fa"	#keep informations before the first space

echo "execution de la commande suivante : ">>log.txt
echo $cmd11>>log.txt	#display the command used in the file called log

(eval "$cmd11") 2>>log.txt	#execute the command 11

echo "mature_sans_espace.fa OK">>log.txt	#display "mature_sans_espace.fa OK" to show the end of the creation of mature_sans_espace.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log

#################creation mature_and_new.fa########################
echo "creation de mature_and_new.fa">>log.txt	#indicate the beginning of the creation of mature_and_new.fa in the file called log

cmd12="cat new_mirna.fa predicted_know_mirna.fa mature_sans_espace.fa > mature_and_new.fa"	#command to concatenate files new_mirna.fa, predicted_know_mirna.fa and mature_sans_espace.fa in mature_and_new.fa

echo "execution de la commande suivante : ">>log.txt
echo $cmd12>>log.txt	#display the command used in the file called log

(eval "$cmd12") 2>>log.txt	#execute the command 12

echo "mature_and_new.fa OK">>log.txt	#display "mature_and_new.fa OK" to show the end of the creation of mature_and_new.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log

################creation hairpin_${2}_and_new.fa#################
echo "creation de hairpin_${2}_and_new.fa">>log.txt	#indicate the beginning of the creation of hairpin_${2}_and_new.fa in the file called log

cmd13="cat new_hairpin.fa ${8} > hairpin_espece_and_new.fa"	#command to concatenate new_hairpin.fa, predicted_know_hairpin.fa and no_identified_${2}_mirna.pre.fasta in hairpin_espece_and_new.fa

echo "execution de la commande suivante : ">>log.txt
echo $cmd13>>log.txt	#display the command used in the file called log

(eval "$cmd13") 2>>log.txt	#execute the command 13

echo "hairpin_espece_and_new.fa OK">>log.txt	#display "hairpin_espece_and_new.fa OK" to show the end of the creation of hairpin_${2}_and_new.fa in the file called log
echo "">>log.txt	#display a blank space in the file called log
