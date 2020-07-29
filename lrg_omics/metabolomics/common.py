#lrg_omics/metabolomics/common.py

import pandas as pd
import os


def metadata_from_worklist(fn: str):
    worklist = pd.read_csv(fn)
    return worklist


def metadata_from_filename(fn: str):
    '''
    this function extracts the metadata from the file name and returns a dataframe
    '''
    file_name = str(os.path.basename(fn))
    if('.mzXML' in file_name):
        file_name = file_name[:-6]
    if('.raw' in file_name):
        file_name = file_name[:-4]
        
        
    bi_nbr = None
    if 'BI_' in file_name:
        bi_nbr = 'BI'+file_name.split('BI')[-1]
        
    date = file_name.split('RG')[0].replace('_','-')
    
    rpt = 0
    if 'RPT' in file_name:
        rpt = int(file_name.split('RPT')[-1][:3])
        
    conc = None
        
    sample_type = 'BI'                             # BI samples
    if 'Standard' in file_name: 
        sample_type = 'ST'                         # standard samples
        conc = float(file_name.split('Standard-')[-1][:-2])
    if 'Blank' in file_name: sample_type = 'BL'    # Blank samples
    if ('SA-pool' in file_name) or ('SA-Pool' in file_name): sample_type = 'PO-SA'  # SA-pool samples
    if ('MH-pool' in file_name) or ('MH-Pool' in file_name): sample_type = 'PO-MH'      # MH-pool samples
    if 'QC' in file_name: sample_type = 'QC'       # QC samples
    mode = file_name.split('HILIC')[-1][:3]
    
    plate_id = 'SA0'+file_name.split('SA0')[-1][:2]
    
    data = {
            'MS_FILE':str(os.path.basename(fn)),
            'BI_NBR': bi_nbr, 
            'DATE': date, 
            'RPT': rpt, 
            'PLATE_ID': plate_id,
            'SAMPLE_TYPE': sample_type,
            'STD_CONC': conc,
            'MS_MODE': mode
            }
    
    df = pd.DataFrame(data, index=[0])
    return df 



def read_plate(filenames, worklist):
    
    return pd.DataFrame()
