def vacuum_cleaner():
    state = {'A': 'Dirty', 'B': 'Dirty'}
    vacuum_location = 'A'
    steps = 0
    while 'Dirty' in state.values():
        print(f"Step {steps}:")
        print(f"Vacuum at: {vacuum_location}")
        print(f"Status: {state}")
        if state[vacuum_location] == 'Dirty':
            print("Action: Suck")
            state[vacuum_location] = 'Clean'
        else:
            if vacuum_location == 'A':
                print("Action: Move Right to B")
                vacuum_location = 'B'
            else:
                print("Action: Move Left to A")
                vacuum_location = 'A'
        print()
        steps += 1
    print(f"Final State: {state}")
    print("All clean!")

vacuum_cleaner()
