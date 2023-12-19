x=0
while x <= 109:
 file = open("Lab9/preproinsulin-seq.txt", "r")
 if x <= 23:
   y = open("Lab9/lsinsulin-seq-clean.txt", "a")
   y.write(file.read()[x])
   x += 1 
 elif x > 23 and x <= 53:
   y = open("Lab9/binsulin-seq-clean.txt", "a")
   y.write(file.read()[x])
   x += 1 
 elif x > 53 and x <= 88:
   y = open("Lab9/cinsulin-seq-clean.txt", "a")
   y.write(file.read()[x])
   x += 1 
 else:
   y = open("Lab9/ainsulin-seq-clean.txt", "a")
   y.write(file.read()[x])
   x += 1 