from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import os

# function to convert the tokenizer output style
def convert(lst):   
    return '\n'.join(lst) 

# declare the directory
directory = "./data/sigbovik/"
outputTokenizer = "./output/sigbovik/Tokenizer"
outputStemming= "./output/sigbovik/Stemming"
#dota file directory
dotaInput = "./data/dota2/"
outputDotaToken="./output/dota2/Tokenizer"
outputDotaStemmer = "./output/dota2/Stemming"
#r-python directory
r_PythonInput = "./data/r-python/"
output_r_Python_Token="./output/r-python/Tokenizer"
output_r_Python_Stemmer = "./output/r-python/Stemming"



# function to read files in directory and tokenize it
def tokenizeFile (input, output=0,combine=False ):
    tokenize_list_combined = []
    for filename in os.listdir(input):
        if filename.endswith(".txt"):
            f = open(os.path.join(input, filename), "r",  encoding="utf8") 
            text = f.read()
            if combine == False:
                file_out =open(os.path.join(output, filename), "w", encoding="utf8")
                tokenize_list =list(dict.fromkeys(word_tokenize(text)))
                file_out.write(convert(tokenize_list)+"\n")
            else:
                for word in word_tokenize(text):
                    tokenize_list_combined.append(word)
    if combine == True:
        file_out =open(os.path.join(output, "combined_files.txt"), "a+", encoding="utf8")
        tokenize_list =list(dict.fromkeys(tokenize_list_combined))
        file_out.write(convert(tokenize_list)+"\n") 

#Function to stem the files 
ps = PorterStemmer()
def StemFile(input, output=0,combine=False ):
        stem_list_combined=[]
        for filename in os.listdir(input):
            if filename.endswith(".txt"):
                f = open(os.path.join(input, filename), "r",  encoding="utf8") 
                tokenizeList = list(dict.fromkeys(word_tokenize(f.read())))
                stemList = []
                if combine == False:
                    file_out =open(os.path.join(output, filename), "w", encoding="utf8")
                    for word in tokenizeList:
                        stemList.append(ps.stem(word))
                        stemList = list(dict.fromkeys(stemList))
                    file_out.write(convert(stemList)+"\n")
                else:                    
                    for word in tokenizeList:
                        stem_list_combined.append(ps.stem(word))
        if( combine ==True ):
            file_out =open(os.path.join(output, "combined_files.txt"), "a+", encoding="utf8")
            stemList = list(dict.fromkeys(stem_list_combined))
            file_out.write(convert(stemList)+"\n") 




#calling the tokenizer function
# tokenizeFile(directory,outputTokenizer,True )
# StemFile(directory,outputStemming ,True)


tokenizeFile(dotaInput,outputDotaToken,True )
StemFile(dotaInput,outputDotaStemmer,True)

tokenizeFile(r_PythonInput,output_r_Python_Token,True )
StemFile(r_PythonInput,output_r_Python_Stemmer,True)

