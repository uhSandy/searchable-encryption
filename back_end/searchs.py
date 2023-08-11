from trapdoor_manager import *
from bloom_test import *
from test import *
from encryption_manager import *
import json
import ast
import time

def searchKeys(searchKeys):

    print("------------------Search started")
    start_time_search = time.time()
    #get trapdoor values
    print("------------------Getting trap door values")
    trapdoorkeys = calltrapdoor(searchKeys)

    #find files for keywords from inverted index
    files_list =  getdatafiles(trapdoorkeys)
    end_time_search = time.time()
    elapsed_time_search = end_time_search - start_time_search
    print(f"-------Data search ended with {elapsed_time_search} seconds-----------")

    return files_list

def calltrapdoor(searchKeys):
    keywordtags = []
    for searchkey in searchKeys:
        tag = create_tag(searchkey)
        keywordtags.append(tag)

    #print(keywordtags)
    #call bllom filter
    print("------------------Check search key values exists using bloom filter")
    exisistingwords = searchWords(keywordtags)
    #print(exisistingwords)
    return exisistingwords


def getdatafiles(trapdoorkeys):

    #decrypt index file
    print("------------------Decrypt index")
    decrypteddata = decryptFile("D:/Private/Python/Sources/data/index_encrypted.bin", '')

    dictionary_data = json.loads(decrypteddata)

    return getfilesincluding(trapdoorkeys, dictionary_data)


def getfilesincluding(trapdoorkeys, dictionary_data):
    #print("=======#######====================================================")
    #print(dictionary_data)
    #print(trapdoorkeys)
    print("------------------Get match files data")
    matchfiles = search_value(dictionary_data, "tag", trapdoorkeys)

    print(matchfiles)

    # if search_value(dictionary_data, "tag", trapdoorkeys):
    #     print("At least one of the search values exists for the given key in the dictionary.")
    # else:
    #     print("None of the search values exist for the given key in the dictionary.")

    # Save output data into files
    files_list = []
    for searchkey in matchfiles:
        #print(">> Saveeeeeeeeeeee====================")
        #print(searchkey)
        #print(matchfiles[searchkey])
        filename = "output_csv_file_"+searchkey+".csv"
        files_list.append(filename)
        utils.test.find_rows_with_word(matchfiles[searchkey], filename, searchkey)

    return files_list

   #utils.test.find_rows_with_word(input_csv_file, output_csv_file, search_word)


def search_value(dictionary, searchkey, values):
    matches = {}

    dictionaryd = ast.literal_eval(dictionary)
    if isinstance(dictionaryd, dict):
        for key, sub_dict in dictionaryd.items():
            #print(sub_dict[searchkey])
            #print(sub_dict[searchkey] in values)
            if searchkey in sub_dict and sub_dict[searchkey] in values:
                matches[key] = sub_dict['docName']

    return matches

searchKeys(['doppler', 'intermittent', 'cool'])