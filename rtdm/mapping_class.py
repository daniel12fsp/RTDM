#!/usr/bin/python2
# -*- coding: utf8 -*-

from tree_lib import is_wildcard, is_leaf, equal
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
	"""
		Class reponsavel por controlar os nós existentes e criar os novos no mapeamento
	"""

	index = hash_index()
	extration_value = []

	composicao_curingas = {
		"asterisco,asterisco" : "asterisco",
		"asterisco,mais" : "asterisco",
		"asterisco,interrogacao" : "asterisco",
		"asterisco,ponto" : "asterisco",
		"mais,mais" : "mais",
		"mais,ponto" : "mais",
		"mais,interrogacao" : "asterisco",
		"ponto,ponto" : "ponto",
		"ponto,interrogacao" : "interrogacao",
		"interrogacao,interrogacao" : "interrogacao"
	}

	def search_tuple_diff(parent, left, right):
		try:
			return Mapping.index[Mapping.index.generate_key(left, right)] 
		except:
		    return NodeMapping(parent, left, right)

	def search_tuple(*kargs):
		"""
			Procura a existencia do no e retorna este se nao cria um novo no
		"""
		if(len(kargs) == 2 ):
			(parent, node) = kargs
			return Mapping.search_tuple_diff(parent, node, node)
		elif(len(kargs) == 3):
			(parent, left, right) = kargs
			return Mapping.search_tuple_diff(parent, left, right)


	search_tuple = staticmethod(search_tuple)
	search_tuple_diff = staticmethod(search_tuple_diff)



class NodeMapping(Mapping):
	"""
		Classe responsavel por interligar os nos semelhantes das diferentes arvores
	"""

	def __init__(self, *kargs):
		(parent, left, right) = kargs
		self.parent = parent
		self.left = left
		self.right = right
		self.tag = self.get_node()
		NodeMapping.index[self.__hash__()] = self
		self.children = []

	def __repr__(self):
		return str((self.tag.name,self.children))
	
	def __eq__(self, other):
		return other != None and self.parent == other.parent and self.left == other.left and self.right== other.right

	def __hash__(self):
		"""
			chave = "id(left)" + "id(right)"
		"""
		return int(str(id(self.left))+str(id(self.right)))

	def push_child(self, child):
		"""
			Insere no inicio da lista
		"""
		self.children.insert(0,child)

	def append_child(self, child):
		"""
			Insere no final da lista
		"""
		self.children.append(child)
		
	def get_node(self):
		def get_curinga(n1, n2):
			if(type(n1) is str):
				return Mapping.composicao_curingas[n1+","+n2]
			else:
				return Mapping.composicao_curingas[n1.name+","+n2.name]
		"""
			Gera o nome da tag com base dos elementos mapeamento(o filho da arvore1 e o filho da arvore2).
			Regra.:
		
			Se algum tiver "0", eh interrogacao
			Se os nós forem diferentes, eh ponto
			obs.: o uso de curingas é só usado quando são árvores
			Se caso algum dos dois sejam coringas então retorna o mais abrangente
			Se caso contrario usa tabela, ver definição na tese do Davi. pag...
			
			
		"""

		left = self.left
		right = self.right
		"""
		try:
			print(is_wildcard(left),is_leaf(left), left.name)
			print(is_wildcard(right), is_leaf(right), right.name)
			print(right.string == left.string, right.name == left.name)
		except:
			pass

		"""


		if(left == "0" or right == "0"):
			tag_name = "interrogacao"

		elif(not is_wildcard(left) and not is_wildcard(right)):
			if(is_leaf(left) and is_leaf(right) and not equal(left, right)):
				tag_name = "ponto"
			else:
				tag_name = left.name
		elif(is_wildcard(left) and not is_wildcard(right)):
			return left
		
		elif(is_wildcard(right) and not is_wildcard(left)):
			return right
		else:
			tag_name = get_curinga(left, right)

		return Tag(name = tag_name)
