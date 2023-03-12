class Property:
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super.__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedroom = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footager: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedroom))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)



def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response



class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry= laundry

    def prompt_init(self):
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does"
            "the property have?",
            Apartment.valid_laundries
        )

        balcony = get_valid_input(
            "Does the property have a balcony?",
            Apartment.valid_laundries
        )

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })

        return parent_init

    promt_init = staticmethod(prompt_init)

