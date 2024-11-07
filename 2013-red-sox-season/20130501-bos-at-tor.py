import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-05-01
# https://www.baseball-reference.com/boxes/TOR/TOR201305010.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/05/01/347160/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-01 19:07-21:59",
        "at": "Rogers Centre, Toronto, ON",
        "att": "21,094",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                18: "Shane Victorino",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [18, "CF"],
                [23, "3B"],
            ],
            "bullpen": [63, 41, 30, 19, 52, 31, 59, 36, 22, 46],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                13: "Brett Lawrie",
                28: "Colby Rasmus",
                19: "José Bautista",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                53: "Melky Cabrera",
                9: "J.P. Arencibia",
                3: "Maicer Izturis",
                66: "Munenori Kawasaki",
                # Starting pitcher
                56: "Mark Buehrle",
                # Bench
                1: "Emilio Bonifácio",
                22: "Henry Blanco",
                16: "Mark DeRosa",
                11: "Rajai Davis",
                # Bullpen
                23: "Brandon Morrow",
                43: "R.A. Dickey",
                52: "Justin Germano",
                62: "Aaron Loup",
                50: "Steve Delabar",
                27: "Brett Cecil",
                48: "J.A. Happ",
                44: "Casey Janssen",
                32: "Esmil Rogers",
                38: "Darren Oliver",
            },
            "lefties": [56, 62, 27, 48, 38],
            "lineup": [
                [13, "5"],
                [28, "8"],
                [19, "9"],
                [10, "3"],
                [26, "0"],
                [53, "7"],
                [9, "2"],
                [3, "4"],
                [66, "6"],
            ],
            "bench": [
                [1, "2B"],
                [22, "C"],
                [16, "3B"],
                [11, "CF"],
            ],
            "bullpen": [23, 43, 52, 62, 50, 27, 48, 44, 32, 38],
        },
        "umpires": {
            "HP": "Bruce Dreckman",
            "1B": "Gary Darling",
            "2B": "Paul Emmel",
            "3B": "Clint Fagan",
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
# Pitching: TOR #56 Mark Buehrle
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.error(1)
t1.advance(2, "15 POE1")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t1.new_ab()
t1.pitch_list("b c s 1 f")
t1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("b 1")
t1.out("F8")

# 4. BOS #34 David Ortiz (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c")
t1.out("F9")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. TOR #13 Brett Lawrie (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G4-3")

# 2. TOR #28 Colby Rasmus (X - X - X)
b1.new_ab()
b1.pitch_list("f f b b b b")
b1.reach("BB")

# 3. TOR #19 José Bautista (X - X - 28)
b1.new_ab()
b1.pitch_list("1 c b c b c")
b1.out("!K")

# 4. TOR #10 Edwin Encarnación (X - X - 28)
b1.new_ab()
b1.pitch_list("s")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #56 Mark Buehrle
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c c b")
t2.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b")
t2.out("F9")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b f f f")
t2.reach("HBP")
t2.advance(4, "7 HR")

# 8. BOS #7  Stephen Drew (X - X - 16)
t2.new_ab()
t2.pitch_list("b")
t2.hit(4, rbis=2)

# 9. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.out("G5-3")

# 6. TOR #53 Melky Cabrera (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G1-3")

# 7. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #56 Mark Buehrle
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("G1-4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.thrown_out(2, "15 FC5-4", 2, 56)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t3.new_ab()
t3.pitch_list("b 1 b b c f")
t3.reach("FC5-4")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 8. TOR #3  Maicer Izturis (X - X - X)
b3.new_ab()
b3.pitch_list("b c f b f b f s")
b3.out("K")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b3.new_ab()
b3.pitch_list("l b l b b")
b3.hit(1)

# 1. TOR #13 Brett Lawrie (X - X - 66)
b3.new_ab()
b3.pitch_list("1 1 b c 1 d c f c")
b3.out("!K")

# 2. TOR #28 Colby Rasmus (X - X - 66)
b3.new_ab()
b3.pitch_list("s s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #56 Mark Buehrle
t4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.hit(4)

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(4)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c")
t4.hit(1)
t4.thrown_out(2, "7 DP4-6-3", 1, 56)

# 8. BOS #7  Stephen Drew (X - X - 16)
t4.new_ab()
t4.pitch_list("c s")
t4.out("DP4-6-3")

# 9. BOS #3  David Ross (X - X - X)
t4.new_ab()
t4.pitch_list("f c b")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 3. TOR #19 José Bautista (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b b")
b4.reach("BB")

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b4.new_ab()
b4.pitch_list("b c d 1 b c s")
b4.out("K")

# 5. TOR #26 Adam Lind (X - X - 19)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("F8")

# 6. TOR #53 Melky Cabrera (X - X - 19)
b4.new_ab()
b4.pitch_list("f f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #56 Mark Buehrle
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")

# 2. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c s b")
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.out("(F)P5")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 7. TOR #9  J.P. Arencibia (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 8. TOR #3  Maicer Izturis (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G4-3")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b5.new_ab()
b5.pitch_list("c c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #56 Mark Buehrle
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("f b")
t6.hit(2)
t6.advance(3, "16 1B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b c b b b")
t6.reach("BB")
t6.advance(2, "16 1B")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t6.new_ab(is_risp=True)
t6.pitch_list("c f")
t6.out("F8")

# 7. BOS #16 Will Middlebrooks (X - 34 - 12)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "7 DP4-6-3", 2, 56)

# 8. BOS #7  Stephen Drew (34 - 12 - 16)
t6.new_ab(is_risp=True)
t6.pitch_list("b f b b")
t6.out("DP4-6-3")


# Bot 6th
# Pitching: BOS #11 Clay Buchholz
b6 = game.new_inning()

# 1. TOR #13 Brett Lawrie (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f f")
b6.out("G4-3")

# 2. TOR #28 Colby Rasmus (X - X - X)
b6.new_ab()
b6.out("(F)P5")

# 3. TOR #19 José Bautista (X - X - X)
b6.new_ab()
b6.pitch_list("c c b b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #56 Mark Buehrle
t7 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
t7.new_ab()
t7.pitch_list("b s s")
t7.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.out("L8")

# 2. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(3, "15 1B")
t7.advance(4, "34 WP")

# Pitching change (TOR): #32 Esmil Rogers replaces #56 Mark Buehrle
t7.pitching_substitution(32)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t7.new_ab()
t7.pitch_list("b f c d b f")
t7.hit(1)
t7.advance(2, "34 WP")
t7.advance(4, "12 HR")

# 4. BOS #34 David Ortiz (5 - X - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("b i i i")
t7.wp()
t7.reach("IBB")
t7.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t7.new_ab(is_risp=True)
t7.pitch_list("b b d")
t7.hit(4, rbis=3)

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("L4")


# Bot 7th
# Pitching: BOS #11 Clay Buchholz
b7 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F8")

# 5. TOR #26 Adam Lind (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c b f b")
b7.reach("BB")
b7.advance(3, "53 1B")

# 6. TOR #53 Melky Cabrera (X - X - 26)
b7.new_ab()
b7.hit(1)
b7.thrown_out(2, "9-6", 2, 11)

# 7. TOR #9  J.P. Arencibia (26 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #52 Justin Germano
t8 = game.new_inning()

# Pitching change (TOR): #52 Justin Germano replaces #32 Esmil Rogers
t8.pitching_substitution(52)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(3, "3 2B")

# 9. BOS #3  David Ross (X - X - 7)
t8.new_ab()
t8.pitch_list("c s")
t8.hit(2)

# 1. BOS #2  Jacoby Ellsbury (7 - 3 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b f")
t8.out("G4-3")

# 2. BOS #5  Jonny Gomes (7 - 3 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.out("G4-3")


# Bot 8th
# Pitching: BOS #63 Alex Wilson
b8 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #11 Clay Buchholz
b8.pitching_substitution(63)

# 8. TOR #3  Maicer Izturis (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f f")
b8.hit(1)
b8.advance(4, "13 3B")

# 9. TOR #66 Munenori Kawasaki (X - X - 3)
b8.new_ab()
b8.pitch_list("c b f b s")
b8.out("K")

# 1. TOR #13 Brett Lawrie (X - X - 3)
b8.new_ab()
b8.pitch_list("c c d b d")
b8.hit(3, rbis=1)

# 2. TOR #28 Colby Rasmus (13 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c t")
b8.out("KT")

# 3. TOR #19 José Bautista (13 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b c f b")
b8.reach("BB")

# Pitching change (BOS): #59 Clayton Mortensen replaces #63 Alex Wilson
b8.pitching_substitution(59)

# 4. TOR #10 Edwin Encarnación (13 - X - 19)
b8.new_ab(is_risp=True)
b8.pitch_list("c d b f d")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #52 Justin Germano
t9 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("G6-3")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #34 David Ortiz, batting 4th
t9.offensive_substitution(4, 37, "PH")

# 4. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(2)
t9.advance(4, "29 1B")

# 6. BOS #29 Daniel Nava (X - 12 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c s b f f")
t9.hit(1, rbis=1)
t9.advance(2, "7 1B")

# 7. BOS #16 Will Middlebrooks (X - X - 29)
t9.new_ab()
t9.pitch_list("c")
t9.out("P4")

# 8. BOS #7  Stephen Drew (X - X - 29)
t9.new_ab()
t9.hit(1)

# 9. BOS #3  David Ross (X - 29 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("P4")


# Bot 9th
# Pitching: BOS #59 Clayton Mortensen
b9 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #59 Clayton Mortensen, batting 5th
b9.pitching_substitution(59)
b9.defensive_substitution(5, 59, "1")

# Defensive switch (BOS): #37 Mike Carp moves to 1B
b9.defensive_switch(37, "3")

# 5. TOR #26 Adam Lind (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.thrown_out(2, "16 DP5-4-3", 1, 59)

# Offensive change (TOR): Pinch-hitter #16 Mark DeRosa replaces #53 Melky Cabrera, batting 6th
b9.offensive_substitution(6, 16, "PH")

# 6. TOR #16 Mark DeRosa (X - X - 26)
b9.new_ab()
b9.pitch_list("s b b f")
b9.out("DP5-4-3")

# Offensive change (TOR): Pinch-hitter #22 Henry Blanco replaces #9 J.P. Arencibia, batting 7th
b9.offensive_substitution(7, 22, "PH")

# 7. TOR #22 Henry Blanco (X - X - X)
b9.new_ab()
b9.pitch_list("b f b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)

# Loser team: TOR
# LP: TOR #56 Mark Buehrle
game.losing_pitcher(56)

# print(game)
game.generate_scorecard()
