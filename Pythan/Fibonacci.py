# Providing the number of sequence by converting input string into integer.
nthTerm = int(input("Please provide Length of sequence :"))

# Take initial two numbers (0,1)
currentVal = 0
nextVal = 1

# Hold the printng number in s
seqNo=1

if nthTerm<= 0:
 print("Please provid valid number.")
else :
 while seqNo <= nthTerm :
   print(currentVal)
   
   # Reset values without using any other temp variable
   # Ex currentVal = 1 , nextVal = 2
   nextVal    = nextVal + currentVal  # nextVal    = 2 + 1 = 3
   currentVal = nextVal - currentVal  # currentVal = 3 - 1 = 2
   seqNo  = seqNo + 1
 
 input("Press enter to exit")