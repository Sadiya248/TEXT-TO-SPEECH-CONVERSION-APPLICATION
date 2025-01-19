import tkinter as tk
from tkinter import messagebox
import os

# Function to convert text to speech using PowerShell
def convert_to_speech():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter text to convert.")
        return
    try:
        # Use PowerShell's text-to-speech feature
        command = f'Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
        os.system(f"powershell -Command \"{command}\"")
        messagebox.showinfo("Success", "Speech played successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to reset the input field
def reset_fields():
    text_input.delete("1.0", tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("Text-to-Speech Conversion App")
root.geometry("500x300")
root.resizable(False, False)

# Add a label for instructions
label = tk.Label(root, text="Enter Text Below:", font=("Arial", 14))
label.pack(pady=10)

# Add a text box for user input
text_input = tk.Text(root, wrap="word", font=("Arial", 12), height=8, width=50)
text_input.pack(pady=10)

# Add a button to convert text to speech
speak_button = tk.Button(root, text="Convert to Speech", font=("Arial", 12), command=convert_to_speech)
speak_button.pack(pady=10)

# Add a button to reset the text input
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_fields)
reset_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
