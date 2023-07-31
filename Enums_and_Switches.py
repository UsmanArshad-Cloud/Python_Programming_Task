from enum import Enum


class Variables(Enum):
    PAK = "PAKISTAN"
    IND = "INDIA"
    AUS = "AUSTRALIA"
    ENG = "ENGLAND"
    BAN = "BANGLADESH"
    NZ = "NEWZEALAND"

print(Variables.PAK)
value = input("Give the abbreviated country name:")
match value:
    case Variables.PAK.value:
        print(Variables.PAK.value)
    case Variables.IND.name:
        print(Variables.IND.value)
    case Variables.AUS.name:
        print(Variables.AUS.value)
    case Variables.BAN.name:
        print(Variables.BAN.value)
    case Variables.ENG.name:
        print(Variables.ENG.value)
    case Variables.NZ.name:
        print(Variables.NZ.value)
    case _:
        print("Wrong Input")