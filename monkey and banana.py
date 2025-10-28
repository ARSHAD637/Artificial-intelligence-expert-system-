# Monkey and Banana Problem Simulation

class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = "A"
        self.box_position = "B"
        self.banana_position = "C"
        self.on_box = False
        self.has_banana = False

    def display_state(self):
        print(f"Monkey: {self.monkey_position}, Box: {self.box_position}, On Box: {self.on_box}, Has Banana: {self.has_banana}")

    def move_monkey(self, position):
        print(f"Monkey moves from {self.monkey_position} to {position}.")
        self.monkey_position = position

    def push_box(self, position):
        if self.monkey_position == self.box_position:
            print(f"Monkey pushes box from {self.box_position} to {position}.")
            self.box_position = position
            self.monkey_position = position
        else:
            print("Monkey must be at the box to push it!")

    def climb_box(self):
        if self.monkey_position == self.box_position:
            print("Monkey climbs on the box.")
            self.on_box = True
        else:
            print("Monkey must be at the box to climb it!")

    def grab_banana(self):
        if self.on_box and self.box_position == self.banana_position:
            print("Monkey grabs the banana! 🍌")
            self.has_banana = True
        else:
            print("Monkey cannot reach the banana yet!")

    def solve(self):
        print("\nInitial State:")
        self.display_state()

        # Step 1: Move monkey to the box
        self.move_monkey("B")

        # Step 2: Push box to banana position
        self.push_box("C")

        # Step 3: Climb the box
        self.climb_box()

        # Step 4: Grab the banana
        self.grab_banana()

        print("\nFinal State:")
        self.display_state()


# Run the simulation
problem = MonkeyBananaProblem()
problem.solve()
