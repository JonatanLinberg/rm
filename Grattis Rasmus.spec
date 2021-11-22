# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['rm.py'],
             pathex=[],
             binaries=[],
             datas=[('rsrc', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Grattis Rasmus',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='build_rsrc/AppIcon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Grattis Rasmus')
app = BUNDLE(coll,
             name='Grattis Rasmus.app',
             icon='build_rsrc/AppIcon.icns',
             bundle_identifier='grattis_rasmus')
