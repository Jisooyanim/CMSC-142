import random

def guesser(low, high):
    computer = random.randint(low, high)
    print(f"Secret number: {computer}")
    mid = (low + high)//2
    userInput = None
    while computer != userInput:
        userInput = int(input("Enter a number: "))
        if userInput == computer:
            print("Congratulations")
        elif computer > mid:
            low = mid + 1
            mid = (low + high) //2
            print(f"Between {low} and {high}")
        elif computer < mid:
            high = mid - 1
            mid = (low + high) // 2
            print(f"Between {low} and {high}")

if __name__ == '__main__':
    low = 1
    high = 100
    guesser(1, 100)