print("This is a program to check if two numbers are equal or not")  # दोन संख्या समान आहेत का ते तपासण्यासाठी प्रोग्राम

a = int(input("Enter first number: "))  # पहिला नंबर वापरकर्त्यांकडून घेणे आणि तो integer मध्ये convert करणे
b = int(input("Enter second number: ")) # दुसरा नंबर वापरकर्त्यांकडून घेणे आणि तो integer मध्ये convert करणे

if a != b:  # जर 'a' आणि 'b' वेगवेगळे असतील (equal नसतील) तर
    print("The numbers are not equal")  # संख्या समान नाहीत असे प्रिंट करा
else:
    print("The numbers are equal")  # जर वरची अट false असेल, म्हणजे दोन्ही संख्या समान असतील, तर हे प्रिंट करा
