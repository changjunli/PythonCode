import unittest
from name_function import get_formatted_name
"""
unittest模块中的断言方法

assertEqual(a,b)表示核实a == b 

assertNotEqual(a,b)表示核实a != b 

assertTrue(x)表示核实x为True

assertFalse(x)表示核实x为False

assertIn(item,list) 表示核实item在list中

assertNotIn(item,list) 表示核实item不在list中
"""
class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin') # 检查返回的姓名是否与预期的姓名一致。断言方法 assertEqual(a,b)表示核实a == b 

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart') # 检查返回的姓名中间名是否与预期的姓名中间名一致

if __name__ == '__main__':
	unittest.main()