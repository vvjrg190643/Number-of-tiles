import sys

def cut_tiles(length, width, alo, ahi):
    max_tiles = 0
    max_area = 0
    for area in range(alo, ahi + 1):
        tiles = 0
        for w in range(1, (length // 2) + 1):
            l = area / w
            if l <= length and l.is_integer() and w <= width:
                tiles += 1
        if tiles > max_tiles:
            max_tiles = tiles
            max_area = area
    return max_area

def no_of_ways(length, width, alo, ahi):
    count = 0
    a = ahi - alo
    maxx_tiles = cut_tiles(length, width, alo, ahi)
    for i in range(length + 1):
       for j in range(width + 1):
           area = i * j
           if area == maxx_tiles:
              count += 2
    if a == 0:
        return maxx_tiles,count+2
    return maxx_tiles,(count + 3*(a))
b = 5
if len(sys.argv) >= b:
   sys.exit()

length = int(sys.argv[1])
width = int(sys.argv[2])
alo = int(sys.argv[3])
ahi = int(sys.argv[4])

print(no_of_ways(length, width, alo, ahi))