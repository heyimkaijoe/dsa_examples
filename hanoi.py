def hanoi(nums_disk, from_rod, to_rod, aux_rod):
    if nums_disk > 0:
        hanoi(nums_disk - 1, from_rod, aux_rod, to_rod)
        print('Moving disk', nums_disk, 'from rod', from_rod, 'to rod', to_rod)
        hanoi(nums_disk - 1, aux_rod, to_rod, from_rod)

hanoi(3, 'A', 'C', 'B') # moves == 2 ** nums_disk - 1 == 7
