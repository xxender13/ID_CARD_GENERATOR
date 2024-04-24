from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from tkinter import Tk, Button
import pandas as pd
import os

# Replace these paths with the actual paths on your system
csv_file_path = 'Employees.csv'  # Replace with your CSV file's path
photos_folder_path = 'C:/Users/harsh/OneDrive/Desktop/ID Card Generator/Photo/'  # Replace with your photos folder path
template_path = 'C:/Users/harsh/OneDrive/Desktop/ID Card Generator/ute_id_template.png'  # Path to the ID template image
output_pdf_path = 'C:/Users/harsh/OneDrive/Desktop/ID Card Generator/ID_cards.pdf'


def generate_id_card(user_details, photos_folder_path, template_path):
    unique_id = user_details['Unique ID']
    # Load the CSV file to find the user details
    unique_id = user_details['Unique ID']
    # Load the ID card template
    template = Image.open(template_path)

    # Load the user's photo
    photo_path = os.path.join(photos_folder_path, f"{unique_id}.jpg")
    if not os.path.exists(photo_path):
        print("Photo file not found.")
        return None
    photo = Image.open(photo_path)

    # Load the ID card template
    template = Image.open(template_path)

    # Load the user's photo
    photo_path = os.path.join(photos_folder_path, f"{unique_id}.jpg")
    if not os.path.exists(photo_path):
        print("Photo file not found.")
        return
    photo = Image.open(photo_path)

    # Assuming the photo should be resized to fit the orange box on the template
    box_size = (120, 120)  # Size of the box where the photo should be placed
    photo = photo.resize(box_size, Image.Resampling.LANCZOS)

    # Position for the photo - this also needs to be adjusted for your template
    position = (176, 20)  # The position where the photo will be pasted onto the template

    # Paste the photo onto the template
    template.paste(photo, position)

    # Prepare to draw text on the template
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype("arial.ttf", size=12)

    # Coordinates and size to cover the old role text, which need to be adjusted
    role_coords = (173, 142.5)  # Replace with the actual coordinates for the role text
    width = 240 # Replace with the width needed to cover the old role text
    height = 16.4  # Replace with the height needed to cover the old role text
    background_color = '#FFFFFF'  # Replace with the background color of the template

    # Cover the old role text with a rectangle that matches the background color
    draw.rectangle([role_coords, (role_coords[0] + width, role_coords[1] + height)], fill=background_color)

    # The role from the CSV data
    role = user_details['Role']

    # The color of the text, which should match the template's text color
    font_color = '#FF6C00'

    # Draw the new role text onto the template
    draw.text(role_coords, role, fill=font_color, font=font)

    # Draw the name text onto the template
    name = user_details['Name']  # Name from the CSV data
    name_coords = (125, 165)  # Adjust as necessary for your template
    name_font_color = '#FFFFFF'  # Font color for the name text
    draw.text(name_coords, 'Name: ' + name, fill=name_font_color, font=font)

    # Draw the unique ID text onto the template
    unique_id_coords = (125, 185)  # Adjust as necessary for your template
    unique_id_font_color = '#FFFFFF'  # Font color for the unique ID text
    draw.text(unique_id_coords, 'ID: ' + unique_id, fill=unique_id_font_color, font=font)

    # Save the resulting image to a temporary file
    temp_path = os.path.join(photos_folder_path, f"{unique_id}_temp_ID_card.png")
    template.save(temp_path)
    return temp_path

def create_id_cards_for_all():
    if not os.path.exists(csv_file_path):
        print("CSV file not found.")
        return

    df = pd.read_csv(csv_file_path)

    # Create a canvas for the PDF
    c = canvas.Canvas(output_pdf_path)

    for _, user_details in df.iterrows():
        print(f"Processing ID card for: {user_details['Unique ID']}")
        image_path = generate_id_card(user_details, photos_folder_path, template_path)

        if image_path:
            # Draw the ID card image onto the canvas
            c.drawImage(image_path, 100, 500)  # Adjust the position as needed
            c.showPage()  # End the current page and start a new one
            os.remove(image_path)  # Clean up the temporary file

    # Save the PDF file
    c.save()
    print(f"All ID cards have been created successfully in: {output_pdf_path}")

# Tkinter frontend
root = Tk()
root.title("ID Card Generator")

start_button = Button(root, text="Start Making ID Cards", command=create_id_cards_for_all)
start_button.pack(pady=20)

root.mainloop()