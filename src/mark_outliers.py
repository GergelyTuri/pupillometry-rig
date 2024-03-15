import detect_outliers as do
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def mark_outlier(df):
  try:
    df['clustering_outlier_detection'] = False
    out_i = do.detect_outlier(df)
    df.loc[out_i, 'clustering_outlier_detection'] = True

    plt.figure(figsize = (12, 10))
    sns.scatterplot(x = df.index, y = df['eye_pupil_area'], hue = df['clustering_outlier_detection'])

    skip = np.array(list(df['eye_pupil_area'])).std()

    plt.yticks(range(int(df['eye_pupil_area'].min()), int(df['eye_pupil_area'].max()), int(skip) ))
    plt.show()

    return df
  except:
    print('Something went wrong while marking the outliers.')