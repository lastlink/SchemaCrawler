from __future__ import print_function
import re
from schemacrawler.schema import TableRelationshipType # pylint: disable=import-error
from schemacrawler.schemacrawler import IdentifierQuotingStrategy # pylint: disable=import-error
from schemacrawler.utility import MetaDataUtility # pylint: disable=import-error

print('Project "' + catalog.crawlInfo.runId + '" {')
print('  database_type: "' + re.sub(r'\"', '', catalog.crawlInfo.databaseVersion.toString()) + '"')
print("  Note: '''")
print(catalog.crawlInfo)
print("  '''")
print("}")

# Columns
for table in catalog.getTables():
  print('Table "' + re.sub(r'\"', '', table.fullName) + '" {')
  for column in table.columns:
    print('  "' + column.name + '" "' + column.columnDataType.name + '"', end = '')
    # Column attributes
    print(' [', end = '')
    if not column.nullable:
      print('not ', end = '')
    print('null', end = '')
    if column.hasDefaultValue():
      print(', default: "' + column.defaultValue + '"', end = '')
    if column.hasRemarks():
      print(", note: '" + column.remarks + "'", end = '')
    print(']', end = '')
    print()
  if table.hasRemarks():
    print("  Note: '''")
    print(table.remarks)
    print("  '''")
  if table.hasPrimaryKey() or not table.indexes.isEmpty():
    print('  indexes {')
    if table.hasPrimaryKey():
      primaryKey = table.primaryKey
      print("    (" + MetaDataUtility.getColumnsListAsString(primaryKey, IdentifierQuotingStrategy.quote_all, '"') + ") [pk]")
    if not table.indexes.isEmpty():
      for index in table.indexes: 
        if table.hasPrimaryKey() and \
          MetaDataUtility.getColumnsListAsString(table.primaryKey, IdentifierQuotingStrategy.quote_all, '"') == \
          MetaDataUtility.getColumnsListAsString(index, IdentifierQuotingStrategy.quote_all, '"'):
          continue    
        print("    (" + MetaDataUtility.getColumnsListAsString(index, IdentifierQuotingStrategy.quote_all, '"') + ")", end = "")
        if index.unique:
          print(" [unique]")
        else:
          print()     
    print('  }')
  print('}')
  print('')
      
"""
for table in catalog.tables:  
  for childTable in table.getRelatedTables(TableRelationshipType.child):
    print('  ' + table.name + ' ||--o{ ' + childTable.name + ' : "foreign key"')
  print('')
"""

# Table groups
for schema in catalog.schemas:
  print('TableGroup "' + re.sub(r'\"', '', schema.fullName) + '" {')
  for table in catalog.getTables(schema):
    print('  "' + re.sub(r'\"', '', table.fullName) + '\"')
  print('}')
  print('')