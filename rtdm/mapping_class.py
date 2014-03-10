#!/usr/bin/python2
# -*- coding: utf8 -*-

from tree_lib import is_wildcard
from bs4 import Tag
import mapping

class hash_index(dict):
	my_hash = dict()
	def __add__(self, obj, index):
		self.my_hash[obj] = index
	def get(self, left,right):	
		return self.my_hash[self.generate_key(left, right)]	

	def generate_key(self, left, right):
		return int(str(id(left))+str(id(right)))

class Mapping():

	index = hash_index()

	def search_tuple_diff(parent, left, right):
		try:
			return Mapping.index[Mapping.index.generate_key(left, right)] 
		except:
		    return NodeMapping(parent, left, right)

	def search_tuple(*kargs):
		if(len(kargs) == 2 ):
			(parent, node) = kargs
			return Mapping.search_tuple_diff(parent, node, node)
		elif(len(kargs) == 3):
			(parent, left, right) = kargs
			return Mapping.search_tuple_diff(parent, left, right)




class NodeMapping(Mapping):

	def __init__(self, *kargs):
		(parent, left, right) = kargs
		self.parent = parent
		self.left = left
		self.right = right
		self.tag = Tag(name = self.get_name_node())
		NodeMapping.index[self.index.generate_key(left, right)] = self
		self.children = []

	def __repr__(self):
		return str((self.tag.name,self.children))
	
	def push_child(self, child):
		self.children.insert(0,child)

	def append_child(self, child):
		self.children += [child]
	
	def __eq__(self, other):
		return other != None and self.parent == other.parent and self.left == other.left and self.right== other.right

	def get_name_node(self):

		left = self.left
		right = self.right

		if(left == "0" or right == "0"):
			return "interrogacao"

		if(not is_wildcard(left) and not is_wildcard(right) and left.name != right.name ):
			return "ponto"
		
		if(not is_wildcard(left) and not is_wildcard(right) and left.name == right.name ):
			return left.name

		if(is_wildcard(left) and not is_wildcard(right)):
			return left.name
		
		if(is_wildcard(right) and not is_wildcard(left)):
			return right.name	
			
		return mapping.get_curinga(left, right)
	
	def __hash__(self):
		return int(str(id(self.left))+str(id(self.right)))
