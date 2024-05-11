from game_logic.move import Move


class EndMove(Move):
    def __init__(self):
        super().__init__(['up', 'down', 'left', 'right'])