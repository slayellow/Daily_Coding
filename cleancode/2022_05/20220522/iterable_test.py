from datetime import date, timedelta


# # __iter__에서 Generator를 사용할 수 있게 변경
# class DateRangeIterable:

#     def __init__(self, start_date, end_date) -> None:
#         self.start_date = start_date
#         self.end_date = end_date

#     def __iter__(self):
#         current_day = self.start_date
#         while current_day < self.end_date:
#             yield current_day
#             current_day += timedelta(days=1)

# # Iterable 객체 만들기
# class DateRangeIterable:

#     def __init__(self, start_date, end_date) -> None:
#         self.start_date = start_date
#         self.end_date = end_date
#         self._present_day = start_date

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._present_day >= self.end_date:
#             raise StopIteration
#         today = self._present_day
#         self._present_day += timedelta(days=1)
#         return today


# Sequnce 방식 (__len__, __getitem__)
class DateRangeSequence:
    def __init__(self, start_date, end_date) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


s1 = DateRangeSequence(date(2022, 5, 20), date(2022, 5, 25))
for day in s1:
    print(day)

# for loop Operation : iter() -> __iter__() ->  next() -> __next__() -> StopIteration이 발생할때까지
# for day in DateRangeIterable(date(2022, 5, 20), date(2022, 5, 31)):
#     print(day)
# r1 = DateRangeIterable(date(2022, 5, 20), date(2022, 5, 22))
# print(", ".join(map(str, r1)))
# print(max(r1))
