class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    # lt it means less than
    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    # repr return a more-information,or offical,
    # string representation of an object
    def __repr__(self):
        return "{}:{}".format(self.string, self.number)
