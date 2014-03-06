from tree_lib import is_wildcard
import composicao_curingas
from bs4 import Tag

class node():

	def __init__(self, parent, left, right):
		self.parent = parent
		self.left = left
		self.right = right
		self.tag = Tag(name = self.get_name_node())
		self.children = 0

	def __repr__(self):
		return str((type(self.parent),self.tag.name))
	
	def add_child(self):
		self.children += 1
	
	def __eq__(self, other):
		return self.parent == other.parent and self.left == other.left and self.right== other.right

	def get_name_node(self):

		left = self.left
		right = self.right

		if(left.name == "0" or right.name == "0"):
			return "interrogacao"

		if(not is_wildcard(left) and not is_wildcard(right) and left.name != right.name ):
			return "ponto"
		
		if(not is_wildcard(left) and not is_wildcard(right) and left.name == right.name ):
			return left.name

		if(is_wildcard(left) and not is_wildcard(right)):
			return left.name
		
		if(is_wildcard(right) and not is_wildcard(left)):
			return right.name	
			
		return composicao_curingas.get_curinga(left, right)


