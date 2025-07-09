if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    sol = Solution()
    order = sol.findOrder(numCourses, prerequisites)
    print("Order to take courses:", order)