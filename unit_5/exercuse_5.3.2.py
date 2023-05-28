class MusicNotes:
    def __init__(self):
        self.notes = ["La", "Si", "Do", "Re", "Mi", "Fa", "Sol"]
        self.octaves = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.current_note_index = 0
        self.current_octave_index = 0
        self.octave_mul = 1
        self.octave_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_note_index >= len(self.notes):
            raise StopIteration
        if self.current_octave_index >= len(self.octaves):
            raise StopIteration
        if self.octave_count > 4:
            self.current_note_index += 1
            self.current_octave_index += 1
            self.octave_mul = 1
            self.octave_count = 0
            if self.current_octave_index >= len(self.octaves):
                raise StopIteration
        frequency = self.octaves[self.current_octave_index]
        note = self.notes[self.current_note_index]
        if self.octave_count != 0:
            self.octave_mul *= 2
        self.octave_count += 1
        return note, frequency * self.octave_mul


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()
