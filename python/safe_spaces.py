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

    def convert_coordinates_inverse(self, agents):
        return [chr(x + 65) + str(y + 1) for x, y in agents]

    def propagate(self, coords, field, n, i):
        next_coords = set()
        for x, y in coords:
            field[x][y] = i
            if x > 0:
                next_coords.add((x - 1, y))
            if x < n - 1:
                next_coords.add((x + 1, y))
            if y > 0:
                next_coords.add((x, y - 1))
            if y < n - 1:
                next_coords.add((x, y + 1))
        next_coords -= {(x, y) for x, y in next_coords if field[x][y]}
        if next_coords:
            self.propagate(next_coords, field, n, i + 1)

    def find_safe_spaces(self, agents, n=10):

        """This method will take an array with agent locations and find
        the safest places in the city for Ada to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """

        field = np.zeros((n, n))
        agents = [(x, y) for x, y in agents if x < n and y < n]
        if len(agents) == n * n:
            return []
        for x, y in agents:
            field[x, y] = 1
        self.propagate(agents, field, n, 2)
        return np.argwhere(field == field.max()).tolist()

    def advice_for_ada(self, agents, l=10):
        """This method will take an array with agent locations and offer advice
        to Ada for where she should hide out in the city, with special advice for
        edge cases.

        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.

        Returns either a list of alphanumeric map coordinates for Ada to hide in,
        or a specialized message informing her of edge cases
        """
        numeric_agents = self.convert_coordinates(agents)
        save_spaces = self.find_safe_spaces(numeric_agents, l)
        if save_spaces:
            if len(save_spaces) == l ** 2:
                return 'The whole city is safe for Ada! :-)'
            return self.convert_coordinates_inverse(save_spaces)
        return 'There are no safe locations for Ada! :-('
