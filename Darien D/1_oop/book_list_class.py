from ast import operator
from audioop import add
from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books=[]
		
		
		

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title,author)
		self.books.append(book)
		

	def count_books(self):
		"""Return the number of books currently in the booklist"""
		return len(self.books)

	def remove_title(self, title):
		"""Remove a book from the book list"""
		for i in range(len(self.books)-1):
			if self.books[i].title == title:
					self.books.remove(self.books[i])



	def display_titles(self):
		"""Print out all titles currently in the book list"""
		list=[]
		for book in self.books:
			list.append(book.title)
		list.sort()
		print(list)

	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		if len(self.books) == 0:
			print(True)
		elif len(self.books) > 0:
			print(False)
		

