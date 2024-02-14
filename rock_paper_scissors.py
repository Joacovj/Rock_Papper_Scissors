import random

def main():
    option = 0
    input_valid = False

    print("Please choose your language / Por favor elija el idioma: " +
            "\n1) English \n2) Español")

    while not input_valid:
        input_valid = True

        try:
            option = int(input())
            while option != 1 and option != 2:
                print("The input is invalid, please choose again / " +
                        "Lo que ha ingresado es incorrecto, por favor ingrese entre: " +
                        "\n1) English \n2) Español")                
                option = int(input())

        except ValueError:
            print("The input is invalid, please choose again / " +
                    "Lo que ha ingresado es incorrecto, por favor ingrese entre: " +
                    "\n1) English \n2) Español")            
            input_valid = False

    if option == 1:
        game_english()
    else:
        game_spanish()



def game_english():
    option = 0
    continue_playing = False
    input_valid = False

    # Asking player if he wants to start the game or exit.

    print("Select 1 or 2: \n1) Start Game \n2) Exit Game")

    while not input_valid:
        try:
            option = int(input())
            input_valid = True

            while option != 1 and option != 2:
                print("You selected a number that isn't on the menu, please choose between: \n1) Start Game \n2) Exit Game")                
                option = int(input())

        except ValueError:
            input_valid = False
            print("Your input was invalid, please choose between: \n1) Start Game \n2) Exit Game")
            

    # If player wants to play, now he must choose between Rock Paper Scissors

    if option == 1:
        continue_playing = True

    while continue_playing:
        input_valid = False

        print("Choose: \n1) Rock \n2) Paper \n3) Scissors")
        while not input_valid:
            try:
                option = int(input())
                input_valid = True

                while option != 1 and option != 2 and option != 3:
                    print("You selected a number that isn't on the menu, please choose between: \n1) Rock \n2) Paper \n3) Scissors")                    
                    option = int(input())
            except ValueError:
                input_valid = False
                print("Your input was invalid, please choose between: \n1) Rock \n2) Paper \n3) Scissors")
                

        # Generating what the computer is going to choose
        
        computer = random.randint(1, 3)

        # Results of the game:

        if option == 1:
            if computer == 1:
                print("Its a DRAW!")
            if computer == 2:
                print("The computer picked Paper, you LOSE!")
            if computer == 3:
                print("The computer picked Scissors, you WON!")
        elif option == 2:
            if computer == 1:
                print("The computer picked Rock, you WON!")
            if computer == 2:
                print("Its a DRAW!")
            if computer == 3:
                print("The computer picked Scissors, you LOSE!")
        elif option == 3:
            if computer == 1:
                print("The computer picked Rock, you LOSE!")
            if computer == 2:
                print("The computer picked Paper, you WON!")
            if computer == 3:
                print("Its a DRAW!")               

        # Asking if the player wants to continue playing

        print("\nWould you like to continue playing?" + "\n1) Yes \n2) No")

        input_check = False

        while not input_check:        
            input_check = True

            try:
                option = int(input())

                while option != 1 and option != 2:
                    print("You selected a number that isn't on the menu, please choose between:" +
                        "\n1) Continue playing" + "\n2) Exit game")                    
                    option = int(input())
            except Exception as e:            
                input_check = False
                print("Your input was invalid, please choose between: " +
                    "\n1) Continue playing" + "\n2) Exit game")
                

        if option == 1:
            continue_playing = True
        else:
            continue_playing = False
            print("You exited the game")

        

def game_spanish():    
    option = 0
    continue_playing = False
    input_valid = False

    # Asking player if he wants to start the game or exit.

    print("Seleccione 1 o 2: " + "\n1) Jugar" + "\n2) Salir del Juego")

    while not input_valid:
        try:
            option = int(input())
            input_valid = True

            while option != 1 and option != 2:
                print("Ha seleccionado un numero invalido, por favor elija entre: " +
                      " \n1) Jugar  \n2) Salir del juego")                
                option = int(input())

        except ValueError:
            input_valid = False
            print("La entrada es invalida, por favor elija entre: \n1) Jugar  \n2) Salir del juego")            

    # If player wants to play, now he must choose between Rock Paper Scissors

    if option == 1:
        continue_playing = True

    while continue_playing:
        input_valid = False

        print("Elija: " + "\n1) Roca" + "\n2) Papel" + "\n3) Tijera")
        while not input_valid:
            try:
                option = int(input())
                input_valid = True

                while option != 1 and option != 2 and option != 3:
                    print("Ha seleccionado un numero invalido, por favor elija entre:" +
                          "\n1) Roca" + "\n2) Papel" + "\n3) Tijera")                    
                    option = int(input())
            except ValueError:
                input_valid = False
                print("La entrada es invalida, por favor elija entre: " +
                      "\n1) Roca" + "\n2) Papel" + "\n3) Tijera")                

        # Generating what the computer is going to choose
        
        computer = random.randint(1, 3)

        # Results of the game:

        if option == 1:
            if computer == 1:
                print("Es un EMPATE!")
            if computer == 2:
                print("La PC a elejido Papel, has PERDIDO!")
            if computer == 3:
                print("La PC a elejido tijera, has GANADO!")
        elif option == 2:
            if computer == 1:
                print("La PC a elejido Roca, has GANADO!")
            if computer == 2:
                print("Es un EMPATE!")
            if computer == 3:
                print("La PC a elejido Tijera, has PERDIDO!")
        elif option == 3:
            if computer == 1:
                print("La PC a elejido Roca, has PERDIDO!")
            if computer == 2:
                print("La PC a elejido Papel, has GANADO!")
            if computer == 3:
                print("Es un EMPATE!")                

        # Asking if the player wants to continue playing

        print("\n¿Quieres seguir jugando?" + "\n1) Si \n2) No")

        input_check = False

        while not input_check:
            input_check = True

            try:
                option = int(input())

                while option != 1 and option != 2:
                    print("Ha seleccionado un numero invalido, por favor elija entre: " +
                          "\n1) Continuar jugando" + "\n2) Salir del Juego")                    
                    option = int(input())
            except Exception as e:
                input_check = False
                print("La entrada es invalida, por favor elija entre: " +
                      "\n1) Continuar jugando" + "\n2) Salir del Juego")                

        if option == 1:
            continue_playing = True
        else:
            continue_playing = False
            print("Has salido del juego")

if __name__ == "__main__":
    main()