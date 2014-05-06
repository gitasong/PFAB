#initial dictionary pairs
scores = {"Lassoff" : 3.12 , "Johnson" : 2.22 , "Reich" : 3.59 , "Honeychurch" : 2.98 , "Maini" : 3.11 , "Levin" : 2.88 , "Marcus" : 2.77 , "Banks" : 3.71}

#prints key + associated value (names and GPAs)
for key in scores:
        print "Last Name: ", key, "   GPA: ", scores[key]

#manually calculates class average
print "The class average is: ", (3.12 + 2.22 + 3.59 + 2.98 + 3.11 + 2.88 + 2.77 + 3.71) / 8

#first attempt at class rankings
#rawScores = scores.values()
#rawScores.sort()
#rawScores.reverse()
##print rawScores
#n = 0
#while n < len(rawScores):
#       print "Rank #", n + 1, "Score: ", rawScores[n]
#       n = n + 1

#finished attempt at class rankings: reverse  sorts dictionary keys by values into a new list
results =  sorted(scores, key=scores.__getitem__, reverse=True)
#print results

#iterates through list of sorted keys, printing each one out along with score
n = 1
for rank in results:
        print "Rank #", n,  rank
        n = n + 1

