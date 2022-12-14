"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    data = open(filename)

    for line in data:
        unique = line.split("|")[1]
        species.add(unique)

    data.close()

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    data = open(filename)

    for line in data:
        names, species = line.split('|')[:2]

        if search_string in ("All"):
            villagers.append(names)


    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    data = open(filename)

    for line in data:
        name, species, group, hobby, motto = line.split('|')

        if hobby == 'Fitness':
            fitness.append(name)
        elif hobby == 'Nature':
            nature.append(name)
        elif hobby == 'Education':
            education.append(name)
        elif hobby == 'Music':
            music.append(name)
        elif hobby == 'Fashion':
            fashion.append(name)
        elif hobby == 'Play':
            play.append(name)



    return [fitness, nature, education, music, fashion, play]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data = open(filename)

    for line in data:
        all_data.append(tuple(line.split('|')))


    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    data = open(filename)

    for line in data:
        name, species, group, hobby, motto = line.split('|')

        if name == villager_name:
            return motto

    return None



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    data = open(filename)
    alike = set()
    specific_group = ''

    for line in data:
        name, species, group, hobby, motto= line.split('|')

        if name == villager_name:
            specific_group = group
            break

    if specific_group:
        for line in data:
            name, species, group, hobby, motto= line.split('|')
            if group == specific_group:
                alike.add(name)

    return alike
