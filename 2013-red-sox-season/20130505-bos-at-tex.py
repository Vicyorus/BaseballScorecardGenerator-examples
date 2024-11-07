import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2013-05-05
# https://www.baseball-reference.com/boxes/TEX/TEX201305050.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2013/05/05/347204/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-05 15:08-18:43",
        "at": "Rangers Ballpark in Arlington, Arlington, TX",
        "att": "46,228",
        "temp": "63F, Sunny",
        "wind": "8mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                3: "David Ross",
                7: "Stephen Drew",
                23: "Pedro Ciriaco",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                5: "Jonny Gomes",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [3, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [39, "C"],
                [16, "3B"],
                [18, "CF"],
                [5, "LF"],
            ],
            "bullpen": [63, 41, 30, 19, 52, 59, 36, 22, 46, 11],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 11,
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
                11: "Yu Darvish",
                # Bench
                7: "David Murphy",
                3: "Leury García",
                2: "Leonys Martin",
                8: "Geovany Soto",
                # Bullpen
                50: "Michael Kirkman",
                44: "Jason Frasor",
                49: "Nick Tepesch",
                45: "Derek Holland",
                41: "Alexi Ogando",
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
            "bullpen": [50, 44, 49, 45, 41, 52, 51, 46, 36, 58, 55],
        },
        "umpires": {
            "HP": "Brian Knight",
            "1B": "Dan Iassogna",
            "2B": "Mark Carlson",
            "3B": "Gerry Davis",
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
# Pitching: TEX #11 Yu Darvish
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f f f s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b c c b")
t1.hit(1)
t1.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("b b b c")
t1.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
t1.new_ab()
t1.pitch_list("b c f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TEX #5  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G6-3")

# 2. TEX #1  Elvis Andrus (X - X - X)
b1.new_ab()
b1.pitch_list("b c c")
b1.out("G5-3")

# 3. TEX #27 Lance Berkman (X - X - X)
b1.new_ab()
b1.pitch_list("f b s f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #11 Yu Darvish
t2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c b f s")
t2.out("K")

# 7. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(4)

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c c b s")
t2.out("K")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t2.new_ab()
t2.pitch_list("b s")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. TEX #29 Adrian Beltré (X - X - X)
b2.new_ab()
b2.pitch_list("c b s")
b2.out("G5-3")

# 5. TEX #17 Nelson Cruz (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 6. TEX #12 A.J. Pierzynski (X - X - X)
b2.new_ab()
b2.pitch_list("f b f b b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #11 Yu Darvish
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("G6-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c c b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 7. TEX #15 Jeff Baker (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G1-3")

# 8. TEX #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("c s")
b3.hit(4)

# 9. TEX #23 Craig Gentry (X - X - X)
b3.new_ab()
b3.pitch_list("b b c s")
b3.out("G4-3")

# 1. TEX #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #11 Yu Darvish
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f f")
t4.out("G1-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c s b f b b b")
t4.reach("BB")

# 6. BOS #37 Mike Carp (X - X - 12)
t4.new_ab()
t4.pitch_list("f d b c c")
t4.out("!K")

# 7. BOS #3  David Ross (X - X - 12)
t4.new_ab()
t4.pitch_list("c s s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 2. TEX #1  Elvis Andrus (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G5-3")

# 3. TEX #27 Lance Berkman (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.hit(2)

# 4. TEX #29 Adrian Beltré (X - 27 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.out("F8")

# 5. TEX #17 Nelson Cruz (X - 27 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b b")
b4.reach("BB")

# 6. TEX #12 A.J. Pierzynski (X - 27 - 17)
b4.new_ab(is_risp=True)
b4.pitch_list("b b s b s c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #11 Yu Darvish
t5 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b c c s")
t5.out("K2-3")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.hit(1)
t5.advance(2, "29 SB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
t5.new_ab()
t5.pitch_list("b 1 f 1 b f")
t5.out("F9")

# 2. BOS #29 Daniel Nava (X - X - 23)
t5.new_ab(is_risp=True)
t5.pitch_list("b f 1 b s f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 7. TEX #15 Jeff Baker (X - X - X)
b5.new_ab()
b5.pitch_list("c b s b f b b")
b5.reach("BB")
b5.advance(2, "5 1B")

# 8. TEX #18 Mitch Moreland (X - X - 15)
b5.new_ab()
b5.pitch_list("c b b f f")
b5.out("F7")

# 9. TEX #23 Craig Gentry (X - X - 15)
b5.new_ab()
b5.pitch_list("c b f f b c")
b5.out("!K")

# 1. TEX #5  Ian Kinsler (X - X - 15)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)

# 2. TEX #1  Elvis Andrus (X - 15 - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("c s b b b f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #11 Yu Darvish
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b c s f b b s")
t6.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b s s b s")
t6.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 3. TEX #27 Lance Berkman (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s f")
b6.out("G6-3")

# 4. TEX #29 Adrian Beltré (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(1)
b6.advance(4, "17 HR")

# 5. TEX #17 Nelson Cruz (X - X - 29)
b6.new_ab()
b6.pitch_list("c b t f b f b")
b6.hit(4, rbis=2)

# 6. TEX #12 A.J. Pierzynski (X - X - X)
b6.new_ab()
b6.pitch_list("f f b s")
b6.out("K")

# 7. TEX #15 Jeff Baker (X - X - X)
b6.new_ab()
b6.pitch_list("f s b b b b")
b6.reach("BB")
# Offensive change (TEX): Pinch-runner #7 David Murphy replaces #15 Jeff Baker
b6.offensive_substitution(7, 7, "PR")
b6.atbase("PR")

# 8. TEX #18 Mitch Moreland (X - X - 15)
b6.new_ab()
b6.pitch_list("f b d f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #11 Yu Darvish
t7 = game.new_inning()

# Defensive switch (TEX): #7 David Murphy moves to LF
t7.defensive_switch(7, "7")

# 6. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f b")
t7.out("G4-3")

# 7. BOS #3  David Ross (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(2, "23 SB")

# 8. BOS #7  Stephen Drew (X - X - 3)
t7.new_ab()
t7.pitch_list("b b f s f s")
t7.out("K")

# 9. BOS #23 Pedro Ciriaco (X - X - 3)
t7.new_ab(is_risp=True)
t7.pitch_list("s s d b b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #19 Koji Uehara
b7 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #31 Jon Lester
b7.pitching_substitution(19)

# 9. TEX #23 Craig Gentry (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.hit(1)
b7.advance(2, "5 SAC1-3")
b7.advance(3, "27 SB")

# 1. TEX #5  Ian Kinsler (X - X - 23)
b7.new_ab()
b7.pitch_list("1 c 1")
b7.out("SAC1-3")

# 2. TEX #1  Elvis Andrus (X - 23 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c s f b s")
b7.out("K")

# 3. TEX #27 Lance Berkman (X - 23 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b b i")
b7.reach("IBB")

# 4. TEX #29 Adrian Beltré (23 - X - 27)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #50 Michael Kirkman
t8 = game.new_inning()

# Pitching change (TEX): #50 Michael Kirkman replaces #11 Yu Darvish
t8.pitching_substitution(50)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b c f")
t8.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c c f b f b b s")
t8.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f f b b b")
t8.reach("BB")
t8.advance(2, "34 SB")

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab(is_risp=True)
t8.pitch_list("b 1 b s s 1 b b")
t8.reach("BB")
t8.thrown_out(2, "12 FC6-4", 3, 44)

# Pitching change (TEX): #44 Jason Frasor replaces #50 Michael Kirkman
t8.pitching_substitution(44)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("b c f b")
t8.reach("FC6-4")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
b8.pitching_substitution(36)

# 5. TEX #17 Nelson Cruz (X - X - X)
b8.new_ab()
b8.out("(F)P3")

# Pitching change (BOS): #30 Andrew Miller replaces #36 Junichi Tazawa
b8.pitching_substitution(30)

# 6. TEX #12 A.J. Pierzynski (X - X - X)
b8.new_ab()
b8.pitch_list("s s b f s")
b8.out("K")

# 7. TEX #7  David Murphy (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)

# 8. TEX #18 Mitch Moreland (X - X - 7)
b8.new_ab()
b8.pitch_list("b s c 1 d s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #36 Joe Nathan
t9 = game.new_inning()

# Pitching change (TEX): #36 Joe Nathan replaces #44 Jason Frasor
t9.pitching_substitution(36)

# 6. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("c c b")
t9.out("L9")

# 7. BOS #3  David Ross (X - X - X)
t9.new_ab()
t9.pitch_list("f b b s b b")
t9.reach("BB")
# Offensive change (BOS): Pinch-runner #18 Shane Victorino replaces #3 David Ross
t9.offensive_substitution(7, 18, "PR")
t9.atbase("PR")
t9.advance(2, "7 1B")

# 8. BOS #7  Stephen Drew (X - X - 3)
t9.new_ab()
t9.pitch_list("1 b f 1")
t9.hit(1)

# Offensive change (BOS): Pinch-hitter #39 Jarrod Saltalamacchia replaces #23 Pedro Ciriaco, batting 9th
t9.offensive_substitution(9, 39, "PH")

# 9. BOS #39 Jarrod Saltalamacchia (X - 18 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("f c b b s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 18 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("f b b c")
t9.out("G3-1")


# Bot 9th
# Pitching: BOS #59 Clayton Mortensen
b9 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #30 Andrew Miller
b9.pitching_substitution(59)

# Defensive switch (BOS): #29 Daniel Nava moves to LF
b9.defensive_switch(29, "7")

# Defensive change (BOS): #16 Will Middlebrooks replaces #37 Mike Carp (LF), playing 3B, batting 6th
b9.defensive_substitution(6, 16, "5")

# Defensive switch (BOS): #18 Shane Victorino moves to RF
b9.defensive_switch(18, "9")

# Defensive switch (BOS): #39 Jarrod Saltalamacchia moves to C
b9.defensive_switch(39, "2")

# Offensive change (TEX): Pinch-hitter #2 Leonys Martin replaces #23 Craig Gentry, batting 9th
b9.offensive_substitution(9, 2, "PH")

# 9. TEX #2  Leonys Martin (X - X - X)
b9.new_ab()
b9.pitch_list("c b f s")
b9.out("K")

# 1. TEX #5  Ian Kinsler (X - X - X)
b9.new_ab()
b9.pitch_list("c b s b f s")
b9.out("K")

# 2. TEX #1  Elvis Andrus (X - X - X)
b9.new_ab()
b9.hit(1)
b9.advance(2, "27 WP")
b9.advance(4, "29 1B")

# 3. TEX #27 Lance Berkman (X - X - 1)
b9.new_ab(is_risp=True)
b9.pitch_list("1 b b i i")
b9.wp()
b9.reach("IBB")
b9.advance(2, "29 1B")

# 4. TEX #29 Adrian Beltré (X - 1 - 27)
b9.new_ab(is_risp=True)
b9.pitch_list("c b s")
b9.hit(1, rbis=1)

# Winning team: TEX
# WP: TEX #36 Joe Nathan
game.winning_pitcher(36)

# Loser team: BOS
# LP: BOS #59 Clayton Mortensen
game.losing_pitcher(59, is_away_team=True)

# print(game)
game.generate_scorecard()
