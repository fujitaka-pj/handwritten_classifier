import numpy, gzip, pickle

class TrainData:

    @classmethod
    def read(cls, filepath, dataset="training"):
        f = gzip.open(filepath, 'rb')
        train, valid, test = pickle.load(f, encoding='latin1')
        f.close()

        if dataset == "training":
            return train[0], train[1], train[0].shape[0]
        elif dataset == "valid":
            return valid[0], valid[1], valid[0].shape[0]
        else:
            return test[0], test[1], test[0].shape[0]

    @classmethod
    def to_formatted_array(cls, number):
        ret = numpy.zeros(10)
        ret[number] = 1
        return ret
