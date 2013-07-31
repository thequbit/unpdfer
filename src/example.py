import time

from unpdfer import UnPDFer

def main():

    filename = "input.pdf"
    print "Running on '{0}' ...".format(filename)

    start_time = time.time()
    
    unpdfer = UnPDFer()
    (pdftext,pdfhash,tokens,success) = unpdfer.unpdf(filename,SCRUB=True)

    end_time = time.time()
 
    print "Done."

    print ""
    print "---- STATS ----"
    print ""
    print "File: {0}".format(filename)
    print "Hash: {0}".format(pdfhash)
    print "Number of Tokens: {0}".format(len(tokens))
    print "Success: {0}".format(success)
    print "Number of Tokens: {0}".format(end_time-start_time)
    print ""

main()
