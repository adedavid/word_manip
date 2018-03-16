''' word_manip module: a module defining a number of useful 
functions:
- takes in a string and returns a list of lists containing sentences parsed out into words: sep_words(userstr_in) function
- takes in a list of lists each containing a sentence and creates a single string: comb_words(big_list) function
- encrypts and decrypts text using a simple letter swap: crypto(x,n,enc)function

'''
# ----------------------------------------------------------
def sep_words(userstr_in) :
    ''' takes in a string and returns a list of lists containing
    sentences parsed out into words'''
    str_in = userstr_in.split(" ") 
    str_in = userstr_in.split(" ") 
    s_end = 0 # to count the number of sentences
    outer_list = []
    inner_list = []
    
    for word in str_in :
        
        wordlen = len(word)
        delimiter_list = ['?','!','.',] #sentence terminator
        
        if len(word) != 0 : # to avoid calculating the lenght of a whitespace character 
            delimiter = word[wordlen - 1]# since index begins at zero, wordlen needs adjustment
            if delimiter in delimiter_list :
                word = word.strip(delimiter) #delimiter is removed from word
                inner_list.append(word)
                inner_list.append(delimiter)
                outer_list.insert(s_end, inner_list) #inner_list is formed when delimiter is found  
                s_end += 1
                inner_list = []  # inner_list is initialized for the next sentence to begin
            else:
                inner_list.append(word) #if no delimiter is found, words are appended straight away     
        else:
            inner_list.append(word)
    if len(inner_list) == 0 :  #this ensures we dont have inner list with empty element
        pass
    else:
        s_end += 1
        outer_list.insert(s_end, inner_list)
    
    return outer_list
# ----------------------------------------------------------
import random
def comb_words(big_list) :
    '''takes in a list of lists each containing a sentence and
    creates a single string'''
    new_list = []
    delimiter_list = ['?','.','!']  # a list of sentence delimiters is created
    for small_list in big_list: #Outer loop to test each work for delimiter
        str_in = ''
        for element in small_list : #inner loop to search for delimiter
            if element in delimiter_list :
                delim_posit = small_list.index(element) #determines the index of delimiter
                element = small_list[delim_posit - 1] + element #concatenates delimiter with preceding word
                small_list[delim_posit - 1] = element #replaces word preceding the delimiter
                del small_list[delim_posit] # deletes the word preceding the delimiter
                
            else:             
                pass
        small_list = ' '.join(small_list) #form string from the inner list   
        new_list.append(small_list)
    out_str = ' '.join(new_list)      
    return out_str            
# ----------------------------------------------------------
def crypto(x,n,enc):
    '''encrypts and decrypts text using a simple letter swap'''
    random.seed(n)
    alphabet = "abcdefghijklmnopqrstuvwxyz"  #string of regular alphabet
    alphabet_list = list(alphabet)
    randarray = range(0,26)    #array to contain randomized alphabet
    random_list = list(randarray) 
    random.shuffle(random_list)
    dic = {}  # dictionary that maps keys(swapped_alphabet) to values(regular alphabet)
    swapped_alphabet = ""
    for i in range(0, len(alphabet)) :
        if enc == 'True' :
            swapped_alphabet += alphabet[random_list[i]]
            dic[alphabet[i]]=alphabet[random_list[i]]  #loop to populate the dic {}
        elif enc == 'False' :
            swapped_alphabet += alphabet[randarray[i]]
            dic[alphabet[i]]=alphabet[randarray[i]]

    #list of encrypted words is initialized
    encrypt = []

    for word in x:  #outer loop for each word in the original list
        str_wap = ""   # encrypted character or string of characters begins here
        for character in word:
            
            if (character in dic) :
                character = dic[character]
                str_wap += character
            elif (character.lower() in dic):  # handles character that appear as uppercase
                character = character.lower()
                character = dic[character]
                character = character.upper()
                str_wap += character
            else:
                str_wap += character
        encrypt.append(str_wap)
    return encrypt
# ----------------------------------------------------------
