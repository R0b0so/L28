class Reverse:
    def __init__(self, string):
        self.string = string
    def reverse(self):
        return(self.string[::-1])
str = input("enter any string ")
rev = Reverse(str)
print(rev.reverse())



        
        

        