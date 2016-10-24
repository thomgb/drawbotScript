# Spacing helper for DrawBot in RoboFont 
# 

# we need the font
f = CurrentFont()

# here the proofs
# make a dictionary
proofs = {}

# populate it
proofs[0] = [
    u"/Users/thom/Pictures/Revivals/Walthari/kannten.png", #image
    "kannten", #the text in the image
    (15, 42) # the translation
    ]
proofs[1] = [
    u"/Users/thom/Pictures/Revivals/Walthari/longer.png", #image
    "Herzens Drang,", #the text in the image
    (14, 30) # the translation
    ]
# feel free to make more and more and more proofs :))
# just copy the 'proof[x] = []' thing, number them 0,1,2,3 etc :)


# loop through all the proofs 
for proofNr in range(len(proofs)):
    
    # get the image
    img = proofs[proofNr][0]
    
    # get the text
    myText  = proofs[proofNr][1]
    
    # the script needs glyph names, this is a way to get them
    text = []
    for l in myText:
        glyph = f.naked().unicodeData.glyphNameForUnicode(ord(l))
        text.append(glyph)

    # how big is the image
    w,h = imageSize(img)
    
    # create a new page/canvas
    newPage(w,h)
    
    # place the image
    image(img, (0,0), alpha=.5)

    #translate to the point where the glyph need to be
    translate(*proofs[proofNr][2])

    # play with this scale, it works for me with image @ 1200 dpi and xHeight of 525
    # probably you need some other scaling
    scale(.144)
    
    # some colours and stuff
    fill(1,0,0,0.0)
    stroke(0)
    strokeWidth(10)
    
    # finally draw them glyphs!
    for letter in text:
        drawGlyph(f[letter])
        translate(f[letter].width)
        
        
        