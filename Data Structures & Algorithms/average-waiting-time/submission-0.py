class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        count = 0
        waiting = 0

        for arrival, prep in customers:
            if count < arrival:
                count = arrival

            count += prep
            waiting += count - arrival

        return waiting / len(customers)