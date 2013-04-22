import unittest
import rfcomm_client as rf

class Test(unittest.TestCase):

    def test_parse_reading(self):
        s1 = '89.00\n90.00\n91.00\n'
        s2 = ''
        s3 = '6.00'
        s4 = '1394.00\n'
        s5 = 'Serial overload\nSerial overload\n'
        s6 = 'Serial overload\n111.00\nSerial overload\n'
        s7 = '22'
        self.assertEqual( rf.parse_reading(s1) , 91)
        assert rf.parse_reading(s2) == -1
        assert rf.parse_reading(s3) == 6
        self.assertEqual( rf.parse_reading(s4) , 1394)
        assert rf.parse_reading(s5) == -1
        self.assertEqual( rf.parse_reading(s6) , 111)
        self.assertEqual(rf.parse_reading(s7),22)
        

if __name__ == '__main__':
    unittest.main()
