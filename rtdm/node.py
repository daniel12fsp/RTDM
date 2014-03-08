from tree_lib import is_wildcard
import composicao_curingas
from bs4 import Tag

class hash_index(dict):
	my_hash = dict()
	def __add__(self, obj, index):
		self.my_hash[obj] = index
	def get(self, left,right):	
		return self.my_hash[self.generate_key(left, right)]	

	def generate_key(self, left, right):
		return int(str(id(left))+str(id(right)))

class Mapeamento():
	index = hash_index()
	def __init__(self, *kargs):

		if(len(kargs) == 2 ):
			(parent, tag) = kargs
			self.parent = parent
			self.left = tag 
			self.right = tag
			self.tag = Tag(name = tag.name)
			left = right = tag

		elif(len(kargs) == 3):
			(parent, left, right) = kargs
			self.parent = parent
			self.left = left
			self.right = right
			self.tag = Tag(name = self.get_name_node())
			self.index[self.index.generate_key(left, right)] = self

		self.children = []
	def __repr__(self):
	#	if(self.parent == None):
	#		return str(("None",self.tag.name,self.children))
	#	else:
			return str((self.tag.name,self.children))
	
	def add_child(self, child):
		self.children += [child]
	
	def __eq__(self, other):
		return other != None and self.parent == other.parent and self.left == other.left and self.right== other.right

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
	
	def __hash__(self):
		return int(str(id(self.left))+str(id(self.right)))


class Node(Mapeamento):
	def __new__(cls, *kargs):
		if(len(kargs) == 2 ):
			(parent,left) = kargs
			right = left
		elif(len(kargs) == 3):
			(parent, left, right) = kargs
		try:
			return cls.index[cls.index.generate_key(left, right)] 
		except:
		    return Mapeamento(parent, left, right)
