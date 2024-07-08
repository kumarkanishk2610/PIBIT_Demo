import PyPDF2
import json

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Function to parse the extracted text into a structured dictionary
def parse_resume(text):
    lines = text.split('\n')
    resume = {
        "name": lines[0].split(":")[1].strip(),
        "contact_information": {
            "email": lines[3].split(":")[1].strip(),
            "phone": lines[2].split(":")[1].strip(),
            "address": lines[4].split(":")[1].strip()
        },
        "summary": lines[6].strip(),
        "experience": [
            {
                "company": lines[8].split(" at ")[0].split(":")[1].strip(),
                "position": lines[8].split(" at ")[0].split(" ")[1],
                "location": lines[8].split(" at ")[1].split(" ")[0],
                "start_date": lines[8].split(", ")[1].split("-")[0].strip(),
                "end_date": lines[8].split(", ")[1].split("-")[1].strip(),
                "responsibilities": []
            }
        ],
        "education": [
            {
                "institution": lines[10].split(" ")[0],
                "degree": "",
                "location": "",
                "graduation_year": lines[10].split(" ")[-1]
            }
        ],
        "skills": [skill.strip() for skill in lines[12].split(":")[1].split(",")],
        "projects": [
            {
                "name": lines[14].split(":")[0].strip(),
                "description": lines[14].split(":")[1].strip(),
                "technologies": []
            },
            {
                "name": lines[15].split(":")[0].strip(),
                "description": lines[15].split(":")[1].strip(),
                "technologies": []
            }
        ]
    }
    return resume

# Main function
def main():
    pdf_path = "Sample Resume for PIBIT Question.pdf"  # Path to your PDF file
    text = extract_text_from_pdf(pdf_path)
    resume = parse_resume(text)
    
    # Convert the resume dictionary to a JSON string
    resume_json = json.dumps(resume, indent=4)
    
    # Save the JSON string to a file
    with open("resume.json", "w") as file:
        file.write(resume_json)
    
    print("Resume has been converted to JSON and saved as resume.json")

if __name__ == "__main__":
    main()
