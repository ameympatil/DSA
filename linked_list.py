from platform import node


class Nodes:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,item):
        node = Nodes(item,self.head)
        self.head = node

    def insert_at_end(self,item):
        if self.head is None:
            node = Nodes(item)
            self.head = node
            return
        itr = self.head
        while(itr.next):
            itr = itr.next
        node = Nodes(item)
        itr.next = node

    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def remove_at(self,idx):
        if idx<0 or idx >=self.get_length():
            raise Exception("Invalid Index")

        if idx == 0:
            self.head = self.head.next
            return

        itr = self.head
        for i in range(1,self.get_length()):
            if i == idx-1:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self,idx,data):
        if idx<0 or idx >= self.get_length():
            raise Exception("Invalid index")
            return
        
        if idx == 0:
            self.insert_at_beg(data)
            return
        
        itr = self.head
        for i in range(0,self.get_length()):
            if i == idx-1:
                node = Nodes(data,itr.next)
                itr.next = node
                break
            itr = itr.next

    def insert_after_value(self,data_after,data_to_insert):
        if self.head == None:
            return

        if self.head.data == data_after:
            self.head.next = Nodes(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if data_after == itr.data:
                node = Nodes(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self,data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def show(self):
        if self.head is None:
            print("Empty List")
            return

        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + ' --> '
            itr = itr.next
        print(lstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana','mango','grapes','orange'])
    ll.show()
    print(ll.get_length())
    ll.remove_at(2)
    ll.show()
    ll.insert_at(0,"papaya")
    ll.show()
    print("**********************")
    print()
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.show()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.show()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.show()
    ll.remove_by_value("figs")
    ll.show()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.show()