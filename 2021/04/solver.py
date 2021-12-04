
class Board():

    def __init__(self, board_string):
        self.rows = []
        for row in board_string.split('\n'):
            self.rows.append(list(map(int, row.split())))

        self.columns = []
        for i in range(5):
            self.columns.append({row[i] for row in self.rows})

        self.rows = list(map(set, self.rows))
        self.winning_lines = self.rows + self.columns

        self.numbers = set()
        for row in self.rows:
            for n in row:
                self.numbers.add(n)
        self.marked_numbers = set()

    def mark(self, number):
        try:
            self.numbers.remove(number)
        except KeyError:
            pass
        else:
            self.marked_numbers.add(number)
            for line in self.winning_lines:
                if line.issubset(self.marked_numbers):
                    print(f'Final score: {sum(self.numbers) * number}')
                    return True
        return False


if __name__ == '__main__':
    with open('input') as f:
        numbers = [int(n) for n in f.readline().strip().split(',')]
        boards = [Board(b_str) for b_str in f.read().strip().split('\n\n')]

    for num in numbers:
        for board in list(boards):
            if board.mark(num):
                boards.remove(board)
