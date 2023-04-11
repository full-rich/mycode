#!/usr/bin/env python3

wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
wordbank.append(4)
#num = int(input("Please input a number between 0 and 20"))
choice = int(input("Pick a student number"))
student_name = tlgstudents[choice]
print(f" {student_name} always uses 4 {wordbank[1]} to indent.")

