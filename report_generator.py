def student_average():
        name=str(input("Enter your name: "))
        marks1= int(input("Enter the first Backend marks: "))
        marks2= int(input("Enter the first Fronend marks: "))
        marks3= int(input("Enter the first Design marks: "))
        average=(marks1 + marks2 + marks3)/3
        return  name,marks1,marks2,marks3,average



def grading(average):
        if average >= 80 :
                return "A"
        elif average >=70:
                return "B"
        elif average >=60:
                return "C" 
        elif average >=50:
                return "D" 
        else:
                return "E" 
                 
def student_report():
        name,marks1,marks2,marks3,average= student_average()
        grade = grading(average)
        report = {
                "Name": name,"Subject1":marks1,"Subject2":marks2,"Subject3":marks3,"average":average,"grade":grade}
        print(report)
            
        
student_report()  



