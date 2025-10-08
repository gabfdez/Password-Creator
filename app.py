import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length=12, include_numbers=True, include_symbols=True):
    """
    Generate a secure but simple password suitable for older adults.
    
    Args:
    - length (int): The desired length of the password.
    - include_numbers (bool): Whether to include numbers.
    - include_symbols (bool): Whether to include symbols.
    
    Returns:
    - str: A randomly generated password.
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''
    
    # Combine all possible characters
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    
    # Ensure basic security requirements
    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    
    if include_numbers:
        password.append(random.choice(digits))
    
    if include_symbols:
        password.append(random.choice(symbols))
    
    # Fill the rest with random characters
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

def on_generate():
    """Generate password when the generate button is clicked"""
    try:
        length = int(length_var.get())
        if length < 8 or length > 20:
            messagebox.showwarning("Warning", "Password length should be between 8 and 20 characters")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number")
        return
    
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    password = generate_password(length, include_numbers, include_symbols)
    password_var.set(password)
    # Make the entry editable so user can select and copy manually
    password_entry.config(state="normal")
    password_entry.icursor(tk.END)  # Put cursor at end

def on_clear():
    """Clear the password field"""
    password_var.set("")
    password_entry.config(state="normal")

def create_app():
    """Create the main application window"""
    global length_var, numbers_var, symbols_var, password_var, password_entry
    
    # Create main window
    root = tk.Tk()
    root.title("Easy Password Generator")
    root.geometry("500x400")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")
    
    # Center the window on screen
    root.eval('tk::PlaceWindow . center')
    
    # Variables
    length_var = tk.StringVar(value="12")
    numbers_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=True)
    password_var = tk.StringVar()
    
    # Main frame
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Title
    title_label = ttk.Label(main_frame, text="Easy Password Generator", 
                           font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
    
    # Length section
    length_frame = ttk.Frame(main_frame)
    length_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    
    ttk.Label(length_frame, text="Password Length:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W)
    length_entry = tk.Entry(length_frame, textvariable=length_var, width=5, font=("Arial", 12))
    length_entry.grid(row=0, column=1, padx=(10, 0))
    ttk.Label(length_frame, text="(8-20 characters)", font=("Arial", 10)).grid(row=0, column=2, padx=(10, 0))
    
    # Options section
    options_frame = ttk.Frame(main_frame)
    options_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    
    tk.Checkbutton(options_frame, text="Include Numbers", variable=numbers_var, 
                   font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
    tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var, 
                   font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
    
    # Generate button
    generate_btn = ttk.Button(main_frame, text="Generate Password", 
                             command=on_generate)
    generate_btn.grid(row=3, column=0, columnspan=2, pady=20)
    
    # Password display
    ttk.Label(main_frame, text="Your Password:", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=(20, 5))
    
    password_entry = tk.Entry(main_frame, textvariable=password_var, 
                              font=("Arial", 14), width=30)
    password_entry.grid(row=5, column=0, columnspan=2, pady=5)
    
    # Instructions for copying
    copy_instruction = ttk.Label(main_frame, 
                                text="To copy: Select the text and press Ctrl+C (Windows) or Cmd+C (Mac)",
                                font=("Arial", 10), justify=tk.CENTER, foreground="blue")
    copy_instruction.grid(row=6, column=0, columnspan=2, pady=10)
    
    # Clear button
    clear_btn = ttk.Button(main_frame, text="Clear", command=on_clear)
    clear_btn.grid(row=7, column=0, columnspan=2, pady=10)
    
    # Instructions
    instructions = ttk.Label(main_frame, 
                           text="Tip: Choose a length between 8-20 characters.\n"
                                "For easier remembering, use only letters and numbers.",
                           font=("Arial", 10), justify=tk.CENTER)
    instructions.grid(row=8, column=0, columnspan=2, pady=(20, 0))
    
    # Configure style for larger generate button
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
    
    return root

def main():
    """Main function to run the application"""
    app = create_app()
    app.mainloop()

if __name__ == "__main__":
    main()
