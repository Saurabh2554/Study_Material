"""
The primary goal of the Strategy pattern is to define a set of algorithms, encapsulate them in their classes, and make them interchangeable within context objects. 
Through this encapsulation, the Strategy pattern promotes the open/closed principle — software entities should be open for extension but closed for modification.

https://chatgpt.com/c/68e88e48-b0c0-8323-9018-c73d609ebc66

"""

from abc import ABC, abstractmethod
from typing import List

class ISortStrategy(ABC):
    @abstractmethod
    def sort(self,nums_list:List):pass


class BubbleSortStrategy(ISortStrategy):
    def sort(self,nums_list:List):
        print("List sorted using bubble sort...")

class MergeSortStrategy(ISortStrategy):
    def sort(self,nums_list:List):
        print("List sorted using merge sort...")

class SortContext():
    def __init__(self, sort_strategy:ISortStrategy):
        self.sort_strategy = sort_strategy

    def set_strategy(self,sort_strategy: ISortStrategy):
        self.sort_strategy = sort_strategy   

    def sort(self,list_nums:List):
        self.sort_strategy.sort(list_nums)

# Dynamic strategy implementation...
STRATEGY_MAP = {
    'bubble_sort':BubbleSortStrategy,
    'merge_sort':MergeSortStrategy
}

def sort_numbers(num_list, strategy_name):
    strategy_class = STRATEGY_MAP.get(strategy_name, None)
    context = SortContext(strategy_class())
    context.sort(num_list)


if __name__ == "__main__":
    list_nums = [1,2,3,4,5]
    sort_numbers(list_nums, 'bubble_sort')
    sort_numbers(list_nums, 'merge_sort')

