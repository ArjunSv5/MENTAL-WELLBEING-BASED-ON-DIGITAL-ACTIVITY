import tkinter as tk
from tkinter import messagebox
from project import train_model, predict_anxiety

# Load trained model and metadata
model, scaler, feature_names, label_levels = train_model()

label_map = {
    0: "Low Anxiety",
    1: "Moderate Anxiety",
    2: "High Anxiety"
}

# --- Styling Variables (Gemini AI inspired) ---
BG_DARK = "#1A1A1A"  # Very dark background
BG_MEDIUM = "#2B2B2B" # Slightly lighter for elements
FG_LIGHT = "#E0E0E0"  # Light grey for text
ACCENT_BLUE = "#4285F4" # A blue accent, similar to Google's palette
FONT_FAMILY = "Segoe UI" # A clean, modern font available on most systems
FONT_SIZE_TITLE = 18
FONT_SIZE_LABEL = 11
FONT_SIZE_BUTTON = 12

root = tk.Tk()
root.title("Anxiety Prediction")
root.configure(bg=BG_DARK)
root.geometry("500x650") # Slightly larger window for better spacing
root.resizable(False, False) # Optional: prevent resizing

# Main frame for content to add padding
main_frame = tk.Frame(root, bg=BG_DARK, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

# Title Label
tk.Label(main_frame, text="Anxiety Level Prediction", bg=BG_DARK, fg=FG_LIGHT,
         font=(FONT_FAMILY, FONT_SIZE_TITLE, "bold")).pack(pady=(10, 20))

# Input fields
input_frame = tk.Frame(main_frame, bg=BG_DARK)
input_frame.pack(pady=10, fill='x')

entries = {}
for i, feature in enumerate(feature_names):
    # Use grid for better alignment
    tk.Label(input_frame, text=feature + ":", bg=BG_DARK, fg=FG_LIGHT,
             font=(FONT_FAMILY, FONT_SIZE_LABEL), anchor='w', width=25).grid(row=i, column=0, pady=5, padx=5, sticky='w')
    
    entry = tk.Entry(input_frame, bg=BG_MEDIUM, fg=FG_LIGHT, insertbackground=ACCENT_BLUE, # Cursor color
                     font=(FONT_FAMILY, FONT_SIZE_LABEL), bd=0, relief="flat", width=25)
    entry.grid(row=i, column=1, pady=5, padx=5, sticky='ew')
    entries[feature] = entry

input_frame.grid_columnconfigure(1, weight=1) # Make the entry column expandable

def on_predict():
    try:
        input_data = [float(entries[f].get()) for f in feature_names]
        pred = predict_anxiety(model, scaler, input_data)
        message = label_map.get(pred, f"Anxiety level: {pred}")
        messagebox.showinfo("Prediction Result", message) # More descriptive title
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.") # More specific error

# Predict Button
predict_button = tk.Button(main_frame, text="Predict Anxiety", command=on_predict,
                           bg=ACCENT_BLUE, fg="white", font=(FONT_FAMILY, FONT_SIZE_BUTTON, "bold"),
                           bd=0, relief="flat", padx=15, pady=8, cursor="hand2") # Hand cursor on hover

predict_button.pack(pady=30)

# Add hover effect for the button
def on_enter(e):
    predict_button['bg'] = "#5C99F9" # Slightly lighter blue on hover

def on_leave(e):
    predict_button['bg'] = ACCENT_BLUE

predict_button.bind("<Enter>", on_enter)
predict_button.bind("<Leave>", on_leave)


root.mainloop()