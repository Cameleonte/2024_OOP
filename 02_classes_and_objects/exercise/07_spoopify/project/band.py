from typing import List

from project.album import Album


class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        current_album: Album = next((hits for hits in self.albums if hits.name == album_name), None)
        if not current_album:
            return f"Album {album_name} is not found."
        elif current_album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(current_album)
        return f"Album {current_album.name} has been removed."

    def details(self) -> str:
        res = f"Band {self.name}\n"
        if self.albums:
            res += '\n'.join(f"{curr_album.details()}" for curr_album in self.albums)
        return res.strip()
