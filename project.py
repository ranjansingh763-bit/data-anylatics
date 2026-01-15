import time

def greet_user(name):
    print(f"Hello, {name} ")

def calculate_sum(a, b):
    return a + b

def show_progress():
    for i in range(1, 6):
        print(f"Processing step {i}...")
        time.sleep(0.2)

# 🔽 NEW 10 LINES START HERE
def calculate_square(n):
    return n * n

def show_time():
    current_time = time.strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

def status_message(msg):
    print(f"[STATUS]: {msg}")
# 🔼 NEW 10 LINES END HERE

def main():
    user_name = "Rishav"
    greet_user(user_name)

    x = 10
    y = 20
    result = calculate_sum(x, y)
    print(f"Sum of {x} and {y} is {result}")

    show_progress()

    square = calculate_square(5)
    print(f"Square of 5 is {square}")

    show_time()
    status_message("All tasks completed successfully")

    print("Program executed successfully ")

if __name__ == "__main__":
    main()