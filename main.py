import pyttsx3, PyPDF2

clean_text = ''
speaker = ''
pdfreader = PyPDF2.PdfReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()
speaker.setProperty('rate', 100)

for page_num in range (len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', '')
    print(clean_text)

speaker.save_to_file(clean_text, "sample.mp3")
speaker.runAndWait()

speaker.stop()