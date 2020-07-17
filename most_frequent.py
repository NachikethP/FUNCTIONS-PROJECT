def most_frequent(string):
    txt=string.lower()
    clean_txt=txt.replace(' ','')
    my_dict={}
    for i in clean_txt:
        my_dict[i]=my_dict.get(i,0)+1

    print("frequency of characters:")

    for j in sorted(my_dict,key=my_dict.get,reverse=True):
        print(j+"=",my_dict[j])

most_frequent(input("Please enter a string:"))
