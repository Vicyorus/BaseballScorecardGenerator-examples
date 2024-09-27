import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2013-05-03
# https://www.baseball-reference.com/boxes/TEX/TEX201305030.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2013/05/03/347174/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-03 20:08-23:12",
        "at": "Rangers Ballpark in Arlington, Arlington, TX",
        "att": "42,441",
        "temp": "66F, Partly Cloudy",
        "wind": "9mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                23: "Pedro Ciriaco",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                7: "Stephen Drew",
                3: "David Ross",
                37: "Mike Carp",
                29: "Daniel Nava",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [22, 30, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [39, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [3, "C"],
                [37, "1B"],
                [29, "LF"],
            ],
            "bullpen": [63, 41, 30, 19, 52, 31, 59, 36, 46, 11],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 45,
            "roster": {
                # Lineup
                5: "Ian Kinsler",
                1: "Elvis Andrus",
                27: "Lance Berkman",
                29: "Adrian Beltré",
                17: "Nelson Cruz",
                12: "A.J. Pierzynski",
                15: "Jeff Baker",
                18: "Mitch Moreland",
                23: "Craig Gentry",
                # Starting pitcher
                45: "Derek Holland",
                # Bench
                7: "David Murphy",
                3: "Leury García",
                2: "Leonys Martin",
                8: "Geovany Soto",
                # Bullpen
                50: "Michael Kirkman",
                44: "Jason Frasor",
                49: "Nick Tepesch",
                11: "Yu Darvish",
                41: "Alexi Ogando",
                52: "Tanner Scheppers",
                51: "Justin Grimm",
                46: "Robbie Ross Jr.",
                36: "Joe Nathan",
                58: "Joe Ortiz",
                55: "Derek Lowe",
            },
            "lefties": [45, 50, 46, 58],
            "lineup": [
                [5, "4"],
                [1, "6"],
                [27, "0"],
                [29, "5"],
                [17, "9"],
                [12, "2"],
                [15, "7"],
                [18, "3"],
                [23, "8"],
            ],
            "bench": [
                [7, "LF"],
                [3, "OF"],
                [2, "CF"],
                [8, "C"],
            ],
            "bullpen": [50, 44, 49, 11, 41, 52, 51, 46, 36, 58, 55],
        },
        "umpires": {
            "HP": "Mark Carlson",
            "1B": "Gerry Davis",
            "2B": "Brian Knight",
            "3B": "Dan Iassogna",
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
# Pitching: TEX #45 Derek Holland
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c s b s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c f b s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. TEX #5  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c f b")
b1.hit(1)
b1.thrown_out(2, "1 FC1-6", 1, 22)

# 2. TEX #1  Elvis Andrus (X - X - 5)
b1.new_ab()
b1.pitch_list("1 b b b c c")
b1.reach("FC1-6")
b1.advance(2, "29 1B")
b1.thrown_out(3, "29 9-6", 3, 22)

# 3. TEX #27 Lance Berkman (X - X - 1)
b1.new_ab()
b1.pitch_list("1 1 b")
b1.out("P4")

# 4. TEX #29 Adrian Beltré (X - X - 1)
b1.new_ab()
b1.pitch_list("c t b b 1 b f")
b1.hit(1)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #45 Derek Holland
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(1)

# 5. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("f b b b s s")
t2.out("K")

# 6. BOS #5  Jonny Gomes (X - X - 34)
t2.new_ab()
t2.pitch_list("f b s d s")
t2.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - 34)
t2.new_ab()
t2.pitch_list("f")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 5. TEX #17 Nelson Cruz (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("L8")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")

# 7. TEX #15 Jeff Baker (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.hit(2)
b2.advance(3, "18 1B")
b2.advance(4, "23 1B")

# 8. TEX #18 Mitch Moreland (X - 15 - X)
b2.new_ab()
b2.pitch_list("b b f")
b2.hit(1)
b2.advance(2, "23 1B")
b2.error(6)
b2.advance(3, "23 E6")

# 9. TEX #23 Craig Gentry (15 - X - 18)
b2.new_ab()
b2.pitch_list("f b")
b2.hit(1, rbis=1)

# 1. TEX #5  Ian Kinsler (18 - X - 23)
b2.new_ab()
b2.pitch_list("b 1 b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #45 Derek Holland
t3 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b b")
t3.out("G5-3")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c b c c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 2. TEX #1  Elvis Andrus (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f")
b3.hit(1)
b3.thrown_out(2, "27 DP4-6-3", 1, 22)

# 3. TEX #27 Lance Berkman (X - X - 1)
b3.new_ab()
b3.pitch_list("b b f c 1 f")
b3.out("DP4-6-3")

# 4. TEX #29 Adrian Beltré (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b f f")
b3.hit(1)
b3.advance(2, "17 1B")

# 5. TEX #17 Nelson Cruz (X - X - 29)
b3.new_ab()
b3.pitch_list("d")
b3.hit(1)

# 6. TEX #12 A.J. Pierzynski (X - 29 - 17)
b3.new_ab()
b3.pitch_list("b f b f f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #45 Derek Holland
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b f f f f f")
t4.hit(1)
t4.thrown_out(2, "34 DP4-6-3", 2, 45)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t4.new_ab()
t4.pitch_list("c f f 1 1 f 1 1 f b 1 s")
t4.out("K")

# 4. BOS #34 David Ortiz (X - X - 18)
t4.new_ab()
t4.pitch_list("s b b")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 7. TEX #15 Jeff Baker (X - X - X)
b4.new_ab()
b4.pitch_list("b f c")
b4.out("P4")

# 8. TEX #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.hit(1)
b4.advance(2, "5 1B")
b4.advance(4, "1 1B")

# 9. TEX #23 Craig Gentry (X - X - 18)
b4.new_ab()
b4.pitch_list("b f s c")
b4.out("!K")

# 1. TEX #5  Ian Kinsler (X - X - 18)
b4.new_ab()
b4.pitch_list("c c 1 f f b")
b4.hit(1)
b4.advance(2, "1 1B")
b4.advance(3, "27 BB")
b4.advance(4, "29 2B")

# 2. TEX #1  Elvis Andrus (X - 18 - 5)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1, rbis=1)
b4.advance(2, "27 BB")
b4.advance(4, "29 2B")

# 3. TEX #27 Lance Berkman (X - 5 - 1)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(4, "29 2B")

# 4. TEX #29 Adrian Beltré (5 - 1 - 27)
b4.new_ab()
b4.pitch_list("d b c f b")
b4.hit(2, rbis=3)
b4.advance(4, "17 1B")

# Pitching change (BOS): #63 Alex Wilson replaces #22 Felix Doubront
b4.pitching_substitution(63)

# 5. TEX #17 Nelson Cruz (X - 29 - X)
b4.new_ab()
b4.pitch_list("b s f b")
b4.hit(1, rbis=1)

# 6. TEX #12 A.J. Pierzynski (X - X - 17)
b4.new_ab()
b4.out("L5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #45 Derek Holland
t5 = game.new_inning()

# Defensive change (TEX): #7 David Murphy replaces #15 Jeff Baker (LF), playing LF, batting 7th
t5.defensive_substitution(7, 7, "7")

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b b")
t5.reach("BB")
t5.thrown_out(2, "16 DP6-4-3", 2, 45)

# 7. BOS #16 Will Middlebrooks (X - X - 5)
t5.new_ab()
t5.pitch_list("c")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: BOS #63 Alex Wilson
b5 = game.new_inning()

# 7. TEX #7  David Murphy (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 8. TEX #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "2 1B")
b5.advance(4, "5 2B")

# Offensive change (TEX): Pinch-hitter #2 Leonys Martin replaces #23 Craig Gentry, batting 9th
b5.offensive_substitution(9, 2, "PH")

# 9. TEX #2  Leonys Martin (X - X - 18)
b5.new_ab()
b5.hit(1)
b5.advance(3, "5 2B")

# 1. TEX #5  Ian Kinsler (X - 18 - 2)
b5.new_ab()
b5.pitch_list("b f")
b5.hit(2, rbis=1)

# 2. TEX #1  Elvis Andrus (2 - 5 - X)
b5.new_ab()
b5.pitch_list("d b c")
b5.out("F9")

# 3. TEX #27 Lance Berkman (2 - 5 - X)
b5.new_ab()
b5.pitch_list("f b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #45 Derek Holland
t6 = game.new_inning()

# Defensive switch (TEX): #2 Leonys Martin moves to CF
t6.defensive_switch(2, "8")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c t")
t6.out("KT")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.advance(2, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
t6.new_ab()
t6.pitch_list("f f b f b")
t6.hit(1)

# 2. BOS #18 Shane Victorino (X - 23 - 2)
t6.new_ab()
t6.pitch_list("b f")
t6.out("(F)P5")

# 3. BOS #15 Dustin Pedroia (X - 23 - 2)
t6.new_ab()
t6.pitch_list("s")
t6.out("G3")


# Bot 6th
# Pitching: BOS #63 Alex Wilson
b6 = game.new_inning()

# 4. TEX #29 Adrian Beltré (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.hit(1)
b6.thrown_out(2, "17 DP6-4-3", 1, 63)

# 5. TEX #17 Nelson Cruz (X - X - 29)
b6.new_ab()
b6.pitch_list("d c b c")
b6.out("DP6-4-3")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
b6.new_ab()
b6.pitch_list("b c f f")
b6.error(5)
b6.reach("E5")

# 7. TEX #7  David Murphy (X - X - 12)
b6.new_ab()
b6.pitch_list("b f f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #45 Derek Holland
t7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c b f")
t7.out("G6-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(1)

# 7. BOS #16 Will Middlebrooks (X - X - 5)
t7.new_ab()
t7.pitch_list("c s f s")
t7.out("K2-3")


# Bot 7th
# Pitching: BOS #63 Alex Wilson
b7 = game.new_inning()

# 8. TEX #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("F9")

# 9. TEX #2  Leonys Martin (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# Pitching change (BOS): #59 Clayton Mortensen replaces #63 Alex Wilson
b7.pitching_substitution(59)

# 1. TEX #5  Ian Kinsler (X - X - 2)
b7.new_ab()
b7.pitch_list("c b f f f f")
b7.out("F7")

# 2. TEX #1  Elvis Andrus (X - X - 2)
b7.new_ab()
b7.pitch_list("f d c f")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #45 Derek Holland
t8 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.out("F9")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t8.new_ab()
t8.pitch_list("b c b f f b s")
t8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)

# 2. BOS #18 Shane Victorino (X - X - 2)
t8.new_ab()
t8.pitch_list("b")
t8.out("(F)P5")


# Bot 8th
# Pitching: BOS #59 Clayton Mortensen
b8 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.out("(F)P2")

# 4. TEX #29 Adrian Beltré (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("G1-3")

# 5. TEX #17 Nelson Cruz (X - X - X)
b8.new_ab()
b8.pitch_list("s b b s b f b")
b8.reach("BB")
b8.advance(3, "12 1B")

# 6. TEX #12 A.J. Pierzynski (X - X - 17)
b8.new_ab()
b8.pitch_list("f")
b8.hit(1)

# 7. TEX #7  David Murphy (17 - X - 12)
b8.new_ab()
b8.pitch_list("f f s")
b8.out("K2-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #55 Derek Lowe
t9 = game.new_inning()

# Pitching change (TEX): #55 Derek Lowe replaces #45 Derek Holland
t9.pitching_substitution(55)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b f")
t9.out("G6-3")

# Winning team: TEX
# WP: TEX #45 Derek Holland
game.winning_pitcher(45)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
