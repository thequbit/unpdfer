unpdfer
=======

takes in a PDF document and returns the text from within it and additional information about the doc

#####About#####

This tool will take in a PDF filename and produce a blob of the text within it, the MD5 hash of that blob,
and the free-form 'created' field from within the PDF document.

#####Flags#####

Setting the SCRUB flag will cause the following characters to be removed:

    , . ? / : ; < > [ ] \ " ' `

It will also remove all duplicate \t, \n, \r, and spaces from the file.

Setting the verbose flag to True will cause debug output to be printed to the screen.

#####Usage#####

    from unpdfer import Unpdfer
    
    # set an input filename
    filename = 'myfile.pdf'
    
    # conver to text
    worker = Unpdfer()
    (created,pdftext,pdfhash,success) = worker.unpdf(filename,SCRUB=False,verbose=False)

Note: the created field within the PDF standard is a free-form field, and can contain ANYTHING.
