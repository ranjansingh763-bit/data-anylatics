import time

def greet_user(name):
    print(f"Hello, {name} ")

def calculate_sum(a, b):
    return a + b

def show_progress():
    for i in range(1, 6):
        print(f"Processing step {i}...")
        time.sleep(0.2)

def main():
    user_name = "Rishav"
    greet_user(user_name)

    x = 10
    y = 20
    result = calculate_sum(x, y)
    print(f"Sum of {x} and {y} is {result}")

    show_progress()

    print("Program executed successfully ")

if __name__ == "__main__":
    main()