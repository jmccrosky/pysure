# pysure
Surrogate residuals for cumulative link and general regression models in Python

---

Calculates surrogate residuals for a statsmodels.miscmodels.ordinal_model.OrderedModel using the method described in [Dungang and Zhang
(2017)](http://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1292915?journalCode=uasa20) and implemented for R on [CRAN](https://cran.r-project.org/web/packages/sure/index.html).

---

Usage:

``` python
model = OrderedModel.from_formula("y ~ 1 + log_x", test_data, distr='logit')
results = modf_logit.fit(method='bfgs')
get_sur_resid(model, results)

