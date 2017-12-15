###
###     Functions commonly used for matching artists/metadata/reviews
###



def clean_serie(series_):
    return series_.str.replace("[", "").str.replace("]","")\
                    .str.replace("'","").str.replace(".","")\
                    .str.replace(", ",",").str.replace('"','')
