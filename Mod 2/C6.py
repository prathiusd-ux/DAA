worths = eval(input("enter list of values:"))
hefts = eval(input("enter list of weights:"))
limit = int(input("enter capacity:"))
count_items = len(worths)

max_worth = 0
best_subset = []

def find_subsets(start_index, current_selection):
    global max_worth, best_subset
    
    total_heft = 0
    total_worth = 0
    for item_index in current_selection:
        total_heft += hefts[item_index]
        total_worth += worths[item_index]
    
    if total_heft <= limit and total_worth > max_worth:
        max_worth = total_worth
        best_subset = current_selection[:]
        
    for k in range(start_index, count_items):
        current_selection.append(k)
        find_subsets(k + 1, current_selection)
        current_selection.pop()

find_subsets(0, [])
print("best combo:", best_subset)
print("max value:", max_worth)