import unittest
import sys
class CollAssert(unittest.TestCase):


    mylist=["1","2","3"]
    Herlist=["1","2","3"]
    # enternum = input("Enter a list of integers separated by spaces: ")

    # def Entry(self):

    #     return self.enternum


    def test_CheckList(self):
        self.assertEqual(self.mylist,self.Herlist, "Not equal")
    def test_SimilarVlues(self):
        
        self.assertIn(self.mylist[0],self.Herlist, "Not present")
        
    
       
if __name__ == '__main__':
    unittest.main()
   
