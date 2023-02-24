import pickle
number_assignments = 2
filename = 'students'
grades = ('S', 'G', 'R', 'U', 'F') 
passed = ('S', 'G', 'R')


def prompt_for_int(prompter, low, high):
    while True:     
        ans = input(prompter)
        try:
            x = int(ans)
            if low <= x <= high:
                return x
            print(f'Ange värde mellan  {low} och {high}')
        except ValueError:
            print('Fel värde: ', ans)
            print(f'Svara med heltal mellan {low} och {high}')


def prompt_for_string(prompter, legal_values):
    while True:
        ans = input(prompter)
        if ans in legal_values:
            return ans
        print(f'{ans} är inte ett giltigt svar')

        

class Student:
    def __init__(self, name):
       self.name = name
       
       self.grade = [(x,'-') for x in range(1,number_assignments+1)]

    def __str__(self):
        return f'{self.name} {self.grade}'

    def update(self, ass, grade):  

        if '-' not in self.grade[ass-1]:
            print(f'Ändrar betyg {ass} till {grade}')
        
        self.grade[ass-1] = (ass,grade)
       
    def done(self):
        sum =0
        for i in self.grade:
            if i in passed:
                    sum+=1
            if sum == number_assignments:
                return True
            return False







class StudentList:
    def __init__(self):
        self.var = []
        
    def print_status(self):
        print()
        print('Status')
        print('======')
        for s in self.var:
            
            print(s)
        print()
        print()
        print()
        

    def add(self, name):
        self.var.append(Student(name))
        return self.var[-1]
    def find(self, name):
        for s in self.var:
            if name == s.name:
                return s
        return None

def handle_student(name):
    
    student = students.find(name)
    if student == None:
        ans = prompt_for_string('Okänd student. Addera? (j/n) ', ['j', 'n'])
        if ans == 'n':
            return
        student = students.add(name)
        
    ass = prompt_for_int('Uppgift (0 om inget ska ändras): ', 0, number_assignments)
    if ass > 0:
        grade = prompt_for_string(f'Betyg: {grades} ', grades)
        student.update(ass, grade)
def initialize():
    global students
    print('\nVälkommen till StudentStatus!\n')
    print('number of assignments: ',number_assignments)
    try:
        with open(filename, 'rb') as pfile:
            students = pickle.load(pfile)
        students.print_status()
    except:
        students



def finalize():
    ans = prompt_for_string('Spara fil (j/n): ', ['j', 'n'])
    if ans == 'j':
        with open(filename, 'wb') as pfile:
            pickle.dump(students, pfile)
        print(f"Resultaten sparade på filen '{filename}'")
    else:
        print('Inget sparat')



def main():
    initialize()
    while True:
        name = input("\nNamn (sluta med tom rad): ")
        if name == '':
            students.print_status()
            break
            
        handle_student(name)
    finalize()



students = StudentList()
main()
