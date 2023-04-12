import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import t

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha=0.09
    n_control = len(x)
    n_test = len(y)
    mean_control = sum(x) / n_control
    mean_test = sum(y) / n_test
    var_control = sum((i - mean_control)**2 for i in x) / (n_control - 1)
    var_test = sum((x - mean_test)**2 for x in y) / (n_test - 1)
    s = (var_control/n_control + var_test/n_test)**0.5
    t_crit = t.ppf(1 - alpha/2, n_control + n_test - 2)
    t = (mean_test - mean_control) / s*(1/n_control + 1/n_test)**0.5
    return True if abs(t) > t_crit else False
