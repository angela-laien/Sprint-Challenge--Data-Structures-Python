class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0
    
    def append(self, item):
        # if the buffer storage is not full
        if len(self.storage) < self.capacity:
            # we can add item to it
            self.storage.append(item)
        # if the buffer storage if full
        else:
            # the newly added item will replace the oldest item in the buffer storage
            self.storage[self.oldest_index] = item
            # the item to the right then become the oldest
            self.oldest_index +=1

        # if the oldest item index reaches the capacity
        if self.oldest_index is self.capacity:
            # the oldest index will be 0 again
            self.oldest_index = 0      

    def get(self):
        return self.storage