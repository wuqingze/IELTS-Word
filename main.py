# -*- coding: utf-8 -*-
from generate_html import generate_page

def word_index(line):
    n = len(line)
    for i in range(n):
        if line[i] == ' ':
            return i

    return 0 

def main():
    for i in range(43,49):
        filename = "./Word-List/WordList-"+str(i)+".txt"
        with open(filename) as wordfile:
            lines = wordfile.readlines()
        lines = lines[1:]
        word_list = []
        for line in lines:
            index = word_index(line)
            word = line[0:index].strip()
            if len(word) >0 and word[-1] == '*':
                word = word[0:-1]
            word_list.append(word)
        outputfile = "./html-page/"
        if i<10:
            outputfile = outputfile+'0'+str(i)+".html"
        else:
            outputfile = outputfile+str(i)+".html"
        page = generate_page(word_list)
        with open(outputfile, 'w') as outfile:
            outfile.write(page)
if __name__ == "__main__":
    main()
