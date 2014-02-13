import sys
import re
import os

directory = sys.argv[1]

for fl in (os.listdir(directory)):  #for each item that appears in the directory
    if fl.endswith('.txt'):  
    	print 'Processing {0}'.format(fl)

    	fl_path = os.path.join(directory, fl) #the full path to the file is the directory plus
                                              #the file name

        with open(fl_path, 'r') as f:         #open the file as f
            full_text = f.read()              #assign its contents to the var full_text


title_search = re.compile(r'(title:)(?P<title>.*)', re.IGNORECASE,re.U)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

for i, doc in enumerate(fl):
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  translator = re.search(translator_search, doc)
  illustrator = re.search(illustrator_search, doc)
"""
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  #translator = re.search(translator_search, doc)
  #illustrator = re.search(illustrator_search, doc)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')
  print "***" * 25
  print "The title of the text is {}".format(title)
  print "The author is {}".format(author)
  print "The translator is {}".format(translator)
  print "\n"

searches = {}
for kw in sys.argv[1:]:
  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

for i, doc in enumerate(fl):
  print "***" * 25
  print "Here's the counts for the keywords you searched for in document1{}:".format(i)
  for search in searches:
    print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))"""