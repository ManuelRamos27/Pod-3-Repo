from operator import indexOf
from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books = []

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title, author)
		self.books.append(book)

	def count_books(self):
		"""Return the number of books currently in the book list"""
		return len(self.books)

	
	def remove_title(self, title):
		"""Remove a book from the book list"""
		[self.books.remove(book) for book in self.books if book.title == title]

	def display_titles(self):
		"""Print out all titles currently in the book list"""
		print(sorted([book.title for book in self.books]))


	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		return len(self.books) == 0