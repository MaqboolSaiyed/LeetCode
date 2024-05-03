class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        lenA = 0
        lenB = 0
        currentA = headA
        currentB = headB

        # Calculate the lengths of the two lists
        while currentA:
            lenA += 1
            currentA = currentA.next

        while currentB:
            lenB += 1
            currentB = currentB.next

        # Move the longer list's head to the same starting position as the shorter list
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        currentA = headA
        currentB = headB

        # Traverse the lists until the end or the intersection is found
        for _ in range(abs(lenA - lenB)):
            currentA = currentA.next

        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next

        return None