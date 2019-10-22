from collections import deque
people=deque(["Jens", "Mike", "Kim", "John", "Lars"])
people.popleft()
people.appendleft("Natazha")
print(people)