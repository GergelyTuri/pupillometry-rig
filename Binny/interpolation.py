import pandas as pd
import numpy as np

def interpolate_data(data, col_pairs, threshold):
  try:
    total_interpolation = 0
    result_df = pd.DataFrame()

    for i in col_pairs:
      data_i = data[i]
      data_i.loc[data_i[i[2]] < threshold, [ i[0], i[1] ]] = np.nan
      total_interpolation += ( data_i.isna().sum().sum() / 2)
      data_i.loc[data_i[i[2]] < threshold, [ i[0], i[1] ]] = data_i.interpolate()
      result_df = pd.concat([result_df, data_i], axis = 1)

    return result_df, total_interpolation
    
  except:
    print('Something went wrong during interpolate execution')