import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

print('---------------')
print("Start PDF Merge")
print('---------------')



def merge_pdfs(result_name):
    pdf_writer = PdfFileWriter()
    root = tkinter.Tk()

    root.withdraw()

    files = filedialog.askopenfilenames(parent=root,title='PDFs auswählen!')
    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(result_name, 'wb') as out:
        pdf_writer.write(out)
        print("PDF-Datei erfolgreich erstellt.")


merge_pdfs('zusammenfassung.pdf')