from PyPDF2 import PdfReader
import genanki

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(len(pdf_reader.Pages)):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Function to create Anki deck
def create_anki_deck(deck_name, card_list):
    model_id = input ("Input your Anki model ID: ") # Ask the user for their Anki model ID 
    deck_id = input ("Input your desired deck ID: ")   # Ask the user for their Anki Deck ID
    model = genanki.Model(
        model_id,
        'Simple Model',
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
        templates=[{'name': 'Card 1', 'qfmt': '{{Question}}', 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'}]
    )
    deck = genanki.Deck(deck_id, deck_name)
    for question, answer in card_list:
        note = genanki.Note(
            model=model,
            fields=[question, answer]
        )
        deck.add_note(note)
    genanki.Package(deck).write_to_file('output.apkg')

# Main function
def main():
    pdf_path = input("Enter the path of the PDF File: ") 
    text = extract_text_from_pdf(pdf_path)
    card_list = []  # List to store tuples of (question, answer)

    # Split the text by lines
    lines = text.split("\n")

    # Iterate through lines to extract questions and answers
    for line in lines:
        # Check if the line starts with "Question #"
        if line.startswith("Question #"):
            question = line  # Assign the line as the question
        # Check if the line starts with "Correct Answer:"
        elif line.startswith("Correct Answer:"):
            # Extract the answer choices from the line
            answer_choices = line.split(":")[1].strip()
            # Extract correct answers from answer choices
            correct_answers = [choice.strip() for choice in answer_choices.split()[-1]]
            # Create answer string by joining correct answers
            answer = "".join(correct_answers)
            card_list.append((question, answer))

    create_anki_deck("MyDeck", card_list)

if __name__ == "__main__":
    main()

