class Stack:

	emptyStackMessage = "The Stack is empty"

	def __init__(self):
		self.stackCollection = []
		self.sizeValue = 0
		self.minValue = None

	def size(self):
		return self.sizeValue

	def push(self, element):
		self.stackCollection.append(element)
		self.sizeValue += 1

		if ( self.minValue == None or element < self.minValue):
			self.minValue = element

	def pop(self):
		if (not self.isEmpty()):
			try:
				topValue = self.stackCollection[self.sizeValue-1]

				if(self.minValue == topValue):
					self.minValue = min(myStack)
					del self.stackCollection[self.sizeValue-1]
					sizeValue -= 1
					return topValue
			except:
				print(emptyStackMessage)

	def top(self):
		try:
			topValue = self.stackCollection[self.sizeValue-1]
			return topValue
		except:
			print(emptyStackMessage)

	def isEmpty(self):
		if (self.sizeValue < 1):
			return True
		else:
			return False

	def min(self):
		return minValue



myStack = Stack()
myStack.push(42)
print(myStack.top())
print(myStack.size())
popped_value = myStack.pop()
print(popped_value)
myStack.isEmpty()
# The pop operation removes (pops) off the value from the stack, # So now the stack is empty since there was only one item in it. print “Printing size (should be 0): ”, myStack.size()







