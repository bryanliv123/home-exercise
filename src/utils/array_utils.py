from typing import List, Tuple

def split_array_into_tuples(arr) -> List[Tuple]:
    '''Loops through list and insert every two items into tuple'''

    result = []
    
    for i in range(0, len(arr), 2):
        result.append((arr[i], arr[i+1] if i+1 < len(arr) else None))

    return result
