import abc
class Parent(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self,val):
		self.val = val
	def set_val(self,val):
		self.val = val
	def get_val(self):
		return self.val
	@abc.abstractmethod
	def showdoc(self):
		return
class FirstBorn(Parent):
        pass
