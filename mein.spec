# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
a = Analysis(
    ['mein.py'],
    pathex=[],
    binaries=[],
    datas=[ ('GunshotIaModel_v9_old.h5','.'),],
    hiddenimports=['numpy', 'numpy.f2py',
      'scipy.signal',
      'scipy.sparse',
      'noisereduce',
      'librosa.core',
      'librosa.feature',
      'pyaudio',
      'tensorflow.python.keras',],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,

)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher,optimize=0 )

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    exclude_binaries=True,
    name='mein',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icono.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mein'
)
