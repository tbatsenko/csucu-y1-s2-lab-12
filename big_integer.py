from node import TwoWayNode


class BigInteger(object):
    """docstring for BigInteger."""
    def __init__(self, initValue="0"):
        self.initValue = initValue
        self._head = TwoWayNode("")
        # print(len(initValue))
        for i in range(0, len(initValue)):
            # if self._
            rest = self._head
            # print("J")
            self._head = TwoWayNode(initValue[i])
            self._head.next = rest

    def toString(self):
        bigIntStr=""
        current = self._head
        previous = None
        while current is not None:
            bigIntStr += current.data
            current = current.next
        return bigIntStr[::-1]

    def comparable(self, other, operator="=="):
        return False
