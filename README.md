# JSD-Tim-2

## Team members

Srdjan Stjepanović E2 58/2023

Dušan Janošević E2 6/2023

Sara Sinjeri E2 66/2023

Ana Vulin E2 62/2023

## Project theme
  Project will implement DSL from domain of games, specifically dance dance revolution, music game in which user needs to input commands left, down, right and up at the time they are shown at the screen. Additionally, the DSL will support the possibility for a pause command to appear during gameplay.
  Code will be in programming language python using meta-language textX.

  Game will firstly load files that contains DSL code and check if they are correctly written, then when user chooses the level, that is DSL written file, execution begins, which reads lines of DSL code and executes them.

  Example of the game can be shown here:
  
  [![Dance Dance revolution](https://img.youtube.com/vi/N8zdf8rbtEU/maxresdefault.jpg)](https://www.youtube.com/watch?v=N8zdf8rbtEU)

  ## Run guide

  To run the game you need to download the github repository and set builtin interpreter from the program, to do this easiest way is to use pycharm, go to **File** then **Settings** after that go to **Add Interpreter** and add interpreter from folder **JSD-Tim-2** needed requirements of packages can be found in **requirements.txt** file.

  ## DSL Specification

  ### Main program

  Name of the level, URL of the song on Youtube, bpm(Beats per minute or how fast level will play) and difficulties should be required variables in every DSL file, after that comes part of the execution where level maker can specify moves that wants to be shown in single line of the game. Example of the simplest DSL file can be shown here:

```
    Name = "Some song name";
    URL = "https://www.youtube.com/watch?v=IcrbM1l_BoI&list=RDcHHLHGNpCSA&index=2";
    bpm = 60;
    difficulties {
        easy : 1;
        normal : 1.1;
        hard : 1.2;
        extreme : 1.5;
    }
    Start {
        left right;
        up down;
        left;
        right;
        pause(5);
        right;
        up;
        down;
        up;
        left;
        left down;
        right down;
    };
```

### If statements

  If player scores enough points in the game, level maker can add bonus points to his next set of moves. In down example if user scores 400 points, his next 20 moves will get bonus points.

```
    Start {
        left right
        left
        right
        right
        if points(400) bonus next 20;
        up
        down
        up
        left
    };
```

### Bonus on perfect set of moves

  If a player complete set of moves defined in program, he will get bonus points in next set of moves

  
```
    Start {
        left right;
        left;
        right;
        right;
        if complete {
                up;
                down;
                up down;
                up;
                down;
                up down;
        } bonus next 20;
        up;
        down;
        up;
        left;
    };
```

### Loop sets

  Sets which are repeated specified number of times that level maker describes. In example below, DSL code have repeat block which inticates that commands inside should be repeated 4 times.

  ```
    Start {
        left right;
        left;
        repeat(4) {
            up down;
            down;
            up down;
        };
        up;
        down;
        up;
        left;
    };
```

### Set definitions

  Level maker can trough DSL file define sets, similar to functions in general code, this can reduce repetitions, sets will hold some number of moves, and can be called in main Start set or other sets. Examples of sets in DSL can be shown here:

```
    Set entrance {
        left right;
        left;
        right;
        right;
    };

    Set Verse {
        Verse_part;
        up;
        down;
        up;
        left;
        Verse_part;
        up;
        down;
        up;
        left;
    };

    Set Verse_part {
    left right;
    left;
    right;
    };

    Start {
        entrance;
        left right;
        left;
        left right;
        left;
        verse;
        up;
        down;
        up;
        down;
    };
```
