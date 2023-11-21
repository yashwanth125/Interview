## Pseudocode
# Code below is written in python by Yashwanth for Qualcomm interview.
#
#Steps:
# 1. Initialise the 
## a. Belt of length 3, for belt we are using Deque Data structure in python.
## b. workers count, here we took it as three
# 2. Iterate for 100 steps and in each step, remove the last element from end 
#    and append the new component randomly generated to the left side of the deque
# 3. During each iteration, perform the assining of components based on below scenarios
## a. If adjacent worker performed a task then block the worker
## b. If the product is completed and waiting then decerement the count by 1
## c. If components is not assigned to worker and its present in the belt adjacent to them then assign it to him
## d. If the belt component is empty then push the product if its ready at workers hand.




import collections
import random
import collections
belt = collections.deque(['-','-','-'])
test_list=['A','B','-']
length = 3
workers = [{'upper': {'items': [], 'wait': 0}, 'lower': {'items': [], 'wait': 0}} for i in range(length)]
result ={}


# helper function to validate making product
def helper(data):
    counts =collections.Counter(data)
    #print(counts)
    return counts['A']>=1 & counts['B']>=1

## For loop to iterate for 100 steps
for i in range(100):
    #remove the last element from belt with capacity of 3
    last = belt.pop()
    print('last_value',last)
    if last != '-':
        result[last] = (result.get(last, 0) + 1)
    new_val = random.choice(test_list)
    ## Adding new element to the left side of the queue
    belt.appendleft(new_val)
    print('added new_value',new_val)
    taken =False
    # Iterate over the workers present in upper and lower side of the belt and assign the components.
    for j, worker in enumerate(workers):
        upper = worker['upper']
        lower = worker['lower']
        def update(side):
            global taken
            if taken:
                return

            if side['wait']:
                side['wait'] -=1

            if belt[j]=='-':
                #print('recieve')
                if len(side['items'])>0:
                    if side['items'][0]=='P':
                        belt[j]=side['items'].pop(0)
                        taken= True
                return

            if belt[j] not in side['items']:
                side['items'].append(belt[j])
                belt[j]='-'
                taken=True
                if helper(side['items']):
                    side['wait'] = 3
                    side['items'] = ['P']

            if belt[j]=='P' or len(side['items'])==2:
                return
        update(upper)
        update(lower)
    print(workers)

print(result)




