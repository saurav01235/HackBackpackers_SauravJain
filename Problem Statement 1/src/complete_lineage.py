import ply.lex as lex, re


class Lex:
    tokens = (
        "TABLE",
        "JOIN",
        "COLUMN",
        "TRASH"
    )

    t_TRASH = r"select|on|=|;|\s+|,|\t|\r"
    tables = {"tables": {}, "alias": {}}
    columns = []
    # def __init__(self):
    #     self.tables = {"tables": {}, "alias": {}}
    #     self.columns = []


    @staticmethod
    def t_TABLE(t):
        r"""from\s(\w+)\sas\s(\w+)"""

        regex = re.compile(Lex.t_TABLE.__doc__)
        m = regex.search(t.value, re.IGNORECASE)
        if m is not None:
            tbl = m.group(1)
            alias = m.group(2)
            Lex.tables["tables"][tbl] = ""
            Lex.tables["alias"][alias] = tbl

        return t

    @staticmethod
    def t_JOIN(t):
        r"""inner\s+join\s+(\w+)\s+as\s+(\w+)"""

        regex = re.compile(Lex.t_JOIN.__doc__)
        m = regex.search(t.value, re.IGNORECASE)
        if m is not None:
            tbl = m.group(1)
            alias = m.group(2)
            Lex.tables["tables"][tbl] = ""
            Lex.tables["alias"][alias] = tbl
        return t

    @staticmethod
    def t_COLUMN(t):
        r"""(\w+\.\w+)"""

        regex = re.compile(Lex.t_COLUMN.__doc__)
        m = regex.search(t.value)
        if m is not None:
            t.value = m.group(1)
            Lex.columns.append(t.value)
        return t

    @staticmethod
    def t_error(t):
        raise TypeError("Unknown text '%s'" % (t.value,))
        t.lexer.skip(len(t.value))


class ParseSql:

    def __init__(self, sql_query):

        self.sql_query = sql_query
        self.run()

        # self.parse_sql()

    def parse_sql(self):
        pass
        print(self.sql_query.split("from"))

    def run(self):
        lexer_rules = Lex()
        lexer = lex.lex(lexer_rules)
        lexer.input(self.sql_query.lower())
        for token in lexer:
            pass

        result = {}
        for col in lexer_rules.columns:
            tbl, c = col.split('.')
            if tbl in lexer_rules.tables["alias"].keys():
                key = lexer_rules.tables["alias"][tbl]
            else:
                key = tbl

            if key in result:
                result[key].append(c)
            else:
                result[key] = list()
                result[key].append(c)

        print(result)


if __name__ == "__main__":
#     query = """SELECT
# a.uid, b.uname
# FROM
# (select * from user) a,
# (select * from user_details) b;"""
    query = """Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;
"""
    obj = ParseSql(query)
