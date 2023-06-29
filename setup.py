from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('OSCCord.py', base=base, icon="assets/program-icon/OSCCord_ICO.ico")
]

setup(name='OSCCord',
      version = '1.0.0',
      description = "A program for VRChat's OSC that outputs Discord Messages to your chatbox",
      options = {'build_exe': build_options},
      url = "https://github.com/Morg-S9/OSCCord",
      maintainer = "morg.mov",
      executables = executables)
