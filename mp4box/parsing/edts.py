from mp4box.box import EditBox
from mp4box.utils.exceptions import InvalidBoxError

def parse_edts(reader, my_size):
    box = EditBox(my_size)
    cnt = 0
    while not reader.reached_eof() and cnt < my_size:
        size = reader.read32()
        type = reader.read32_as_str()
        cnt += size
        if type == 'elst':
            box.elts = parse_elst(self, size)
        else:
            raise InvalidBoxError("type %s unknown")
   
    return box
