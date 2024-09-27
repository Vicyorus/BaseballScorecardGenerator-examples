import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2013-05-04
# https://www.baseball-reference.com/boxes/TEX/TEX201305040.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2013/05/04/347189/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-04 20:06-23:01",
        "at": "Rangers Ballpark in Arlington, Arlington, TX",
        "att": "47,173",
        "temp": "73F, Clear",
        "wind": "10mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                5: "Jonny Gomes",
                # Bullpen
                63: "Alex Wilson",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [23, "3B"],
                [5, "LF"],
            ],
            "bullpen": [63, 30, 19, 52, 31, 59, 36, 22, 46, 11],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 41,
            "roster": {
                # Lineup
                5: "Ian Kinsler",
                1: "Elvis Andrus",
                27: "Lance Berkman",
                29: "Adrian Beltré",
                12: "A.J. Pierzynski",
                17: "Nelson Cruz",
                18: "Mitch Moreland",
                23: "Craig Gentry",
                2: "Leonys Martin",
                # Starting pitcher
                41: "Alexi Ogando",
                # Bench
                7: "David Murphy",
                3: "Leury García",
                8: "Geovany Soto",
                15: "Jeff Baker",
                # Bullpen
                50: "Michael Kirkman",
                44: "Jason Frasor",
                49: "Nick Tepesch",
                45: "Derek Holland",
                11: "Yu Darvish",
                52: "Tanner Scheppers",
                51: "Justin Grimm",
                46: "Robbie Ross Jr.",
                36: "Joe Nathan",
                58: "Joe Ortiz",
                55: "Derek Lowe",
            },
            "lefties": [50, 45, 46, 58],
            "lineup": [
                [5, "4"],
                [1, "6"],
                [27, "0"],
                [29, "5"],
                [12, "2"],
                [17, "9"],
                [18, "3"],
                [23, "8"],
                [2, "7"],
            ],
            "bench": [
                [7, "LF"],
                [3, "OF"],
                [8, "C"],
                [15, "2B"],
            ],
            "bullpen": [50, 44, 49, 45, 11, 52, 51, 46, 36, 58, 55],
        },
        "umpires": {
            "HP": "Gerry Davis",
            "1B": "Brian Knight",
            "2B": "Dan Iassogna",
            "3B": "Mark Carlson",
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
# Pitching: TEX #41 Alexi Ogando
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b")
t1.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.out("F9")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. TEX #5  Ian Kinsler (X - X - X)
b1.new_ab()
b1.hit(4)

# 2. TEX #1  Elvis Andrus (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f")
b1.out("G6-3")

# 3. TEX #27 Lance Berkman (X - X - X)
b1.new_ab()
b1.pitch_list("b c b s b f c")
b1.out("!K")

# 4. TEX #29 Adrian Beltré (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f f")
b1.error(5)
b1.reach("E5")

# 5. TEX #12 A.J. Pierzynski (X - X - 29)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #41 Alexi Ogando
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(2)
t2.advance(4, "29 1B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
t2.new_ab()
t2.pitch_list("c b b s f s")
t2.out("K")

# 6. BOS #29 Daniel Nava (X - 34 - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1, rbis=1)
t2.advance(2, "16 WP")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t2.new_ab()
t2.pitch_list("c b 1 f s")
t2.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - 29)
t2.new_ab()
t2.pitch_list("b b c c b f f f")
t2.wp()
t2.out("F9")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 6. TEX #17 Nelson Cruz (X - X - X)
b2.new_ab()
b2.pitch_list("f c f s")
b2.out("K")

# 7. TEX #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("P5")

# 8. TEX #23 Craig Gentry (X - X - X)
b2.new_ab()
b2.pitch_list("b c s c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #41 Alexi Ogando
t3 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G3-1")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f")
t3.hit(1)
t3.advance(2, "18 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab()
t3.pitch_list("b 1 b b c c f b")
t3.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t3.new_ab()
t3.pitch_list("b c c s")
t3.out("K")

# 4. BOS #34 David Ortiz (X - 2 - 18)
t3.new_ab()
t3.out("F7")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 9. TEX #2  Leonys Martin (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b")
b3.hit(1)
b3.thrown_out(2, "1 CS", 2, 41)

# 1. TEX #5  Ian Kinsler (X - X - 2)
b3.new_ab()
b3.pitch_list("c 1")
b3.out("P6")

# 2. TEX #1  Elvis Andrus (X - X - 2)
b3.new_ab()
b3.pitch_list("b b t f b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #41 Alexi Ogando
t4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b b s s")
t4.out("L1-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b s f")
t4.hit(2)

# 8. BOS #16 Will Middlebrooks (X - 39 - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("F8")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s b")
b4.out("G3-1")

# 4. TEX #29 Adrian Beltré (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b b")
b4.reach("BB")
b4.advance(2, "12 1B")
b4.advance(3, "17 F9")
b4.advance(4, "23 1B")

# 5. TEX #12 A.J. Pierzynski (X - X - 29)
b4.new_ab()
b4.pitch_list("f b s")
b4.hit(1)
b4.advance(2, "18 BB")
b4.error(5)
b4.advance(3, "23 1B")
b4.advance(4, "23 E5")

# 6. TEX #17 Nelson Cruz (X - 29 - 12)
b4.new_ab()
b4.pitch_list("s c b d")
b4.out("F9")

# 7. TEX #18 Mitch Moreland (29 - X - 12)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(3, "23 E5")

# 8. TEX #23 Craig Gentry (29 - 12 - 18)
b4.new_ab()
b4.hit(1, rbis=1)
b4.advance(2, "2 BB")

# 9. TEX #2  Leonys Martin (18 - X - 23)
b4.new_ab()
b4.pitch_list("1 f b b 1 b b")
b4.reach("BB")

# 1. TEX #5  Ian Kinsler (18 - 23 - 2)
b4.new_ab()
b4.pitch_list("f f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #41 Alexi Ogando
t5 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c c b")
t5.reach("BB")
t5.thrown_out(1, "2 DP3", 2, 41)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t5.new_ab()
t5.pitch_list("f b")
t5.out("DP3")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("F8")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 2. TEX #1  Elvis Andrus (X - X - X)
b5.new_ab()
b5.pitch_list("c c s")
b5.out("K")

# 3. TEX #27 Lance Berkman (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.hit(1)
b5.advance(2, "29 1B")

# 4. TEX #29 Adrian Beltré (X - X - 27)
b5.new_ab()
b5.pitch_list("b c b")
b5.hit(1)

# 5. TEX #12 A.J. Pierzynski (X - 27 - 29)
b5.new_ab()
b5.pitch_list("b f")
b5.out("F9")

# 6. TEX #17 Nelson Cruz (X - 27 - 29)
b5.new_ab()
b5.pitch_list("b s c f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #41 Alexi Ogando
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("f s f")
t6.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c f")
t6.hit(1)
t6.advance(2, "29 HBP")

# 6. BOS #29 Daniel Nava (X - X - 12)
t6.new_ab()
t6.pitch_list("b c")
t6.reach("HBP")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
t6.new_ab()
t6.pitch_list("s f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #30 Andrew Miller
b6 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #41 John Lackey
b6.pitching_substitution(30)

# 7. TEX #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(1)
b6.thrown_out(2, "23 FC4-6", 1, 30)

# 8. TEX #23 Craig Gentry (X - X - 18)
b6.new_ab()
b6.pitch_list("b")
b6.reach("FC4-6")

# 9. TEX #2  Leonys Martin (X - X - 23)
b6.new_ab()
b6.pitch_list("1 f")
b6.out("F7")

# 1. TEX #5  Ian Kinsler (X - X - 23)
b6.new_ab()
b6.pitch_list("c b c 1 f")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #41 Alexi Ogando
t7 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(1)
t7.thrown_out(2, "7 FC3-6", 1, 46)

# Pitching change (TEX): #46 Robbie Ross Jr. replaces #41 Alexi Ogando
t7.pitching_substitution(46)

# 9. BOS #7  Stephen Drew (X - X - 16)
t7.new_ab()
t7.pitch_list("t")
t7.reach("FC3-6")
t7.advance(2, "2 1B")
t7.advance(3, "18 G3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t7.new_ab()
t7.pitch_list("b f b")
t7.hit(1)
t7.advance(2, "18 G3")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G3")

# Pitching change (TEX): #52 Tanner Scheppers replaces #46 Robbie Ross Jr.
t7.pitching_substitution(52)

# 3. BOS #15 Dustin Pedroia (7 - 2 - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("G3-1")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #30 Andrew Miller
b7.pitching_substitution(36)

# 2. TEX #1  Elvis Andrus (X - X - X)
b7.new_ab()
b7.pitch_list("f b b b")
b7.hit(1)
b7.advance(2, "29 SB")

# 3. TEX #27 Lance Berkman (X - X - 1)
b7.new_ab()
b7.pitch_list("c b b f s")
b7.out("K")

# 4. TEX #29 Adrian Beltré (X - X - 1)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")

# 5. TEX #12 A.J. Pierzynski (X - 1 - X)
b7.new_ab()
b7.pitch_list("c b f b b f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #52 Tanner Scheppers
t8 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.reach("HBP")

# 6. BOS #29 Daniel Nava (X - X - 12)
t8.new_ab()
t8.pitch_list("b")
t8.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t8.new_ab()
t8.pitch_list("b")
t8.out("L6")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b8.pitching_substitution(19)

# 6. TEX #17 Nelson Cruz (X - X - X)
b8.new_ab()
b8.pitch_list("f c c")
b8.out("!K")

# 7. TEX #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(4, "23 HR")

# 8. TEX #23 Craig Gentry (X - X - 18)
b8.new_ab()
b8.pitch_list("b f b f")
b8.hit(4, rbis=2)

# 9. TEX #2  Leonys Martin (X - X - X)
b8.new_ab()
b8.pitch_list("s b l s")
b8.out("K")

# 1. TEX #5  Ian Kinsler (X - X - X)
b8.new_ab()
b8.pitch_list("c s f f")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #36 Joe Nathan
t9 = game.new_inning()

# Pitching change (TEX): #36 Joe Nathan replaces #52 Tanner Scheppers
t9.pitching_substitution(36)

# 8. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c c f b s")
t9.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("b c b s f b")
t9.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c f b s")
t9.out("K")

# Winning team: TEX
# WP: TEX #41 Alexi Ogando
game.winning_pitcher(41)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
