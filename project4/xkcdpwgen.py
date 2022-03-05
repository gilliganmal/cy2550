Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World

with open('words.txt','r') as file:
      
    for line in file:
        
        for word in line.split():
             
            print(word)