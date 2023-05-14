# Fill the Python code in this file
# from test_data import *
# ret_val=[]
# def json_search(key,input_object):
#     # ret_val=[]
#     if isinstance(input_object, dict): # Iterate dictionary
#         for k, v in input_object.items(): # searching key in the dict
#             if k == key:
#                 temp={k:v}
#                 ret_val.append(temp)
#             if isinstance(v, dict): # the value is another dict so repeat
#                 json_search(key,v)
#             elif isinstance(v, list): # it's a list
#                 for item in v:
#                     if not isinstance(item, (str,int)): # if dict or list repeat
#                         json_search(key,item)
#     else: # Iterate a list because some APIs return JSON object in a list
#         for val in input_object:
#             if not isinstance(val, (str,int)):
#                 json_search(key,val)
#     return ret_val
# print(json_search("issueSummary",data))
from test_data import *
def json_search(key,input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : "keyword" to be searched, case sensitive
    input_object : JSON object to be parsed, test_data.py in this case
    inner_function() is actually doing the recursive search
    return a list of key:value pair
    """
    ret_val=[]
    def inner_function(key,input_object):
        if isinstance(input_object, dict): # Iterate dictionary
            for k, v in input_object.items(): # searching key in the dict
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict): # the value is another dict so repeat
                    inner_function(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)): # if dict or list repeat
                            inner_function(key,item)
        else: # Iterate a list because some APIs return JSON object in a list
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_function(key,val)
    inner_function(key,input_object)
    return ret_val
print(json_search("issueSummary",data))
