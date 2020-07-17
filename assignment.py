def most_freq_dict(string):
    txt=string.lower()
    clean_txt=txt.replace(' ','')
    my_dict={}
    for i in clean_txt:
        my_dict[i]=my_dict.get(i,0)+1
    print(my_dict)
most_freq_dict(input("Enter the string:"))
