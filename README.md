# allcombos
#Description:
A Python script that creates all possible alphanumerical and symbol combinations in string format for URL Fuzzing.

While I was working on courses in Pentesterlab, I felt like I needed a list of URL Fuzzing possibilities that varied between A0 and 9F
I did some googling and found two seperate tutorial scripts that I merged together and tweaked, those were used to make this.

This script allows us to create a list of all the combinations between any characters you insert
It then leaves behind a .txt file so we can cat, pipe and grep our URL's together for proper FUZZING!

Do you need a list that contains all the combinations with the characters 'A012' in 2x2 format? (Like I did!)
  This script does it automatically!
  Just change the input to 'A012' and you'll get =>
  
  aa
  a0
  a1
  a2
  0a
  00
  01
  02
  1a
  10
  11
  12
  2a
  20
  21
  22
  
*Ooooo Sparkle Sparkle!*

The .py file can be edited for any string lengths as well: 1x1, 1x2, 2x2, 8x9 and so on!
    
This script has been very useful to me, and its quite flexiable as well, you can add almost anything to it as its currently written.
I hope others find this useful as well!

I will be building upon this later, to make it cleaner with command input so you do not have to edit/save the
allcombo.py file constantly. That would be fun!

Fuzz The Planet!
