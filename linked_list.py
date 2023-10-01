class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_by_value(self, value):
        current_node = self.head

        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None

        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def delete_by_position(self, position):
        current_node = self.head

        if current_node == None:
            return

        current_position = 0
        prev_node = None

        while current_node and current_position != position:
            prev_node = current_node
            current_node = current_node.next
            current_position += 1

        if current_node != None:
            prev_node = current_node.next
            current_node = None

    def len_iterative(self):
        if self.head is None:
            return 0

        current = self.head
        counter = 0

        while current:
            counter += 1
            current = current.next

        return counter

    def __len_recursive(self, node: Node):
        if node == None:
            return 0

        return 1 + self.__len_recursive(node.next)

    def len_recursive(self):
        return self.__len_recursive(self.head)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    # This one swaps the values of the nodes ant not the nodes themselves
    def node_swap1(self, key1: str, key2: str):
        if self.head == None or key1 == key2:
            return

        node_1: Node | None = None
        node_2: Node | None = None
        current_node = self.head

        while current_node or (node_1 != None and node_2 != None):
            if current_node.data == key1:
                node_1 = current_node
            elif current_node.data == key2:
                node_2 = current_node

            current_node = current_node.next

        if node_1 and node_2:
            node_1.data, node_2.data = node_2.data, node_1.data

    # Change the direction of all the pointers in the list
    def reverse_iterative(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, prev_node):
            if not current_node:
                return prev_node

            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

            return _reverse_recursive(current_node, prev_node)

        self.head = _reverse_recursive(current_node=self.head, prev_node=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.data <= q.data:
            s, p = p, p.next
        else:
            s, q = q, q.next

        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next, p = p, p.next
            else:
                s.next, q = q, q.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def remove_duplicates_using_hash(self):
        prev_node = None
        current_node = self.head
        existing_nodes = dict()

        while current_node:
            if current_node.data in existing_nodes:
                prev_node.next = current_node.next
                current_node = None
            else:
                existing_nodes[current_node.data] = 1

            current_node = current_node.next

    def remove_nth_from_last(self, nth: int):
        length = self.len_iterative()

        if nth > length or nth <= 0:
            return

        if nth == length:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

        position = length - nth
        current = self.head
        for i in range(0, position):
            current = current.next

        node_to_delete = current.next
        current.next = current.next.next
        node_to_delete = None

    def print_nth_from_last(self, n):
        pointer = self.len_iterative()

        cur = self.head

        while cur:
            if pointer == n:
                print(cur.data)
                return cur.data

            pointer -= 1
            cur = cur.next

        if cur is None:
            return

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count
