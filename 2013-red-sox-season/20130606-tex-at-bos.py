import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2013-06-06
# https://www.baseball-reference.com/boxes/BOS/BOS201306060.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2013/06/06/347644/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-06 19:09-22:30",
        "at": "Fenway Park, Boston, MA",
        "att": "35,352",
        "temp": "67F, Cloudy",
        "wind": "13mph, Out To LF",
        "away": {
            "team": "Texas Rangers",
            "starter": 45,
            "roster": {
                # Lineup
                1: "Elvis Andrus",
                7: "David Murphy",
                27: "Lance Berkman",
                29: "Adrian Beltré",
                17: "Nelson Cruz",
                12: "A.J. Pierzynski",
                15: "Jeff Baker",
                23: "Craig Gentry",
                13: "Jurickson Profar",
                # Starting pitcher
                45: "Derek Holland",
                # Bench
                3: "Leury García",
                21: "Chris McGuiness",
                2: "Leonys Martin",
                8: "Geovany Soto",
                # Bullpen
                50: "Michael Kirkman",
                51: "Justin Grimm",
                46: "Robbie Ross Jr.",
                36: "Joe Nathan",
                44: "Jason Frasor",
                55: "Ross Wolf",
                49: "Nick Tepesch",
                56: "Neal Cotts",
                11: "Yu Darvish",
                52: "Tanner Scheppers",
            },
            "lefties": [45, 50, 46, 56],
            "lineup": [
                [1, "6"],
                [7, "7"],
                [27, "3"],
                [29, "5"],
                [17, "9"],
                [12, "2"],
                [15, "0"],
                [23, "8"],
                [13, "4"],
            ],
            "bench": [
                [3, "OF"],
                [21, "1B"],
                [2, "CF"],
                [8, "C"],
            ],
            "bullpen": [50, 51, 46, 36, 44, 55, 49, 56, 11, 52],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                3: "David Ross",
                10: "Jose Iglesias",
                23: "Pedro Ciriaco",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                44: "Jackie Bradley Jr.",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [3, "2"],
                [10, "6"],
                [23, "5"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [44, "CF"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Joe West",
            "1B": "Sam Holbrook",
            "2B": "Andy Fletcher",
            "3B": "Rob Drake",
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
# Pitching: BOS #31 Jon Lester
t1 = game.new_inning()

# 1. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G6-3")

# 2. TEX #7  David Murphy (X - X - X)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("L8")

# 3. TEX #27 Lance Berkman (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b b")
t1.reach("BB")
t1.advance(2, "29 1B")

# 4. TEX #29 Adrian Beltré (X - X - 27)
t1.new_ab()
t1.pitch_list("b c b b")
t1.hit(1)

# 5. TEX #17 Nelson Cruz (X - 27 - 29)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")


# Bot 1st
# Pitching: TEX #45 Derek Holland
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f c b")
b1.hit(1)
b1.advance(2, "5 1B")
b1.advance(3, "15 DP6-4-3")

# 2. BOS #5  Jonny Gomes (X - X - 2)
b1.new_ab()
b1.hit(1)
b1.thrown_out(2, "15 DP6-4-3", 1, 45)

# 3. BOS #15 Dustin Pedroia (X - 2 - 5)
b1.new_ab()
b1.pitch_list("c t b f f")
b1.out("DP6-4-3")

# 4. BOS #34 David Ortiz (2 - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t2.new_ab()
t2.pitch_list("t b")
t2.hit(2)
t2.advance(4, "15 HR")

# 7. TEX #15 Jeff Baker (X - 12 - X)
t2.new_ab()
t2.pitch_list("b b b c f f")
t2.hit(4, rbis=2)

# 8. TEX #23 Craig Gentry (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("F8")

# 9. TEX #13 Jurickson Profar (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "1 G5-3")

# 1. TEX #1  Elvis Andrus (X - X - 13)
t2.new_ab()
t2.pitch_list("b b c d f")
t2.out("G5-3")

# 2. TEX #7  David Murphy (X - 13 - X)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: TEX #45 Derek Holland
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b f")
b2.hit(1)
b2.thrown_out(2, "8-6", 1, 45)

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b f b f f c")
b2.out("!K")

# 7. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("b f f s")
b2.out("K2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.hit(1)
t3.thrown_out(2, "7-4", 1, 31)

# 4. TEX #29 Adrian Beltré (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(4)

# 5. TEX #17 Nelson Cruz (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G1-3")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t3.new_ab()
t3.pitch_list("b f c")
t3.out("G3")


# Bot 3rd
# Pitching: TEX #45 Derek Holland
b3 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c c b")
b3.reach("BB")
b3.advance(2, "2 1B")
b3.advance(3, "5 L9")
b3.advance(4, "15 2B")

# 9. BOS #23 Pedro Ciriaco (X - X - 10)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b3.new_ab()
b3.pitch_list("f s f 1 1")
b3.hit(1)
b3.advance(4, "15 2B")

# 2. BOS #5  Jonny Gomes (X - 10 - 2)
b3.new_ab()
b3.pitch_list("b c")
b3.out("L9")

# 3. BOS #15 Dustin Pedroia (10 - X - 2)
b3.new_ab()
b3.pitch_list("b d b c 1 f f")
b3.hit(2, rbis=2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b3.new_ab()
b3.pitch_list("d")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 7. TEX #15 Jeff Baker (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 8. TEX #23 Craig Gentry (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b b b")
t4.reach("BB")
t4.advance(2, "1 1B")

# 9. TEX #13 Jurickson Profar (X - X - 23)
t4.new_ab()
t4.pitch_list("f b s f d")
t4.out("F7")

# 1. TEX #1  Elvis Andrus (X - X - 23)
t4.new_ab()
t4.pitch_list("b b c f f")
t4.hit(1)

# 2. TEX #7  David Murphy (X - 23 - 1)
t4.new_ab()
t4.pitch_list("c")
t4.out("L7")


# Bot 4th
# Pitching: TEX #45 Derek Holland
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b")
b4.out("F9")

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c s f b")
b4.out("F9")

# 7. BOS #3  David Ross (X - X - X)
b4.new_ab()
b4.pitch_list("f b b f")
b4.hit(1)
b4.advance(2, "10 BB")

# 8. BOS #10 Jose Iglesias (X - X - 3)
b4.new_ab()
b4.pitch_list("b b c b f f b")
b4.reach("BB")

# 9. BOS #23 Pedro Ciriaco (X - 3 - 10)
b4.new_ab()
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("P3")

# 4. TEX #29 Adrian Beltré (X - X - X)
t5.new_ab()
t5.pitch_list("b b c c b s")
t5.out("K")

# 5. TEX #17 Nelson Cruz (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b")
t5.out("G6-3")


# Bot 5th
# Pitching: TEX #45 Derek Holland
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2)
b5.advance(3, "5 1B")
b5.thrown_out(4, "15 FC3-2", 1, 45)

# 2. BOS #5  Jonny Gomes (X - 2 - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1)
b5.advance(2, "15 FC3-2")

# 3. BOS #15 Dustin Pedroia (2 - X - 5)
b5.new_ab()
b5.pitch_list("s b s")
b5.reach("FC3-2")
b5.thrown_out(2, "34 DP6-3", 2, 45)

# 4. BOS #34 David Ortiz (X - 5 - 15)
b5.new_ab()
b5.pitch_list("f b c")
b5.out("DP6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t6.new_ab()
t6.hit(2)

# 7. TEX #15 Jeff Baker (X - 12 - X)
t6.new_ab()
t6.pitch_list("b c b s f b f c")
t6.out("!K")

# 8. TEX #23 Craig Gentry (X - 12 - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.out("G5-3")

# 9. TEX #13 Jurickson Profar (X - 12 - X)
t6.new_ab()
t6.pitch_list("t b b f c")
t6.out("!K")


# Bot 6th
# Pitching: TEX #45 Derek Holland
b6 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f b b")
b6.reach("BB")
b6.advance(2, "10 1B")
b6.advance(3, "23 WP")

# 7. BOS #3  David Ross (X - X - 29)
b6.new_ab()
b6.pitch_list("b 1 f")
b6.out("P3")

# 8. BOS #10 Jose Iglesias (X - X - 29)
b6.new_ab()
b6.pitch_list("c f 1 f b d")
b6.hit(1)
b6.advance(2, "23 WP")

# 9. BOS #23 Pedro Ciriaco (X - 29 - 10)
b6.new_ab()
b6.pitch_list("c f b f s")
b6.wp()
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #36 Junichi Tazawa
t7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t7.pitching_substitution(36)

# 1. TEX #1  Elvis Andrus (X - X - X)
t7.new_ab()
t7.pitch_list("b b s b c")
t7.out("F9")

# 2. TEX #7  David Murphy (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.hit(2)
t7.advance(3, "29 1B")

# 3. TEX #27 Lance Berkman (X - 7 - X)
t7.new_ab()
t7.out("L5")

# 4. TEX #29 Adrian Beltré (X - 7 - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1)

# 5. TEX #17 Nelson Cruz (7 - X - 29)
t7.new_ab()
t7.pitch_list("b b f")
t7.out("F8")


# Bot 7th
# Pitching: TEX #46 Robbie Ross Jr.
b7 = game.new_inning()

# Pitching change (TEX): #46 Robbie Ross Jr. replaces #45 Derek Holland
b7.pitching_substitution(46)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(2)
b7.advance(3, "5 1B")
b7.advance(4, "12 FC3-6")

# 2. BOS #5  Jonny Gomes (X - 2 - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(1)
b7.advance(2, "34 BB")
b7.advance(3, "12 FC3-6")

# 3. BOS #15 Dustin Pedroia (2 - X - 5)
b7.new_ab()
b7.pitch_list("b f s s")
b7.out("K")

# 4. BOS #34 David Ortiz (2 - X - 5)
b7.new_ab()
b7.pitch_list("b s b f b b")
b7.reach("BB")
b7.thrown_out(2, "12 FC3-6", 2, 44)

# Pitching change (TEX): #44 Jason Frasor replaces #46 Robbie Ross Jr.
b7.pitching_substitution(44)

# 5. BOS #12 Mike Napoli (2 - 5 - 34)
b7.new_ab()
b7.pitch_list("s s f")
b7.reach("FC3-6", rbis=1)

# 6. BOS #29 Daniel Nava (5 - X - 12)
b7.new_ab()
b7.pitch_list("c b f 1 s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t8.pitching_substitution(19)

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t8.new_ab()
t8.pitch_list("b b s t s")
t8.out("K")

# 7. TEX #15 Jeff Baker (X - X - X)
t8.new_ab()
t8.pitch_list("s c c")
t8.out("!K")

# Offensive change (TEX): Pinch-hitter #2 Leonys Martin replaces #23 Craig Gentry, batting 8th
t8.offensive_substitution(8, 2, "PH")

# 8. TEX #2  Leonys Martin (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")


# Bot 8th
# Pitching: TEX #52 Tanner Scheppers
b8 = game.new_inning()

# Pitching change (TEX): #52 Tanner Scheppers replaces #44 Jason Frasor
b8.pitching_substitution(52)

# Defensive switch (TEX): #2 Leonys Martin moves to CF
b8.defensive_switch(2, "8")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #3 David Ross, batting 7th
b8.offensive_substitution(7, 37, "PH")

# 7. BOS #37 Mike Carp (X - X - X)
b8.new_ab()
b8.pitch_list("b f c b s")
b8.out("K2-3")

# 8. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")

# Offensive change (BOS): Pinch-hitter #7 Stephen Drew replaces #23 Pedro Ciriaco, batting 9th
b8.offensive_substitution(9, 7, "PH")

# 9. BOS #7  Stephen Drew (X - X - 10)
b8.new_ab()
b8.pitch_list("c 1 b f 1 s")
b8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b8.new_ab()
b8.pitch_list("b b 1")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
t9.pitching_substitution(40)

# Defensive change (BOS): #39 Jarrod Saltalamacchia replaces #37 Mike Carp (PH), playing C, batting 7th
t9.defensive_substitution(7, 39, "2")

# Defensive switch (BOS): #10 Jose Iglesias moves to 3B
t9.defensive_switch(10, "5")

# Defensive switch (BOS): #7 Stephen Drew moves to SS
t9.defensive_switch(7, "6")

# 9. TEX #13 Jurickson Profar (X - X - X)
t9.new_ab()
t9.pitch_list("c f b f b f")
t9.hit(1)
t9.advance(2, "1 SAC3-4")

# 1. TEX #1  Elvis Andrus (X - X - 13)
t9.new_ab()
t9.pitch_list("b 1 b b c m")
t9.out("SAC3-4")

# 2. TEX #7  David Murphy (X - 13 - X)
t9.new_ab()
t9.pitch_list("c f f")
t9.out("(F)P5")

# 3. TEX #27 Lance Berkman (X - 13 - X)
t9.new_ab()
t9.pitch_list("b f s f s")
t9.out("K")


# Bot 9th
# Pitching: TEX #50 Michael Kirkman
b9 = game.new_inning()

# Pitching change (TEX): #50 Michael Kirkman replaces #52 Tanner Scheppers
b9.pitching_substitution(50)

# 2. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.hit(2)
b9.advance(4, "34 HR")

# 3. BOS #15 Dustin Pedroia (X - 5 - X)
b9.new_ab()
b9.pitch_list("i i i i")
b9.reach("IBB")
b9.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - 5 - 15)
b9.new_ab()
b9.hit(4, rbis=3)

# Winning team: BOS
# WP: BOS #40 Andrew Bailey
game.winning_pitcher(40)

# Loser team: TEX
# LP: TEX #50 Michael Kirkman
game.losing_pitcher(50, is_away_team=True)

# print(game)
game.generate_scorecard()
