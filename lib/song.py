class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment count of songs
        Song.add_song_to_count()
        # Add genre and artist to class attributes
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        # Update genre count
        Song.add_to_genre_count(genre)
        # Update artist count
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
umbrella = Song("Umbrella", "Rihanna", "Pop")
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", "Pop")

print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Rihanna', 'Adele']
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 2}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Rihanna': 1, 'Adele': 1}
