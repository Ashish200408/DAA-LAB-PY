# DFA Simulation Program

def simulate_dfa(transition_table, initial_state, final_states, input_string):
    current_state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        # Check if transition exists
        if symbol not in transition_table[current_state]:
            print(f"No transition defined for state {current_state} on symbol '{symbol}'")
            return False
        
        # Move to next state
        current_state = transition_table[current_state][symbol]

    # Check if final state is reached
    if current_state in final_states:
        return True
    else:
        return False


# -----------------------------
# Example DFA Definition
# -----------------------------

# Transition table (dictionary format)
transition_table = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q1'},
    'q2': {'0': 'q0', '1': 'q1'}
}

# Initial state
initial_state = 'q0'

# Final states
final_states = {'q2'}

# Input string
input_string = input("Enter input string (only 0s and 1s): ")

# Run DFA
if simulate_dfa(transition_table, initial_state, final_states, input_string):
    print("String is ACCEPTED")
else:
    print("String is REJECTED")