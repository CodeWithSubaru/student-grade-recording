
def sanitize(data, sliceNum=0):
    dataRecord = list()

    for item in data:
        if sliceNum < 1:
            dataRecord.append(item.strip())
        else:
            dataRecord.append(item[sliceNum:].strip())

    return dataRecord
