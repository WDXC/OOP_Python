from Inherit_implements import Property, get_valid_input

class House(Property):
    valid_garge = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories="",
                 garge="", fenced="", **kwargs):
        super().__init__(**kwargs)
        self.garage = garge
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garge: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garge = get_valid_input("Is there a garge? ",
                                House.valid_garge)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garge": garge,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase(House):
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

class Rental(House):
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished = get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")
            )
        )

    prompt_init = staticmethod(prompt_init)
