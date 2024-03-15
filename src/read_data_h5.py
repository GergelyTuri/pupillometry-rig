import pandas as pd

def read_df_from_h5(file_path, file_type):
  try:
    data = pd.read_hdf(file_path)

    if file_type == 'new':
      
      data.columns = ['eye_top_x', 'eye_top_y', 'eye_top_likelihood', 
                    'eye_bottom_x', 'eye_bottom_y', 'eye_bottom_likelihood', 
                    'eye_left_x', 'eye_left_y', 'eye_left_likelihood',
                    'eye_right_x', 'eye_right_y', 'eye_right_likelihood']

    else:
      data.columns = ['eye_top_x', 'eye_top_y', 'eye_top_likelihood', 
                    'eye_bottom_x', 'eye_bottom_y', 'eye_bottom_likelihood', 
                    'eye_left_x', 'eye_left_y', 'eye_left_likelihood',
                    'eye_right_x', 'eye_right_y', 'eye_right_likelihood',
                    'nose_x', 'nose_y', 'nose_likelihood',
                    'nostril_x', 'nostril_y', 'nostril_likelihood',
                    'chin_x', 'chin_y', 'chin_likelihood']

    data = data.astype(float)

    return data
  except:
    print('Something went wrong while reading the data')