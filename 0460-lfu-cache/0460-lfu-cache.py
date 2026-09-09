class Node:

  def __init__(self, key=None, val=None):
    self.key = key
    self.val = val
    self.freq = 1
    self.prev = None
    self.next = None


class DoublyLinkedList:

  def __init__(self):
    self.head = Node()  # Dummy head
    self.tail = Node()  # Dummy tail
    self.head.next = self.tail
    self.tail.prev = self.head
    self._size = 0

  def __len__(self):
    return self._size

  def append_head(self, node):
    """Inserts a node right after the dummy head (Most Recently Used)."""
    node.next = self.head.next
    node.prev = self.head
    self.head.next.prev = node
    self.head.next = node
    self._size += 1

  def remove(self, node):
    """Removes a given node from the list."""
    node.prev.next = node.next
    node.next.prev = node.prev
    self._size -= 1

  def pop_tail(self):
    """Removes and returns the node right before the dummy tail (LRU)."""
    if self._size == 0:
      return None
    tail_node = self.tail.prev
    self.remove(tail_node)
    return tail_node


class LFUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}  # key -> Node
    self.freq_map = {}  # freq -> DoublyLinkedList
    self.min_freq = 0

  def _update_frequency(self, node: Node):
    """Increments a node's frequency and shifts it to the next frequency list."""
    freq = node.freq

    # Remove from current frequency list
    self.freq_map[freq].remove(node)
    if freq == self.min_freq and len(self.freq_map[freq]) == 0:
      self.min_freq += 1

    # Update node frequency
    node.freq += 1
    new_freq = node.freq

    # Add to the new frequency list
    if new_freq not in self.freq_map:
      self.freq_map[new_freq] = DoublyLinkedList()
    self.freq_map[new_freq].append_head(node)

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    node = self.cache[key]
    self._update_frequency(node)
    return node.val

  def put(self, key: int, value: int) -> None:
    if self.capacity == 0:
      return

    if key in self.cache:
      node = self.cache[key]
      node.val = value
      self._update_frequency(node)
    else:
      # If cache is full, evict the LRU node from the min_freq list
      if len(self.cache) >= self.capacity:
        evict_node = self.freq_map[self.min_freq].pop_tail()
        if evict_node:
          del self.cache[evict_node.key]

      # Insert new node
      new_node = Node(key, value)
      self.cache[key] = new_node
      self.min_freq = 1  # Reset min frequency to 1 for a brand new element

      if 1 not in self.freq_map:
        self.freq_map[1] = DoublyLinkedList()
      self.freq_map[1].append_head(new_node)
