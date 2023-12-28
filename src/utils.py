import numpy as np
import statsmodels.stats.weightstats as ws
import statsmodels.api as sm
import statsmodels.formula.api as smf
import json
import patsy
from statsmodels.genmod.families.links import probit

def datamean(data, x, weight):
    return  ws.DescrStatsW(data[x], weights = data[weight]).mean

def logit_residualize(df, y, Z, weight='weight'):
    X = patsy.dmatrix(Z, df, return_type='dataframe')

    model = sm.GLM(df[y], X, freq_weights=df[weight], family=sm.families.Binomial())
    fit = model.fit()
    resid = fit.resid_pearson
    return resid, model

def probit_residualize(df, y, Z, weight='weight'):
    X = patsy.dmatrix(Z, df, return_type='dataframe')

    model = sm.GLM(df[y], X, freq_weights=df[weight], family=sm.families.Binomial(probit()))
    fit = model.fit()
    resid = fit.resid_pearson
    return resid, model

def residualize_model(df, y, Z, weight='weight'):
    """Residualize income measure of predictable components 
    Predictable components:
        sex
        education
        age
        hh_size
        location_size

    lhs includes log_income: log of whatever income measure is used
    weights are given by 'weight'

    """

    formula = y + ' ~ '  + Z 
    model = smf.wls(formula, df, weights=df[weight]).fit()
    return  model


def residualize(df, y, Z, weight='weight'):
    """Residualize income measure of predictable components 
    Predictable components:
        sex
        education
        age
        hh_size
        location_size

    lhs includes log_income: log of whatever income measure is used
    weights are given by 'weight'

    """

    formula = y + ' ~ '  + Z 
    model = smf.wls(formula, df, weights=df[weight]).fit()
    return  model.resid


def get_deciles(x, weights=None):
    stats = ws.DescrStatsW(x, weights=weights)

    deciles =  np.arange(0.1, 1.1, .1)
    income_deciles = stats.quantile(deciles).values
    x_deciles = np.array([np.argmax(income_deciles > xi) for xi in x])
    return x_deciles + 1

def get_quartiles(x, weights=None):
    stats = ws.DescrStatsW(x, weights=weights)

    deciles =  np.arange(0.25, 1.25, .25)
    income_deciles = stats.quantile(deciles).values
    x_deciles = np.array([np.argmax(income_deciles > xi) for xi in x])
    return x_deciles + 1

def make_education(educ):
    """Returns modified education status 

    Args:
        educ (_type_): _description_
    """
    if educ <= 3.0 :
        out = 1.0
    elif educ <= 5.0 :
        out = 2.0
    elif educ <= 7.0 :
        out = 3.0
    elif educ <= 10.0 :
        out = 4.0
    else:
        out = 0.0
    return out

def make_gender(thi01):
    """Takes in thi01:
    1. woman
    2. man not in couple
    3. man in couple

    Returns:
        int64: gender
        0 : man
        1 : woman
    """
    if thi01 == 1.0: # woman
        gender = 1
    else: # man
        gender = 0
    return gender

def sum_over_household(data, key):
    data_hh = (data.groupby('folio')[key]
                .apply(np.sum)
                .rename(key + '_hh'))
    data = data.merge(data_hh, on='folio', how='inner')
    return data

def any_in_household(data, key):
    data_hh = (data.groupby('folio')[key]
                .apply(np.any)
                .rename(key + '_hh'))
    data = data.merge(data_hh, on='folio', how='inner')
    return data

def indicator_by_decile(data, metric, key, weight):
    metric_decile = get_deciles(data[metric], data[weight])
    deciles = np.sort(np.unique(metric_decile))
    key_by_decile = np.ones_like(deciles).astype('object')

    ii = 0
    for decile in deciles:
        data2 = data.loc[metric_decile == decile, [key, weight]].dropna()
        stats = ws.DescrStatsW(data2[key], weights=data2[weight])
        key_by_decile[ii] = stats.mean
        ii +=1
    return key_by_decile

def load_json(filename):
    with open(filename, "r") as read_file:
        json_out = json.load(read_file)
    return json_out

        
    



    