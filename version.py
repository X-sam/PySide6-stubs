"""Version numbers."""
PYSIDE6_VERSION=(6, 4, 2, 0)
PYSIDE6_VERSION_STR='.'.join(str(v) for v in PYSIDE6_VERSION)
STUB_VERSION = 0
PYSIDE6_STUB_VERSION = '%d.%d.%d.%d.%d' % (PYSIDE6_VERSION + (STUB_VERSION,))