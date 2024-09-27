import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2013-05-17
# https://www.baseball-reference.com/boxes/MIN/MIN201305170.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2013/05/17/347356/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-17 20:11-23:35",
        "at": "Target Field, Minneapolis, MN",
        "att": "30,210",
        "temp": "59F, Overcast",
        "wind": "13mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                5: "Jonny Gomes",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                18: "Shane Victorino",
                23: "Pedro Ciriaco",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [16, "5"],
                [7, "6"],
                [5, "7"],
                [37, "3"],
                [39, "2"],
            ],
            "bench": [
                [18, "CF"],
                [23, "3B"],
                [12, "1B"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 31, 59, 36, 19, 22, 46],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 49,
            "roster": {
                # Lineup
                2: "Brian Dozier",
                27: "Chris Parmelee",
                16: "Josh Willingham",
                33: "Justin Morneau",
                9: "Ryan Doumit",
                31: "Oswaldo Arcia",
                24: "Trevor Plouffe",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                49: "Vance Worley",
                # Bench
                7: "Joe Mauer",
                22: "Wilkin Ramirez",
                8: "Jamey Carroll",
                5: "Eduardo Escobar",
                # Bullpen
                15: "Glen Perkins",
                30: "Kevin Correia",
                58: "Scott Diamond",
                60: "Pedro Hernandez",
                20: "Josh Roenicke",
                50: "Casey Fien",
                61: "Jared Burton",
                37: "Mike Pelfrey",
                52: "Brian Duensing",
                57: "Ryan Pressly",
                51: "Anthony Swarzak",
            },
            "lefties": [15, 58, 60, 52],
            "lineup": [
                [2, "4"],
                [27, "9"],
                [16, "0"],
                [33, "3"],
                [9, "2"],
                [31, "7"],
                [24, "5"],
                [32, "8"],
                [25, "6"],
            ],
            "bench": [
                [7, "C"],
                [22, "LF"],
                [8, "2B"],
                [5, "3B"],
            ],
            "bullpen": [15, 30, 58, 60, 20, 50, 61, 37, 52, 57, 51],
        },
        "umpires": {
            "HP": "Eric Cooper",
            "1B": "Paul Schrieber",
            "2B": "Chad Fairchild",
            "3B": "Jeff Kellogg",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: MIN #49 Vance Worley
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b")
t1.out("G1-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b s f f f")
t1.hit(1)
t1.error(4)
t1.advance(2, "E4")
t1.advance(3, "15 G4-3")
t1.advance("U", "34 1B")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
t1.new_ab()
t1.pitch_list("c t f b")
t1.out("G4-3")

# 4. BOS #34 David Ortiz (29 - X - X)
t1.new_ab()
t1.pitch_list("d c c f f")
t1.hit(1, rbis=1)

# 5. BOS #16 Will Middlebrooks (X - X - 34)
t1.new_ab()
t1.pitch_list("c s d f")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. MIN #2  Brian Dozier (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G4-3")

# 2. MIN #27 Chris Parmelee (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b c")
b1.out("!K")

# 3. MIN #16 Josh Willingham (X - X - X)
b1.new_ab()
b1.pitch_list("b f c c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #49 Vance Worley
t2 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c c f b")
t2.out("L7")

# 7. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.out("G6-3")

# 8. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t2.new_ab()
t2.pitch_list("c b b b f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 4. MIN #33 Justin Morneau (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 5. MIN #9  Ryan Doumit (X - X - X)
b2.new_ab()
b2.pitch_list("b f f s")
b2.out("K")

# 6. MIN #31 Oswaldo Arcia (X - X - X)
b2.new_ab()
b2.pitch_list("b f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #49 Vance Worley
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("F7")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.thrown_out(2, "15 DP4-6-3", 2, 49)

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t3.new_ab()
t3.pitch_list("f 1 f")
t3.out("DP4-6-3")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 7. MIN #24 Trevor Plouffe (X - X - X)
b3.new_ab()
b3.hit(2)
b3.advance(3, "32 G4-3")
b3.advance(4, "25 HR")

# 8. MIN #32 Aaron Hicks (X - 24 - X)
b3.new_ab()
b3.pitch_list("c l")
b3.out("G4-3")

# 9. MIN #25 Pedro Florimón (24 - X - X)
b3.new_ab()
b3.hit(4, rbis=2)

# 1. MIN #2  Brian Dozier (X - X - X)
b3.new_ab()
b3.pitch_list("b f b")
b3.out("F7")

# 2. MIN #27 Chris Parmelee (X - X - X)
b3.new_ab()
b3.out("P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #49 Vance Worley
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b f b")
t4.hit(1)
t4.advance(2, "7 BB")

# 5. BOS #16 Will Middlebrooks (X - X - 34)
t4.new_ab()
t4.out("F9")

# 6. BOS #7  Stephen Drew (X - X - 34)
t4.new_ab()
t4.pitch_list("b c b b b")
t4.reach("BB")

# 7. BOS #5  Jonny Gomes (X - 34 - 7)
t4.new_ab()
t4.pitch_list("c")
t4.out("L8")

# 8. BOS #37 Mike Carp (X - 34 - 7)
t4.new_ab()
t4.pitch_list("f")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 3. MIN #16 Josh Willingham (X - X - X)
b4.new_ab()
b4.pitch_list("b s b c b f")
b4.out("(F)P3")

# 4. MIN #33 Justin Morneau (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 5. MIN #9  Ryan Doumit (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.advance(2, "31 BB")

# 6. MIN #31 Oswaldo Arcia (X - X - 9)
b4.new_ab()
b4.pitch_list("c b f b b f b")
b4.reach("BB")

# 7. MIN #24 Trevor Plouffe (X - 9 - 31)
b4.new_ab()
b4.pitch_list("b b c c d s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #49 Vance Worley
t5 = game.new_inning()

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.hit(1)
t5.advance(3, "29 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t5.new_ab()
t5.pitch_list("f b")
t5.out("F7")

# 2. BOS #29 Daniel Nava (X - X - 39)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(1)
t5.thrown_out(2, "15 DP4-6-3", 2, 49)

# 3. BOS #15 Dustin Pedroia (39 - X - 29)
t5.new_ab()
t5.pitch_list("c b b f b f")
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 8. MIN #32 Aaron Hicks (X - X - X)
b5.new_ab()
b5.pitch_list("c b s")
b5.hit(1)
b5.advance(2, "2 BB")
b5.advance(3, "27 1B")

# 9. MIN #25 Pedro Florimón (X - X - 32)
b5.new_ab()
b5.pitch_list("1 b f 1 1")
b5.out("P5")

# 1. MIN #2  Brian Dozier (X - X - 32)
b5.new_ab()
b5.pitch_list("1 1 b 1 b 1 b c b")
b5.reach("BB")
b5.advance(2, "27 1B")

# 2. MIN #27 Chris Parmelee (X - 32 - 2)
b5.new_ab()
b5.pitch_list("b s f")
b5.hit(1)

# 3. MIN #16 Josh Willingham (32 - 2 - 27)
b5.new_ab()
b5.pitch_list("s d c c")
b5.out("!K")

# 4. MIN #33 Justin Morneau (32 - 2 - 27)
b5.new_ab()
b5.pitch_list("d b f f f")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #49 Vance Worley
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "16 DP6-4-3", 1, 49)

# 5. BOS #16 Will Middlebrooks (X - X - 34)
t6.new_ab()
t6.pitch_list("c c")
t6.out("DP6-4-3")

# 6. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b")
t6.out("F7")


# Bot 6th
# Pitching: BOS #11 Clay Buchholz
b6 = game.new_inning()

# 5. MIN #9  Ryan Doumit (X - X - X)
b6.new_ab()
b6.pitch_list("c s c")
b6.out("!K")

# 6. MIN #31 Oswaldo Arcia (X - X - X)
b6.new_ab()
b6.pitch_list("b f c f")
b6.out("G4-3")

# 7. MIN #24 Trevor Plouffe (X - X - X)
b6.new_ab()
b6.pitch_list("s c b f b b")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #52 Brian Duensing
t7 = game.new_inning()

# Pitching change (MIN): #52 Brian Duensing replaces #49 Vance Worley
t7.pitching_substitution(52)

# 7. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b c f b")
t7.reach("BB")
t7.advance(3, "39 1B")
t7.advance(4, "2 1B")

# 8. BOS #37 Mike Carp (X - X - 5)
t7.new_ab()
t7.pitch_list("b s 1 s c")
t7.out("!K")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t7.new_ab()
t7.hit(1)
t7.advance(3, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (5 - X - 39)
t7.new_ab()
t7.hit(1, rbis=1)
t7.advance(2, "29 SB")

# 2. BOS #29 Daniel Nava (39 - X - 2)
t7.new_ab()
t7.pitch_list("1 1 c f d s")
t7.out("K")

# Pitching change (MIN): #50 Casey Fien replaces #52 Brian Duensing
t7.pitching_substitution(50)

# 3. BOS #15 Dustin Pedroia (39 - 2 - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("P4")


# Bot 7th
# Pitching: BOS #11 Clay Buchholz
b7 = game.new_inning()

# 8. MIN #32 Aaron Hicks (X - X - X)
b7.new_ab()
b7.out("B1-3")

# 9. MIN #25 Pedro Florimón (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.out("G1-4-3")

# 1. MIN #2  Brian Dozier (X - X - X)
b7.new_ab()
b7.pitch_list("b c b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #61 Jared Burton
t8 = game.new_inning()

# Pitching change (MIN): #61 Jared Burton replaces #50 Casey Fien
t8.pitching_substitution(61)

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G4-3")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.out("G5-3")

# 6. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.hit(2)

# 7. BOS #5  Jonny Gomes (X - 7 - X)
t8.new_ab()
t8.pitch_list("s d c b b b")
t8.reach("BB")

# 8. BOS #37 Mike Carp (X - 7 - 5)
t8.new_ab()
t8.pitch_list("b s b b f c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #11 Clay Buchholz
b8.pitching_substitution(30)

# 2. MIN #27 Chris Parmelee (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f b c")
b8.out("!K")

# 3. MIN #16 Josh Willingham (X - X - X)
b8.new_ab()
b8.pitch_list("c c b b")
b8.out("F8")

# 4. MIN #33 Justin Morneau (X - X - X)
b8.new_ab()
b8.pitch_list("s s b s")
b8.out("K2-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #15 Glen Perkins
t9 = game.new_inning()

# Pitching change (MIN): #15 Glen Perkins replaces #61 Jared Burton
t9.pitching_substitution(15)

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("f s b f f b s")
t9.out("K2-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b c c f")
t9.out("G6-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b b f f b s")
t9.out("K")


# Bot 9th
# Pitching: BOS #30 Andrew Miller
b9 = game.new_inning()

# 5. MIN #9  Ryan Doumit (X - X - X)
b9.new_ab()
b9.pitch_list("b b c")
b9.out("G6-3")

# 6. MIN #31 Oswaldo Arcia (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# Pitching change (BOS): #63 Alex Wilson replaces #30 Andrew Miller
b9.pitching_substitution(63)

# 7. MIN #24 Trevor Plouffe (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F8")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: MIN #20 Josh Roenicke
t10 = game.new_inning()

# Pitching change (MIN): #20 Josh Roenicke replaces #15 Glen Perkins
t10.pitching_substitution(20)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t10.new_ab()
t10.pitch_list("c")
t10.hit(1)
t10.advance(2, "34 BB")
t10.advance(3, "16 SAC1-4")
t10.advance(4, "5 SF8")

# 4. BOS #34 David Ortiz (X - X - 15)
t10.new_ab()
t10.pitch_list("b d s d b")
t10.reach("BB")
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #34 David Ortiz
t10.offensive_substitution(4, 23, "PR")
t10.atbase("PR")
t10.advance(2, "16 SAC1-4")

# 5. BOS #16 Will Middlebrooks (X - 15 - 34)
t10.new_ab()
t10.pitch_list("b")
t10.out("SAC1-4")

# 6. BOS #7  Stephen Drew (15 - 23 - X)
t10.new_ab()
t10.pitch_list("i i i i")
t10.reach("IBB")

# 7. BOS #5  Jonny Gomes (15 - 23 - 7)
t10.new_ab()
t10.pitch_list("d f")
t10.out("SF8", rbis=1)

# 8. BOS #37 Mike Carp (X - 23 - 7)
t10.new_ab()
t10.pitch_list("c b f")
t10.out("G3")


# Bot 10th
# Pitching: BOS #19 Koji Uehara
b10 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #63 Alex Wilson
b10.pitching_substitution(19)

# Defensive switch (BOS): #23 Pedro Ciriaco moves to DH
b10.defensive_switch(23, "0")

# 8. MIN #32 Aaron Hicks (X - X - X)
b10.new_ab()
b10.pitch_list("c s b b f b")
b10.out("F7")

# 9. MIN #25 Pedro Florimón (X - X - X)
b10.new_ab()
b10.pitch_list("c b b s s")
b10.out("K")

# Offensive change (MIN): Pinch-hitter #22 Wilkin Ramirez replaces #2 Brian Dozier, batting 1st
b10.offensive_substitution(1, 22, "PH")

# 1. MIN #22 Wilkin Ramirez (X - X - X)
b10.new_ab()
b10.pitch_list("c s b s")
b10.out("K")

# Winning team: BOS
# WP: BOS #63 Alex Wilson
game.winning_pitcher(63, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: MIN
# LP: MIN #20 Josh Roenicke
game.losing_pitcher(20)

# print(game)
game.generate_scorecard()
