a = "my name is anirudh hello \n\n"

# with open("text.txt","w") as f:
#   f.write(a)


fp =  open("text.txt","r") 

print(fp.read())
fp.close()
