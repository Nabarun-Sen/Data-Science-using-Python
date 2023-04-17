class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
        
    def work(self):
        if self.occupation == 'tennis':
            print(self.name,'Plays Tennis')
        elif self.occupation == 'actor':
            print(self.name,'Shoots Movie')

    def speak(self):
        print(self.name, "Says What's Up")

t=Human("Tom Cruise", "actor")
t.work()
t.speak()
print('\n')
t=Human("Sania Mirza", "tennis")
t.work()
t.speak()