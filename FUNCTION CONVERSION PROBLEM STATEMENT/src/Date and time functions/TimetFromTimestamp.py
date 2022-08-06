def TimetFromTimestamp(timestamps):
    # currentUTC()
    retrun toLong( timestamps - toTimestamp('1970-01-01 00:00:00.000', 'yyyy-MM-dd HH:mm:ss.SSS') ) * 1000l