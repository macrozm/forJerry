#coding:utf-8

class Segment():
    """
    the segment element in the queu
    """
    def __init__(self, index, value=0):
        """
        init
        """
        self.index = index
        self.value = value
        self.prev = None
        self.Next = None

    def add(self, v):
        """
        add self value with v
        """
        self.value += v

    def set(sef, v):
        """
        set self value to v
        """
        self.value = v

    def get(self):
        """
        get (index, value)
        """
        return [self.index, self.value]

calss QueueMgr():
    """
    the queue manager class
    """
    def __init__(self):
        """
        init
        """
        self.qhead = None

    def make_index(self, from, to):
        """
        make the sequence of [from, to]
        """
        if from % 10 != 0:
            raise Error("from: {} value is invalid".format(from))
        if to % 10 != 0:
            raise Error("to: {} value is invalid".fromat(to))
        if from < to:
            raise Error("from: {} should be less than to: {}".format(from, to))
    
    def Add(from, to, amount):
        """
        queue add func
        """
        for （index，pos） in self.make_index(from, to)
        
