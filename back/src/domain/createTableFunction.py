# def cjech():
#     table_variables = ['cat_id', 'name', 'subject', 'comments']
#     requiredCreateString = 'insert into'
#     tableName = "requestables"
#     requiredString= 'values'
#     query_parts = []
#     queryPart= ': '.join(table_variables)
#     print(queryPart)
#     if len(table_variables) > 0:
#         query_parts.extend([requiredCreateString, tableName, '('])
#         query_parts.extend([ i for i in table_variables])
#         query_parts.append(')')
#     query_parts.extend([requiredString, '('])
#     query_parts.append([map(Utils.dynamicSaveQuery(':', i)) for i in table_variables])
#     query_parts.append(')')
#     print(query_parts)

#     query = ' '.join(query_parts)
#     print(query)

    