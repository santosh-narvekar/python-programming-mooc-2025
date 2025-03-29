class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list):
    def length_of_route(route: ClimbingRoute):
        return route.length
    
    return sorted(routes,key=length_of_route,reverse=True)

def sort_by_difficulty(routes: list):
    def length_of_route(route: ClimbingRoute):
        return route.length
    
    def grade_of_route(route: ClimbingRoute):
        return route.grade
    
    hardest_to_easiest_route_via_length = sorted(routes,key=length_of_route,reverse=True)

    return sorted(hardest_to_easiest_route_via_length, key = grade_of_route, reverse=True)
