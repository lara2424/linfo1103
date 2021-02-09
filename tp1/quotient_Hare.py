def plus_fort_reste(n_sieges, resultat_vote):
    """
    Calcul la repartition des sieges selon la methode du plus
    fort reste (variante du quotient de Hare)
    pre: `n_sieges` > 0
    pre: len(`resultat_vote`) > 1
    pre: `resultat_vote[i]` >= 0
        pour tout `i` tel que 0 <= `i` < len(`resultat_vote`)
    post: retourne un tableau `t` de même longueur que `resultat_vote`
        et tel que `t[i]` est le nombre de sieges attribues au parti
        correspondant a `resultat_vote[i]`
    """

    t = [0] * len(resultat_vote)
    rst = [0] * len(resultat_vote)
    rstb = [0] * len(resultat_vote)
    siege = n_sieges
    for i in range(len(t)):
        t[i] = int((resultat_vote[i] / sum(resultat_vote)) * n_sieges)
        rst[i] = ((resultat_vote[i] / sum(resultat_vote)) * n_sieges) - t[i]
        rstb[i] = rst[i]
        siege = siege - t[i]
    rstb.sort(reverse=True)
    x = 0
    ok = [False] * len(resultat_vote)
    while siege > 0:
        if ok[rst.index(rstb[x])]:
            for n in range(len(rst)):
                if rst[n] == rstb[x] and not ok[n]:
                    t[n] = t[n] + 1

        else:
            t[rst.index(rstb[x])] = t[rst.index(rstb[x])] + 1
            ok[rst.index(rstb[x])] = True

        siege = siege - 1
        x = x + 1
        if x == len(resultat_vote):
            x = 0
            ok = [False] * len(resultat_vote)

    return t