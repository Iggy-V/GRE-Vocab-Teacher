import pandas as pd
import random
import tkinter as tk
from tkinter import filedialog, simpledialog

# Function to read the Excel file and store it in a global variable
def load_excel():
    global df, shown_indices, row_range
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        shown_indices = set()  # Reset shown indices when a new file is loaded
        row_range = (0, len(df) - 1)  # Default to all rows until user selects a range
        display_random_item()

# Function to set the range of rows to be used from the input boxes
def set_row_range():
    global row_range, shown_indices
    if df is not None and not df.empty:
        start_row = simpledialog.askinteger("Input", "Enter the start row (1-based):", minvalue=1, maxvalue=len(df))
        end_row = simpledialog.askinteger("Input", "Enter the end row (1-based):", minvalue=start_row, maxvalue=len(df))
        if start_row and end_row:
            row_range = (start_row - 1, end_row - 1)  # Adjust for 0-based indexing
            shown_indices = set()  # Reset used indices for the new range
            display_random_item()


# Function to reset the used indices and counters
def reset_used_indices():
    global shown_indices, right_count, wrong_count
    shown_indices = set()
    right_count_text.set("Right: 0")
    wrong_count_text.set("Wrong: 0")
    right_count = 0
    wrong_count = 0
    display_random_item()

# Function to display a random item from the selected range
def display_random_item():
    global selected_item_index
    if df is not None and not df.empty:
        # Calculate the valid range of indices to display
        valid_indices = list(set(range(row_range[0], row_range[1] + 1)) - shown_indices)
        if valid_indices:
            selected_item_index = random.choice(valid_indices)
            item_text.set(df.iloc[selected_item_index, 0])  # Word (column 1)
            part_of_speech_text.set(df.iloc[selected_item_index, 2])  # Part of speech (column 3)
            second_column_text.set("")  # Clear the definition when a new item is selected
            example_text.set("")  # Clear the example when a new item is selected
        else:
            item_text.set("No more items available.")
            part_of_speech_text.set("")
            second_column_text.set("")
            example_text.set("")
    else:
        item_text.set("No data available. Load an Excel file.")
        part_of_speech_text.set("")
        second_column_text.set("")
        example_text.set("")

# Function to show the second column (definition) of the selected item
def show_second_column():
    if selected_item_index is not None and df is not None:
        second_column_text.set(df.iloc[selected_item_index, 1])  # Definition (column 2)
    else:
        second_column_text.set("No item selected.")

# Function to show the example from the fourth column
def show_example():
    if selected_item_index is not None and df is not None:
        example_text.set(df.iloc[selected_item_index, 3])  # Example (column 4)
    else:
        example_text.set("No example available.")

# Function to handle "Right" button click or pressing space bar
def right_button_clicked(event=None):
    global right_count, shown_indices
    if df is not None and not df.empty and selected_item_index is not None:
        right_count += 1
        right_count_text.set(f"Right: {right_count}")
        shown_indices.add(selected_item_index)  # Mark the item as used only if "Right" button is clicked
        display_random_item()

# Function to handle "Wrong" button click
def wrong_button_clicked():
    global wrong_count
    if df is not None and not df.empty and selected_item_index is not None:
        wrong_count += 1
        wrong_count_text.set(f"Wrong: {wrong_count}")
        display_random_item()

# Main window setup
root = tk.Tk()
root.title("Excel Random Item Viewer")

df = None  # Global variable to store the DataFrame
selected_item_index = None  # Variable to track the selected random item
shown_indices = set()  # Set to store indices of items that have already been shown
row_range = (0, 0)  # Range of rows to use (default 0 until set by user)

item_text = tk.StringVar()
second_column_text = tk.StringVar()
part_of_speech_text = tk.StringVar()  # Part of speech text
example_text = tk.StringVar()  # Example text

# Counters for "Right" and "Wrong"
right_count = 0
wrong_count = 0
right_count_text = tk.StringVar(value=f"Right: {right_count}")
wrong_count_text = tk.StringVar(value=f"Wrong: {wrong_count}")

# Load button to load the Excel file
load_button = tk.Button(root, text="Load Excel", command=load_excel)
load_button.pack(pady=10)


# Set range button to use the values from the input boxes
range_button = tk.Button(root, text="Set Row Range", command=set_row_range)
range_button.pack(pady=10)

# Display button to show a random item
display_button = tk.Button(root, text="Show Random Item", command=display_random_item)
display_button.pack(pady=10)

# Label to display the random word (first column)
item_label = tk.Label(root, textvariable=item_text, font=('Arial', 14))
item_label.pack(pady=10)

# Label to display the part of speech (third column), in smaller font
part_of_speech_label = tk.Label(root, textvariable=part_of_speech_text, font=('Arial', 10), fg="gray")
part_of_speech_label.pack(pady=5)

# Button to display the second column data (definition)
click_button = tk.Button(root, text="Click Me for Definition", command=show_second_column)
click_button.pack(pady=10)

# Label to display the corresponding second column data (definition)
second_column_label = tk.Label(root, textvariable=second_column_text, font=('Arial', 14), fg="blue")
second_column_label.pack(pady=10)

# Button to display the example (fourth column)
example_button = tk.Button(root, text="Show Example", command=show_example)
example_button.pack(pady=10)

# Label to display the example from the fourth column
example_label = tk.Label(root, textvariable=example_text, font=('Arial', 12), fg="purple")
example_label.pack(pady=10)

# Reset button to reset the used indices and counters
reset_button = tk.Button(root, text="Reset Used Indices", command=reset_used_indices)
reset_button.pack(pady=10)

# Right and Wrong counters displayed in green and red
right_count_label = tk.Label(root, textvariable=right_count_text, font=('Arial', 14), fg="green")
right_count_label.pack(pady=5)

wrong_count_label = tk.Label(root, textvariable=wrong_count_text, font=('Arial', 14), fg="red")
wrong_count_label.pack(pady=5)

# Right and Wrong buttons
right_button = tk.Button(root, text="Right", command=right_button_clicked, bg="green", fg="white", font=('Arial', 12))
right_button.pack(side=tk.LEFT, padx=20, pady=20)

wrong_button = tk.Button(root, text="Wrong", command=wrong_button_clicked, bg="red", fg="white", font=('Arial', 12))
wrong_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Bind keyboard events for D, E, and Space keys
root.bind('<d>', lambda event: show_second_column())
root.bind('<e>', lambda event: show_example())
root.bind('<space>', right_button_clicked)
root.bind('<w>', lambda event: wrong_button_clicked())  # Wrong action with Enter key


root.mainloop()
