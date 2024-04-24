
# Employee ID Card Generator

This project automates the generation of employee ID cards using Python, PIL for image manipulation, ReportLab for PDF creation, and Tkinter for a simple graphical user interface. The system takes employee data from a CSV file, generates ID cards by placing employee photos and information onto a predefined template, and compiles all generated ID cards into a single PDF file.

## Features

- **CSV Data Input:** Read employee data from a CSV file to automate ID card creation.
- **Photo Integration:** Automatically resize and integrate employee photos into the ID cards.
- **Text Placement:** Dynamically place employee name, role, and unique ID on the ID card.
- **PDF Compilation:** Compile all generated ID cards into a single PDF file for easy printing and distribution.
- **GUI Interface:** Start the ID card generation process through a simple graphical interface.

## Setup and Installation

### Requirements

- Python 3.6+
- Pillow (PIL Fork)
- ReportLab
- Tkinter (usually included with Python)

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/xxender13/ID_CARD_GENERATOR.git
cd yourproject
```

Install the required Python packages:

```bash
pip install pillow reportlab
```

### Configuration

Before running the application, ensure the paths in the script are configured to your specific environment:

- `csv_file_path`: Path to the CSV file containing employee data.
- `photos_folder_path`: Directory containing employee photos named according to their unique IDs.
- `template_path`: Path to the ID card template image.
- `output_pdf_path`: Path where the generated PDF file containing all ID cards will be saved.

## Usage

To run the ID Card Generator:

1. **Start the Application:**
   Navigate to the project directory and run the script.
   ```bash
   python ID.py
   python generator.py
   ```
2. **Generate ID Cards:**
   Use the GUI button "Start Making ID Cards" to generate ID cards for all employees listed in the CSV file. The ID cards will be saved as individual images and compiled into a single PDF file.


## Demo
![ID Card Generation Process](https://github.com/xxender13/ID_CARD_GENERATOR/blob/main/Demo.gif?raw=true)

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## Contact

For any queries, you can reach out to [Harshil Sharma](harshil.sharma@slu.edu).
```
