import pandas as pd
from fpdf import FPDF

# Load the Excel file
file_path = 'words.xlsx'
df = pd.read_excel(file_path)

# Define A4 paper size dimensions in mm (210 x 297 mm)
A4_WIDTH = 210
A4_HEIGHT = 297

# Create the PDF object
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(False)  # Disable automatic page breaks

words_per_page = 12  # 12 flashcards per page (6 per column)
flashcard_height = A4_HEIGHT / 6  # Height for each row (6 rows on A4 page)
flashcard_width = A4_WIDTH / 2  # Two columns on A4 page
padding = 10  # Padding to prevent text from hitting the edges

def add_flashcard_page(pdf, data, page_type='word', draw_boxes=True, mirrored=False):
    """
    Adds a flashcard page (either words or definitions) to the PDF and draws lines around each flashcard.
    
    :param pdf: FPDF object
    :param data: List of words or definitions
    :param page_type: 'word' for words page, 'definition' for definitions page
    :param draw_boxes: Boolean, if True draws lines around flashcards
    :param mirrored: Boolean, if True reverses the column order (for definitions)
    """
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Positioning for rows and columns
    for i, item in enumerate(data):
        # Reverse columns for mirrored (definition) page to align with words when printed double-sided
        col = (i // 6) if not mirrored else 1 - (i // 6)
        row = i % 6   # Row index (0 to 5)

        # X and Y coordinates for each flashcard
        x = col * flashcard_width
        y = row * flashcard_height

        # Draw the box around the flashcard
        if draw_boxes:
            pdf.rect(x, y, flashcard_width, flashcard_height)  # Draw a rectangle for the flashcard box

        # Move to the position of each flashcard box
        pdf.set_xy(x + padding/2, y + padding/2)  # Add padding

        if page_type == 'word':
            # Center word horizontally and vertically
            pdf.cell(flashcard_width - padding, flashcard_height - padding, 
                     f"{item['Word']}", ln=1, align='C')
        else:
            # Wrap definition text within the flashcard, multiline if needed
            pdf.multi_cell(flashcard_width - padding, 10, 
                           f"{item['Meaning']}", align='C')

# Loop through data and split into pages
for i in range(0, len(df), words_per_page):
    words_chunk = df.iloc[i:i + words_per_page].to_dict('records')

    # Add page with words (front side) and draw boxes
    add_flashcard_page(pdf, words_chunk, page_type='word', draw_boxes=True)

    # Add page with corresponding definitions (back side) and mirror columns
    add_flashcard_page(pdf, words_chunk, page_type='definition', draw_boxes=True, mirrored=True)

# Save the PDF file
pdf_output_path = 'flashcards.pdf'
pdf.output(pdf_output_path)

print(f"PDF flashcards created: {pdf_output_path}")
