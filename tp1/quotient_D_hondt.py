def plus_forte_moyenne(n_sieges, resultat_vote):
    '''
   Calcul la repartition des sieges selon la methode de la plus
   forte moyenne (variante de D Hondt)
   pre: `n_sieges` > 0
   pre: len(`resultat_vote`) > 1
   pre: `resultat_vote[i]` >= 0
       pour tout `i` tel que 0 <= `i` < len(`resultat_vote`)
   post: retourne un tableau `t` de meme longueur que `resultat_vote`
       et tel que `t[i]` est le nombre de sieges attribues au parti
       correspondant a `resultat_vote[i]`
   '''
    t = [0] * len(resultat_vote)
    max = 0
    siege = n_sieges
    ind = 0
    for i in range(len(t)):
        t[i] = int((resultat_vote[i] / sum(resultat_vote)) * n_sieges)
        siege = siege - t[i]
    while siege > 0:
        for i in range(len(resultat_vote)):
            max_tmp = resultat_vote[i] / (t[i] + 1)
            if max_tmp > max:
                max = max_tmp
                ind = i
        t[ind] += 1
        siege = siege - 1
        max = 0
    return t