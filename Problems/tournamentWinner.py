def tournamentWinner(competitions, results):
	scores={}
	x=0
	for competition in competitions:	
		winner=competition[abs((results[x]-1))]
		print(winner)
		if winner in scores:
			scores[winner]+=3
		else:
			scores[winner]=3
		x+=1
    return max(scores, key=scores.get)
