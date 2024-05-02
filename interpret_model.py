class Level:
    def __init__(self, debug=False):
        self.points = 0
        self.bonus_moves = 0
        self.debug = debug
        self.count_moves = False
        self.number_if_complete_moves = 0

    def interpret_level(self, model):
        if self.debug:
            print("level name: " + model.songName)
            print("===========")
        for command in model.commands:
            self.interpret_command(command)
        if self.debug:
            print("===========")
            print("end level: " + model.songName)

    def interpret_command(self, command):
        if command.move is not None:
            self.interpret_move(command.move)
        elif command.if_ is not None:
            if command.if_.__class__.__name__ == 'IfCompleteStatement':
                self.interpret_if_complete(command.if_)
            if command.if_.__class__.__name__ == 'IfPointsStatement':
                self.interpret_if_points(command.if_)
        elif command.loop is not None:
            self.interpret_loop(command.loop)
        elif command.set is not None:
            self.interpret_set(command.set)

    def interpret_set(self, set):
        if self.debug:
            print("===========")
            print("set name running: " + set.name)
            print("===========")
        for command in set.commands:
            self.interpret_command(command)
        if self.debug:
            print("===========")
            print("set name done: " + set.name)
            print("===========")

    def interpret_loop(self, loop):
        if self.debug:
            print("===========")
            print("loop!")
            print("===========")
        for i in range(loop.timesToRepeat):
            if self.debug:
                print("===========")
                print("repeat:" + str(i+1))
                print("===========")
            for command in loop.commands:
                self.interpret_command(command)
        if self.debug:
            print("===========")
            print("end loop!")
            print("===========")

    def interpret_if_complete(self, if_complete):
        self.number_if_complete_moves = 0
        self.count_moves = True
        if self.debug:
            print("===========")
            print("if complete!")
            print("===========")
        for command in if_complete.commands:
            self.interpret_command(command)
        if self.debug:
            print("===========")
            print("if complete end!")
        if len(if_complete.commands) == self.number_if_complete_moves:
            self.bonus_moves += if_complete.movesWithBonus
            if self.debug:
                print("yoo hoo bonus points from if complete for number of moves:" + if_complete.movesWithBonus + "!")
        if self.debug:
            print("===========")
        self.count_moves = False

    def interpret_if_points(self, if_points):
        if self.debug:
            print("===========")
            print("if points!")
        if self.points > if_points.points:
            self.bonus_moves += if_points.movesWithBonus
            if self.debug:
                print("yoo hoo bonus points from if points for number of moves:" + if_points.movesWithBonus + "!")
        if self.debug:
            print("===========")

    def interpret_move(self, move):
        if self.debug:
            print("move:" + move)
