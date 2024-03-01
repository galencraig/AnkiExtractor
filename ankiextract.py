import genanki
import fitz

# Define MyClass
class MyClass:
    def __init__(self, extracted_content):
        self.extracted_content = extracted_content
    
    @property
    def my_property(self):
        content = []
        for page_content in self.extracted_content:
            if isinstance(page_content, str):
                content.append(('text', page_content.strip()))
            elif isinstance(page_content, bytes):
                content.append(('image', page_content))
        return content

# Function to extract content from PDF (both text and images)
def extract_content_from_pdf(pdf_path):
    content = []
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            # Extract text
            text = page.get_text()
            content.append(text)
            # Extract images
            images = page.get_images(full=True)
            for img_index, img_info in enumerate(images):
                base_image = pdf_document.extract_image(img_info[0])
                image_bytes = base_image["image"]
                content.append(image_bytes)  # Store image bytes
    return content

# Function to create Anki deck
def create_anki_deck(deck_name, card_list):
    model_id = random.randrange(1 << 30, 1 << 31)  # Generate model ID
    deck_id = random.randrange(1 << 30, 1 << 31) # Generate Deck ID
    model = genanki.Model(
        model_id,
        'Simple Model',
        fields=[{'name': 'Type'}, {'name': 'Content'}],
        templates=[{'name': 'Card 1', 'qfmt': '{{Type}}', 'afmt': '{{FrontSide}}<hr id="answer">{{Content}}'}]
    )
    deck = genanki.Deck(deck_id, deck_name)
    for card_type, content in card_list:
        note = genanki.Note(
            model=model,
            fields=[card_type, content]
        )
        deck.add_note(note)
    genanki.Package(deck).write_to_file('output.apkg')

# Main function
def main():
    pdf_path = input("Enter the path of the PDF File: ")
    extracted_content = extract_content_from_pdf(pdf_path)  # Extract content (both text and images) from the PDF file
    obj = MyClass(extracted_content)  # Pass the extracted content to MyClass constructor
    content_list = obj.my_property
    create_anki_deck(input("What would you like to name this deck? "), content_list)

if __name__ == "__main__":
    main()





#from PyPDF2 import PdfReader
#import genanki

## Define MyClass
#class MyClass:
#    def __init__(self, extracted_text):
#        self.extracted_text = extracted_text
#    
#    @property
#    def my_property(self):
#        question_answer_pairs = []
#        lines = self.extracted_text.split("\n")
#        for line in lines:
#            if line.startswith("Question #"):
#                question = line
#            elif line.startswith("Correct Answer:"):
#                answer = line.split(":")[1].strip()
#                question_answer_pairs.append((question, answer))
#            else:
#                print("Warning: Skipped line: ", line)
#        return question_answer_pairs
#
## Function to extract text from PDF
#def extract_text_from_pdf(pdf_path):
#    text = ""
#    with open(pdf_path, "rb") as f:
#        reader = PdfReader(f)
#        for page_num in range(len(reader.pages)):
#            page = reader.pages[page_num] 
#            text += page.extract_text()
#    return text
#
# Function to create Anki deck
#def create_anki_deck(deck_name, card_list):
#    model_id = input ("Input your Anki model ID: ") # Ask the user for their Anki model ID 
#    deck_id = input ("Input your desired deck ID: ")   # Ask the user for their Anki Deck ID
#    model = genanki.Model(
#        model_id,
#        'Simple Model',
#        fields=[{'name': 'Question'}, {'name': 'Answer'}],
#        templates=[{'name': 'Card 1', 'qfmt': '{{Question}}', 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'}]
#    )
#    deck = genanki.Deck(deck_id, deck_name)
#    for question, answer in card_list:
#        note = genanki.Note(
#            model=model,
#            fields=[question, answer]
#        )
#        deck.add_note(note)
#    genanki.Package(deck).write_to_file('output.apkg')
#
## Main function
#def main():
#    pdf_path = input("Enter the path of the PDF File: ") 
#    extracted_text = extract_text_from_pdf(pdf_path)
#    card_list = []  # List to store tuples of (question, answer)
#    obj = MyClass(extracted_text)
#    question_answer_pairs = obj.my_property 
#    # Now you can use data_list to process the extracted data further
#
#    # Split the text by lines
#    lines = text.split("\n")
#
#    # Iterate through lines to extract questions and answers
#    for line in lines:
#        # Check if the line starts with "Question #"
#        if line.startswith("Question #"):
#            question = line  # Assign the line as the question
#        # Check if the line starts with "Correct Answer:"
#        elif line.startswith("Correct Answer:"):
#            # Extract the answer choices from the line
#            answer_choices = line.split(":")[1].strip()
#            # Extract correct answers from answer choices
#            correct_answers = [choice.strip() for choice in answer_choices.split()[-1]]
#            # Create answer string by joining correct answers
#            answer = "".join(correct_answers)
#            card_list.append((question, answer))
#
#    create_anki_deck(input ("What would you like to name this deck? "), question_answer_pairs) 
#if __name__ == "__main__":
#    main()
#
