def c3_linearization(cls):
    # Base case: If cls has no parent (i.e., it's the base class like object), its MRO is just [cls]
    if cls.__bases__ == ():
        return [cls]
    
    # Initialize with the class itself at the start of the MRO
    mro = [cls]
    
    # Collect MROs of all the parents
    parents_mros = [list(c3_linearization(parent)) for parent in cls.__bases__]
    
    # Add the list of direct parents
    parents_mros.append(list(cls.__bases__))
    
    # Merge MROs of the parents
    while parents_mros:
        # Find a valid candidate class to add to MRO
        for candidate in parents_mros[0]:
            if not any(candidate in parent_mro[1:] for parent_mro in parents_mros):  # Check if candidate is in head of other lists
                break
        else:
            raise Exception("Inconsistent hierarchy, no valid candidate found")
        
        # Add candidate to the MRO
        mro.append(candidate)
        
        # Remove the candidate from all lists
        for parent_mro in parents_mros:
            if parent_mro and parent_mro[0] == candidate:
                parent_mro.pop(0)
        
        # Remove empty lists
        parents_mros = [parent_mro for parent_mro in parents_mros if parent_mro]
    
    return mro

# Example usage
class O: pass
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass
class K1(A, B, C): pass
class K2(D, B, E): pass
class K3(D, A): pass
class Z(K1, K2, K3): pass

# Calculate and print the MRO for class Z using C3 Linearization
print([cls.__name__ for cls in c3_linearization(Z)])
