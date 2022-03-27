import docx2txt
from PyPDF2 import PdfFileReader
from icecream import ic


def doc_to_text(file_path):
    """Extract text from a DOCX file

    Parameters
    ----------
    file_path : str
        Path to the DOCX file.

    Returns
    -------
    str
        Text extracted from the DOCX file.
    """
    temp = docx2txt.process(file_path)
    resume_text = [line.replace('\t', ' ')
                   for line in temp.split('\n') if line]
    text = ' '.join(resume_text)
    return (text)


def pdf_to_text(file_path):
    """Extract text from a PDF file

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    str
        Text extracted from the PDF file.
    """

    # initial values
    currentPageNumber = 0
    text = ''

    # create pdf file object and extract pdf reader object and the number of pages
    pdfFileObj = open(file_path, 'rb')
    pdfFileReader = PdfFileReader(pdfFileObj)
    num_pages = pdfFileReader.numPages

    # loop over all pdf pages
    while(currentPageNumber < num_pages):

        # Get the specified pdf page object
        pdfPage = pdfFileReader.getPage(currentPageNumber)
        ic(pdfPage)

        # Get pdf page text
        text = text + ic(pdfPage.extractText())

        # Process next page.
        currentPageNumber += 1
    return (text)
