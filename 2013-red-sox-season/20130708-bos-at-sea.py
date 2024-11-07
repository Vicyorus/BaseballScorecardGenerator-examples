import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SEA, 2013-07-08
# https://www.baseball-reference.com/boxes/SEA/SEA201307080.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2013/07/08/348082/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-08 22:10-01:31 +1",
        "at": "Safeco Field, Seattle, WA",
        "att": "21,830",
        "temp": "76F, Clear",
        "wind": "3mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                26: "Brock Holt",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                40: "Andrew Bailey",
                41: "John Lackey",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 32, 22],
            "lineup": [
                [29, "8"],
                [5, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [10, "6"],
                [26, "5"],
            ],
            "bench": [
                [2, "CF"],
                [18, "CF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [63, 65, 40, 41, 32, 91, 36, 64, 19, 22, 46],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 34,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                28: "Raul Ibanez",
                8: "Kendrys Morales",
                15: "Kyle Seager",
                12: "Jason Bay",
                17: "Justin Smoak",
                3: "Mike Zunino",
                55: "Michael Saunders",
                # Starting pitcher
                34: "Félix Hernández",
                # Bench
                26: "Brendan Ryan",
                9: "Endy Chavez",
                13: "Dustin Ackley",
                33: "Henry Blanco",
                # Bullpen
                44: "Lucas Luetge",
                39: "Aaron Harang",
                40: "Danny Farquhar",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                49: "Blake Beavan",
                58: "Carter Capps",
                31: "Yoervis Medina",
                54: "Tom Wilhelmsen",
                23: "Joe Saunders",
                18: "Hisashi Iwakuma",
            },
            "lefties": [44, 41, 59, 23],
            "lineup": [
                [5, "6"],
                [6, "4"],
                [28, "7"],
                [8, "0"],
                [15, "5"],
                [12, "9"],
                [17, "3"],
                [3, "2"],
                [55, "8"],
            ],
            "bench": [
                [26, "SS"],
                [9, "CF"],
                [13, "2B"],
                [33, "C"],
            ],
            "bullpen": [44, 39, 40, 41, 59, 49, 58, 31, 54, 23, 18],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Jim Joyce",
            "2B": "Cory Blaser",
            "3B": "Jeff Nelson",
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
# Pitching: SEA #34 Félix Hernández
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("F7")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b f")
t1.hit(1)
t1.thrown_out(2, "15 DP6-4-3", 2, 34)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t1.new_ab()
t1.pitch_list("c")
t1.out("DP6-4-3")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b1.new_ab()
b1.pitch_list("f b c b c")
b1.out("!K")

# 2. SEA #6  Nick Franklin (X - X - X)
b1.new_ab()
b1.pitch_list("b f b s")
b1.out("G6-3")

# 3. SEA #28 Raul Ibanez (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #34 Félix Hernández
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.hit(1)
t2.advance(2, "37 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("c b s c")
t2.out("!K")

# 6. BOS #37 Mike Carp (X - X - 34)
t2.new_ab()
t2.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (X - 34 - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b b c")
t2.out("L7")

# 8. BOS #10 Jose Iglesias (X - 34 - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("b f c s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b2.new_ab()
b2.pitch_list("b c b c f")
b2.hit(2)

# 5. SEA #15 Kyle Seager (X - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("L8")

# 6. SEA #12 Jason Bay (X - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("F7")

# 7. SEA #17 Justin Smoak (X - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b")
b2.out("P6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #34 Félix Hernández
t3 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "29 G4-3")

# 1. BOS #29 Daniel Nava (X - X - 26)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - 26 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("d c b c f b f")
t3.out("L8")

# 3. BOS #15 Dustin Pedroia (X - 26 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 8. SEA #3  Mike Zunino (X - X - X)
b3.new_ab()
b3.pitch_list("f c b f b b")
b3.hit(1)
b3.advance(2, "5 1B")

# 9. SEA #55 Michael Saunders (X - X - 3)
b3.new_ab()
b3.pitch_list("b b c s f f c")
b3.out("!K")

# 1. SEA #5  Brad Miller (X - X - 3)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 2. SEA #6  Nick Franklin (X - 3 - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("s s f s")
b3.out("K")

# 3. SEA #28 Raul Ibanez (X - 3 - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("f b b d f")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #34 Félix Hernández
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b b b")
t4.hit(1)

# 5. BOS #12 Mike Napoli (X - X - 34)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")

# 6. BOS #37 Mike Carp (X - X - 34)
t4.new_ab()
t4.pitch_list("c d f c")
t4.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 34)
t4.new_ab()
t4.pitch_list("s s d d b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b4.new_ab()
b4.pitch_list("c f f")
b4.hit(1)
b4.advance(3, "15 1B")
b4.advance(4, "17 2B")

# 5. SEA #15 Kyle Seager (X - X - 8)
b4.new_ab()
b4.hit(1)
b4.advance(3, "17 2B")
b4.advance(4, "55 BB")

# 6. SEA #12 Jason Bay (8 - X - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("b b s f c")
b4.out("!K")

# 7. SEA #17 Justin Smoak (8 - X - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("b f f")
b4.hit(2, rbis=1)
b4.advance(3, "55 BB")

# 8. SEA #3  Mike Zunino (15 - 17 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b b f f d")
b4.reach("BB")
b4.advance(2, "55 BB")

# 9. SEA #55 Michael Saunders (15 - 17 - 3)
b4.new_ab(is_risp=True)
b4.pitch_list("b b s b b")
b4.reach("BB", rbis=1)

# 1. SEA #5  Brad Miller (17 - 3 - 55)
b4.new_ab(is_risp=True)
b4.pitch_list("d f")
b4.out("IF5")

# 2. SEA #6  Nick Franklin (17 - 3 - 55)
b4.new_ab(is_risp=True)
b4.pitch_list("b c c f f b f f b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #34 Félix Hernández
t5 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.reach("HBP")
t5.advance(3, "26 1B")
t5.advance(4, "29 1B")

# 9. BOS #26 Brock Holt (X - X - 10)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(3, "29 1B")
t5.advance(4, "5 WP")

# 1. BOS #29 Daniel Nava (10 - X - 26)
t5.new_ab(is_risp=True)
t5.hit(1, rbis=1)
t5.advance(2, "5 WP")
t5.advance(3, "15 G6-3")

# 2. BOS #5  Jonny Gomes (26 - X - 29)
t5.new_ab(is_risp=True)
t5.pitch_list("b f c s")
t5.wp()
t5.out("K")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f f")
t5.out("G6-3")

# 4. BOS #34 David Ortiz (29 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b b b")
t5.reach("BB")

# 5. BOS #12 Mike Napoli (29 - X - 34)
t5.new_ab(is_risp=True)
t5.pitch_list("s s s")
t5.out("K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 3. SEA #28 Raul Ibanez (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.hit(4)

# 4. SEA #8  Kendrys Morales (X - X - X)
b5.new_ab()
b5.out("F8")

# 5. SEA #15 Kyle Seager (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# 6. SEA #12 Jason Bay (X - X - X)
b5.new_ab()
b5.pitch_list("f f b f f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #34 Félix Hernández
t6 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("L8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b")
t6.out("F7")

# 8. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F9")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 7. SEA #17 Justin Smoak (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.hit(1)
b6.advance(2, "3 1B")
b6.advance(4, "55 2B")

# 8. SEA #3  Mike Zunino (X - X - 17)
b6.new_ab()
b6.pitch_list("c b b f")
b6.hit(1)
b6.error(8)
b6.advance(3, "55 2B")
b6.advance(4, "55 E8")

# Pitching change (BOS): #63 Alex Wilson replaces #31 Jon Lester
b6.pitching_substitution(63)

# 9. SEA #55 Michael Saunders (X - 17 - 3)
b6.new_ab(is_risp=True)
b6.pitch_list("b b")
b6.hit(2, rbis=1)
b6.advance(3, "5 G5-3")
b6.advance(4, "28 1B")

# 1. SEA #5  Brad Miller (X - 55 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c")
b6.out("G5-3")

# 2. SEA #6  Nick Franklin (55 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s s t")
b6.out("KT")

# 3. SEA #28 Raul Ibanez (55 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.hit(1, rbis=1)

# 4. SEA #8  Kendrys Morales (X - X - 28)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #34 Félix Hernández
t7 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G6-3")

# 1. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")

# 2. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #63 Alex Wilson
b7 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "17 WP")
b7.advance(4, "17 2B")

# 6. SEA #12 Jason Bay (X - X - 15)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("P4")

# 7. SEA #17 Justin Smoak (X - X - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("f b")
b7.wp()
b7.hit(2, rbis=1)
b7.advance(4, "55 2B")

# Pitching change (BOS): #65 Jose De La Torre replaces #63 Alex Wilson
b7.pitching_substitution(65)

# 8. SEA #3  Mike Zunino (X - 17 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b s f s")
b7.out("K")

# 9. SEA #55 Michael Saunders (X - 17 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c s f d f d f")
b7.hit(2, rbis=1)
b7.advance(4, "5 1B")

# 1. SEA #5  Brad Miller (X - 55 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b s")
b7.hit(1, rbis=1)
b7.advance(4, "6 2B")

# 2. SEA #6  Nick Franklin (X - X - 5)
b7.new_ab()
b7.pitch_list("c d")
b7.hit(2, rbis=1)

# 3. SEA #28 Raul Ibanez (X - 6 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #59 Oliver Pérez
t8 = game.new_inning()

# Pitching change (SEA): #59 Oliver Pérez replaces #34 Félix Hernández
t8.pitching_substitution(59)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
# Offensive change (BOS): Pinch-runner #23 Brandon Snyder replaces #15 Dustin Pedroia
t8.offensive_substitution(3, 23, "PR")
t8.atbase("PR")
t8.advance(4, "12 2B")

# Offensive change (BOS): Pinch-hitter #20 Ryan Lavarnway replaces #34 David Ortiz, batting 4th
t8.offensive_substitution(4, 20, "PH")

# 4. BOS #20 Ryan Lavarnway (X - X - 15)
t8.new_ab()
t8.pitch_list("b f")
t8.out("F7")

# 5. BOS #12 Mike Napoli (X - X - 23)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(2, rbis=1)
t8.advance(3, "37 G4-3")
t8.advance(4, "39 2B")

# 6. BOS #37 Mike Carp (X - 12 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (12 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c s")
t8.hit(2, rbis=1)

# 8. BOS #10 Jose Iglesias (X - 39 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b s b")
t8.out("P3")


# Bot 8th
# Pitching: BOS #65 Jose De La Torre
b8 = game.new_inning()

# Defensive switch (BOS): #23 Brandon Snyder moves to 3B
b8.defensive_switch(23, "5")

# Defensive switch (BOS): #20 Ryan Lavarnway moves to DH
b8.defensive_switch(20, "0")

# Defensive switch (BOS): #26 Brock Holt moves to 2B
b8.defensive_switch(26, "4")

# 4. SEA #8  Kendrys Morales (X - X - X)
b8.new_ab()
b8.reach("HBP")
b8.advance(2, "15 BB")
b8.advance(3, "17 BB")
b8.advance(4, "3 G3-4")

# 5. SEA #15 Kyle Seager (X - X - 8)
b8.new_ab()
b8.pitch_list("b b b c d")
b8.reach("BB")
b8.advance(2, "17 BB")
b8.advance(3, "3 G3-4")

# 6. SEA #12 Jason Bay (X - 8 - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("c s s")
b8.out("K")

# 7. SEA #17 Justin Smoak (X - 8 - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("b d b c b")
b8.reach("BB")
b8.advance(2, "3 G3-4")

# 8. SEA #3  Mike Zunino (8 - 15 - 17)
b8.new_ab(is_risp=True)
b8.pitch_list("s f")
b8.out("G3-4", rbis=1)

# 9. SEA #55 Michael Saunders (15 - 17 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f f b f d b t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #31 Yoervis Medina
t9 = game.new_inning()

# Pitching change (SEA): #31 Yoervis Medina replaces #59 Oliver Pérez
t9.pitching_substitution(31)

# 9. BOS #26 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G4-3")

# 1. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "23 DI")

# 2. BOS #5  Jonny Gomes (X - X - 29)
t9.new_ab()
t9.pitch_list("c b c s")
t9.out("K")

# 3. BOS #23 Brandon Snyder (X - X - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("b f c b")
t9.reach("HBP")
t9.thrown_out(2, "20 FC5-4", 3, 31)

# 4. BOS #20 Ryan Lavarnway (X - 29 - 23)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.reach("FC5-4")

# Winning team: SEA
# WP: SEA #34 Félix Hernández
game.winning_pitcher(34)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
