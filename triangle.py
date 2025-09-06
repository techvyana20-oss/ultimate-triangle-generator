import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- Helper for coloring ---
def colored(text, color):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE
    }
    return colors.get(color, Fore.WHITE) + text + Style.RESET_ALL

# --- Core Triangle Generator ---
def draw_triangle(size=5, triangle_type="equilateral", orientation="normal",
                  fill="solid", pattern="star", color="green"):
    """
    Draws any triangle based on parameters.
    
    Parameters:
        size : int : Height of triangle
        triangle_type : str : equilateral, isosceles, scalene, right
        orientation : str : normal, inverted, rotate90, rotate180, rotate270
        fill : str : solid, hollow
        pattern : str : star, number, letter, fibonacci, pascal, sierpinski
        color : str : red, green, yellow, blue, magenta, cyan
    """
    
    # Helper for pattern selection
    def get_char(i=0, j=0, seq={"num":1,"alpha":65,"fib":[0,1]}):
        if pattern == "star":
            return "*"
        elif pattern == "number":
            val = seq["num"]
            seq["num"] += 1
            return str(val)
        elif pattern == "letter":
            val = chr(seq["alpha"])
            seq["alpha"] += 1
            if seq["alpha"] > 90:  # Loop A-Z
                seq["alpha"] = 65
            return val
        elif pattern == "fibonacci":
            val = seq["fib"][0]
            seq["fib"] = [seq["fib"][1], seq["fib"][0]+seq["fib"][1]]
            return str(val)
        elif pattern == "pascal":
            from math import comb
            return str(comb(i,j))
        elif pattern == "sierpinski":
            if (i & j) == 0:
                return "*"
            else:
                return " "
        else:
            return "*"
    
    # Draw function
    def print_row(text):
        print(colored(text, color))
    
    seq = {"num":1,"alpha":65,"fib":[0,1]}  # Sequence trackers
    n = size

    # Equilateral / Isosceles / Pyramid
    if triangle_type in ["equilateral","isosceles","pyramid"]:
        for i in range(1, n+1):
            if orientation == "normal":
                spaces = n - i
            elif orientation == "inverted":
                spaces = 0
            else:
                spaces = n - i
            row = ""
            for j in range(i):
                char = get_char(i-1,j,seq)
                if fill == "hollow" and j not in [0,i-1] and i!=n:
                    row += "  " if pattern=="star" else " "
                else:
                    row += str(char) + " "
            print_row(" "*spaces + row)
        if orientation == "inverted":
            for i in range(n-1,0,-1):
                row = ""
                for j in range(i):
                    char = get_char(i-1,j,seq)
                    if fill == "hollow" and j not in [0,i-1] and i!=1:
                        row += "  " if pattern=="star" else " "
                    else:
                        row += str(char) + " "
                print_row(row)
    
    # Right-angled triangles
    elif triangle_type == "right":
        for i in range(1, n+1):
            row = ""
            for j in range(i):
                char = get_char(i-1,j,seq)
                if fill=="hollow" and j not in [0,i-1] and i!=n:
                    row += " "
                else:
                    row += str(char)
            if orientation == "normal":
                print_row(row)
            elif orientation == "inverted":
                print_row(" "*(n-i) + row)
            elif orientation == "rotate90":
                for _ in range(n-i):
                    print()
                print_row(row)
            elif orientation == "rotate180":
                print_row(row[::-1])
            elif orientation == "rotate270":
                print_row(row)
    
    # Scalene (example)
    elif triangle_type=="scalene":
        for i in range(1,n+1):
            row = ""
            for j in range(i):
                char = get_char(i-1,j,seq)
                if fill=="hollow" and j not in [0,i-1] and i!=n:
                    row += " "
                else:
                    row += str(char)
            print_row(row)
    
    # Explanation
    print("\nExplanation:")
    print(f"Type: {triangle_type.capitalize()}, Orientation: {orientation}, Fill: {fill}, Pattern: {pattern}, Size: {size}")
    print("This triangle is generated dynamically using parameters, combining patterns, orientations, and fills.\n")


# --- Random Triangle Generator ---
def random_triangle(size=5):
    triangle_type = random.choice(["equilateral","isosceles","pyramid","right","scalene"])
    orientation = random.choice(["normal","inverted","rotate90","rotate180","rotate270"])
    fill = random.choice(["solid","hollow"])
    pattern = random.choice(["star","number","letter","fibonacci","pascal","sierpinski"])
    color = random.choice(["red","green","yellow","blue","magenta","cyan"])
    draw_triangle(size, triangle_type, orientation, fill, pattern, color)

# --- Main Menu ---
def main():
    print(colored("Welcome to the Ultimate Infinite Triangle Generator!", "cyan"))
    try:
        size = int(input("Enter triangle size (e.g., 5): "))
        if size <= 0:
            print("Size must be positive.")
            return

        while True:
            print("\nSelect option:")
            print("1. Generate Custom Triangle")
            print("2. Generate Random Triangle")
            print("3. Generate Multiple Random Triangles")
            print("0. Exit")
            choice = input("Enter choice: ")

            if choice=="1":
                t_type = input("Triangle type (equilateral, isosceles, pyramid, right, scalene): ").strip().lower()
                orientation = input("Orientation (normal, inverted, rotate90, rotate180, rotate270): ").strip().lower()
                fill = input("Fill type (solid, hollow): ").strip().lower()
                pattern = input("Pattern (star, number, letter, fibonacci, pascal, sierpinski): ").strip().lower()
                color = input("Color (red, green, yellow, blue, magenta, cyan): ").strip().lower()
                draw_triangle(size, t_type, orientation, fill, pattern, color)
            elif choice=="2":
                random_triangle(size)
            elif choice=="3":
                count = int(input("How many triangles to generate? "))
                for _ in range(count):
                    random_triangle(size)
            elif choice=="0":
                print(colored("Exiting. Goodbye!", "red"))
                break
            else:
                print("Invalid choice.")

    except ValueError:
        print("Invalid input. Enter numbers where required.")

if __name__=="__main__":
    main()
