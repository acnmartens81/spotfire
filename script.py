import sys
import math

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a single number as input.")
        sys.exit(1)
    
    try:
        number = float(sys.argv[1])
        result = math.sqrt(number)
        print(result)  # Output the result
    except ValueError:
        print("Error: Invalid number provided.")
        sys.exit(1)

if __name__ == "__main__":
    main()
