class Inventory:
    def lock(self, item_type):
        '''Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different customers'''
        pass

    def unlock(self, item_type):
        '''Release the given type so that other
        customers can access it.'''
        pass

    def purchase(self, item_type):
        '''if the item is not locaked, raise an
        exception. If the itemtype does not exist,
        raise an exception. If the item is currently
        Is available, subtract one item and return
        the number of items left.'''
        pass

item_type = 'widget'
inv = Inventory
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("sorry, we don't sell {}".format(item_type))

except OutOfStock:
    print("Sorry, that item is out of stock")

else:
    print("Purchase complete. There are "
          "{} {}s left".format(num_left, item_type))