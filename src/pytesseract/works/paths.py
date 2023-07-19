import pathlib

ext = ".png"
filename = f"original{ext}"
dir_ = f"{pathlib.Path.home()}/Downloads"

#
original = f"{dir_}/{filename}"
extended = f"{dir_}/extended{ext}"
large = f"{dir_}/large{ext}"
new = f"{dir_}/new{ext}"