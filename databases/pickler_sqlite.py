# Rochelle
from pickle import dumps
from pickle import Unpickler
from io import BytesIO


class Pickle(object):

    @staticmethod
    def pickle_data(data):
        p = []  # pickled_list
        for value in data:
            pickled = dumps(value)
            p.append(pickled)
        return p

    @staticmethod
    def unpickle_data(data):
        un_p = []  # un-pickled list
        for value in data:
            file = BytesIO(value)
            un_pickled = Unpickler(file).load()
            un_p.append(un_pickled)
        return un_p
