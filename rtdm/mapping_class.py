#!/usr/bin/python2
# -*- coding: utf8 -*-

from tree_lib import is_wildcard, is_leaf
from bs4 import Tag
#import mapping

class hash_index(dict):
	my_hash = dict()

	def __add__(self, obj, index):
		self.my_hash[obj] = index

	def get(self, left,right):	
		return self.my_hash[self.generate_key(left, right)]	

	def generate_key(self, left, right):
		return int(str(id(left))+str(id(right)))

class Mapping():

	mape_hash = hash_index()
	extration_value = []
	wildcard = []

	def search_tuple_diff(parent, left, right):
		try:
			return Mapping.mape_hash[Mapping.mape_hash.generate_key(left, right)] 
		except:
		    return NodeMapping(parent, left, right)

	def search_tuple(*kargs):
		if(len(kargs) == 2 ):
			(parent, node) = kargs
			return Mapping.search_tuple_diff(parent, node, node)
		elif(len(kargs) == 3):
			(parent, left, right) = kargs
			return Mapping.search_tuple_diff(parent, left, right)


	search_tuple = staticmethod(search_tuple)
	search_tuple_diff = staticmethod(search_tuple_diff)



class NodeMapping(Mapping):

	def __init__(self, *kargs):
		(parent, left, right) = kargs
		self.parent = parent
		self.left = left
		self.right = right
		self.tag = Tag(name = self.get_name_node())
		NodeMapping.mape_hash[self.__hash__()] = self
		self.children = []
		if(self.parent != None):
			self.path = '%s %s ' % (self.parent.path, self.tag.name)
		else:
			self.path = ''
		self.index = -1

	def __repr__(self):
		return str(self.path)
	
	def __eq__(self, other):
		return other != None and self.parent == other.parent and self.left == other.left and self.right== other.right

	def __hash__(self):
		return int(str(id(self.left))+str(id(self.right)))

	def push_child(self, child):
		if(self != None):
			child.path = '%s %s[%d] ' % (child.parent.path, child.tag.name, child.index)
		self.children.insert(0,child)

	def append_child(self, child):
		if(self != None):
			child.path = '%s %s [%d] ' % (child.parent.path, child.tag.name, child.index)
		self.children += [child]
		
	def get_name_node(self):

		left = self.left
		right = self.right

		if(left == "0" or right == "0"):
			NodeMapping.wildcard.append(self)
			return "interrogacao"

		if(not is_wildcard(left) and not is_wildcard(right) and left.name != right.name ):
			NodeMapping.wildcard.append(self)
			return "ponto"
		
		if(not is_wildcard(left) and not is_wildcard(right) and left.name == right.name ):
			return left.name

		NodeMapping.wildcard.append(self)

		if(is_wildcard(left) and not is_wildcard(right)):
			return left.name
		
		if(is_wildcard(right) and not is_wildcard(left)):
			return right.name	
			
		return mapping.get_curinga(left, right)
	
