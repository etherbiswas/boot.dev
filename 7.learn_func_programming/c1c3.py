def deduplicate_lists(lst1, lst2, reverse=False):
     #return sorted(set(lst1 + lst2), reverse=reverse)
    # Remove duplicates by converting both lists to sets
    lst1_ = set(lst1)
    lst2_ = set(lst2)

    # Combine both sets
    list_ = list(lst1_ | lst2_)

    # Return the list sorted in ascending or descending order depending on reverse flag
    if reverse:
        return sorted(list_, reverse=True)
    return sorted(list_)
