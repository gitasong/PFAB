#input("Enter your  four test scores for averaging: ")
#input() not needed with sys.argv

#imports four test scores from command line and assigns them variables
import sys
test1 = int(sys.argv[1])
test2 = int(sys.argv[2])
test3 = int(sys.argv[3])
test4 = int(sys.argv[4])

#averages the four test scores and prints average
average = (test1 + test2 + test3 + test4) / 4
print "Your average score is ",average,"."

#determines letter grade from average using elif command
if average >= 90:
        print "Your grade is A."
elif average >= 80:
        print "Your grade is B."
elif average >= 70:
        print "Your grade is C."
elif average >= 60:
        print "Your grade is D."
else:
        print "Your grade is F."
