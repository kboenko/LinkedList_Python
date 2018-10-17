def deleteItemsByValue(list, value):
    currentList = list

    if currentList.value == value and currentList.next != None:
        return deleteItemsByValue(currentList.next, value)
    elif currentList.value != value and currentList.next != None:
        currentList.next = deleteItemsByValue(currentList.next, value)
    elif currentList.value == value and currentList.next == None:
        return None

    return currentList