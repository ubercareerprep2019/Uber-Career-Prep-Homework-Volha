# Implement the function: Boolean isStringPermutation(String s1, String s2)
# This function takes two strings and returns true if one string is a 
# permutation of the other, false otherwise.

def isStringPermutation(s1, s2):

	messageInputNotStr = "Please make sure the input is of type string."
	messageInputEmptyString = "The input is an empty string."

	try:
		if (type(s1)==str and type(s2)==str):
			if (len(s1)==0 or len(s2)==0):
				return print(messageInputEmptyString)

			if (len(s1)==len(s2)):

				lowers1=s1.lower()
				lowers2=s2.lower()

				letters = {}
				for i in lowers1:
					if i in letters:
						letters[i]=letters[i]+1
					else:
						letters[i]=1

				for j in lowers2:
					if j in letters:
						letters[j]=letters[j]-1
						if letters[j]<0:
							return False
					else:
						return False

				return True
			else:
				return False
		else:
			print(messageInputNotStr)

	except:
		print(messageInputNotStr)


# Implement the function: Array<Pair<int>> pairsThatEqualSum(Array<int> inputArray, 
# int targetSum). This function takes an array of integers and a target integer to 
# which the array elements must sum. It returns an array of all pairs of integers 
# from the input array whose sum equals the target.		


def pairSum(arrayOfInt, target):
	allPairsSumEqualsTarget= []

	messageEmptyArray = "The input array is empty"
	messageTargetNotInt = "Please make sure target is an integer"
	messageNonIntValuesInArray = "Please make sure input is an array of integers"
	messageNoMatchingPairs = "No such pairs exist"

	if len(arrayOfInt)==0:
		return print(messageEmptyArray)
	elif type(target) != int:
		return print(messageTargetNotInt)

	for i in arrayOfInt:
		if type(i)!= int:
			return messageNonIntValuesInArray
		for j in arrayOfInt:
			if type(j)!= int:
				return messageNonIntValuesInArray
			elif ((i)+(j)==target):
				a = (i, j)
				allPairsSumEqualsTarget.append(a)
		
	if len(allPairsSumEqualsTarget)==0:
		return  print(messageNoMatchingPairs)
	else:
		return list(set(allPairsSumEqualsTarget))

