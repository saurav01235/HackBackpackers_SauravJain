def DateFromDaysSince2(days_to_add: int, baseline_date: str):
    return addDays(toDate(baseline_date), days_to_add)
