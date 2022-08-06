import sqlparse
import re


class SqlParse:
    def __init__(self, text: str):
        self.text = text.lower()
        self.tables = {"tables": {}, "alias": {}}
        self.columns = []
        self.splited_str = []
        self.result = {}
        a = sqlparse.split(self.text)
        for i in a:
            self.process_sql_statement(i)
        self.parse_data()
        self.get_col()

    def process_sql_statement(self, text):
        split_str_comma = text.split(",")
        for i in split_str_comma:
            for j in i.split('\n'):
                if j == '':
                    pass
                else:
                    self.splited_str.append(j.strip())
                    # if j in ignore_keyword:
                    #     pass
                    # else:
                    #     splited_str.append(j.strip())

    def parse_data(self):
        for i in self.splited_str:
            columns_pattern = [r"(\w+\.\w+)"]
            table_pattern = ["from\s(\w+)\)\sas\s(\w+)", "from\s(\w+)\)\s+(\w+)", "from\s(\w+)\sas\s(\w+)",
                             "inner\s+join\s+(\w+)\s+as\s+(\w+)"]

            for pat in columns_pattern:
                regex = re.compile(pat)
                match = regex.search(i)
                if match:
                    self.columns.append(match.group(1))
                    break

            for pat in table_pattern:
                regex = re.compile(pat)
                match = regex.search(i)
                # print(match)
                if match:
                    tbl = match.group(1)
                    alias = match.group(2)
                    self.tables["tables"][tbl] = ""
                    self.tables["alias"][alias] = tbl
                    # print("--", match)

    def get_col(self):

        for col in self.columns:
            tbl, c = col.split('.')
            if tbl in self.tables["alias"].keys():
                key = self.tables["alias"][tbl]
            else:
                key = tbl

            if key in self.result:
                self.result[key].append(c)
            else:
                self.result[key] = list()
                self.result[key].append(c)


string1 = "Select a.name, b.age from contact as a inner join address as b on a.name = b.name;"
# string2 = "Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;"
# string3 = """
# SELECT
# a.uid, b.uname
# FROM
# (select * from user) as a,
# (select * from user_details) as b;"""
#
# string4 = """
# SELECT
# a.uid, b.uname
# FROM
# (select * from user) a,
# (select * from user_details)  b"""
obj = SqlParse(string1)
result = obj.result

for i, k in result.items():
    print(k,"==>", i)
