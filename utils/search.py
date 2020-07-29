
def searchDictInListOfDict(dict_list, search_by_filed, expected_field_content):
  return next((item for item in dict_list if
               item[search_by_filed] == expected_field_content), None)
