class HashSet:
    def __init__(self, contents=[]):
        # creates an empty list with size ten
        self.list = [None] * 10 
        
        # tracks the amount of non-'None' values stored in the list 
        self.numlist = 0

        # takes an array as an argument when HashSet is construced.
        # uses add method to place data in HashSet. 
        for item in contents:
            self.add(item)

    # helper function called by core 'add' method  
    # "__function" is a helper function        
    def __add(item, list):

        # idx = index where data should be stored
        idx = hash(item) % len(list)
        loc = -1
        
        # linear probing
        # while the index in the list holds data
        while list[idx] != None:        # the reason placeholder is needed
            if(list[idx] == item):      # if the value already appears in the list
                return False            # if false is returned then the main 'add' function does nothing
            if ((loc < 0) and (type(list[idx]) == HashSet.__Placeholder)): # loc will be less than 1 on it's first place only.
                loc = idx
            # wrap arround
            idx = (idx + 1) % len(list)
            
        if (loc < 0):
            loc = idx
        
        list[loc] = item
        
        return True
    
    def __rehash(oldlist: list[None], newlist: list[None]):
        for x in oldlist:
            if ((x != None) and (type(x) != HashSet.__Placeholder)):
                HashSet.__add(x, newlist)
        return newlist
    
    def add(self, item):
        if (HashSet.__add(item, self.list)):
            self.numlist += 1
            load = self.numlist / len(self.list)
            if (load > 0.75):
                # make a new list that is twice the size
                self.list = HashSet.__rehash(self.list, [None]*2*len(self.list))
    
    # Used as a placeholder for None in a the list for technical reasons (checking)
    class __Placeholder: 
        def __init__(self):
            pass
        
        def __eq__(self, other):
            return False
        
        def __str__(self):
            return "Placeholder"
        
    def __remove(item, list):
        # idx = index that should be removed from list
        idx = hash(item) % len(list) # [1, 2, 5, None, None, None, 7, 3, 4, Placeholder, 8, None]
        
        while list[idx] != None:                    # while data is stored at the specfic index in the HashSet
            if (list[idx] == item):                     # if the data you want to remove is located at the index
                nextIdx = (idx + 1) % len(list)             # set next index in HashSet
                if (list[nextIdx] == None):                 # if next index is empty
                    list[idx] = None                            # set currnt list index = empty
                else:                                       # if the next index holds data
                    list[idx] = HashSet.__Placeholder()         # set data in index to be the Placeholder/ this also ensures linear probing is not infinite(two lines down)
                return True
            
            idx = (idx + 1) % len(list)                     # if their was data stored at list[idx] that is not equal begin linear probing searching
        return False                                # if the list[idx] has no data then simply return false as it does not appear in the HashSet.
    
    def remove(self, item):
        if (HashSet.__remove(item, self.list)):
            self.numlist -= 1
            load = max(self.numlist, 10) / len(self.list)
            if load <= 0.25:
                # self.list = HashSet.__rehash(self.list, [None]*int(len(self.list)/2))
                self.list = HashSet.__rehash(self.list, [None]*(len(self.list)//2))
        else:
            raise KeyError("Item not is HashSet")
            
    def discard(self, item):
        if (HashSet.__remove(item, self.list)):
            self.numlist -= 1
            load = max(self.numlist, 10) / len(self.list)
            if load <= 0.25:
                # self.list = HashSet.__rehash(self.list, [None]*int(len(self.list)/2))
                self.list = HashSet.__rehash(self.list, [None]*(len(self.list)//2))
                
    def __contains__(self, item):
        idx = hash(item) % len(self.list)
        
        while self.list[idx] != None:
            if self.list[idx] == item:
                return True
            idx = (idx + 1) % len(self.list)            
        return False
    
    def __iter__(self):
        for i in range(len(self.list)):
            if (self.list[i] != None) and (type(self.list[i]) != HashSet.__Placeholder):
                yield self.list[i]
    
    def difference_update(self, other): # self = A, other = B -> A = A - B
        for item in other:
            self.discard(item)
            
    def difference(self, other): # self = A, other = B, result = C -> C = A - B
        result = HashSet(self)
        result.difference_update(other)
        return result
    
    def __len__(self):
        return self.numlist

    # hashSet[index]
    def __getitem__(self, item):
        idx = hash(item) % len(list)
        
        while self.list[idx] != None:
            if self.list[idx] == item:
                return self.list[idx]
            idx = (idx + 1) % len(self.list)

        return None

    
    def clear(self):
        self.numlist = 0
        self.list = [None] * 10
        
    def update(self, other):
        for item in other:
            self.add(item)
            
    def issupperset(self, other):
        for item in other:
            if item not in self:
                return False
        return True
        
    def __str__(self) -> str:
        return str(self.list)



def main():
    s = HashSet(list(range(100)))
    t = HashSet(list(range(10, 20)))
    u = HashSet(list(range(10, 20)))
    
    # Test #1: __len__ function
    if len(t) == len(u) and len(t) == 10:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    # Test #2: update function
    t.update(s)
    if len(s) == len(t):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
    
    # Test #2: clear function
    t.clear()
    t.update(u)
    if len(t) == len(u):
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")
        
    x = HashSet(['a','b','c','d','e','f','g','h','i','j','k'])
    y = HashSet(['c','d','e','l','m','n'])
    z = x.difference(y) # z = [a, b, f, g, h, i, j, k]
    
    # Test #4: difference & difference update functions
    if len(z) == 8:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")
        
    # Test #5: difference & difference update functions
    test5passed = True
    for item in z:
        if item not in ['a','b','f','g','h','i','j','k']:
            test5passed = False
            print("Test 5 Failed on ", item)
    if test5passed:
        print("Test 5 Passed")
        
    # Test #6: issuperset functionality
    if x.issupperset(z):
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")

if __name__ == '__main__':
    main()
    
