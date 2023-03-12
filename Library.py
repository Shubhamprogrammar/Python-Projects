'''Author: Shubham Maurya'''

# Defining the class with name (library)
class library:
	def __init__(self,lob,name):
		self.lob=lob
		self.libname=name
		self.books={}

	# Function for displaying the book	
	def display_books(self):
		return f"The available books are {self.lob}"

	# Function for adding books into the library	
	def add_books(self):
		a=input("Enter the name of the book you want to add\n")
		#a=a.split(",")
		self.lob.append(a)
		return f"The books are {self.lob}"

	# Function for lending books from the library	
	def lend_books(self):
		bookname=input("Enter book name you want\n")
		personname=input("Enter person name the one who want book\t")
		# If the bookname is in library remove it from the library and add it to the user's account
		if bookname in self.lob:
			self.lob.remove(bookname)
			self.books.update({bookname:personname})
			return f"{self.lob},{self.books}"
			#b=self.lob.index(bookname)
		# If the book is already lended to someone then display the name of that person
		elif bookname in self.books.keys():
			p=self.books.get(bookname)
			return f"The book is already lended to {p}"
		
		# If book is not available in library then display it to it
		else:
			return "The book is not available in our library"

	# The function for returning the book from user		
	def return_books(self):
		a=input("Please enter the name of the book you want to return\n")
		#a=a.split(",")
		# IF the bookname is registered that it is given to someone else then take it from the user
		if a in self.books.keys():
			self.lob.append(a)
			q=self.books.get(a)
			del self.books[a]
			return f"{q} has returned the book"
		# If the bookname is not registered then display the output
		else:
			return "Yor book has not lended to anyone from our library, You might have taken from any other library"

# Object is defined							
shubh_library=library(["book1","book2", "book3","book4"],"Shubham Library")

# Function for taking the user's performance
def main():
	while True:
		user_in=input("'d' for display all the books, 'a' for add the books, 'l' for lend the books, 'r' for return the book\n")
		if user_in=="display" or user_in=="d":
			print(shubh_library.display_books())
		elif user_in=="add" or user_in=="a":
			print(shubh_library.add_books())
		elif user_in=="lend" or user_in=="l":
			print(shubh_library.lend_books())
		elif user_in=="return" or user_in=="r":
			print(shubh_library.return_books())
		else:
			return "It is invalid"			
main()
