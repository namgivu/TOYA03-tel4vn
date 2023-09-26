import os
from pathlib import Path


THIS_FILE = Path(__file__)
THIS_DIR  = THIS_FILE.parent

p0 = THIS_DIR/'LAB'
stop_at_depth = 3
for (dirpath, dirnames, filenames) in os.walk(p0):
  depth_str = dirpath.replace(str(p0),'')
  depth     = len(depth_str.split('/'))

  if depth <= stop_at_depth:
    print(f'{p0} - {depth=} - I am at {dirpath}')

debug=122
