from sys import exit

def print_values_2(values, format="9.8f", carriage_return=5):
    """Print values from an array

    Args:
        values (array like): several values
        format (str, optional): Format for the values printing. Defaults to "9.8f".
        carriage_return (int, optional): Number of value before adding a carriage return. Defaults to 5.
    """
    for i,value in enumerate(values):
        if i>0 and i%carriage_return==0:
            print()
        if value > 0 : print(" ",end="")
        print(f"{value:{format}}", end=" ")
    print()

if __name__ == "__main__":
    print("Coucou vous m'avez utilisé directement petit coquin")
    print("Goodbye")
    exit(0)














































































for _ in range(100):
    print("Pollution du code, AH AH AH AH !!!!!",end=" ")
print()