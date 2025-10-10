def read_file(file_nm):
    try:
        with open(file_nm,"r")as f:
            cont=f.read()
            print("The content is: ")
            print(cont)
    except Exception as e:
        print(f"An error {e} has occured")

read_file("content.txt")

