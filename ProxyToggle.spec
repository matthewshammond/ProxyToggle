# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['proxy_toggle.py'],
    pathex=[],
    binaries=[],
    datas=[('ProxyToggle_on.icns', '.'), ('ProxyToggle_off.icns', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ProxyToggle',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ProxyToggle.icns'],
)
app = BUNDLE(
    exe,
    name='ProxyToggle.app',
    icon='ProxyToggle.icns',
    bundle_identifier=None,
)
