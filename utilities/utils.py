
class  Utils():
    
    def assertListItemText(self, list, value):
        for item in list:
            print("The Airplane is : " + item.text)
            assert item.text == value
            print("assert pass")