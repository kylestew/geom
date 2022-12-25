def throws_impossible_for(dat, data_types):
    if any([isinstance(dat, type) for type in data_types]):
        raise Exception("IMPOSSIBLE")
