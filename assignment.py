class MaxSizeList(object):
    
    def __init__(self,limit):
        self.limit = limit
        self.mylist = []
        
    def push(self,val):
        self.val = val
        self.mylist.append(self.val)
        if len(self.mylist)> self.limit:
            self.mylist.pop(0)
        
    def get_list(self):
        return self.mylist
        
