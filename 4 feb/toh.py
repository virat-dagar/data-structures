def tower_of_hanoi(n, source = 'A', helper = 'B', destination = 'C'):
    moves = []
    def solve(k,s,h,d):

        if k == 0:
            return

        solve(k-1,s,d,h)
        moves.append(f'move disk {k} from {s} -> {d}')
        solve(k-1,h,s,d)

    solve(n, source, helper, destination)
    return moves


def print_moves(moves):
    for move in moves:
        print(move)
    print(f"total moves: {len(moves)}")


if __name__ == "__main__":
    n = int(input("enter number of disks: "))
    moves = tower_of_hanoi(n)
    print_moves(moves)
