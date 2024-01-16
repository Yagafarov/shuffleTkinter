import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random
import subprocess

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        label.config(text="Tanlangan fayl: " + file_name)
        display_file_content(file_path)

def shuffle_options():
    current_content = text_widget.get('1.0', tk.END)
    lines = current_content.split('\n')

    for i in range(1, len(lines), 5):  # Assuming every question has 4 options
        options = lines[i:i + 4]
        random.shuffle(options)
        lines[i:i + 4] = options

    shuffled_content = '\n'.join(lines)
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, shuffled_content)

def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get('1.0', tk.END))
        label.config(text="Fayl saqlandi: " + file_path)
        show_completion_message("Fayl muvaffaqiyatli saqlandi!")
        open_file_in_editor(file_path)

def show_completion_message(message):
    completion_label.config(text=message)

def open_file_in_editor(file_path):
    try:
        subprocess.run(["notepad", file_path], check=True)
    except Exception as e:
        print(f"Error opening file: {e}")

def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.delete('1.0', tk.END)  # Clear previous content
            text_widget.insert(tk.END, content)
    except Exception as e:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, f"Error: {str(e)}")


def open_link(link):
    try:
        subprocess.run(["start", link], check=True, shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error opening link: {e}")

def show_tutorial():
    tutorial_text = """
    Test Shuffle App dasturiga xush kelibsiz 🎉!

    Dasturdan foydalanish:
    1. "Fayl tanlash" tugmasini bosing va faylni tanlang.
    2. Matn maydonidagi tarkibni ko'ring va tahrirlang.
    3. "Variantlarni aralashtirish" tugmasini bosing.
    4. "Saqlash" tugmasini bosing natijani saqlash uchun.

    Qo'shimcha yordam olish uchun www.anodra.uz saytiga tashrif buyuring.

    Biz bilan bog'laning:
    - Telegram: t.me/anodra_uz
    - Github: www.github.com/yagafarov
    - Instagram: www.instagram.com/yagafarov_d_

    
     Testlar quyidagi shablon asodida bo'lishi kerak:
    # savol 1
    variant 1
    variant 2
    variant 3
    variant 4
    # savol 2
    variant 1
    variant 2
    variant 3
    variant 4
    ...

    Eslatma savollar va variantlar matni bir qatorda bo'lishi kerak!

     Test savollaringizni aralashtirib bahramand bo'ling!

    """
    tutorial_window = tk.Toplevel(root)
    tutorial_window.title("Yordam")
    
    tutorial_label = tk.Label(tutorial_window, text=tutorial_text, justify=tk.LEFT, wraplength=600)
    tutorial_label.pack(padx=10, pady=10)





# Create the main application window
root = tk.Tk()
root.title("Test Shuffle [www.anodra.uz]")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = int(0.9 * screen_width)
window_height = int(0.9 * screen_height)

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - window_width) // 2
y_coordinate = 0

# Set the geometry of the window to be centered
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


# Create a label to display the selected file path
label = tk.Label(root, text="Tanlangan Fayl: ")
label.pack(pady=10)

# Create a button to trigger file selection
browse_button = tk.Button(root, text="Fayl tanlash", command=browse_file)
browse_button.pack(pady=10)

# Create an Entry widget for editing content
text_widget = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text_widget.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

# Create a button to shuffle options
shuffle_button = tk.Button(root, text="Variantlarni aralashtirish", command=shuffle_options)

shuffle_button.pack(pady=10,padx=10, side=tk.LEFT)

# Create a button to save the modified content
save_button = tk.Button(root, text="Saqlash", command=save_as)
save_button.pack(pady=10,padx=10, side=tk.LEFT)

help_button = tk.Button(root, text="Yordam", command=show_tutorial)
help_button.pack(pady=10,padx=10, side=tk.LEFT)

# Create a label for completion messages
completion_label = tk.Label(root, text="")
completion_label.pack(pady=10)



if __name__ == "__main__":
    root.mainloop()
