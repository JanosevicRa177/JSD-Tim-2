from game.game_logic.model.command import Command
from game.game_logic.model.if_complete import IfComplete
from game.game_logic.model.if_points import IfPoints
from game.game_logic.model.loop import Loop
from game.game_logic.model.move import Move
from game.game_logic.model.pause import Pause
from game.game_logic.model.set import Set


def interpret_command(command) -> Command:
    if command.move is not None:
        return Move(command.move)
    elif command.if_ is not None:
        if command.if_.__class__.__name__ == 'IfCompleteStatement':
            return interpret_if_complete(command.if_)
        if command.if_.__class__.__name__ == 'IfPointsStatement':
            return IfPoints(command.if_.points, command.if_.movesWithBonus)
    elif command.loop is not None:
        return interpret_loop(command.loop)
    elif command.set is not None:
        return interpret_set(command.set)
    elif command.pause is not None:
        return Pause(command.pause.value)


def interpret_set(a_set) -> Command:
    set_command = Set(a_set.name)
    for command in a_set.commands:
        interpreted_command = interpret_command(command)
        set_command.commands.append(interpreted_command)
    return set_command


def interpret_loop(loop) -> Command:
    loop_command = Loop(loop.timesToRepeat)
    for command in loop.commands:
        interpreted_command = interpret_command(command)
        loop_command.commands.append(interpreted_command)
    return loop_command


def interpret_if_complete(if_complete) -> Command:
    if_complete_command = IfComplete(if_complete.movesWithBonus)
    for command in if_complete.commands:
        interpreted_command = interpret_command(command)
        if_complete_command.commands.append(interpreted_command)
    return if_complete_command
