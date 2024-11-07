import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SEA, 2013-07-11
# https://www.baseball-reference.com/boxes/SEA/SEA201307110.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2013/07/11/348122/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-11 15:41-19:45",
        "at": "Safeco Field, Seattle, WA",
        "att": "25,367",
        "temp": "60F, Cloudy",
        "wind": "1mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                26: "Brock Holt",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                18: "Shane Victorino",
                44: "Jackie Bradley Jr.",
                12: "Mike Napoli",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                40: "Andrew Bailey",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
            },
            "lefties": [32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [37, "3"],
                [20, "2"],
                [26, "5"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [18, "CF"],
                [44, "CF"],
                [12, "1B"],
                [23, "1B"],
            ],
            "bullpen": [35, 40, 41, 67, 32, 31, 36, 19, 54, 22],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 50,
            "roster": {
                # Lineup
                5: "Brad Miller",
                9: "Endy Chavez",
                28: "Raul Ibanez",
                8: "Kendrys Morales",
                15: "Kyle Seager",
                17: "Justin Smoak",
                3: "Mike Zunino",
                55: "Michael Saunders",
                26: "Brendan Ryan",
                # Starting pitcher
                50: "Erasmo Ramírez",
                # Bench
                12: "Jason Bay",
                13: "Dustin Ackley",
                33: "Henry Blanco",
                6: "Nick Franklin",
                # Bullpen
                44: "Lucas Luetge",
                39: "Aaron Harang",
                40: "Danny Farquhar",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                49: "Blake Beavan",
                31: "Yoervis Medina",
                34: "Félix Hernández",
                54: "Tom Wilhelmsen",
                23: "Joe Saunders",
                18: "Hisashi Iwakuma",
            },
            "lefties": [44, 41, 59, 23],
            "lineup": [
                [5, "4"],
                [9, "9"],
                [28, "7"],
                [8, "0"],
                [15, "5"],
                [17, "3"],
                [3, "2"],
                [55, "8"],
                [26, "6"],
            ],
            "bench": [
                [12, "LF"],
                [13, "2B"],
                [33, "C"],
                [6, "2B"],
            ],
            "bullpen": [44, 39, 40, 41, 59, 49, 31, 34, 54, 23, 18],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Ed Hickox",
            "2B": "Jim Joyce",
            "3B": "Cory Blaser",
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
# Pitching: SEA #50 Erasmo Ramírez
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(4)

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("b c b")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b c s")
t1.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
t1.new_ab()
t1.pitch_list("b b b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b1.new_ab()
b1.pitch_list("f c b s")
b1.out("K")

# 2. SEA #9  Endy Chavez (X - X - X)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")

# 3. SEA #28 Raul Ibanez (X - X - X)
b1.new_ab()
b1.pitch_list("b s b f b")
b1.hit(1)

# 4. SEA #8  Kendrys Morales (X - X - 28)
b1.new_ab()
b1.pitch_list("s b f b d f f")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #50 Erasmo Ramírez
t2 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c c b b b c")
t2.out("!K")

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c s b f b b b")
t2.reach("BB")

# 7. BOS #20 Ryan Lavarnway (X - X - 37)
t2.new_ab()
t2.pitch_list("b")
t2.out("F9")

# 8. BOS #26 Brock Holt (X - X - 37)
t2.new_ab()
t2.pitch_list("b b f b")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(4)

# 6. SEA #17 Justin Smoak (X - X - X)
b2.new_ab()
b2.pitch_list("c f b")
b2.out("F7")

# 7. SEA #3  Mike Zunino (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)
b2.advance(2, "26 WP")
b2.advance(3, "26 E5")
b2.advance("U", "5 2B")

# 8. SEA #55 Michael Saunders (X - X - 3)
b2.new_ab()
b2.pitch_list("b c c b")
b2.out("F7")

# 9. SEA #26 Brendan Ryan (X - X - 3)
b2.new_ab(is_risp=True)
b2.pitch_list("c f f f b f")
b2.wp()
b2.error(5)
b2.reach("E5")
b2.advance(3, "5 2B")
b2.advance("U", "9 1B")

# 1. SEA #5  Brad Miller (3 - X - 26)
b2.new_ab(is_risp=True)
b2.pitch_list("f f")
b2.hit(2, rbis=1)
b2.advance("U", "9 1B")

# 2. SEA #9  Endy Chavez (26 - 5 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b s c b")
b2.hit(1, rbis=2)
b2.advance(2, "28 SB")

# 3. SEA #28 Raul Ibanez (X - X - 9)
b2.new_ab(is_risp=True)
b2.pitch_list("f f f b b f f b")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #50 Erasmo Ramírez
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f f b b")
t3.reach("BB")
t3.thrown_out(2, "15 FC5-4", 3, 50)

# 2. BOS #29 Daniel Nava (X - X - 2)
t3.new_ab()
t3.pitch_list("b")
t3.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t3.new_ab()
t3.pitch_list("c 1 1 s")
t3.reach("FC5-4")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 5. SEA #15 Kyle Seager (X - X - X)
b3.new_ab()
b3.pitch_list("c s")
b3.out("F9")

# 6. SEA #17 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("f b b b b")
b3.reach("BB")
b3.advance(2, "3 HBP")
b3.advance(4, "55 1B")

# 7. SEA #3  Mike Zunino (X - X - 17)
b3.new_ab()
b3.pitch_list("b c")
b3.reach("HBP")
b3.advance(2, "55 1B")

# 8. SEA #55 Michael Saunders (X - 17 - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.hit(1, rbis=1)

# 9. SEA #26 Brendan Ryan (X - 3 - 55)
b3.new_ab(is_risp=True)
b3.pitch_list("s b")
b3.out("P4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #50 Erasmo Ramírez
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b b")
t4.reach("BB")
t4.advance(2, "37 HBP")
t4.advance(4, "26 1B")

# 5. BOS #5  Jonny Gomes (X - X - 34)
t4.new_ab()
t4.pitch_list("f b b s 1 d c")
t4.out("!K")

# 6. BOS #37 Mike Carp (X - X - 34)
t4.new_ab()
t4.pitch_list("f f")
t4.reach("HBP")
t4.advance(3, "26 1B")
t4.advance(4, "10 1B")

# 7. BOS #20 Ryan Lavarnway (X - 34 - 37)
t4.new_ab(is_risp=True)
t4.pitch_list("b c f s")
t4.out("K")

# 8. BOS #26 Brock Holt (X - 34 - 37)
t4.new_ab(is_risp=True)
t4.pitch_list("b f d f b f")
t4.hit(1, rbis=1)
t4.advance(2, "10 1B")
t4.advance(4, "2 1B")

# 9. BOS #10 Jose Iglesias (37 - X - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("c b 1 b")
t4.hit(1, rbis=1)
t4.advance(3, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 26 - 10)
t4.new_ab(is_risp=True)
t4.hit(1, rbis=1)

# 2. BOS #29 Daniel Nava (10 - X - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b c b 1 1")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(2, "9 1B")
b4.advance(4, "8 1B")

# 2. SEA #9  Endy Chavez (X - X - 5)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.advance(2, "8 1B")
# Offensive change (SEA): Pinch-runner #13 Dustin Ackley replaces #9 Endy Chavez
b4.offensive_substitution(2, 13, "PR")
b4.atbase("PR")
b4.advance(4, "15 1B")

# 3. SEA #28 Raul Ibanez (X - 5 - 9)
b4.new_ab(is_risp=True)
b4.pitch_list("s f f s")
b4.out("K")

# 4. SEA #8  Kendrys Morales (X - 5 - 9)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.hit(1, rbis=1)
b4.advance(2, "15 1B")
b4.advance(3, "17 WP")

# Pitching change (BOS): #35 Steven Wright replaces #46 Ryan Dempster
b4.pitching_substitution(35)

# 5. SEA #15 Kyle Seager (X - 9 - 8)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f d")
b4.hit(1, rbis=1)
b4.advance(2, "17 WP")

# 6. SEA #17 Justin Smoak (X - 8 - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("s b b s")
b4.wp()
b4.out("G4-3")

# 7. SEA #3  Mike Zunino (8 - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #50 Erasmo Ramírez
t5 = game.new_inning()

# Defensive switch (SEA): #13 Dustin Ackley moves to CF
t5.defensive_switch(13, "8")

# Defensive switch (SEA): #55 Michael Saunders moves to RF
t5.defensive_switch(55, "9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("f c")
t5.hit(1)
t5.advance(2, "34 BB")
t5.advance(3, "5 1B")
t5.advance(4, "37 SF7")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("b b f b b")
t5.reach("BB")
t5.advance(2, "5 1B")
t5.advance(4, "26 1B")

# 5. BOS #5  Jonny Gomes (X - 15 - 34)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "26 1B")
t5.advance(4, "10 1B")

# 6. BOS #37 Mike Carp (15 - 34 - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("b b")
t5.out("SF7", rbis=1)

# 7. BOS #20 Ryan Lavarnway (X - 34 - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("b b s c")
t5.out("F7")

# Pitching change (SEA): #41 Charlie Furbush replaces #50 Erasmo Ramírez
t5.pitching_substitution(41)

# 8. BOS #26 Brock Holt (X - 34 - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("c s")
t5.hit(1, rbis=1)
t5.advance(2, "10 1B")

# 9. BOS #10 Jose Iglesias (X - 5 - 26)
t5.new_ab(is_risp=True)
t5.pitch_list("b c f f b f")
t5.hit(1, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - 26 - 10)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #35 Steven Wright
b5 = game.new_inning()

# 8. SEA #55 Michael Saunders (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 9. SEA #26 Brendan Ryan (X - X - X)
b5.new_ab()
b5.pitch_list("s s")
b5.out("P4")

# 1. SEA #5  Brad Miller (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b b")
b5.reach("BB")
b5.thrown_out(2, "13 FC6", 3, 35)

# 2. SEA #13 Dustin Ackley (X - X - 5)
b5.new_ab()
b5.pitch_list("b c")
b5.reach("FC6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #41 Charlie Furbush
t6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b c f f s")
t6.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("L3")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# 3. SEA #28 Raul Ibanez (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)
b6.thrown_out(2, "8 DP6-4-3", 1, 35)

# 4. SEA #8  Kendrys Morales (X - X - 28)
b6.new_ab()
b6.out("DP6-4-3")

# 5. SEA #15 Kyle Seager (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("P5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #41 Charlie Furbush
t7 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b c f s")
t7.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b c")
t7.out("!K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t7.new_ab()
t7.pitch_list("f s b b f b")
t7.hit(2)

# 8. BOS #26 Brock Holt (X - 20 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("f s f f")
t7.out("G3")


# Bot 7th
# Pitching: BOS #35 Steven Wright
b7 = game.new_inning()

# 6. SEA #17 Justin Smoak (X - X - X)
b7.new_ab()
b7.out("F8")

# 7. SEA #3  Mike Zunino (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("F8")

# 8. SEA #55 Michael Saunders (X - X - X)
b7.new_ab()
b7.pitch_list("c f b")
b7.error(3)
b7.reach("E3", end_base=2)

# 9. SEA #26 Brendan Ryan (X - 55 - X)
b7.new_ab(is_risp=True)
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #59 Oliver Pérez
t8 = game.new_inning()

# Pitching change (SEA): #59 Oliver Pérez replaces #41 Charlie Furbush
t8.pitching_substitution(59)

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("b c f f f c")
t8.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c c b s")
t8.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("s c f f f f f b b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #35 Steven Wright
b8 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 2. SEA #13 Dustin Ackley (X - X - X)
b8.new_ab()
b8.pitch_list("c f f b f b")
b8.out("F7")

# 3. SEA #28 Raul Ibanez (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b f f b")
b8.reach("BB")

# 4. SEA #8  Kendrys Morales (X - X - 28)
b8.new_ab()
b8.pitch_list("b c b f f d s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #59 Oliver Pérez
t9 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("F8")

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")

# Pitching change (SEA): #54 Tom Wilhelmsen replaces #59 Oliver Pérez
t9.pitching_substitution(54)

# Offensive change (BOS): Pinch-hitter #18 Shane Victorino replaces #37 Mike Carp, batting 6th
t9.offensive_substitution(6, 18, "PH")

# 6. BOS #18 Shane Victorino (X - X - 5)
t9.new_ab()
t9.pitch_list("d s c s")
t9.out("K")


# Bot 9th
# Pitching: BOS #35 Steven Wright
b9 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b9.defensive_switch(29, "3")

# Defensive switch (BOS): #18 Shane Victorino moves to RF
b9.defensive_switch(18, "9")

# 5. SEA #15 Kyle Seager (X - X - X)
b9.new_ab()
b9.pitch_list("f f b b b")
b9.out("G3")

# 6. SEA #17 Justin Smoak (X - X - X)
b9.new_ab()
b9.pitch_list("c b f")
b9.hit(1)
b9.thrown_out(2, "3 DP6-4-3", 2, 35)

# 7. SEA #3  Mike Zunino (X - X - 17)
b9.new_ab()
b9.pitch_list("f s f")
b9.out("DP6-4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: SEA #54 Tom Wilhelmsen
t10 = game.new_inning()

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t10.new_ab()
t10.pitch_list("b s f f f b f f b b")
t10.reach("BB")
# Offensive change (BOS): Pinch-runner #44 Jackie Bradley Jr. replaces #20 Ryan Lavarnway
t10.offensive_substitution(7, 44, "PR")
t10.atbase("PR")
t10.advance(2, "26 SAC1-3")
t10.advance(4, "29 1B")

# 8. BOS #26 Brock Holt (X - X - 20)
t10.new_ab()
t10.pitch_list("1")
t10.out("SAC1-3")

# 9. BOS #10 Jose Iglesias (X - 44 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("c b s f f d f s")
t10.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 44 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("i i i i")
t10.reach("IBB")
t10.advance(3, "29 1B")

# 2. BOS #29 Daniel Nava (X - 44 - 2)
t10.new_ab(is_risp=True)
t10.pitch_list("c s b")
t10.hit(1, rbis=1)

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t10.new_ab(is_risp=True)
t10.pitch_list("b s b b f f")
t10.out("F8")


# Bot 10th
# Pitching: BOS #19 Koji Uehara
b10 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #35 Steven Wright
b10.pitching_substitution(19)

# Defensive change (BOS): #39 Jarrod Saltalamacchia replaces #18 Shane Victorino (PH), playing C, batting 6th
b10.defensive_substitution(6, 39, "2")

# Defensive switch (BOS): #44 Jackie Bradley Jr. moves to RF
b10.defensive_switch(44, "9")

# 8. SEA #55 Michael Saunders (X - X - X)
b10.new_ab()
b10.pitch_list("b")
b10.out("(F)P5")

# Offensive change (SEA): Pinch-hitter #12 Jason Bay replaces #26 Brendan Ryan, batting 9th
b10.offensive_substitution(9, 12, "PH")

# 9. SEA #12 Jason Bay (X - X - X)
b10.new_ab()
b10.pitch_list("s s f b b c")
b10.out("!K")

# 1. SEA #5  Brad Miller (X - X - X)
b10.new_ab()
b10.pitch_list("s b b c s")
b10.out("K")

# Winning team: BOS
# WP: BOS #35 Steven Wright
game.winning_pitcher(35, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: SEA
# LP: SEA #54 Tom Wilhelmsen
game.losing_pitcher(54)

# print(game)
game.generate_scorecard()
