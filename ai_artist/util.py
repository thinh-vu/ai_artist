import os

# Working with file systems
def lmt_detect():
    """Detect the running OS and return file path delimiter"""
    if os.name == 'nt':
        lmt = '\\'
    else:
        lmt = '/'
    return lmt

ROOT_DIR = os.path.abspath(os.curdir)
LMT = lmt_detect()

# Cleaning
def memory_cleaner():
    """Free up memory from large model data"""
    import gc
    import torch
    gc.collect()
    torch.cuda.empty_cache()