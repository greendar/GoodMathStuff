

class NonLineError(Exception):

    def __init__(self, m, message = "A line cannot have 0 slope0"):
        pass
        """THIS IS NOT TRUE
        Need to add code for vertical and horizontal lines
        """


class NonQuadraticError(Exception):

    def __init__(self, a, message = "A quadratic cannot have a leading coefficient equal to zero."):
        self.a = a
        self.message = message
        super().__init__(self.message)