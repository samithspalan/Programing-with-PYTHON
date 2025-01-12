import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'eggs.txt', p / 'some_folder')