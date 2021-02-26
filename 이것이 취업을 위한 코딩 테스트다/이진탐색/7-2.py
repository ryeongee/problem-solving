def bin_search(start,end,array,target):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]> target:
        return bin_search(start,mid-1,array,target)
    else:
        return bin_search(mid+1,end,array,target);
