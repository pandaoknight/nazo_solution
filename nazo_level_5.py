#!/usr/bin/python

encrypted = "ofyu mfwfm:qjofusff.iunm"

for sk in range(-10, 10):
    de_str = ""
    for ch in encrypted:
        #print ord(ch)
        #print chr( ord('z') - ord(ch) + ord('a') )
        de_ch = chr( sk + ord(ch) )
        de_str += de_ch
    print de_str
