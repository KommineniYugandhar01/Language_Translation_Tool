import tkinter as tk
from tkinter import ttk, messagebox

try:
    from googletrans import Translator, LANGUAGES
except ImportError as err:
    messagebox.showerror(
        "Import Error",
        "googletrans is not installed. Install it with:\npython -m pip install googletrans==4.0.0rc1"
    )
    raise err

translator = Translator(service_urls=["translate.googleapis.com", "translate.google.com"])

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    src_lang = source_lang.get()
    dest_lang = target_lang.get()

    if src_lang not in lang_dict or dest_lang not in lang_dict:
        messagebox.showerror(
            "Error",
            "Please choose valid source and target languages from the dropdown lists."
        )
        return

    try:
        translated = translator.translate(
            text,
            src=lang_dict[src_lang],
            dest=lang_dict[dest_lang]
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# Dictionary for language codes
lang_dict = {value.title(): key for key, value in LANGUAGES.items()}

# GUI Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x550")
root.configure(bg="#EAF4FC")

title = tk.Label(
    root,
    text="🌍 Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#EAF4FC",
    fg="#003366"
)
title.pack(pady=10)

# Input Label
tk.Label(root, text="Enter Text:", font=("Arial", 12, "bold"),
         bg="#EAF4FC").pack(anchor="w", padx=20)

input_text = tk.Text(root, height=6, width=70, font=("Arial", 11))
input_text.pack(pady=5)

frame = tk.Frame(root, bg="#EAF4FC")
frame.pack(pady=10)

# Source Language
tk.Label(frame, text="From:", font=("Arial", 11),
         bg="#EAF4FC").grid(row=0, column=0, padx=10)

source_lang = ttk.Combobox(
    frame,
    values=sorted(lang_dict.keys()),
    width=20,
    state="readonly"
)
source_lang.grid(row=0, column=1)
source_lang.set("English")

# Target Language
tk.Label(frame, text="To:", font=("Arial", 11),
         bg="#EAF4FC").grid(row=0, column=2, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=sorted(lang_dict.keys()),
    width=20,
    state="readonly"
)
target_lang.grid(row=0, column=3)
target_lang.set("Hindi")

# Translate Button
translate_btn = tk.Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="#007ACC",
    fg="white",
    command=translate_text
)
translate_btn.pack(pady=15)

# Output Label
tk.Label(root, text="Translated Text:",
         font=("Arial", 12, "bold"),
         bg="#EAF4FC").pack(anchor="w", padx=20)

output_text = tk.Text(root, height=6, width=70,
                      font=("Arial", 11))
output_text.pack(pady=5)

root.mainloop()