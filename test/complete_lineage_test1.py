import sqlparse
import re

tables = {"tables": {}, "alias": {}}
columns = []
splited_str = []


def process_sql_statement(text):
    split_str_comma = text.split(",")
    for i in split_str_comma:
        for j in i.split('\n'):
            if j == '':
                pass
            else:
                splited_str.append(j.strip())
                # if j in ignore_keyword:
                #     pass
                # else:
                #     splited_str.append(j.strip())


def parse_data():
    for i in splited_str:
        columns_pattern = [r"(\w+\.\w+)"]
        table_pattern = ["from\s(\w+)\)\sas\s(\w+)", "from\s(\w+)\)\s+(\w+)", "from\s(\w+)\sas\s(\w+)",
                         "inner\s+join\s+(\w+)\s+as\s+(\w+)"]

        for pat in columns_pattern:
            regex = re.compile(pat)
            match = regex.search(i)
            if match:
                columns.append(match.group(1))
                break

        for pat in table_pattern:
            regex = re.compile(pat)
            match = regex.search(i)
            print(match)
            if match:
                tbl = match.group(1)
                alias = match.group(2)
                tables["tables"][tbl] = ""
                tables["alias"][alias] = tbl
                print("--", match)


string = "Select a.name, b.age from contact as a inner join address as b on a.name = b.name;"
string = "Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;"
# string = """
# SELECT
# a.uid, b.uname
# FROM
# (select * from user) as a,
# (select * from user_details) as b;"""
#
# string = """
# SELECT
# a.uid, b.uname
# FROM
# (select * from user) a,
# (select * from user_details)  b"""

a = sqlparse.split(string.lower())

for i in a:
    process_sql_statement(i)
parse_data()

result = {}

for col in columns:
    tbl, c = col.split('.')
    if tbl in tables["alias"].keys():
        key = tables["alias"][tbl]
    else:
        key = tbl

    if key in result:
        result[key].append(c)
    else:
        result[key] = list()
        result[key].append(c)

print(splited_str)
print(tables)
print(columns)
print(result)
# mylex(string.lower())
