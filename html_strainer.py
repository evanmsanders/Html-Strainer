#!/usr/bin/python

from BeautifulSoup import BeautifulSoup, Comment

try:
    file = open('input.html')
except IOError:
    print('Could not load source file. You must have a file named input.html in the script folder.')
    exit()
    
input = file.read()
soup = BeautifulSoup(input)

#first remove comments - NB this should always be first as some tags appear in comments in older html
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
for comment in comments:
    comment.extract()
    
#remove script tags
scripts = soup.findAll('script')
for script in scripts:
    script.extract()
    
#remove inline style blocks
styles = soup.findAll('style')
for style in styles:
    style.extract()
    
#remove inline style attributes
inline_styles = soup.findAll(style=True)
for inline_style in inline_styles:
    del(inline_style['style'])
    
#remove html ids
ids = soup.findAll(id=True)
for id in ids:
    del(id['id'])
    
#remove html classes
classes = soup.findAll(attrs={'class' : True}) #this is necessary as 'class' is a reserved word
for single_class in classes:
    del(single_class['class'])
    
#remove link target attributes
targets = soup.findAll(target=True)
for target in targets:
    del(target['target'])
    
#remove width attributes
widths = soup.findAll(width=True)
for width in widths:
    del(width['width'])
    
#remove height attributes
heights = soup.findAll(height=True)
for height in heights:
    del(height['height'])

#remove border attributes
borders = soup.findAll(border=True)
for border in borders:
    del(border['border'])
    
#remove bordercolor attributes
bordercolors = soup.findAll(bordercolor=True)
for bordercolor in bordercolors:
    del(bordercolor['bordercolor'])
    
#remove color attributes
colors = soup.findAll(color=True)
for color in colors:
    del(color['color'])

#remove bgcolor attributes
bgcolors = soup.findAll(bgcolor=True)
for bgcolor in bgcolors:
    del(bgcolor['bgcolor'])
    
#remove align attributes
aligns = soup.findAll(align=True)
for align in aligns:
    del(align['align'])

#remove valign attributes
valigns = soup.findAll(valign=True)
for valign in valigns:
    del(valign['valign'])
    
#remove cellspacing attributes
cellspacings = soup.findAll(cellspacing=True)
for cellspacing in cellspacings:
    del(cellspacing['cellspacing'])

#remove cellpadding attributes
cellpaddings = soup.findAll(cellpadding=True)
for cellpadding in cellpaddings:
    del(cellpadding['cellpadding'])

output = soup.prettify()

outputfile = open('output.html', 'w')
outputfile.write(output)
outputfile.close()
