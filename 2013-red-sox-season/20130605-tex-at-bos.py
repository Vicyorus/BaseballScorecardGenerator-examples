import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2013-06-05
# https://www.baseball-reference.com/boxes/BOS/BOS201306050.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2013/06/05/347631/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-05 19:11-22:28",
        "at": "Fenway Park, Boston, MA",
        "att": "33,296",
        "temp": "70F, Cloudy",
        "wind": "13mph, Out To LF",
        "away": {
            "team": "Texas Rangers",
            "starter": 41,
            "roster": {
                # Lineup
                1: "Elvis Andrus",
                7: "David Murphy",
                27: "Lance Berkman",
                29: "Adrian Beltré",
                17: "Nelson Cruz",
                12: "A.J. Pierzynski",
                18: "Mitch Moreland",
                13: "Jurickson Profar",
                2: "Leonys Martin",
                # Starting pitcher
                41: "Alexi Ogando",
                # Bench
                3: "Leury García",
                8: "Geovany Soto",
                15: "Jeff Baker",
                23: "Craig Gentry",
                # Bullpen
                50: "Michael Kirkman",
                44: "Jason Frasor",
                49: "Nick Tepesch",
                56: "Neal Cotts",
                45: "Derek Holland",
                11: "Yu Darvish",
                52: "Tanner Scheppers",
                51: "Justin Grimm",
                46: "Robbie Ross Jr.",
                36: "Joe Nathan",
                55: "Ross Wolf",
            },
            "lefties": [50, 56, 45, 46],
            "lineup": [
                [1, "6"],
                [7, "7"],
                [27, "0"],
                [29, "5"],
                [17, "9"],
                [12, "2"],
                [18, "3"],
                [13, "4"],
                [2, "8"],
            ],
            "bench": [
                [3, "OF"],
                [8, "C"],
                [15, "2B"],
                [23, "CF"],
            ],
            "bullpen": [50, 44, 49, 56, 45, 11, 52, 51, 46, 36, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
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
                41: "John Lackey",
                # Bench
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
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
            "bullpen": [40, 56, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Rob Drake",
            "1B": "Joe West",
            "2B": "Sam Holbrook",
            "3B": "Andy Fletcher",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f")
t1.out("G4-3")

# 2. TEX #7  David Murphy (X - X - X)
t1.new_ab()
t1.pitch_list("c c f c")
t1.out("!K")

# 3. TEX #27 Lance Berkman (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c c f")
t1.out("G5-3")


# Bot 1st
# Pitching: TEX #41 Alexi Ogando
b1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b f")
b1.out("G6-3")

# 2. BOS #37 Mike Carp (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K2-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b f c")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. TEX #29 Adrian Beltré (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F8")

# 5. TEX #17 Nelson Cruz (X - X - X)
t2.new_ab()
t2.pitch_list("s b f s")
t2.out("K")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t2.new_ab()
t2.pitch_list("b b f f f")
t2.out("G3-1")


# Bot 2nd
# Pitching: TEX #41 Alexi Ogando
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b c f b b b")
b2.reach("BB")
b2.thrown_out(2, "39 DP4-6-3", 2, 41)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b2.new_ab()
b2.pitch_list("c t f")
b2.out("DP4-6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 7. TEX #18 Mitch Moreland (X - X - X)
t3.new_ab()
t3.pitch_list("c l f b b f b f f f")
t3.hit(2)
t3.advance(3, "13 G3")

# 8. TEX #13 Jurickson Profar (X - 18 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.out("G3")

# 9. TEX #2  Leonys Martin (18 - X - X)
t3.new_ab(is_risp=True)
t3.out("G1-3")

# 1. TEX #1  Elvis Andrus (18 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b s f f b")
t3.out("F9")


# Bot 3rd
# Pitching: TEX #41 Alexi Ogando
b3 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b c b s")
b3.hit(1)
b3.thrown_out(2, "7-4", 1, 41)

# 8. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("L7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 2. TEX #7  David Murphy (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f f f b f")
t4.out("F8")

# 3. TEX #27 Lance Berkman (X - X - X)
t4.new_ab()
t4.pitch_list("f b b b f f c")
t4.out("!K")

# 4. TEX #29 Adrian Beltré (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.hit(4)

# 5. TEX #17 Nelson Cruz (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(2)

# 6. TEX #12 A.J. Pierzynski (X - 17 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f c b c")
t4.out("!K")


# Bot 4th
# Pitching: TEX #41 Alexi Ogando
b4 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b c")
b4.out("!K")

# 2. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(2)
b4.advance(3, "12 WP")

# 3. BOS #15 Dustin Pedroia (X - 37 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b d c b f d")
b4.reach("BB")
b4.advance(2, "12 WP")

# 4. BOS #34 David Ortiz (X - 37 - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("b d c f b s")
b4.out("K")

# 5. BOS #12 Mike Napoli (X - 37 - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b c f b f c")
b4.wp()
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 7. TEX #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("c c f")
t5.out("G4-3")

# 8. TEX #13 Jurickson Profar (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.advance(2, "1 1B")

# 9. TEX #2  Leonys Martin (X - X - 13)
t5.new_ab()
t5.pitch_list("1 b c s f s")
t5.out("K")

# 1. TEX #1  Elvis Andrus (X - X - 13)
t5.new_ab()
t5.pitch_list("f b")
t5.hit(1)

# 2. TEX #7  David Murphy (X - 13 - 1)
t5.new_ab(is_risp=True)
t5.pitch_list("b b b c f")
t5.out("G4-3")


# Bot 5th
# Pitching: TEX #41 Alexi Ogando
b5 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F8")

# 7. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c c f b c")
b5.out("!K")

# 8. BOS #10 Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 10)
b5.new_ab()
b5.pitch_list("1 f c 1 b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("F7")

# 4. TEX #29 Adrian Beltré (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F8")

# 5. TEX #17 Nelson Cruz (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.reach("HBP")
t6.advance(2, "12 SB")

# 6. TEX #12 A.J. Pierzynski (X - X - 17)
t6.new_ab(is_risp=True)
t6.pitch_list("s s b f")
t6.out("G4-3")


# Bot 6th
# Pitching: TEX #41 Alexi Ogando
b6 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.out("F9")

# 2. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("L8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.hit(4)

# Pitching change (TEX): #56 Neal Cotts replaces #41 Alexi Ogando
b6.pitching_substitution(56)

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("b b c b b")
b6.reach("BB")
b6.advance(2, "12 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
b6.new_ab()
b6.pitch_list("b b s b c f b")
b6.reach("BB")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b6.new_ab(is_risp=True)
b6.pitch_list("f f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #41 John Lackey
t7.pitching_substitution(32)

# 7. TEX #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(2)
# Offensive change (TEX): Pinch-runner #15 Jeff Baker replaces #18 Mitch Moreland
t7.offensive_substitution(7, 15, "PR")
t7.atbase("PR")
t7.advance(4, "1 2B")

# 8. TEX #13 Jurickson Profar (X - 18 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("l")
t7.out("B1-4")

# Offensive change (TEX): Pinch-hitter #23 Craig Gentry replaces #2 Leonys Martin, batting 9th
t7.offensive_substitution(9, 23, "PH")

# 9. TEX #23 Craig Gentry (X - 15 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("s f b b d b")
t7.reach("BB")
t7.advance(4, "1 2B")

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t7.pitching_substitution(19)

# 1. TEX #1  Elvis Andrus (X - 15 - 23)
t7.new_ab(is_risp=True)
t7.hit(2, rbis=2)

# 2. TEX #7  David Murphy (X - 1 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c s")
t7.out("F7")

# 3. TEX #27 Lance Berkman (X - 1 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b c b c f f s")
t7.out("K")


# Bot 7th
# Pitching: TEX #56 Neal Cotts
b7 = game.new_inning()

# Defensive switch (TEX): #15 Jeff Baker moves to 1B
b7.defensive_switch(15, "3")

# Defensive switch (TEX): #23 Craig Gentry moves to CF
b7.defensive_switch(23, "8")

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b f f b")
b7.reach("BB")
b7.advance(2, "10 1B")
b7.advance(3, "29 G1-3")

# Pitching change (TEX): #46 Robbie Ross Jr. replaces #56 Neal Cotts
b7.pitching_substitution(46)

# 8. BOS #10 Jose Iglesias (X - X - 7)
b7.new_ab()
b7.pitch_list("b c c f b f")
b7.hit(1)
b7.advance(2, "29 G1-3")

# 9. BOS #44 Jackie Bradley Jr. (X - 7 - 10)
b7.new_ab(is_risp=True)
b7.pitch_list("2 l c s")
b7.out("K")

# 1. BOS #29 Daniel Nava (X - 7 - 10)
b7.new_ab(is_risp=True)
b7.out("G1-3")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 2nd
b7.offensive_substitution(2, 5, "PH")

# 2. BOS #5  Jonny Gomes (7 - 10 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c s d")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
t8.pitching_substitution(36)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 4. TEX #29 Adrian Beltré (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 5. TEX #17 Nelson Cruz (X - X - X)
t8.new_ab()
t8.pitch_list("f c b b f s")
t8.out("K")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
t8.new_ab()
t8.out("F8")


# Bot 8th
# Pitching: TEX #52 Tanner Scheppers
b8 = game.new_inning()

# Pitching change (TEX): #52 Tanner Scheppers replaces #46 Robbie Ross Jr.
b8.pitching_substitution(52)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("L8")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b b c s")
b8.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(4, "39 2B")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b8.new_ab()
b8.pitch_list("b c s")
b8.hit(2, rbis=1)
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #39 Jarrod Saltalamacchia
b8.offensive_substitution(6, 23, "PR")
b8.atbase("PR")

# 7. BOS #7  Stephen Drew (X - 39 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
t9.pitching_substitution(40)

# Defensive change (BOS): #3 David Ross replaces #23 Pedro Ciriaco (PR), playing C, batting 6th
t9.defensive_substitution(6, 3, "2")

# 7. TEX #15 Jeff Baker (X - X - X)
t9.new_ab()
t9.pitch_list("s b f b b")
t9.out("L7")

# 8. TEX #13 Jurickson Profar (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.out("F9")

# 9. TEX #23 Craig Gentry (X - X - X)
t9.new_ab()
t9.pitch_list("b f c b f b b")
t9.reach("BB")
t9.thrown_out(2, "1 CS", 3, 40)

# 1. TEX #1  Elvis Andrus (X - X - 23)
t9.new_ab()
t9.pitch_list("1 b")
t9.no_ab("CS")


# Bot 9th
# Pitching: TEX #36 Joe Nathan
b9 = game.new_inning()

# Pitching change (TEX): #36 Joe Nathan replaces #52 Tanner Scheppers
b9.pitching_substitution(36)

# 8. BOS #10 Jose Iglesias (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G1-3")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G6-3")

# 1. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.out("G4-3")

# Winning team: TEX
# WP: TEX #56 Neal Cotts
game.winning_pitcher(56, is_away_team=True)
# SV: TEX #36 Joe Nathan
game.save_pitcher(36, is_away_team=True)

# Loser team: BOS
# LP: BOS #32 Craig Breslow
game.losing_pitcher(32)

# print(game)
game.generate_scorecard()
