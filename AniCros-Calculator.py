import math


def InventoryCalculator(
    InventorySize,
    InvSpaceTaken,
    Compo1Cost,
    Compo1Stack,
    Compo2Cost=0,
    Compo2Stack=1,
    Compo3Cost=0,
    Compo3Stack=1,
    Compo4Cost=0,
    Compo4Stack=1,
    Compo5Cost=0,
    Compo5Stack=1,
    Compo6Cost=0,
    Compo6Stack=1,
):
    SpaceAvailable = InventorySize - InvSpaceTaken
    # get the number of slots we have available

    Compo1Total = SpaceAvailable * Compo1Cost
    Total1Stacks = Compo1Total / Compo1Stack
    Total1Stacks = math.ceil(Total1Stacks)
    # get the number of items we need, and the number of stacks that converts to

    Compo2Total = SpaceAvailable * Compo2Cost
    Total2Stacks = Compo2Total / Compo2Stack
    Total2Stacks = math.ceil(Total2Stacks)
    # get the same for 2

    Compo3Total = SpaceAvailable * Compo3Cost
    Total3Stacks = Compo3Total / Compo3Stack
    Total3Stacks = math.ceil(Total3Stacks)
    # get the same for 3

    Compo4Total = SpaceAvailable * Compo4Cost
    Total4Stacks = Compo4Total / Compo4Stack
    Total4Stacks = math.ceil(Total4Stacks)
    # get the same for 4

    Compo5Total = SpaceAvailable * Compo5Cost
    Total5Stacks = Compo5Total / Compo5Stack
    Total5Stacks = math.ceil(Total5Stacks)
    # get the same for 5

    Compo6Total = SpaceAvailable * Compo6Cost
    Total6Stacks = Compo6Total / Compo6Stack
    Total6Stacks = math.ceil(Total6Stacks)
    # get the same for 6

    print(
        f"To make {SpaceAvailable} items you will need {Compo1Total} of item 1 ({Total1Stacks} stacks)",
        end="",
    )
    if Compo2Total > 0:
        if Compo3Total == 0:
            print(f" and {Compo2Total} of item 2 ({Total2Stacks} stacks)", end="")

        if Compo3Total != 0:
            print(
                f", {Compo2Total} of item 2 ({Total2Stacks} stacks)",
                end="",
            )
            if Compo4Total == 0:
                print(" and", end="")
                print(f" {Compo3Total} of item 3 ({Total3Stacks} stacks)", end="")

            if Compo4Total != 0:
                print(f", {Compo3Total} of item 3 ({Total3Stacks} stacks)", end="")

                if Compo5Total == 0:
                    print(
                        f", and {Compo4Total} of item 4 ({Total4Stacks} stacks)",
                        end="",
                    )

                if Compo5Total != 0:
                    print(f", {Compo4Total} of item 4 ({Total4Stacks} stacks)", end="")

                    if Compo6Total == 0:
                        print(
                            f", and {Compo5Total} of item 5 ({Total5Stacks} stacks)",
                            end="",
                        )

                    if Compo6Total != 0:
                        print(
                            f", {Compo5Total} of item 5 ({Total5Stacks} stacks)",
                            end="",
                        )
                        print(
                            f", and {Compo6Total} of item 6 ({Total6Stacks} stacks)",
                            end="",
                        )

    print(".")


# test functions
# InventoryCalculator(40, 8, 5, 30, 1, 10)
# InventoryCalculator(40, 8, 5, 30, 1, 10, 2, 20)
# InventoryCalculator(40, 8, 5, 30, 1, 10, 2, 20, 3, 30)
# InventoryCalculator(40, 8, 5, 30, 1, 10, 2, 20, 3, 30, 5, 50)
# InventoryCalculator(40, 8, 5, 30, 1, 10, 2, 20, 3, 30, 5, 50, 6)
# InventoryCalculator(40, 8, 5, 30, 1, 10, 2, 20, 3, 30, 5, 50, 6, 60)