
class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        def str_to_tuple(date:str)-> tuple[int,int]:
            nums=date.split("-")
            return (int(nums[0]),int(nums[1]))

        def date_to_day_count(date:tuple[int,int])->int:
            days_in_month=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            result=0
            for i in range(date[0]):
                result+=days_in_month[i]
            result+=date[1]
            return result

        
        date_arriveAlice=str_to_tuple(arriveAlice)
        date_leaveAlice=str_to_tuple(leaveAlice)
        date_arriveBob=str_to_tuple(arriveBob)
        date_leaveBob=str_to_tuple(leaveBob)

        start_date_together_count=date_to_day_count(max(date_arriveAlice,date_arriveBob))
        end_date_together_count=date_to_day_count(min(date_leaveAlice,date_leaveBob))
        result=end_date_together_count-start_date_together_count+1
        return max(0,result)

def run_tests():
    sol = Solution()

    tests = [
        ("08-15", "08-18", "08-16", "08-19", 3),
        ("10-01", "10-31", "11-01", "12-31", 0),
        ("01-01", "01-01", "01-01", "01-01", 1),
        ("05-01", "05-10", "05-03", "05-05", 3),
        ("05-03", "05-05", "05-01", "05-10", 3),
        ("12-30", "12-31", "12-31", "12-31", 1),
        ("02-28", "03-02", "03-01", "03-05", 2),
    ]

    for i, (arriveAlice, leaveAlice, arriveBob, leaveBob, expected) in enumerate(
        tests, start=1
    ):
        result = sol.countDaysTogether(
            arriveAlice,
            leaveAlice,
            arriveBob,
            leaveBob
        )

        print(f"Test {i}")
        print(f"Alice:    {arriveAlice} -> {leaveAlice}")
        print(f"Bob:      {arriveBob} -> {leaveBob}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()