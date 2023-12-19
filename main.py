from dataType import learnDataType


def main():
    print("Let's Learn together")
    print("--------------------")
    print("[dataType]")
    print("please input like the list above")
    userInput = input("What you want to learn: ")
    
    if userInput == "dataType":
        # Memanggil fungsi dari dataType.py
        print("--------------------")
        learnDataType()
    

if __name__ == "__main__":
    main()
