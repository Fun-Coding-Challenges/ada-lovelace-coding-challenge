"""Solve the spy game!"""
import numpy as np


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Ada to hide out
    """

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """

        def convert_coordinate(coordinate):
            letter, digit = coordinate[0], coordinate[1:]
            return [ord(letter) - 65, int(digit) - 1]

        return [convert_coordinate(coordinate) for coordinate in agents]

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Ada to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        l = 10
        field = np.full((l, l), l)
        for x, y in agents:
            field[y, x] = 1
        for i in range(1, l + 1):
            for y in range(l):
                for x in range(l):
                    val = field[y][x]
                    if val == i:
                        if x > 0:
                            field[y][x - 1] = min(field[y][x - 1], val + 1)
                        if x < l - 1:
                            field[y][x + 1] = min(field[y][x + 1], val + 1)
                        if y > 0:
                            field[y - 1][x] = min(field[y - 1][x], val + 1)
                        if y < l - 1:
                            field[y + 1][x] = min(field[y + 1][x], val + 1)
        print(field)
        print(np.where(field == field.max()))

    def advice_for_ada(self, agents):
        """This method will take an array with agent locations and offer advice
        to Ada for where she should hide out in the city, with special advice for
        edge cases.

        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.

        Returns either a list of alphanumeric map coordinates for Ada to hide in,
        or a specialized message informing her of edge cases
        """
        pass
