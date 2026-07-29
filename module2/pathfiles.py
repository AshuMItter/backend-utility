from pathlib import Path

directory = Path(__file__).resolve().parent.parent/"datascv2"/ "demo.json"





#directory.mkdir(parents=True,exist_ok=True)

print(directory.exists())

print(directory.suffix)



# from pathlib import Path

# pathv = Path(__file__).resolve().parent.parent / "datajson"/ "somelines.txt"

# newPathv= Path(__file__).resolve().parent.parent / "somedata"

# print(f"Data path: {pathv}")

# newPathv.mkdir(parents=True, exist_ok=True) 
# newPathv.rmdir() # Create the directory if it doesn't exist

# print(f"Data path from module2: {pathv.home()}")
# print(f"Data path from module2: {pathv.cwd()}")


# print(f"Data path from module2: {pathv.name}, {pathv.stem}, {pathv.suffix}, {pathv.parent}, {pathv.parent.parent}")          # 'input.json'
# print(f"Data path from module2: {pathv.stem}")          # 'input'
# print(f"Data path from module2: {pathv.suffix}")        # '.json'
# print(f"Data path from module2: {pathv.parent}")        # 'data'
# print(f"Data path from module2: {pathv.parent.parent}") # Grandparent directory
# print(f"Data path from module2: {pathv.exists()}")     # True if the file exists, False otherwise





with open(directory,'w',encoding='utf-8') as f:
    f.writelines("Some non json data")



with open(directory,'a',encoding='utf-8') as a:
   a.writelines("\n Some more lines")



with open(directory,'r',encoding='utf-8') as file:
    print(file.readline())
    print(file.readline())
       
    
# with open(pathv, 'r') as file:
#     for line in file:
#         print(f"Line from somelines: {line.strip()}")
        
# with open(pathv, 'a', encoding='utf-8') as file:      
#     file.write("This is a new line.\n")


# with open(pathv, 'r', encoding='utf-8') as file:
#     for line in file:
#         print(f"Line from somelines: {line.strip()}")


# with open(pathv, 'w', encoding='utf-8') as f:
#     f.write('Hello 世界')  
#     #data = file.readline() 

# with open(pathv, 'r', encoding='utf-8') as file:
#     for line in file:
#         print(f"Line from somelines: {line.strip()}")

    #print(f"Data from somelines {data}")

