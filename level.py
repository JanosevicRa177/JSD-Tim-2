import string

from game_logic.command import Command
from game_logic.if_complete import IfComplete
from game_logic.if_points import IfPoints
from game_logic.loop import Loop
from game_logic.move import Move
from game_logic.set import Set


class Level:
    def __init__(self, debug=False):
        self.points = 0
        self.bonus_moves = 0
        self.debug = debug
        self.count_moves = False
        self.number_if_complete_moves = 0
        self.commands: list[Command] = []

    def get_speed(self):
        return 5

    def interpret_level(self, model):
        if self.debug:
            print("level name: " + model.songName)
            print("===========")
        for command in model.commands:
            interpreted_command = self.interpret_command(command)
            self.commands.append(interpreted_command)
        if self.debug:
            print("===========")
            print("end level: " + model.songName)

    def interpret_command(self, command) -> Command:
        if command.move is not None:
            return self.interpret_move(command.move)
        elif command.if_ is not None:
            if command.if_.__class__.__name__ == 'IfCompleteStatement':
                return self.interpret_if_complete(command.if_)
            if command.if_.__class__.__name__ == 'IfPointsStatement':
                return self.interpret_if_points(command.if_)
        elif command.loop is not None:
            return self.interpret_loop(command.loop)
        elif command.set is not None:
            return self.interpret_set(command.set)

    def interpret_set(self, set):
        set_command = Set(set.name)
        if self.debug:
            print("===========")
            print("set name running: " + set.name)
            print("===========")
        for command in set.commands:
            interpreted_command = self.interpret_command(command)
            set_command.commands.append(interpreted_command)
        if self.debug:
            print("===========")
            print("set name done: " + set.name)
            print("===========")
        return set_command

    def interpret_loop(self, loop):
        loop_command = Loop(loop.timesToRepeat)
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
                interpreted_command = self.interpret_command(command)
                loop_command.commands.append(interpreted_command)
        if self.debug:
            print("===========")
            print("end loop!")
            print("===========")
        return loop_command

    def interpret_if_complete(self, if_complete):
        if_complete_command = IfComplete(if_complete.movesWithBonus)
        self.number_if_complete_moves = 0
        self.count_moves = True
        if self.debug:
            print("===========")
            print("if complete!")
            print("===========")
        for command in if_complete.commands:
            interpreted_command = self.interpret_command(command)
            if_complete_command.commands.append(interpreted_command)
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
        return if_complete_command

    def interpret_if_points(self, if_points) -> Command:
        if_points_command = IfPoints(if_points.points, if_points.movesWithBonus)
        if self.debug:
            print("===========")
            print("if points!")
        if self.points > if_points.points:
            self.bonus_moves += if_points.movesWithBonus
            if self.debug:
                print("yoo hoo bonus points from if points for number of moves:" + if_points.movesWithBonus + "!")
        if self.debug:
            print("===========")
        return if_points_command

    def interpret_move(self, move) -> Command:
        if self.debug:
            print("move:" + move)

        combination: list[string] = []
        if "right" in move:
            combination.append("right")
        if "left" in move:
            combination.append("left")
        if "up" in move:
            combination.append("up")
        if "down" in move:
            combination.append("down")
        move_command = Move(combination)
        return move_command
