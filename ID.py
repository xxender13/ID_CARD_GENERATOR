
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from PIL import Image
import os

csv_file_path = 'Employees.csv'  # Replace with your CSV file's path
photos_folder_path = 'C:/Users/harsh/OneDrive/Desktop/ID Card Generator/Photo/'  # Replace with your photos folder path



# Function to save the details to the CSV and the photo with the next Dev number
def save_details(name, email, gender, phone_number, role, photo_path):
    # Load the existing CSV data
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        # Determine the next available unique ID based on the existing data
        last_id = df['Unique ID'].str.extract(r'(Dev0(\d+))')[1].astype(int).max()
        next_id = f'Dev0{last_id + 1}'
    else:
        df = pd.DataFrame(columns=['Name', 'Email', 'Unique ID', 'Gender', 'Phone Number', 'Role'])
        next_id = 'Dev001'

    # Add the new entry
    new_entry = pd.DataFrame([{
        'Name': name,

        'Email': email,
        'Unique ID': next_id,
        'Gender': gender,
        'Phone Number': phone_number,
        'Role': role
    }])

    # Use pd.concat to append the new entry
    df = pd.concat([df, new_entry], ignore_index=True)

    # Save the updated DataFrame to the CSV file
    df.to_csv(csv_file_path, index=False)

    # Save the photo in the photos folder with the new unique ID
    if photo_path:
        image = Image.open(photo_path)
        image.save(os.path.join(photos_folder_path, f"{next_id}.jpg"))

    return next_id


# Function to handle the "Upload Photo" button click
# Function to handle the "Upload Photo" button click
def upload_photo():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_photo.delete(0, tk.END)
        entry_photo.insert(0, file_path)


# Function to handle the "Save" button click
def save():
    name = entry_name.get()

    email = entry_email.get()
    gender = entry_gender.get()
    phone_number = entry_phone.get()
    role = entry_role.get()
    photo_path = entry_photo.get()

    # Call the save_details function
    next_id = save_details(name,  email, gender, phone_number, role, photo_path)

    # Show a message box with the result
    messagebox.showinfo("Success", f"Details saved with ID: {next_id}")

    # Clear the form entries
    entry_name.delete(0, tk.END)

    entry_email.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_photo.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Employee Registration")

# Create and place the form elements
label_name = tk.Label(root, text="Name")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)


label_email = tk.Label(root, text="Email")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

label_gender = tk.Label(root, text="Gender")
label_gender.grid(row=3, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=3, column=1)

label_phone = tk.Label(root, text="Phone Number")
label_phone.grid(row=4, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=4, column=1)

label_role = tk.Label(root, text="Role")
label_role.grid(row=5, column=0)
entry_role = tk.Entry(root)
entry_role.grid(row=5, column=1)

label_photo = tk.Label(root, text="Photo")
label_photo.grid(row=6, column=0)
entry_photo = tk.Entry(root)
entry_photo.grid(row=6, column=1)
button_upload = tk.Button(root, text="Upload Photo", command=upload_photo)
button_upload.grid(row=6, column=2)

button_save = tk.Button(root, text="Save", command=save)
button_save.grid(row=7, column=1)

# Run the main loop
root.mainloop()
