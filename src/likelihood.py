import matplotlib.pyplot as plt
import seaborn as sns

def likelihood_plot(df1):
  try:
    fig, axes = plt.subplots(2, 2, figsize = (16,8))
    sns.boxplot(df1['eye_top_likelihood'], ax = axes[0][0])
    sns.boxplot(df1['eye_bottom_likelihood'], ax = axes[0][1])
    sns.boxplot(df1['eye_left_likelihood'], ax = axes[1][0])
    sns.boxplot(df1['eye_right_likelihood'], ax = axes[1][1])
    plt.show()
  except:
    print('Something went wrong while visualizing the liklihood of the coordinates.')