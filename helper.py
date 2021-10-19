# When to use class methods and when to use static methods?


class Item:
    pass

    @staticmethod
    def is_integer(num):
        pass
    '''
    This should do something that has a relationship with the class,
    but not something that must be unique per instance
    '''

    @classmethod
    def instantiate_fom_csv(cls):
        pass
    '''
    This should also do something that has a relationship with the class,
    but usually, those are used to manipulate different structures of data to
    instantiate objects, like we have done with CSV.
    '''