# Towers of Hanoi Recursive Solution

def towers_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Towers of Hanoi problem.
    
    Parameters:
        n (int): Number of disks
        source (str): The source peg
        target (str): The target peg
        auxiliary (str): The auxiliary peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    # Move n-1 disks from source to auxiliary
    towers_of_hanoi(n - 1, source, auxiliary, target)
    
    # Move the remaining largest disk to target
    print(f"Move disk {n} from {source} → {target}")
    
    # Move the n-1 disks from auxiliary to target
    towers_of_hanoi(n - 1, auxiliary, target, source)


# Example usage
num_disks = int(input("Enter the number of disks: "))
print(f"\nSteps to solve Towers of Hanoi with {num_disks} disks:\n")
towers_of_hanoi(num_disks, 'A', 'C', 'B')
