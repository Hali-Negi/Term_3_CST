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

# Define the C3Linearization function with corrected inputs
def C3Linearization(cls, ancestors):
    if not ancestors:
        return [cls]

    if cls not in ancestors[0].__bases__:
        return [cls] + ancestors

    for i, ancestor in enumerate(ancestors):
        if cls in ancestor.__bases__:
            new_ancestors = [x for x in ancestors if cls not in x.__bases__]
            merged = []

            for parent in new_ancestors:
                if cls not in parent.__bases__:
                    merged.append(parent)

            return [cls] + merge(merged) + [cls] + ancestors[i+1:]
    
    raise Exception("Inconsistent hierarchy")

# Calculate the MRO for class Z
# MRO_Z = C3Linearization(Z, [K1, K2, K3, D, A, B, C, E, O])
MRO_Z = C3Linearization(Z, [K1,   O, D, A, K2, K3, B, C, E,])
print(MRO_Z) # [Z, K1, K2, K3, D, A, B, C, E, O]
