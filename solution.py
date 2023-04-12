import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import math
import scipy.stats

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(x_success,
             y_success) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha=0.09
    n_control = len(x_success)
    n_test = len(y_success)
    mean_control = sum(x_success) / n_control
    mean_test = sum(y_success) / n_test
    var_control = sum((x - mean_control)**2 for x in x_success) / (n_control - 1)
    var_test = sum((x - mean_test)**2 for x in y_success) / (n_test - 1)
    s = math.sqrt(var_control/n_control + var_test/n_test)
    t_crit = scipy.stats.t.ppf(1 - alpha/2, n_control + n_test - 2)
    t = (mean_test - mean_control) / s*math.sqrt(1/n_control + 1/n_test)
    return True if abs(t) > t_crit else False 
