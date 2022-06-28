class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1
