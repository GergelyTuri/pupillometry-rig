def euclidean_distance(x1, y1, x2, y2):
  try:
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return d ** (1/2)
  except:
    print('Something went wrong while calculating euclidean distance')