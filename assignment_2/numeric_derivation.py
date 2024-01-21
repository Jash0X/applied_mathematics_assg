def derive(f, x, h=0.0001):
    df_dx = (f(x + h) - f(x - h)) / (2 * h)
    return df_dx 
