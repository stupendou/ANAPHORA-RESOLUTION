file = open("0003_hin_tourism.txt", 'r', encoding="utf8")  # file = "asdfk#jhas faskl#dfsa"
data3 = file.read() # Read data from file
f = open("data3.txt", 'w', encoding="utf8")
final=[]
final_list=[]
for word in data3.split(" "):
    sent=[]
    for indi_word in word.split('#'):
        #if not(indi_word.isdigit()):
            sent.append(indi_word)
    #sent.append("|")
    final.append(sent)
for i in final: 
    final_list.append(i[0])
doc_1= " ".join(final_list)
#re.sub(r'ctx_[0-9]+', "" , doc_1)
f.write(doc_1)
f.close()
print("done")              


