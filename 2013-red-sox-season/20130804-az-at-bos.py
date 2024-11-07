import os
from baseball_scorecard.baseball_scorecard import Scorecard

# AZ @ BOS, 2013-08-04
# https://www.baseball-reference.com/boxes/BOS/BOS201308040.shtml
# https://www.mlb.com/gameday/d-backs-vs-red-sox/2013/08/04/348397/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-04 13:39-16:55",
        "at": "Fenway Park, Boston, MA",
        "att": "37,611",
        "temp": "78F, Partly Cloudy",
        "wind": "6mph, R To L",
        "away": {
            "team": "Arizona Diamondbacks",
            "starter": 32,
            "roster": {
                # Lineup
                11: "AJ Pollock",
                2: "Aaron Hill",
                44: "Paul Goldschmidt",
                14: "Martín Prado",
                7: "Cody Ross",
                27: "Wil Nieves",
                8: "Gerardo Parra",
                54: "Tuffy Gosewisch",
                1: "Didi Gregorius",
                # Starting pitcher
                32: "Brandon McCarthy",
                # Bench
                6: "Adam Eaton",
                12: "Eric Chavez",
                13: "Jason Kubel",
                4: "Cliff Pennington",
                # Bullpen
                40: "J.J. Putz",
                38: "Will Harris",
                36: "Wade Miley",
                30: "David Hernandez",
                52: "Zeke Spruill",
                48: "Randall Delgado",
                55: "Josh Collmenter",
                46: "Patrick Corbin",
                21: "Heath Bell",
                29: "Brad Ziegler",
                54: "Joe Thatcher",
            },
            "lefties": [36, 46, 54],
            "lineup": [
                [11, "8"],
                [2, "4"],
                [44, "3"],
                [14, "5"],
                [7, "7"],
                [27, "0"],
                [8, "9"],
                [54, "2"],
                [1, "6"],
            ],
            "bench": [
                [6, "CF"],
                [12, "3B"],
                [13, "LF"],
                [4, "SS"],
            ],
            "bullpen": [40, 38, 36, 30, 52, 48, 55, 46, 21, 29, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                26: "Brock Holt",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                29: "Daniel Nava",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [7, "6"],
                [26, "5"],
            ],
            "bench": [
                [29, "LF"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 32, 66, 44, 31, 36, 19, 38, 62, 46],
        },
        "umpires": {
            "HP": "Paul Schrieber",
            "1B": "Chad Fairchild",
            "2B": "Jeff Kellogg",
            "3B": "Eric Cooper",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. AZ #11 AJ Pollock (X - X - X)
t1.new_ab()
t1.pitch_list("b c f c")
t1.out("!K")

# 2. AZ #2  Aaron Hill (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("F8")

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(1)

# 4. AZ #14 Martín Prado (X - X - 44)
t1.new_ab()
t1.pitch_list("b c b")
t1.out("G4-3")


# Bot 1st
# Pitching: AZ #32 Brandon McCarthy
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f b s b f f")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c f s")
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f b b")
b1.reach("BB")
b1.advance(3, "34 E9")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("c d 1")
b1.error(9)
b1.reach("E9")

# 5. BOS #12 Mike Napoli (15 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b c c s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 5. AZ #7  Cody Ross (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.hit(1)
t2.thrown_out(2, "27 DP5-4-3", 1, 22)

# 6. AZ #27 Wil Nieves (X - X - 7)
t2.new_ab()
t2.pitch_list("1 b b f")
t2.out("DP5-4-3")

# 7. AZ #8  Gerardo Parra (X - X - X)
t2.new_ab()
t2.out("B4-3")


# Bot 2nd
# Pitching: AZ #32 Brandon McCarthy
b2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("b f b s b c")
b2.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("f f b b f b b")
b2.reach("BB")
b2.thrown_out(2, "7 DP4-6-3", 2, 32)

# 8. BOS #7  Stephen Drew (X - X - 39)
b2.new_ab()
b2.pitch_list("c b c")
b2.out("DP4-6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 8. AZ #54 Tuffy Gosewisch (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.out("F7")

# 9. AZ #1  Didi Gregorius (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f s")
t3.out("K")

# 1. AZ #11 AJ Pollock (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f")
t3.out("G4-3")


# Bot 3rd
# Pitching: AZ #32 Brandon McCarthy
b3 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
b3.new_ab()
b3.pitch_list("b f s b c")
b3.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("f b f b f")
b3.reach("HBP")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("1 c 1 b b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 2. AZ #2  Aaron Hill (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c f b")
t4.out("F8")

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t4.new_ab()
t4.out("L9")

# 4. AZ #14 Martín Prado (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 5. AZ #7  Cody Ross (X - X - 14)
t4.new_ab()
t4.pitch_list("c s c")
t4.out("!K")


# Bot 4th
# Pitching: AZ #32 Brandon McCarthy
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f f")
b4.out("F7")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("f f b b s")
b4.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 6. AZ #27 Wil Nieves (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.hit(1)
t5.thrown_out(1, "54 DP5-3", 3, 22)

# 7. AZ #8  Gerardo Parra (X - X - 27)
t5.new_ab()
t5.pitch_list("1")
t5.out("F8")

# 8. AZ #54 Tuffy Gosewisch (X - X - 27)
t5.new_ab()
t5.pitch_list("b f f")
t5.out("DP5-3")


# Bot 5th
# Pitching: AZ #32 Brandon McCarthy
b5 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(3, "26 1B")
b5.advance(4, "2 SF8")

# 9. BOS #26 Brock Holt (X - X - 7)
b5.new_ab()
b5.hit(1)
b5.advance(3, "18 1B")
b5.advance(4, "15 2B")

# 1. BOS #2  Jacoby Ellsbury (7 - X - 26)
b5.new_ab(is_risp=True)
b5.pitch_list("f f")
b5.out("SF8", rbis=1)

# 2. BOS #18 Shane Victorino (X - X - 26)
b5.new_ab()
b5.pitch_list("s")
b5.hit(1)
b5.advance(3, "15 2B")

# 3. BOS #15 Dustin Pedroia (26 - X - 18)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f 1 1 f f f f")
b5.hit(2, rbis=1)

# 4. BOS #34 David Ortiz (18 - 15 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("i i i i")
b5.reach("IBB")

# Pitching change (AZ): #38 Will Harris replaces #32 Brandon McCarthy
b5.pitching_substitution(38)

# 5. BOS #12 Mike Napoli (18 - 15 - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("b s b")
b5.out("IF3")

# 6. BOS #37 Mike Carp (18 - 15 - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("b c")
b5.out("P5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 9. AZ #1  Didi Gregorius (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b b")
t6.out("G3")

# 1. AZ #11 AJ Pollock (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L7")

# 2. AZ #2  Aaron Hill (X - X - X)
t6.new_ab()
t6.pitch_list("c f b f s")
t6.out("K")


# Bot 6th
# Pitching: AZ #55 Josh Collmenter
b6 = game.new_inning()

# Pitching change (AZ): #55 Josh Collmenter replaces #38 Will Harris
b6.pitching_substitution(55)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c s f f")
b6.hit(1)
b6.advance(2, "7 1B")
b6.advance(3, "26 SAC5-3")
b6.advance(4, "2 1B")

# 8. BOS #7  Stephen Drew (X - X - 39)
b6.new_ab()
b6.pitch_list("b b c")
b6.hit(1)
b6.advance(2, "26 SAC5-3")
b6.advance(4, "18 1B")

# 9. BOS #26 Brock Holt (X - 39 - 7)
b6.new_ab(is_risp=True)
b6.out("SAC5-3")

# 1. BOS #2  Jacoby Ellsbury (39 - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("t s f b b b f")
b6.hit(1, rbis=1)
b6.advance(2, "18 1B")
b6.advance(3, "15 BB")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("f c b")
b6.hit(1, rbis=1)
b6.advance(2, "15 BB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b b")
b6.reach("BB")

# Pitching change (AZ): #54 Joe Thatcher replaces #55 Josh Collmenter
b6.pitching_substitution(54)

# 4. BOS #34 David Ortiz (2 - 18 - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("c s s")
b6.out("K")

# 5. BOS #12 Mike Napoli (2 - 18 - 15)
b6.new_ab(is_risp=True)
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.error(5)
t7.reach("E5")
t7.advance(2, "7 1B")

# 4. AZ #14 Martín Prado (X - X - 44)
t7.new_ab()
t7.pitch_list("b b b c")
t7.out("F8")

# 5. AZ #7  Cody Ross (X - X - 44)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(1)

# 6. AZ #27 Wil Nieves (X - 44 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("b b b c f f s")
t7.out("K")

# 7. AZ #8  Gerardo Parra (X - 44 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("c b f f")
t7.out("G6-3")


# Bot 7th
# Pitching: AZ #54 Joe Thatcher
b7 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
b7.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("c b c f s")
b7.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b b s b f f")
b7.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")
b7.advance(2, "26 BB")

# 9. BOS #26 Brock Holt (X - X - 7)
b7.new_ab()
b7.pitch_list("1 b b b c 1 b")
b7.reach("BB")

# Pitching change (AZ): #21 Heath Bell replaces #54 Joe Thatcher
b7.pitching_substitution(21)

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 26)
b7.new_ab(is_risp=True)
b7.pitch_list("c c b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #38 Matt Thornton
t8 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #22 Felix Doubront
t8.pitching_substitution(38)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 8. AZ #54 Tuffy Gosewisch (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "11 1B")

# Pitching change (BOS): #66 Drake Britton replaces #38 Matt Thornton
t8.pitching_substitution(66)

# 9. AZ #1  Didi Gregorius (X - X - 54)
t8.new_ab()
t8.pitch_list("c f b f b b s")
t8.out("K")

# 1. AZ #11 AJ Pollock (X - X - 54)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(1)

# 2. AZ #2  Aaron Hill (X - 54 - 11)
t8.new_ab(is_risp=True)
t8.pitch_list("f")
t8.out("F9")

# 3. AZ #44 Paul Goldschmidt (X - 54 - 11)
t8.new_ab(is_risp=True)
t8.out("G1-3")


# Bot 8th
# Pitching: AZ #21 Heath Bell
b8 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.reach("HBP")
b8.advance(2, "15 G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G4-3")

# 4. BOS #34 David Ortiz (X - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("d b f")
b8.out("F8")

# 5. BOS #12 Mike Napoli (X - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b d s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #66 Drake Britton
t9.pitching_substitution(19)

# 4. AZ #14 Martín Prado (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1)
t9.advance(2, "8 DI")

# 5. AZ #7  Cody Ross (X - X - 14)
t9.new_ab()
t9.pitch_list("c s f f 1 s")
t9.out("K")

# 6. AZ #27 Wil Nieves (X - X - 14)
t9.new_ab()
t9.out("F8")

# 7. AZ #8  Gerardo Parra (X - X - 14)
t9.new_ab(is_risp=True)
t9.pitch_list("l s d d")
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)

# Loser team: AZ
# LP: AZ #32 Brandon McCarthy
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
