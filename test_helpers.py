
"""
You will find here unitary tests for helpers functions
"""

import pandas as pd
import numpy as np
from Helpers import drop_invalid_datetime

def test_drop_invalid_datetime():
    ''' 
    dataframe: 
       Dates: date valide, espace, string vide, jour impossible, mois impossible, année impossible, espace avant, espace après, les 2
       Temps: temps valide, espace, string vide, seconde impossible, minute impossible, heure impossible, espace avant, espace après, les 2
    format : année / mois / jour | heure / minute / seconde
    '''
    data = {
        "Date" : ['20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',],
        "Time" : ['13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','','','','','','','','','','',
                    np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
                    '13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70',
                    '13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25',
                    '25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25',
                    ' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',
                    '13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ',
                    ' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ']
    } 
    df = drop_invalid_datetime(pd.DataFrame(data))

    assert pd.to_datetime('20/01/01', format='%y/%m/%d').date() in df["Date"].values, "La fonction enlève des dates valides"
    assert pd.to_datetime('13:45:25', format='%H:%M:%S').time() in df["Time"].values, "La fonction enlève des temps valides"
    assert ' ' not in df["Date"], "La fonction ne gère par les strings ' ' pour les dates"
    assert ' ' not in df["Time"], "La fonction ne gère par les strings ' ' pour les temps"
    assert '' not in df["Date"], "La fonction ne gère par les strings '' pour les dates"
    assert '' not in df["Time"], "La fonction ne gère par les strings '' pour les temps"
    assert not df["Date"].isnull().values.any(), "Il y à un Null/NaN/NaT dans la colonne Date: les nan déjà présents ne sont pas traités où les erreurs sont transformées en nan et non traités"
    assert not df["Time"].isnull().values.any(), "Il y à un Null/NaN/NaT dans la colonne Time: les nan déjà présents ne sont pas traités où les erreurs sont transformées en nan et non traités"
    assert '25/01/40' not in df['Date'], "Les erreurs de type jour impossible ne sont pas traités"
    assert '12/24/23' not in df['Date'], "Les erreurs de type mois impossible ne sont pas traités"
    assert '254/02/15' not in df['Date'], "Les erreurs de type année impossible ne sont pas traités"
    assert '13:45:70' not in df['Time'], "Les erreurs de type seconde impossible ne sont pas traités"
    assert '13:70:25' not in df['Time'], "Les erreurs de type minute impossible ne sont pas traités"
    assert '25:45:25' not in df['Time'], "Les erreurs de type heure impossible ne sont pas traités"
    assert ' 13:45:26' not in df["Time"], "les temps avec un espace avant ne sont pas traités"
    assert '13:45:27 ' not in df["Time"], "les temps avec un espace après ne sont pas traités"
    assert ' 13:45:28 ' not in df['Time'], "les temps avec un espace avant et après ne sont pas traités"
    assert pd.to_datetime('13:45:26', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace avant sont supprimés et non modifiées"
    assert pd.to_datetime('13:45:27', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace après sont supprimés et non modifiées"
    assert pd.to_datetime('13:45:28', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace avant et après sont supprimés et non modifiées"
    assert ' 20/02/02'   not in df["Date"], "les dates avec un espace avant ne sont pas traités"
    assert '20/02/03 ' not in df["Date"], "les dates avec un espace après ne sont pas traités"
    assert ' 20/02/04 ' not in df['Date'], "les dates avec un espace avant et après ne sont pas traités"
    assert pd.to_datetime('20/02/02', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace avant sont supprimés et non modifiées"
    assert pd.to_datetime('20/02/03', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace après sont supprimés et non modifiées"
    assert pd.to_datetime('20/02/04', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace avant et après sont supprimés et non modifiées"

