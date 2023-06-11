import matplotlib.pyplot as plt
import seaborn as sns

def visualize_coords(df1):
  try:
    fig, axes = plt.subplots(2, 2, figsize = (16, 8) )

    sns.scatterplot(y = df1['eye_top_y'], x = df1['eye_top_x'], ax = axes[0][0])
    sns.scatterplot(y = df1['eye_bottom_y'], x = df1['eye_bottom_x'], ax = axes[0][1])
    sns.scatterplot(y = df1['eye_left_y'], x = df1['eye_left_x'], ax = axes[1][0])
    sns.scatterplot(y = df1['eye_right_y'], x = df1['eye_right_x'], ax = axes[1][1])
    
    plt.show()
  except:
    print('Something went wrong while visualizing the coordinates.')