def split_teamim(pasuk):
    words = []
    teamim = []
    for word_with_teamim in pasuk.split(" "):
        print(word_with_teamim)
        word = ""
        taam = ""
        for char in word_with_teamim:
            if (ord(char) >= ord("֑") and ord(char) <= ord("֮")) or ord(char) == ord('ֽ'):  # https://www.utf8-chartable.de/unicode-utf8-table.pl?start=1424
                taam += char
            elif ord(char) >= ord("א") and ord(char) <= ord("ת"):
                word += char
        words.append(word)
        teamim.append(taam)

    return [words, teamim]
