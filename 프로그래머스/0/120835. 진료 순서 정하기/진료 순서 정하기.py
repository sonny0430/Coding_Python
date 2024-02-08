def solution(emergency):
    sorted_list = sorted(emergency, reverse=True)
    order_list = []
    for i in range(0, len(emergency)):
        order_list.append(sorted_list.index(emergency[i])+1)

    return order_list