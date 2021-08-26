class MusicNotes:
    def __init__(self):
        self._notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._octave_num = 5
        self._note_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._note_index >= self._octave_num - 1:
            raise StopIteration
        self._note_index += 1
        res = map(lambda item: (2 ** self._note_index) * item, self._notes)
        return list(res)


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()
