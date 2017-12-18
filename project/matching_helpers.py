###
###     Functions commonly used for matching artists/metadata/reviews
###

import pandas as pd


def cleanstr(string, version='v2') : 
#    if type(string) != str : 
#        print('WARNING : cleanstr received non-string : ', string)
#        return string
    tmp = string.lower().split('(')[0].split(')')[0].split('|')[0]\
                        .replace('\\', ' ')
    if version =='v2' :
        tmp =	 tmp.replace("[", "").replace("]","").replace("'","")\
                    .replace(".","").replace('"','')
    res = ''
    for w in tmp.split(' '): 
        if len(w)>0 :
            res = res+' '+w
    res = res[1:]
    return res
    
    
def splitstr(string) : 
    tmp = string.replace(' & ',',').replace(' , ',',').replace(':',',')\
                 .replace(' / ',',').replace('/',',').replace(", ",",")
    return tmp.split(',')
    
    
    
########################################################################
## better not use it

def clean_comas(list_):
    ''' fix for unclosed parenthesis screwing up regex
    '''
    clean_ = []
    for word in list_:
        clean_.append(word.split('(')[0].replace('(','').replace(')',''))
    return clean_

def df_rm_punctuation(df, columns=None) : 
    # Check arguments
    if columns == None : 
        columns = df.columns
    else :
        # todo
        raise NotImplementedError
    # process column by column
    res = pd.DataFrame(columns=columns)
    for col in columns : 
        res[col] = _serie_rm_punctuation(df[col])
    return res


def clean_serie(serie) : 
    _serie_rm_punctuation(serie)



def _serie_rm_punctuation(series_):
    return series_.str.replace("[", "").str.replace("]","")\
                    .str.replace("'","").str.replace(".","")\
                    .str.replace(", ",",").str.replace('"','')\

