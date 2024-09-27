import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2013-06-04
# https://www.baseball-reference.com/boxes/BOS/BOS201306040.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2013/06/04/347616/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-04 19:12-22:22",
        "at": "Fenway Park, Boston, MA",
        "att": "32,035",
        "temp": "71F, Partly Cloudy",
        "wind": "15mph, In From LF",
        "away": {
            "team": "Texas Rangers",
            "starter": 51,
            "roster": {
                # Lineup
                1: "Elvis Andrus",
                7: "David Murphy",
                27: "Lance Berkman",
                17: "Nelson Cruz",
                18: "Mitch Moreland",
                12: "A.J. Pierzynski",
                15: "Jeff Baker",
                13: "Jurickson Profar",
                2: "Leonys Martin",
                # Starting pitcher
                51: "Justin Grimm",
                # Bench
                3: "Leury García",
                29: "Adrian Beltré",
                8: "Geovany Soto",
                23: "Craig Gentry",
                # Bullpen
                50: "Michael Kirkman",
                44: "Jason Frasor",
                49: "Nick Tepesch",
                56: "Neal Cotts",
                45: "Derek Holland",
                11: "Yu Darvish",
                52: "Tanner Scheppers",
                46: "Robbie Ross Jr.",
                36: "Joe Nathan",
                55: "Ross Wolf",
                58: "Joe Ortiz",
            },
            "lefties": [50, 56, 45, 46, 58],
            "lineup": [
                [1, "6"],
                [7, "7"],
                [27, "0"],
                [17, "9"],
                [18, "3"],
                [12, "2"],
                [15, "5"],
                [13, "4"],
                [2, "8"],
            ],
            "bench": [
                [3, "OF"],
                [29, "3B"],
                [8, "C"],
                [23, "CF"],
            ],
            "bullpen": [50, 44, 49, 56, 45, 11, 52, 46, 36, 55, 58],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                37: "Mike Carp",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [29, "9"],
                [37, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
                [44, "8"],
            ],
            "bench": [
                [2, "CF"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 31, 59, 36, 11, 19, 22],
        },
        "umpires": {
            "HP": "Andy Fletcher",
            "1B": "Rob Drake",
            "2B": "Joe West",
            "3B": "Sam Holbrook",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b f")
t1.out("(F)P3")

# 2. TEX #7  David Murphy (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.reach("HBP")
t1.advance(2, "27 1B")
t1.advance(3, "17 FC4-6")

# 3. TEX #27 Lance Berkman (X - X - 7)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "17 FC4-6", 2, 46)

# 4. TEX #17 Nelson Cruz (X - 7 - 27)
t1.new_ab()
t1.pitch_list("b b s f b")
t1.reach("FC4-6")

# 5. TEX #18 Mitch Moreland (7 - X - 17)
t1.new_ab()
t1.pitch_list("b f b")
t1.out("G4-3")


# Bot 1st
# Pitching: TEX #51 Justin Grimm
b1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c b b")
b1.reach("BB")
b1.advance(3, "37 1B")
b1.advance(4, "34 2B")

# 2. BOS #37 Mike Carp (X - X - 29)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(3, "34 2B")
b1.advance(4, "39 G3-1")

# 3. BOS #15 Dustin Pedroia (29 - X - 37)
b1.new_ab()
b1.pitch_list("c b b t t")
b1.out("KT")

# 4. BOS #34 David Ortiz (29 - X - 37)
b1.new_ab()
b1.pitch_list("b b c b")
b1.hit(2, rbis=1)
b1.advance(3, "39 G3-1")

# 5. BOS #12 Mike Napoli (37 - 34 - X)
b1.new_ab()
b1.pitch_list("f b s b b b")
b1.reach("BB")
b1.advance(2, "39 G3-1")

# 6. BOS #39 Jarrod Saltalamacchia (37 - 34 - 12)
b1.new_ab()
b1.pitch_list("c b c b f")
b1.out("G3-1", rbis=1)

# 7. BOS #7  Stephen Drew (34 - 12 - X)
b1.new_ab()
b1.pitch_list("b c c")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)

# 7. TEX #15 Jeff Baker (X - X - 12)
t2.new_ab()
t2.pitch_list("b c f c")
t2.out("!K")

# 8. TEX #13 Jurickson Profar (X - X - 12)
t2.new_ab()
t2.pitch_list("c f b b")
t2.out("F9")

# 9. TEX #2  Leonys Martin (X - X - 12)
t2.new_ab()
t2.pitch_list("d s c f s")
t2.out("K")


# Bot 2nd
# Pitching: TEX #51 Justin Grimm
b2 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(2)
b2.advance(4, "44 HR")

# 9. BOS #44 Jackie Bradley Jr. (X - 10 - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.hit(4, rbis=2)

# 1. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b c b")
b2.hit(1)
b2.advance(2, "37 BB")
b2.advance(4, "34 3B")

# 2. BOS #37 Mike Carp (X - X - 29)
b2.new_ab()
b2.pitch_list("b b b 1 b")
b2.reach("BB")
b2.advance(4, "34 3B")

# 3. BOS #15 Dustin Pedroia (X - 29 - 37)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 4. BOS #34 David Ortiz (X - 29 - 37)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(3, rbis=2)
b2.advance(4, "12 SF7")

# 5. BOS #12 Mike Napoli (34 - X - X)
b2.new_ab()
b2.out("SF7", rbis=1)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(2)
b2.advance(4, "7 2B")

# Pitching change (TEX): #50 Michael Kirkman replaces #51 Justin Grimm
b2.pitching_substitution(50)

# 7. BOS #7  Stephen Drew (X - 39 - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2, rbis=1)

# 8. BOS #10 Jose Iglesias (X - 7 - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 1. TEX #1  Elvis Andrus (X - X - X)
t3.new_ab()
t3.pitch_list("c f f c")
t3.out("!K")

# 2. TEX #7  David Murphy (X - X - X)
t3.new_ab()
t3.pitch_list("b c c s")
t3.out("K")

# 3. TEX #27 Lance Berkman (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b")
t3.out("G5-3")


# Bot 3rd
# Pitching: TEX #50 Michael Kirkman
b3 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("L7")

# 1. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b")
b3.hit(2)
b3.advance(4, "37 1B")

# 2. BOS #37 Mike Carp (X - 29 - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(1, rbis=1)
b3.advance(3, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 37)
b3.new_ab()
b3.pitch_list("c")
b3.hit(2)

# 4. BOS #34 David Ortiz (37 - 15 - X)
b3.new_ab()
b3.pitch_list("b b t f f f s")
b3.out("K")

# 5. BOS #12 Mike Napoli (37 - 15 - X)
b3.new_ab()
b3.pitch_list("i i i i")
b3.reach("IBB")

# 6. BOS #39 Jarrod Saltalamacchia (37 - 15 - 12)
b3.new_ab()
b3.pitch_list("c s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 4. TEX #17 Nelson Cruz (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("F9")

# 5. TEX #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b c s b f")
t4.out("G4-3")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t4.new_ab()
t4.pitch_list("b c f b f")
t4.hit(2)
t4.advance(4, "15 HR")

# 7. TEX #15 Jeff Baker (X - 12 - X)
t4.new_ab()
t4.hit(4, rbis=2)

# 8. TEX #13 Jurickson Profar (X - X - X)
t4.new_ab()
t4.out("F7")


# Bot 4th
# Pitching: TEX #58 Joe Ortiz
b4 = game.new_inning()

# Pitching change (TEX): #58 Joe Ortiz replaces #50 Michael Kirkman
b4.pitching_substitution(58)

# 7. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c t")
b4.hit(4)

# 8. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")

# 1. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 9. TEX #2  Leonys Martin (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")

# 1. TEX #1  Elvis Andrus (X - X - 2)
t5.new_ab()
t5.pitch_list("c d f b f s")
t5.out("K")

# 2. TEX #7  David Murphy (X - X - 2)
t5.new_ab()
t5.pitch_list("t")
t5.out("P5")

# 3. TEX #27 Lance Berkman (X - X - 2)
t5.new_ab()
t5.out("G3")


# Bot 5th
# Pitching: TEX #58 Joe Ortiz
b5 = game.new_inning()

# 2. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.out("G5-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b b f b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 4. TEX #17 Nelson Cruz (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(4)

# 5. TEX #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("f b f c")
t6.out("!K")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c")
t6.out("F8")

# 7. TEX #15 Jeff Baker (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")


# Bot 6th
# Pitching: TEX #58 Joe Ortiz
b6 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.hit(4)

# 7. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(3, "10 E5")
b6.advance("U", "44 G3")

# 8. BOS #10 Jose Iglesias (X - X - 7)
b6.new_ab()
b6.pitch_list("c b s")
b6.error(5)
b6.reach("E5", end_base=2)
b6.advance(3, "44 G3")
b6.advance("U", "29 SF9")

# 9. BOS #44 Jackie Bradley Jr. (7 - 10 - X)
b6.new_ab()
b6.pitch_list("b b f s f b")
b6.out("G3", rbis=1)

# 1. BOS #29 Daniel Nava (10 - X - X)
b6.new_ab()
b6.pitch_list("d s b f")
b6.error(9)
b6.reach("SF9", rbis=1)
b6.advance(3, "E9")
b6.advance("U", "37 SF8")

# Pitching change (TEX): #44 Jason Frasor replaces #58 Joe Ortiz
b6.pitching_substitution(44)

# 2. BOS #37 Mike Carp (29 - X - X)
b6.new_ab()
b6.pitch_list("f s f b b f b")
b6.out("SF8", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# 8. TEX #13 Jurickson Profar (X - X - X)
t7.new_ab()
t7.pitch_list("f f b b b")
t7.out("G4-3")

# 9. TEX #2  Leonys Martin (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3-1")

# Offensive change (TEX): Pinch-hitter #3 Leury García replaces #1 Elvis Andrus, batting 1st
t7.offensive_substitution(1, 3, "PH")

# 1. TEX #3  Leury García (X - X - X)
t7.new_ab()
t7.pitch_list("b c s b")
t7.out("G4-3")


# Bot 7th
# Pitching: TEX #55 Ross Wolf
b7 = game.new_inning()

# Pitching change (TEX): #55 Ross Wolf replaces #44 Jason Frasor
b7.pitching_substitution(55)

# Defensive switch (TEX): #3 Leury García moves to SS
b7.defensive_switch(3, "6")

# Defensive change (TEX): #23 Craig Gentry replaces #17 Nelson Cruz (RF), playing CF, batting 4th
b7.defensive_substitution(4, 23, "8")

# Defensive switch (TEX): #2 Leonys Martin moves to RF
b7.defensive_switch(2, "9")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.out("G3-1")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("P3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(1)
b7.advance(3, "7 2B")
b7.advance(4, "10 1B")

# 7. BOS #7  Stephen Drew (X - X - 39)
b7.new_ab()
b7.pitch_list("c b b s")
b7.hit(2)
b7.advance(4, "10 1B")

# 8. BOS #10 Jose Iglesias (39 - 7 - X)
b7.new_ab()
b7.hit(1, rbis=2)

# 9. BOS #44 Jackie Bradley Jr. (X - X - 10)
b7.new_ab()
b7.pitch_list("c f b")
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #59 Clayton Mortensen
t8 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #46 Ryan Dempster
t8.pitching_substitution(59)

# Defensive change (BOS): #23 Pedro Ciriaco replaces #15 Dustin Pedroia (2B), playing 3B, batting 3rd
t8.defensive_substitution(3, 23, "5")

# Defensive switch (BOS): #10 Jose Iglesias moves to 2B
t8.defensive_switch(10, "4")

# 2. TEX #7  David Murphy (X - X - X)
t8.new_ab()
t8.pitch_list("f f b s")
t8.out("K")

# 3. TEX #27 Lance Berkman (X - X - X)
t8.new_ab()
t8.pitch_list("b b f s s")
t8.out("K")

# 4. TEX #23 Craig Gentry (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1)
t8.advance(4, "18 HR")

# 5. TEX #18 Mitch Moreland (X - X - 23)
t8.new_ab()
t8.hit(4, rbis=2)

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t8.new_ab()
t8.pitch_list("b b f f b f f")
t8.hit(1)
t8.advance(2, "15 1B")
t8.advance(3, "13 BB")

# 7. TEX #15 Jeff Baker (X - X - 12)
t8.new_ab()
t8.pitch_list("s c b")
t8.hit(1)
t8.advance(2, "13 BB")

# 8. TEX #13 Jurickson Profar (X - 12 - 15)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.thrown_out(2, "2 FC6-4", 3, 30)

# Pitching change (BOS): #30 Andrew Miller replaces #59 Clayton Mortensen
t8.pitching_substitution(30)

# 9. TEX #2  Leonys Martin (12 - 15 - 13)
t8.new_ab()
t8.reach("FC6-4")


# Bot 8th
# Pitching: TEX #7  David Murphy
b8 = game.new_inning()

# Pitching change (TEX): #7  David Murphy replaces #55 Ross Wolf, batting 2nd
b8.pitching_substitution(7)
b8.defensive_substitution(2, 7, "1")

# Defensive change (TEX): #8 Geovany Soto replaces #27 Lance Berkman (DH), playing 3B, batting 3rd
b8.defensive_substitution(3, 8, "5")

# Defensive switch (TEX): #15 Jeff Baker moves to LF
b8.defensive_switch(15, "7")

# 1. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f b f b f")
b8.hit(2)

# 2. BOS #37 Mike Carp (X - 29 - X)
b8.new_ab()
b8.pitch_list("c b f c")
b8.out("!K")

# 3. BOS #23 Pedro Ciriaco (X - 29 - X)
b8.new_ab()
b8.pitch_list("b f b b")
b8.out("L7")

# 4. BOS #34 David Ortiz (X - 29 - X)
b8.new_ab()
b8.pitch_list("d")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #30 Andrew Miller
t9 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #37 Mike Carp (LF), playing LF, batting 2nd
t9.defensive_substitution(2, 5, "7")

# 1. TEX #3  Leury García (X - X - X)
t9.new_ab()
t9.pitch_list("f f f c")
t9.out("!K")

# 2. TEX #7  David Murphy (X - X - X)
t9.new_ab()
t9.pitch_list("s")
t9.out("F8")

# 3. TEX #8  Geovany Soto (X - X - X)
t9.new_ab()
t9.pitch_list("b b s s c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)

# Loser team: TEX
# LP: TEX #51 Justin Grimm
game.losing_pitcher(51, is_away_team=True)

# print(game)
game.generate_scorecard()
