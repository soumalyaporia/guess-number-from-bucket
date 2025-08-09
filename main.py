# Import Required Libraries
import random



if __name__ == '__main__':
    bucket = [] # Initialized a Bucket.

    for _ in range(10):
        n = random.randint(99,999)  
        bucket.append(n)    # Insert Random Values

    print("\n-------------------------------------Choose a Number from the bucket:------------------------------")
    print("The Bucket: ",bucket)    # Print the Bucket.
    answer = random.choice(bucket)  # Make a Random value as Answer.


    for i in range(1,4):
        user_choice= int(input("Enter your guess: "))   # Take input from user.
        if user_choice == answer:     # Checks wheather user choose right answer.
            print("Guess Match ^_^")
            print("You Win 👑")
            break
        else:
            print("Wrong guess!!")
            print(f"Try Again!!(chance left: {3-i})")   