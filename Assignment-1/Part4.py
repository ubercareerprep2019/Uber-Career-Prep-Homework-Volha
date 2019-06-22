class Node:
	def __init__(self, value):
		self.next = None
		self.nodeValue = value

class LinkedList:
	def __init__(self):
		self.head = None
		self.sizeValue = 0
		self.index = None


	def pushBack(self, element):
		listElement = Node(element)

		if (self.head == None): 
			self.head = listElement
			listElement.nodeValue = element
			listElement.next = None
			self.sizeValue += 1

		else:
			self.index = self.head
			while (self.index.next != None):
				self.index = self.index.next

			listElement.nodeValue = element
			self.index.next = listElement
			listElement.next = None
			self.sizeValue += 1
			self.index = None


	def popBack(self):
		if (self.sizeValue == 0):
			return print("List is Empty")	

		if (self.sizeValue == 1):
			self.head = None
			self.sizeValue -= 1

		if (self.sizeValue > 1):
			self.index = self.head
			while (self.index.next.next != None):
				self.index = self.index.next
			self.index.next = None
			self.sizeValue -= 1
			self.index = None
				


	def insert(self, i, element):
		listElement = Node(element)

		if (i <= self.sizeValue and i >= 0):

			if (self.sizeValue == 0):
				self.head = listElement
				self.head.next = None
				self.sizeValue += 1

			else:
				if (i == 0):
					listElement.next = self.head
					self.head = listElement
					self.sizeValue += 1
				else:
					self.index = self.head
					x = 0
					while(x != i-1):
						self.index = self.index.next
						x+=1
					before = self.index
					after = self.index.next
					before.next = listElement
					listElement.next = after
					self.sizeValue += 1


	def erase(self, i):
		if (i < self.sizeValue and i >= 0):

			if (self.sizeValue > 0):
				self.index = self.head

				if (self.sizeValue == 1):
					self.head = None
					self.sizeValue -= 1
					return

				if (i == 0):
					next = self.head.next
					self.head = next
					self.sizeValue -= 1
					return

				else:
					x = 0
					while (x != i-1):
						self.index = self.index.next
						x+=1
					if (self.index.next != None):
						after = self.index.next.next
						self.index.next = after
						self.sizeValue -= 1
					else:
						self.index = None
						self.sizeValue -= 1
				return


	def elementAt(self, i):
		if (i < self.sizeValue and i >= 0):
			if (self.sizeValue == 0):
				return None
			if (self.sizeValue == 1):
				return self.head.nodeValue
			else:
				self.index = self.head
				x = 0
				while (x != i):
					self.index = self.index.next
					x+=1
				return self.index.nodeValue


	def size(self):
		x = self.sizeValue
		return x

	def hasCycle(self):
		earlierNodes = set()
		self.index = self.head

		while(self.index):
			if (self.index not in earlierNodes):
				earlierNodes.add(self.index)
				self.index = self.index.next
			else:
				return True
		
		return False


	def isPalindrome(self):

		reversedSelf = []
		counter = sizeValue
		while(counter >= 0):
			reversedSelf.append(self.elementAt(counter-1))
			counter -=1
		self.index = self.head

		for value in reversedSelf:
			if (self.index.nodeValue != reversedSelf[value].nodeValue):
				return False
			else:
				self.index = self.index.next
		return True


 myLinkedList = LinkedList()
 print("LinkedList created, Expected values: 0, None \nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0))

 myLinkedList.pushBack('Lorem')
 print("\nPushed Back Lorem, Expected values: 1, Lorem \nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0))

 myLinkedList.pushBack('ipsum')
 print("\nPushed Back ipsum, Expected values: 2, Lorem, ipsum\nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0), myLinkedList.elementAt(1))

 myLinkedList.popBack()
 print("\nPoppedBack, Expected values: 1, Lorem, None \nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0), myLinkedList.elementAt(1))

 myLinkedList.pushBack('dolor')
 myLinkedList.pushBack('sit')
 myLinkedList.pushBack('amet')

 print("\nPushed Back dolor sit amet, Expected values: 4, Lorem, dolor, sit, amet\nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0), myLinkedList.elementAt(1), myLinkedList.elementAt(2), myLinkedList.elementAt(3),)

 myLinkedList.erase(2)
 print("\nErase (2), Expected values: 3, Lorem, dolor, amet, None\nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0), myLinkedList.elementAt(1), myLinkedList.elementAt(2), myLinkedList.elementAt(3),)

 myLinkedList.erase(10)
 print("\nErase (10), Expected values: 3, Lorem, dolor, amet, None\nActual values: ")
 print(myLinkedList.size(), myLinkedList.elementAt(0), myLinkedList.elementAt(1), myLinkedList.elementAt(2), myLinkedList.elementAt(3),)

 myLinkedList.elementAt(1)
 print("\nElementAt (1), Expected values: dolor \nActual values: ")
 print(myLinkedList.elementAt(1))

 myLinkedList.elementAt(11)
 print("\nElementAt (11), Expected values: None \nActual values: ")
 print(myLinkedList.elementAt(11))



