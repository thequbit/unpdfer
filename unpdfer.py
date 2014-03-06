from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdftypes import PDFObjRef
from cStringIO import StringIO

from time import mktime, strptime
from datetime import datetime

import hashlib

import re

class Unpdfer:

    _verbose = False

    def __init__(self,verbose=False):
        self._verbose = verbose

    def _report(self,text):
        if self._verbose:
            print "[unPDFer ] {0}".format(text)

    def _pdf2text(self,fp):
        try:
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            codec = 'ascii'
            laparams = LAParams()
            laparams.all_texts = True
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

            process_pdf(rsrcmgr, device, fp)
            device.close()

            # fix the non-utf8 string ...
            result = retstr.getvalue()
            txt = result.encode('ascii','ignore')

            # TODO: clean this up, I feel like I'm doing the converstion twice ...
            # http://stackoverflow.com/a/16503222/2154772
            parser = PDFParser(fp)
            doc = PDFDocument()
            parser.set_document(doc)
            doc.set_parser(parser)
            doc.initialize()
            #print doc.info[0]['CreationDate'].resolve()
            
            #
            # as messed up as this is ... CreationDate isn't always the same type as it
            # comes back from the PDFParser, so we need to base it on an instance of a
            # basestring or not.
            #
            created = ""
            try:
                if not isinstance(doc.info[0]['CreationDate'],basestring):
                    creatd = doc.info[0]['CreationDate'].resolve()[2:-7]
                else:
                    created = doc.info[0]['CreationDate'][2:-7]
            except:
                self._report("CreationDate field could not be decoded within PDF, setting to ''")
                pass
            retVal = (created,txt,True)
            retstr.close()
        except Exception, e:
            self._report("Error: \n\t%s" % str(e))
            retVal = (None,"",False)
            pass
        return retVal

    def _scrubtext(self,text):

        # remove all the 'fancy' chars
        text = text.replace(',','').replace('.','').replace('?','')
        text = text.replace('/','').replace(':','').replace(';','')
        text = text.replace('<','').replace('>','').replace('[','')
        text = text.replace(']','').replace('\\',' ').replace('"','')
        text = text.replace("'",'').replace('`','')

        # this is done 4 times for the situation of ' \n\t \n\t' 
        for i in range(0,3):
            text = re.sub(' +',' ',text)
            text = re.sub('\n+','\n',text)
            text = re.sub('\t+','\t',text)

        # this happens way more than you would think ...
        text = text.replace(' \n','\n')
        text = text.replace(' \t','\t')
        text = text.replace(' \r','\r')

        return text

    def unpdf(self,filename,SCRUB=False,verbose=False):
        self._verbose = verbose
        self._report("Processing '{0}'".format(filename))
        with open(filename,'rb') as fp:
            created,pdftext,success = self._pdf2text(fp)
            if SCRUB == True:
                # this is done twice because PDF
                pdftext = self._scrubtext(pdftext)
                pdftext = self._scrubtext(pdftext)
            pdfhash = hashlib.md5(fp.read()).hexdigest()
            #_tokens = nltk.word_tokenize(pdftext)
            #tokens = nltk.FreqDist(word.lower() for word in _tokens)
        return (created,pdftext,pdfhash,success)

