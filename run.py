#coding:utf-8

import numpy as np

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
        self.next = None
    
    def insert_to_next(self, seg):
        """
        add seg to our next, if self is tail, then just add tail,
            else insert it
        """
        if self.next:
            next = self.next
            print("seg add_next, {} insert {}, {}".format(self.index, seg.index, next.index))
            self.next, next.prev, seg.prev, seg.next = seg, seg, self, next
        else:
            print("seg add_next to tail: {} {}".format(self.index, seg.index))
            self.next, seg.prev = seg, self
    
    def insert_to_prev(self, seg):
        """
        add seg to our prev
        """
        if self.prev:
            prev = self.prev
            print("seg add_prev, {} insert {}, {}".format(prev.index, seg.index, self.index))
            prev.next, self.prev, seg.prev, seg.next = seg, seg, prev, self
        else:
            print("seg add_next to tail: {} {}".format(self.index, seg.index))
            self.next, seg.prev = seg, self

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

class QueueMgr():
    """
    the queue manager class
    """
    def __init__(self):
        """
        init
        """
        self.qhead = None
        self.index_dict = {}

    def check_valid(self, start, end):
        """
        check the value is valid
        """
        if start % 10 != 0:
            raise Error("from: {} value is invalid".format(start))
        if end % 10 != 0:
            raise Error("to: {} value is invalid".fromat(end))
        if start >= end:
            raise Error("from: {} should be less than to: {}".format(start, end))

    def make_index(self, start, end):
        """
        make the sequence of [from, to]
        """
        seq = np.arange(start, end + 10, 10)
        yield (seq[0], 'head')
        for e in seq[1:-1]:
            yield (e, 'middle')
        yield (seq[-1], 'end')

    def is_empty(self):
        """
        test if the queue is empty
        """
        return self.qhead is None

    def init_queue(self, start, end, amount):
        """
        init the queue, called when the queue is empty
        """
        for (index, pos) in self.make_index(start, end):
            if pos == 'head':
                seg = Segment(index, value=amount)
                self.qhead = seg
                print("init queue(head) add index {} value {} to queue".format(seg.index, seg.value))
                self.index_dict[index] = seg
            if pos == 'end':
                seg = Segment(index, value=0)
                self.index_dict[index] = seg
                self.qhead.insert_to_next(seg)
                print("init queue(end) add index {} value {} to queue".format(seg.index, seg.value))

    
    def get_tail(self):
        """
        return the tail seg
        """
        if not self.qhead:
            raise(Error("the queue is empty"))

        head = self.qhead
        while head:
            if head.next is None:
                return head
            head = head.next


    def add_node(self, node):
        """
        add one node to the queue
        """
        pos = None
        for seg in self.all_seg():
            if node.index < seg.index:
                pos = seg
                print("add_node, find pos:", seg.index)
                break
        #if not find position,  it would be the new tail;
        if not pos:
            pos = self.get_tail()
        #insert the next of seg
        pos.insert_to_prev(node)
        if node.prev:
            node.add(node.prev.value)

    def add_head(self, index, amount):
        """
        add head, check index in queue or not,
            in queue: just add amount to the value
            not in queue:
                if index is the new head of the queue, just add it;
                if index is not the head, then the new value is seq(index).prev.value + amount
        """
        print("add_head ", index, " ", amount)
        is_exist = index in self.index_dict
        if is_exist:
            print('exist ', index, ' ', amount, '')
            node = self.index_dict[index]
            node.add(amount)
            return

        is_newhead = index < self.qhead.index
        node = Segment(index, value=amount)
        if is_newhead:
            node.add_to_next(self.qhead)
            self.qhead = node
            self.index_dict[index] = node
            return
        #would be in the middle of the queue
        self.add_node(node)
        self.index_dict[index] = node


    def add_middle(self, index, amount):
        """
        add in the middle of the queue
        """
        print("add middle {} {}".format(index, amount))
        if index in self.index_dict:
            self.index_dict[index].add(amount)
            print("in add middle {} {}".format(index, amount))
        else:
            print("in add middle {} not in dict".format(index))
            print(self.index_dict)
        return
    
    def add_end(self, index, amount):
        """
        add to the end of the queue
        """
        print("add end  {} {}".format(index, amount))
        if index in self.index_dict:
            return
        #if index is in the middle, also do nothing
        tail = self.get_tail()
        if tail.index > index:
            return
        node = Segment(index, value=0) #required from the demo
        tail.insert_to_next(node)
        self.index_dict[index] = node
        return

    def add(self, start, end, amount):
        """
        queue add func
        """
        self.check_valid(start, end)
        if self.is_empty():
            self.init_queue(start, end, amount)
            return

        for (index, pos) in self.make_index(start, end):
            print("make_index return index: {} pos:{}".format(index, pos))
            if pos == 'head':
                self.add_head(index, amount)
            if pos == 'middle':
                self.add_middle(index, amount)
            if pos == 'end':
                self.add_end(index, amount)
    
    def all_seg(self):
        """
        iter the segs in self.qhead in order
        """
        head = self.qhead
        while head != None:
            yield head
            head = head.next

    def to_string(self):
        """
        show the queue with string
        """
        for e in self.all_seg():
            print(e.get())
        
def main():
    print("main")
    queue_mgr = QueueMgr()
    queue_mgr.add(10, 30, 1)
    queue_mgr.to_string()
    print("new")
    queue_mgr.add(20, 40, 1)
    queue_mgr.to_string()

    print("new")
    queue_mgr.add(10, 40, -2)
    queue_mgr.to_string()

    print("new main")
    queue_mgr = QueueMgr()
    queue_mgr.add(10, 30, 1)
    queue_mgr.to_string()
    print("new")
    queue_mgr.add(20, 40, 1)
    queue_mgr.to_string()

    print("new")
    queue_mgr.add(10, 40, -1)
    queue_mgr.to_string()
    print("new")
    queue_mgr.add(10, 40, -1)
    queue_mgr.to_string()

if __name__ == "__main__":
    main()