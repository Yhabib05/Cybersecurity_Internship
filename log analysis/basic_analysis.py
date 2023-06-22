# File is automatically closed when exiting the 'with' block
with open("input.txt", "r") as f:
    for line in f:
        linestrip = line.strip().split() #the split without any arguments split even if there is more than one space

        if len(linestrip) >= 7:  # we checking for the length of the line to not have some index errors
            joursemaine = linestrip[0]
            jour = linestrip[1]
            mois = linestrip[2]
            annee = linestrip[3]
            time = linestrip[4]
            message = linestrip[5]
            errormessage = linestrip[6]

            user = linestrip[-1]

            print('L\'utilisateur', user, '=>', 'Erreur:', message, 'le', joursemaine, jour, mois, annee, 'à', time)

