# Import Required Libraries
import random



if __name__ == '__main__':

    print("\n[Guess Number From Bucket Game]:")
    while(True):
        bucket = [] # Initialized a Bucket.

        for _ in range(10):
            n = random.randint(99,999)  
            bucket.append(n)    # Insert Random Values

        print("\n\t----------------Choose a Number from the bucket:---------------")
        print("\tThe Bucket: ",bucket)    # Print the Bucket.
        answer = random.choice(bucket)  # Make a Random value as Answer.


        for i in range(1,4):
            user_choice= int(input("\n\tEnter your guess: "))   # Take input from user.
            is_right = (user_choice == answer)
            if is_right:     # Checks wheather user choose right answer.
                print("\tGuess Match ^_^")
                print("\tYou Win 👑")
                break
            else:
                print("\tWrong guess!!")
                print(f"\tTry Again!!(chance left: {3-i})")   

        print("\n\n\n\t------------------------You Win-----------------------" if is_right else "\n\n\n\t------------------------You Lose-----------------------")
        # -----------------------------------------------------------------------------        
        action = input("\tWants to play again!!(press 'Y')\n\t   >> ")
        if action.casefold() != 'y':
            break 