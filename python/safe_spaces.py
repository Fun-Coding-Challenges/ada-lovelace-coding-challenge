import string
import numpy as np

"""Solve the spy game!"""

class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Ada to hide out
    """

    def convert_to_alphanumeric(self, coordinates):
        letter_translation = {}

        for index, letter in enumerate(string.ascii_uppercase):
            letter_translation[index] = letter     

        newCoordinates = [letter_translation[x] + str(y + 1) for x, y in tuple(coordinates)] 
        return newCoordinates

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        letter_translation = {}

        for index, letter in enumerate(string.ascii_uppercase):
            letter_translation[letter] = index       
        
        newCoordinates = [[letter_translation[value[0]], int(value[1:]) - 1] for value in agents]
        return newCoordinates   


    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Ada to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """

        places = []
        for y in range(10):
            for x in range(10):
                places.append([x,y])
        
        secure_places = []
        max_value = 0
        for place in places:
            min_space = 100
            
            for agent in agents:
                difference = np.subtract(agent, place)
                square = sum(abs(difference))   
                if square < min_space:
                    min_space = square
                
            if(max_value < min_space):
                max_value = min_space
                secure_places.clear()
                secure_places.append(place)
            elif(max_value == min_space):                
                secure_places.append(place)
        
        if max_value != 0:   
            return secure_places
        else:
            return []   

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
        coordinates = self.convert_coordinates(agents)
        copy = list(coordinates)       
        coordinates = [copy.remove([x,y]) if ((x > 9) or (y > 9)) else [x,y] for x, y in tuple(coordinates)]        
        
        if coordinates == [None]:
            return 'The whole city is safe for Ada! :-)'
        else:
            safe_places = self.find_safe_spaces(coordinates)
            if safe_places == []:
                return 'There are no safe locations for Ada! :-('
           
            result = self.convert_to_alphanumeric(safe_places)            
            return result