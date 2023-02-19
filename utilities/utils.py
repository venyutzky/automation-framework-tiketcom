import softest
class  Utils(softest.TestCase):
            
    def assertListItemText(self, list, value):
        for item in list:
            print("The Filter Transit is " + item.text)
            self.soft_assert(self.assertEqual, item.text, value)
            if item.text == value:
                print("test passed")
            else:
                print("test failed")
        self.assert_all()