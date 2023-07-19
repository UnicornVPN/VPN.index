import pathlib

ext = ".png"
filename = f"original{ext}"
dir_ = f"{pathlib.Path.home()}/Downloads"

#
original = f"{dir_}/{filename}"
large = f"{dir_}/large{ext}"
margin = f"{dir_}/margin{ext}"
new = f"{dir_}/new{ext}"