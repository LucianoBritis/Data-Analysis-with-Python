def calculate(list_x):
    # get array numpy
    before = np.array((list_x))
    # check array
    if (len(before) != 9):
        raise ValueError(before, "List must contain nine numbers.")
 
    # convert the list into a 3 x 3
    after = before.reshape((3,3))

    dictionary = {    
        'mean':[np.mean(after, axis=0).tolist(), np.mean(after, axis=1).tolist(), np.mean(after).tolist()],
        'variance':[np.var(after, axis=0).tolist(), np.var(after, axis=1).tolist(), np.var(after).tolist()],
        'standard deviation':[np.std(after, axis=0).tolist(), np.std(after, axis=1).tolist(), np.std(after).tolist()],
        'max':[np.max(after, axis=0).tolist(), np.max(after, axis=1).tolist(), np.max(after).tolist()],
        'min':[np.min(after, axis=0).tolist(), np.min(after, axis=1).tolist(), np.min(after).tolist()],
        'sum':[np.sum(after, axis=0).tolist(), np.sum(after, axis=1).tolist(), np.sum(after).tolist()],
    }
    for item in dictionary:
        return dictionary   







