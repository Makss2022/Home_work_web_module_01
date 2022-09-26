from abc import abstractmethod, ABCMeta
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def save_file(self, file_name, some_date):
        pass


class SerializationDateJson(SerializationInterface):

    def save_file(self, file_name, some_date):
        with open(file_name, "w") as fh:
            json.dump(some_date, fh)


class SerializationDateBin(SerializationInterface):

    def save_file(self, file_name, some_date):
        with open(file_name, "wb") as fh:
            pickle.dump(some_date, fh)

