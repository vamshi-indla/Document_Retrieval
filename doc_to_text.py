# Author: Vamshi Krishna Indla
# Objective: Converts ppts to pdfs, and then text is extracted from pdfs. Text is stored in pickle directory
# Date: 3-May-2018
# Usage: python doc_to_text.py C:\Users\username\pptlib

'''
convert ppt to pdf
'''
def ppt_to_pdf(inputFileName, formatType = 32):
    
    outputFileName = os.path.splitext(inputFileName)[0] + ".pdf" 
    input_file_path = os.path.join(path,inputFileName)
    output_file_path = os.path.join(path,"temp",outputFileName)
    
    if not(os.path.exists(output_file_path)): 
        
        if inputFileName[-3:] != 'pdf':
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = 1
            deck = powerpoint.Presentations.Open(input_file_path)
            deck.SaveAs(output_file_path, formatType) # formatType = 32 for ppt to pdf
            deck.Close()
            powerpoint.Quit()
        else:
           copyfile(input_file_path,output_file_path)
    
    return outputFileName


'''
extract pdf to text
'''

def pdf_to_text(infile):
    pdf_file = open(os.path.join(path,"temp",infile), "rb")
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    return (page_content.encode("utf-8"))



if __name__ == '__main__':
    import os, sys
    from shutil import copyfile
    import comtypes.client
    import _pickle as pickle
    import PyPDF2
    import glob
   
    # check if path exists
    path = sys.argv[1]
    if not(os.path.exists(path)):
        print('Invalid path %s' %path)
    
    '''
    convert ppt to pdf
    pdf to text
    pickle the text
    '''
    
    #initialize variables
    pdftext = {}
    
    # create temp dir to store pdfs
    pdfdir = os.path.join(path,"temp")
    if not os.path.exists(pdfdir):
        os.mkdir(pdfdir)
        
    pkldir = os.path.join(path,"pickle")
    if not os.path.exists(pkldir):
        os.mkdir(pkldir)
    
    os.chdir(path)
    for file in glob.glob('*.*'):
        outfile = ppt_to_pdf(file)
        pdftext[file] = pdf_to_text(outfile)

    pklpath = open(os.path.join(path,"pickle","picklef.txt"), 'wb')           
    pickle.dump(pdftext, pklpath )
    pklpath.close()