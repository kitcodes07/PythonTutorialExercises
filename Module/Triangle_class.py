from points_on_a_plane import Point


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__p_list = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return self.__p_list[0].distance_from_point(self.__p_list[1]) + \
            self.__p_list[0].distance_from_point(self.__p_list[2]) + \
            self.__p_list[1].distance_from_point(self.__p_list[2])


        # Write code here
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

