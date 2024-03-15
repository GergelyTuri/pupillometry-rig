import hdbscan

def detect_outlier(data):
  try:
    cluster = hdbscan.HDBSCAN()
    cluster.fit(data[['eye_pupil_area']].values)
    ypred = cluster.labels_
    data['cluster'] = ypred
    data['cluster'] = data['cluster'].astype(str)
    data['outlier_score'] = cluster.outlier_scores_
    data['outlier_score'] = data['outlier_score'].astype(float)
    data.loc[data['outlier_score'] <= 0.85, 'cluster'] = '0'
    data.loc[data['outlier_score'] > 0.85, 'cluster'] = '-1'

    outlier_ind = data[data['outlier_score'] > 0.85].index

    return list(outlier_ind)
  except:
    print('Something went wrong while detecting the outliers.')