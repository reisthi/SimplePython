""" Algorithm to calculate how much time it will take to read a book."""

BOOK_PAGES = 283

reading_times = {
    'first_try':    2.1098,
    'second_try':   2.2325,
    'third_try':    2.07,
    'fourth_try':   1.0856,
    'fifth_try':    1.4842,
    'sixth_try':    2.0333,
    'seventh_try':  2.0,
    'eighth_try':   1.4138,
    'ninth_try':    2.3052,
    'tenth_try':    1.3418,
}


def get_times_only(times):
    times_only = times.values()
    return times_only


def sum_times(times):
    # total = sum(times.values())
    return sum(times.values())


def average_times(times):
    total = sum(times.values())
    return total / len(times)


def estimate_time(average_time):
    pages_per_day = BOOK_PAGES / 7
    time = pages_per_day * average_time
    return time


def needed_time(reading_results):
    sum_values = sum(reading_results.values())
    average_time = sum_values / len(reading_results)
    pages_per_day = BOOK_PAGES / 7
    time_needed = pages_per_day * average_time
    total = BOOK_PAGES * average_time / 60
    # print(f"sum of times:   {sum_values:.2f}",
    #       f"\naverage time:     {average_time:.2f}",
    #       f"\npages per day:    {pages_per_day:.2f}",
    #       f"\ntime needed:      {time_needed:.2f}",
    #       )
    print(f'The time you will have to spend to finish '
          f'the book in a week is: {time_needed:.2f} '
          f'mins a day. Total is: {total}hrs .'
          )


needed_time(reading_times)
