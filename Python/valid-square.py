class Solution:
    def validSquare(
        self,
        p1: list[int],
        p2: list[int],
        p3: list[int],
        p4: list[int]
    ) -> bool:
        def vector(p1,p2)->list[int]:
            return [p1[0]-p2[0],p1[1]-p2[1]]
        def dot_prod(p1,p2,p3)->int:
            v1=vector(p1,p2)
            v2=vector(p2,p3)
            return v1[0]*v2[0]+v1[1]*v2[1]
        def distance_squared(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy
        points=[p2,p3,p4]
        point2=p1
        is_found=False
        for pf in points:
            points_remove_pf=points.copy()
            points_remove_pf.remove(pf)
            is_break=False
            for ps in points_remove_pf:
                if dot_prod(pf,point2,ps)==0:
                    point1=pf
                    point3=ps
                    is_break=True
                    is_found=True
                    break
            if is_break:
                break
        if not is_found:
            return False
        points.remove(point1)
        points.remove(point3)
        point4=points[0]
        if dot_prod(point2,point3,point4)!=0:
            return False
        if dot_prod(point3,point4,point1)!=0:
            return False            
        if dot_prod(point4,point1,point2)!=0:
            return False
        d1=distance_squared(point2,point3)
        d2=distance_squared(point3,point4)
        d3=distance_squared(point1,point4)
        d4=distance_squared(point1,point2)
        return d1!=0 and d1==d2 and d1==d3 and d1==d4


def run_tests():
    sol = Solution()

    tests = [
        (
            [0, 0],
            [1, 1],
            [1, 0],
            [0, 1],
            True,
        ),
        (
            [0, 0],
            [1, 1],
            [1, 0],
            [0, 12],
            False,
        ),
        (
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            True,
        ),
        (
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 0],
            False,
        ),
        (
            [0, 0],
            [2, 0],
            [2, 2],
            [0, 2],
            True,
        ),
        (
            [0, 0],
            [2, 0],
            [3, 1],
            [1, 1],
            False,
        ),
    ]

    for i, (p1, p2, p3, p4, expected) in enumerate(tests, start=1):
        result = sol.validSquare(p1, p2, p3, p4)

        print(f"Test {i}")
        print(f"points:   {p1}, {p2}, {p3}, {p4}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()