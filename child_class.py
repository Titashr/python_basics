from classExample import newemployee

class oldemployee(newemployee):
    def __init__(self, age, name, YOE):
        super().__init__(age, name)
        self.yoe = YOE
    

    def display_old_employee(self):
        print('\n\nDetails of the old employee : \nname - '+self.name+'\nage - '+str(self.age)+'\nYear of ending - '+str(self.yoe))


B=oldemployee(50, 'Peter', 2019)
B.display_old_employee()

A = newemployee(28, 'John')
A.display_employee()