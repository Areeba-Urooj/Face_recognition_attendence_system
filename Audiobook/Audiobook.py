import pyttsx3
import PyPDF3
 
book = open('The One Thing [{by Gary.W Kellar & Jay Papasan}].pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
page = pdfReader.getPage(8)
text = page.extractText()
 
speaker.say(text)
speaker.runAndWait()
