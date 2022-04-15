import random

def roll_stats():
    """
    This method uses dice rolls to generate ability scores.
    """
    Stat_array = []
    for x in range(6):
        total = 0
        Dielist = [0, 0, 0, 0]
        for item in range(len(Dielist)):
            roll = 0
            while roll <= 1:
                roll = random.randint(1, 6)
            Dielist[item] = roll
        Dielist.sort(reverse=True)
        Dielist.pop(3)
        for result in Dielist:
            total = total + result
        Stat_array.append(total)
    return Stat_array
