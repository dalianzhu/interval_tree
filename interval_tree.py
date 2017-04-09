class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0

class IntervalTree(object):
    def __init__(self, left, right):
        self.nodes = [Node() for x in range(0, 2 * ((right - left) * 2 - 1))]
        self._build_tree(left, right, 1)

    def _build_tree(self, left, right, node_index):
        try:
            self.nodes[node_index].left = left
            self.nodes[node_index].right = right
            mid = (left + right) // 2
            # print("left {} right {} node_index{} nodes length{}".format(left, right, node_index, len(self.nodes)))

            if left != right - 1:
                self._build_tree(left, mid, 2 * node_index)
                self._build_tree(mid, right, 2 * node_index + 1)
        except:
            print("error left {} right {} node_index{} nodes length{}".format(left, right, node_index, len(self.nodes)))
    
    def insert_line(self, left, right):
        self._insert_line(left, right, 1)
    
    def _insert_line(self, left, right, node_index):
        mid = (self.nodes[node_index].left + self.nodes[node_index].right) // 2
        if [self.nodes[node_index].left, self.nodes[node_index].right] == [left, right]:
            self.nodes[node_index].count += 1
            return

        if right <= mid:
            # 线段在左子树上  
            self._insert_line(left, right, 2 * node_index)
            return
        
        elif left >= mid:
            # 线段在右子树上
            self._insert_line(left, right, 2 * node_index + 1)
            return
        else:
            # 一半在左，一半在右
            self._insert_line(left, mid, 2 * node_index)
            self._insert_line(mid, right, 2 * node_index + 1)
            return


    def search_line(self, left, right):
        return self._search_line(left, right, 1)
    
    def _search_line(self, left, right, node_index):
        mid = (self.nodes[node_index].left + self.nodes[node_index].right) // 2
        if [self.nodes[node_index].left, self.nodes[node_index].right] == [left, right]:
            return self.nodes[node_index].count

        if right <= mid:
            # 线段在左子树上  
            return self._search_line(left, right, 2 * node_index)
                    
        elif left >= mid:
            # 线段在右子树上
            return self._search_line(left, right, 2 * node_index + 1)
            
        else:
            # 一半在左，一半在右
            return self._search_line(left, mid, 2 * node_index) and \
            self._search_line(mid, right, 2 * node_index + 1)
            