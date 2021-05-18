def teamFormation(score, team_size, k):
    sempl = []
    while len(sempl)<team_size:
        l = [score[i] for i in range(0,k)]+[score[i] for i in range(len(score)-k,len(score))]
        emp = max(l)
        score.remove(emp)
        sempl.append(emp)
    return sum(sempl)
