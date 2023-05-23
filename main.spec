import os
import sys
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import copy_metadata

# Application name and icon path
app_name = 'Market Sentiment Analysis'
icon_path = ''  # Optional: Provide the path to your application icon

# Define block_cipher variable (replace with the appropriate cipher if needed)
block_cipher = None

# Get the path to the spec file
spec_file = sys.argv[0]
spec_dir = os.path.dirname(os.path.abspath(spec_file))

# Get the path to the 'gui' directory
gui_path = os.path.join(spec_dir, 'gui')
if not os.path.exists(gui_path):
    # 'gui' directory not found in the spec directory, specify a direct path
    gui_path = r'C:\Users\joshu\source\repos\Market-Sentiment-Analysis'

# Get the path to the 'holdings' directory
holdings_path = os.path.join(spec_dir, 'holdings')
if not os.path.exists(holdings_path):
    # 'holdings' directory not found in the spec directory, specify a direct path
    holdings_path = r'C:\Users\joshu\source\repos\Market-Sentiment-Analysis\holdings'  # Update with the correct path

# Analysis configuration
a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=collect_data_files('', include_py_files=True),
             hiddenimports=collect_submodules('gui') + collect_submodules('holdings'),
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# PYZ configuration
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE configuration
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=app_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          argv_emulation=False,
          splash=None,
          icon=icon_path)

# COLLECT configuration
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=app_name,
               debug=False,
               bootloader_ignore_signals=False,
               console=True)
