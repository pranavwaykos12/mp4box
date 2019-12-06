from mp4box.box import MovieFragmentHeaderBox

def parse_mfhd(reader, my_size):
    box = MovieFragmentHeaderBox(my_size, 0, 0)
    box.sequence_num = reader.read32()
    return box
