# https://leetcode.com/problems/the-skyline-problem/
# https://youtu.be/POUMNJou4vc

import heapq
class Solution:
    def getSkyline(self, buildings):
        corners = []
        for l, r, h in buildings:
            corners.append((l, -h))
            corners.append((r, h))
        corners.sort()
        print(corners)
        # as heapq does not support delete element by value. 
        removed = []
        maxHeap = [0]
        res = []
        
        def getMaxHeight():
            mh = - maxHeap[0]  # max height
            while mh in removed:
                removed.remove(mh)
                heapq.heappop(maxHeap)
                mh = - maxHeap[0]
            return mh
        
        for x, y in corners:
            mh = getMaxHeight()
            if y < 0:
                if -y > mh:
                    res.append([x, -y])
                heapq.heappush(maxHeap, y)
            else:
                ph = mh
                removed.append(y)
                if y == mh:
                    mh = getMaxHeight()
                    if ph > mh: res.append([x, mh])
        
        return res