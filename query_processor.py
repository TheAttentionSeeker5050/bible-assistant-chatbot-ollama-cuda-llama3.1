import sqlite3
from config import Config

class QueryProcessor:
    def __init__(self, db_file):
        self.db_file = db_file

    def find_verses(self, query):
        """
        Finds Bible verses matching the query.
        :param query: The user's query.
        :return: A list of relevant verses with their verse count.
        """
        found_verses = []
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''
            SELECT Book, Chapter, Versecount, verse FROM bible
            WHERE verse LIKE ?
        ''', ('%' + query + '%',))
        rows = c.fetchall()
        book_names = [
            "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges",
            "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
            "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon",
            "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
            "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah",
            "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
            "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
            "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
            "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"
        ]
        for row in rows[:3]:  # Limit to 3 verses
            book_index, chapter, verse_count, verse_text = row
            book_name = book_names[book_index]
            found_verses.append(f"{book_name} {chapter} (Verse Count: {verse_count}): {verse_text}")
        conn.close()
        return found_verses
