#import re
#def real_len(text):
    
  
   #control_chars_pattern = r'[\n\f\r\t\v]'
    #cleaned_string = re.sub(control_chars_pattern, '', text)
    #return len(cleaned_string)
fd = open("test123", "w" )
fd.write("HEllo World\n")

fd.write("\ngood day.\nand i like it ")
fd.flush()
#fd.close
#exit()
fd = open("test123", "r")
buf = fd.read()
print(buf)
fd.seek(2)
buf = fd.read(3)
print(buf)