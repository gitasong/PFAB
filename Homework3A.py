Bradys = ["Mike", "Carol", "Marsha", "Jan", "Cindy", "Greg", "Peter", "Bobby", "Alice"]

#print len(Bradys)

numBradys = len(Bradys)
n = 0
while n < numBradys:
        print Bradys[n]
        n = n + 1

print "####################################"
#Sorted
Bradys.sort()
n = 0
while n < numBradys:
        print Bradys[n]
        n = n + 1
#Note: The .sort()  function permanently sorts the list. To sort the list only temporarily, use the sorted() function (per Python Central at http://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/)
numBradys = len(Bradys)


print "###################################"
#For... In Loop
for n in Bradys:
        print n

