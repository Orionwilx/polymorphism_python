from presentation.presentation_layer import PresentationLayer
from os import system

def main():
    presetation = PresentationLayer()

    while True:
        print("\n1. Add item")
        print("2. Display item")
        print("3. Exit")
        option = input("Select an option: ")
        system('cls')

        if option == "1":
            presetation.add_item()
            system('cls')

        elif option == "2":
            presetation.display_items()

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Option. Please try again.")

if __name__ == "__main__":
    main() 