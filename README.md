# TEXT-TO-SPEECH-CONVERSION-APPLICATION
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SADIYA ABOOBACKER

*INTERN ID*: CT08DS74

*DOMAIN*: MACHINE LEARNING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

#This Python script uses the Tkinter library to create a simple graphical user interface (GUI) application that converts entered text into speech. Below is a detailed description of how the code works, the libraries used, and its applicability.

### Libraries Used:
1. **Tkinter (tk):**
   Tkinter is a built-in Python library used for creating GUI applications. It provides tools for designing interactive windows, buttons, text boxes, and labels. This script uses Tkinter to create a user-friendly interface for interacting with the text-to-speech functionality.

2. **Messagebox (from tkinter):**
   The `messagebox` module is part of Tkinter and is used to display message boxes to the user. It provides pop-up dialogs that can display informational, warning, or error messages.

3. **OS:**
   The `os` module allows interaction with the operating system. In this case, it's used to execute PowerShell commands from within the Python script to use the built-in text-to-speech functionality on Windows.

### Functionality:

#### 1. **Text Input:**
   The application provides a text box where users can enter the text they want to convert to speech. Tkinter’s `Text` widget is used to create a multi-line text input area. The input area is set to wrap words and is sized to fit 50 characters in width and 8 lines in height.

#### 2. **Text-to-Speech Conversion:**
   - **`convert_to_speech` function:** 
     When the user clicks the "Convert to Speech" button, this function is triggered. It retrieves the text entered by the user using `text_input.get("1.0", tk.END).strip()`. If no text is provided, an error message is displayed via the `messagebox.showerror()` function, prompting the user to enter some text.
     - If text is entered, the script forms a PowerShell command that uses the `System.Speech.Synthesis.SpeechSynthesizer` class to convert the text into speech. This class is part of the .NET framework and is available on Windows.
     - The command is executed through `os.system()`, which invokes PowerShell from within the Python environment.
     - A success message is shown after the speech is played successfully. If any error occurs during the execution (such as a missing PowerShell module), the program catches the exception and displays an error message.

#### 3. **Reset Function:**
   - **`reset_fields` function:** 
     This function clears the text input field. It is triggered when the "Reset" button is pressed, providing a way to start over by clearing any previously entered text.

#### 4. **GUI Components:**
   - **Main Window (root):** 
     The GUI window is created using Tkinter’s `Tk()` function. The window’s title is set to "Text-to-Speech Conversion App," and its size is fixed to 500x300 pixels. The window is also set to be non-resizable to maintain its layout consistency.
   
   - **Label:**
     A label is added above the text box, providing the user with instructions to enter text. It uses the Arial font with a size of 14 for clear readability.
   
   - **Buttons:**
     Two buttons are created:
     - The **Convert to Speech** button is linked to the `convert_to_speech` function.
     - The **Reset** button is linked to the `reset_fields` function. Both buttons are styled with the Arial font and a size of 12.

#### 5. **Event Loop:**
   The `root.mainloop()` method starts the Tkinter event loop, which listens for user actions such as button clicks and keeps the application responsive.

### Applicability:

This text-to-speech application is highly practical in scenarios where accessibility is important. For instance:
- **Assistive Technologies:** It can assist people with visual impairments or reading difficulties by converting written text into spoken words.
- **Educational Tools:** It can be used in language learning apps where students can hear the correct pronunciation of text.
- **Automated Responses:** It could be integrated into systems that provide audio feedback for instructions, alerts, or notifications.
- **Multitasking:** Users can listen to the text while performing other tasks, such as when driving or exercising, making it ideal for multitasking environments.


#output
![image](https://github.com/user-attachments/assets/7c3e9f51-0afc-49c9-859c-379fe647dbd2)
![image](https://github.com/user-attachments/assets/c2ea2443-50ed-4062-b08b-3ac4979a334d)

