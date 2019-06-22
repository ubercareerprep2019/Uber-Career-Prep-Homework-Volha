class Stack:

	emptyStackMessage = "The Stack is empty"
	pushErrorMessage = "Unable to push"

	def __init__(self):
		self.stackCollection = []
		self.sizeValue = 0
		self.minValue = None
		self.minValueCollection = []

	def size(self):
		return self.sizeValue

	def push(self, element):
		try:
			self.stackCollection.append(element)
			self.sizeValue += 1

			if (type(element)==int or type(element)==float):
				self.minValueCollection.append(element)
				if (self.minValue == None or element < self.minValue):
					self.minValue = element
		except: print(self.pushErrorMessage)

	def pop(self):
		if (self.sizeValue == 0):
			return print(self.emptyStackMessage)

		if (self.sizeValue == 1):
			topValue = self.stackCollection[0]
			del self.stackCollection[0]

			self.sizeValue = 0
			self.minValue = None
			self.minValueCollection = []
			
			return topValue

		else:
			topValue = self.stackCollection[self.sizeValue-1]
			del self.stackCollection[self.sizeValue-1]

			self.sizeValue -= 1
			if(self.minValue == topValue):
				del self.minValueCollection[-1]

				if (len(self.minValueCollection)>0):
					self.minValue = self.minValueCollection[len(self.minValueCollection) - 1]
				else:
					self.minValue = None

			return topValue


	def top(self):
		if(self.sizeValue > 1):
			topValue = self.stackCollection[self.sizeValue-1]
			return topValue

		if(self.sizeValue == 1):
			topValue = self.stackCollection[0]
			return topValue

		if(self.sizeValue == 0):
			topValue = None
			return topValue

	def isEmpty(self):
		if (self.sizeValue < 1):
			return True
		else:
			return False

	def min(self):
		return self.minValue



 myStack = Stack()
 print("Stack created, Expected values: 0, None, None, True \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())

 myStack.push("")
 print("\nPushed an empty string, Expected values: 1, None,  , False\nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())

 myStack.push(42)
 print("\nPushed int 42, Expected values: 2, 42, 42, False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())

 myStack.push("lambda")
 print("\nPushed str lambda, Expected values: 3, 42, lambda, False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())

 myStack.push(7)
 print("\nPushed int 7, Expected values: 4, 7, 7, False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())


 myStack.pop()
 print("\nPopped, Expected values: 3, 42, lambda, False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())


 myStack.pop()
 print("\nPopped, Expected values: 2, 42, 42, False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())

 myStack.pop()
 print("\nPopped, Expected values: 1, None,  , False \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())


 myStack.pop()
 print("\nPopped, Expected values: 0, None, None, True \nActual values: ")
 print(myStack.size(), myStack.min(), myStack.top(), myStack.isEmpty())


 print("\nCalling pop on empty stack, Expected output: The Stack is empty \nActual values: ")
 myStack.pop()



 class Queue:
     def __init__(self):
         self.queueCollection = Stack()

     def enqueue(self, element):
         self.queueCollection.push(element)

     def reverse(self):
         reversedQueue = Stack()
         while (not self.queueCollection.isEmpty()):
             reversedQueue.push(self.queueCollection.pop())
         return reversedQueue

     def dequeue(self):
         revesedCollection = Stack()
         revesedCollection =  self.reverse()
         dequevalue = revesedCollection.pop()
         self.queueCollection = revesedCollection.reverse()
         return dequevalue



