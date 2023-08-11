# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import utils.in_memoryDb
# import utils.inverted_index4
# import sys
# sys.path.append('utils')
import os
from flask import Flask, request, render_template
from flask_cors import CORS
# from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
# try:
#     from search import * 
# except NameError:
#     from search import *
# import search
# from search import searchKeys
# from utils.search import *
# from utils.search import searchKeys
# from search import *
# from search import searchKeys
# from testdocuments import *
# from utils import *
# from utils import *
# from utils.search import searchKeys
# from utils.myclass import MyClass

app = Flask(__name__)
cors = CORS(app)

@app.route("/static/", methods = ["GET"])
def loadHome():
    # return {'data': 'test'}, 200  # return data and 200 OK code
    return render_template('index.html')

@app.route("/search", methods = ["POST"])
def search_key():
    print("@@@@@@@@@@@")
    request_data = request.get_json()

    print(type(request_data))
    print("@@")

    # # Create an instance of the MyClass
    # my_class_instance = MyClass()
    #
    # # Call the method from the MyClass to process the data
    # processed_data = my_class_instance.process_data("tttt")
    #
    print(request_data["searchkeys"])
    print("----------")

    # my_class_instance = searchKeys(request_data)
    # utils.search.searchKeys(request_data["searchkeys"])

    return {'data': "success"}, 200  # return data with 200 OK
    # files_list = searchKeys(request_data["searchkeys"])
    # return {'data': 'hj'}, 200  # return data with 200 OK
    # return {"path": "output_csv_file_cool.csv"}


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# def highlight_term(id, term, text):
#     replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
#     return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)
#
# #path to documents folder
# folder_path = '/documents'
#
# def read_all_documents(folder_path):
#     document_names = []
#     for file_name in os.listdir(folder_path):
#         if os.path.isfile(os.path.join(folder_path, file_name)):
#             document_names.append(file_name)
#     return document_names
#
# def main():
#     utils.in_memoryDb = utils.in_memoryDb.InMemoryDb()
#     utils.inverted_index4 = utils.inverted_index4.InvertedIndex4(utils.in_memoryDb)
#
#     utils.inverted_index4.writeToFile(*utils.inverted_index4.createDictionary())
#
#     document1 = {
#         'id': '1',
#         'text': 'The beer drinking big sharks of Belgium drink beer.'
#     }
#     document2 = {
#         'id': '2',
#         'text': 'Belgium has great beer. They drink beer all the time.'
#     }
#
#     documents = read_all_documents('./documents')

    # Print the document names
    # for document in documents:
    #     print('Reading document---------------- '+document)
    #     utils.inverted_index.index_document(document)

    # utils.inverted_index.index_document(document1)
    # utils.inverted_index.index_document(document2)
    #
    # search_term = input("Enter term(s) to search: ")
    # result = utils.inverted_index.lookup_query(search_term)

    # for term in result.keys():
    #     for appearance in result[term]:
    #         # Belgium: { docId: 1, frequency: 1}
    #         document = utils.in_memoryDb.get(appearance.docId)
    #         print(highlight_term(appearance.docId, term, document['text']))
    #     print("-----------------------------")


# api.add_resource(Search, '/search')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #main()
    app.run(debug=True)  # run our Flask app


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
