import numpy as np
from scipy.stats import logistic


def sample_trunc_logistic(a, b, loc, scale):
  u = np.random.uniform()
  return logistic.ppf(
      u * (logistic.cdf(b, loc=loc, scale=scale) - logistic.cdf(a, loc=loc, scale=scale)) +
      logistic.cdf(a, loc=loc, scale=scale),
      loc=loc, scale=scale
      )

def get_sur_resid(model, results):
  y = results.endog
  response_values = np.sort(np.unique(y))
  classes = len(response_values)
  mean_response_value = results.predict(which="linpred") - results.params.iloc[1-classes]
  cut_points = model.transform_threshold_params(results.params[1-classes:])
  cut_points = cut_points - cut_points[1]
  s = [sample_trunc_logistic(cut_points[y[i]], cut_points[y[i]+1], mean_response_value[i], 1) for i in range(len(y))] # Currently assuming that y takes sequential integer values starting at 0
  return s - mean_response_value