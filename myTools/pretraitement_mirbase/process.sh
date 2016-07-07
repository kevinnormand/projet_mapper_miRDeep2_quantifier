#extraction des precurseur $word de hairpin.fa de miRBase et retirer ceux qu'il y apres le premier espace
extract_seq_which_id_contains_modifier.pl --fasta_in $1 --word $3 --inverse no --begining no --file_out precurseur_espece #extract sequence with word in the identifier
modification_identifier.py precurseur_espece precurseur_espece_sans_espace #recuperate informations before the first space

#extraction des mirna mature $word de mature.fa de miRBase
extract_seq_which_id_contains_modifier.pl --fasta_in $2 --word $3 --inverse no --begining no --file_out mirna_mature_espece #extract sequence with word in the identifier
modification_identifier.py mirna_mature_espece mirna_mature_espece_sans_espace #recuperate informations before the first space

#extraction des mirna mature no $word de mature.fa de miRBase
extract_seq_which_id_contains_modifier.pl --fasta_in $2 --word $3 --inverse yes --begining no --file_out mirna_mature_no_espece #extract sequence without word in the identifier
modification_identifier.py mirna_mature_no_espece mirna_mature_no_espece_sans_espace #recuperate informations before the first space
