import enum
from enum import auto

class ClothingId(enum.Enum):
    SHOE_BEGIN = SHOE_1 = auto() #1
    SHOE_2 = auto() #2
    SHOE_3 = auto() #3
    SHOE_END = PANT_BEGIN = PANT_1 = auto() #4
    PANT_2 = auto() #5
    PANT_3 = auto() #6
    PANT_4 = auto() #7
    PANT_5 = auto() #8
    PANT_END = NUM_CLOTHES = auto() #9

for shoe in range(ClothingId.SHOE_BEGIN.value, ClothingId.SHOE_END.value):
    print("shoe id:",shoe)
print("Number of Shoes ", ClothingId.SHOE_END.value - ClothingId.SHOE_BEGIN.value)

for pant in range(ClothingId.PANT_BEGIN.value, ClothingId.PANT_END.value):
    print("pantId id:", pant)
print("Number of Pants", ClothingId.PANT_END.value - ClothingId.PANT_BEGIN.value)

print("Number of Clothes:", ClothingId.PANT_END.value - 1)