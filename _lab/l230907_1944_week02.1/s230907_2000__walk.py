import os
from pathlib import Path


THIS_FILE = Path(__file__)
THIS_DIR  = THIS_FILE.parent

l = list( os.walk(THIS_DIR/'LAB') )
print(l)
'''
# dirpath , dirnames, filenames
(./LAB    , [a]     , []        ),
(./LAB/a  , [b, c]  , []        ),

(./LAB/a/b, []      , test.txt  ),
(./LAB/a/c, []      , test.yaml ),
'''

# for (dirpath, dirnames, filenames) in os.walk(THIS_DIR/'LAB'):
#   print(f'I am at {dirpath}')

debug=122
