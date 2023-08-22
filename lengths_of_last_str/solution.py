
def last_str(s: str) -> int:
    s = s.strip()
    words = s.split(' ')

    return len(words[-1])

last_str(s="   fly me   to   the moon  ")
last_str(s="Everything is awesome!")