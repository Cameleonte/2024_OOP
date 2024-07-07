from typing import List

from project.song import Song


class Album:

    def __init__(self, name: str, *song: Song) -> None:
        self.name = name
        self.songs: List[Song] = [*song]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        hit: Song = next((hit for hit in self.songs if hit.name == song_name), None)
        if self.published:
            return "Cannot remove songs. Album is published."
        if hit:
            self.songs.remove(hit)
            return f"Removed song {hit.name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        res = f"Album {self.name}\n"
        res += '\n'.join(f'== {s.get_info()}' for s in self.songs)
        return res.strip() + '\n'
