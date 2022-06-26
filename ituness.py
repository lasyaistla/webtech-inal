import itunespy

track = itunespy.search_track('Iter Impius')  # Returns a list
print(track[0].artist_name + ': ' + track[0].track_name + ' | Length: ' + str(track[0].get_track_time_minutes())) # Get info from the first result
import itunespy

author = itunespy.search_book_author('Fyodor Dostoevsky')  # Search for Dostoevsky

books = author[0].get_books()  # Get books from the firs result

for book in books:
    print(book.track_name)  # Show each book's name
    import itunespy

lookup = itunespy.lookup(id=428011728)  # Steven Wilson's ID

for l in lookup:
    if l.type == 'artist':
        print('Artist!')
        print(l.artist_type)  # Since it's an artist, you can also check its artist type