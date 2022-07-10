from glob import glob

from pikepdf import Pdf


def merge_pdfs(n, name):
    pdf = Pdf.new()


    for i in range(1, n + 1):  # you can change this to browse directories recursively

        with Pdf.open('Folder/f' + str(i) + '.pdf') as src: # It is the location of the pdf files Note: all file formats should be in f* series
            pdf.pages.extend(src.pages)

    pdf.save('Folder/' + name + '.pdf')
    pdf.close()


merge_pdfs(2, 'merge')




