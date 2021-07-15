
class linkedListNode:
	def __init__(self,value,nextNode=None):
		self.value=value
		self.nextNode=None

class linkedList:
	def __init__(self,head=None):
		self.head=head

	def insertAtBegining(self,value):
		node=linkedListNode(value,self.head) 
		self.head=node
				

	def insertAtEnd(self,value):
		node=linkedListNode(value)
		if self.head==None:
			self.head=node
			return	
		
		
		itr = self.head
		while itr.nextNode:
		    
		    itr=itr.nextNode
		itr.nextNode=node
			

	
	def printLinkedList(self):
		if(self.head==None):
			print('LinkedList is empty')
		itr=self.head
		llstr=''
		while(itr):
			llstr+=str(itr.value)+'-->' if itr.nextNode else str(itr.value)
			itr=itr.nextNode
			
		print(llstr)
	
	def countNode(self):		
		if(self.head==None):
			print('LinkedList is empty')
		itr=self.head
		count=0
		while(itr):
			count=count+1
			itr=itr.nextNode
		print(count)

	def removeNode(self,index):
		flag=0
		if(self.head==None):
				print('LinkedList is empty')
		itr=self.head
		if(itr.value==index):
			self.head=itr.nextNode
			flag=1

			
		while(itr and flag==0):
			if(itr.value==index):
				prev.nextNode=itr.nextNode	
				break
			prev=itr
			itr=itr.nextNode
		if(flag==0):
			print(str(index)+' Not Found')
		




		

if __name__ == '__main__':
    ll = linkedList()
    ll.printLinkedList()
    ll.insertAtEnd(67)
    ll.insertAtEnd(6)
    ll.insertAtEnd(7)
    ll.insertAtEnd(4)
    ll.printLinkedList()
    ll.countNode()
    ll.removeNode(67)
    ll.printLinkedList()
