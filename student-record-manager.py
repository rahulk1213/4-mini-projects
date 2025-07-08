student_record = []


while True:
    print("STUDENT RECORD MANAGER")
    print("1. create student record")
    print("2.update student record")
    print("3.view update record")
    print("4. exit ")


    choice = int(input("Enter your number between (1-4)"))

    if choice == 1:
     name = input("Enter your name: ")
     roll_no = input("Enter your roll number: ")
     percentage = float(input("Enter your percentage: "))

     student = {
        "name": name, "roll_no": roll_no,"percentage": percentage }

     student_record.append(student)
     print("✅ Student record created successfully!")

    elif choice ==  2:
       old_record = input("enter your updated record")
       if old_record in student_record:
          new_record = input("enter your new updated record")
          index = student_record.index(old_record)
          student_record[index] = new_record
          print("✅ Contact updated!")

       else:
            print("❌ Contact not found!")
    
    elif choice == 3:
        if not student_record:
            print("❌ No record in the list")
        else:
            print("\n📋 Your Student Record List:")
            for i, student in enumerate(student_record, start=1):
                print(f"{i}. Name: {student['name']}, Roll No: {student['roll_no']}, Percentage: {student['percentage']}")

     

    if choice == 4:
      print("exiting ! good bye") 
    else:
       print("invaild ! please enter between between (1-4)")         

    
             
