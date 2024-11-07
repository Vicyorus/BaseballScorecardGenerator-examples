import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2013-07-31
# https://www.baseball-reference.com/boxes/BOS/BOS201307310.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2013/07/31/348351/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-31 19:11-00:14 +1",
        "at": "Fenway Park, Boston, MA",
        "att": "35,059",
        "temp": "75F, Partly Cloudy",
        "wind": "12mph, R To L",
        "away": {
            "team": "Seattle Mariners",
            "starter": 18,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                15: "Kyle Seager",
                8: "Kendrys Morales",
                28: "Raul Ibanez",
                38: "Michael Morse",
                55: "Michael Saunders",
                13: "Dustin Ackley",
                35: "Humberto Quintero",
                # Starting pitcher
                18: "Hisashi Iwakuma",
                # Bench
                26: "Brendan Ryan",
                9: "Endy Chavez",
                17: "Justin Smoak",
                33: "Henry Blanco",
                # Bullpen
                44: "Lucas Luetge",
                39: "Aaron Harang",
                50: "Erasmo Ramírez",
                40: "Danny Farquhar",
                37: "Brandon Maurer",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                31: "Yoervis Medina",
                34: "Félix Hernández",
                54: "Tom Wilhelmsen",
                23: "Joe Saunders",
            },
            "lefties": [44, 41, 59, 23],
            "lineup": [
                [5, "6"],
                [6, "4"],
                [15, "5"],
                [8, "0"],
                [28, "7"],
                [38, "3"],
                [55, "9"],
                [13, "8"],
                [35, "2"],
            ],
            "bench": [
                [26, "SS"],
                [9, "CF"],
                [17, "1B"],
                [33, "C"],
            ],
            "bullpen": [44, 39, 50, 40, 37, 41, 59, 31, 34, 54, 23],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                7: "Stephen Drew",
                26: "Brock Holt",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                29: "Daniel Nava",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [37, "7"],
                [7, "6"],
                [26, "5"],
            ],
            "bench": [
                [29, "LF"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 67, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Gary Darling",
            "1B": "David Rackley",
            "2B": "Jerry Meals",
            "3B": "Chris Conroy",
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

# 1. SEA #5  Brad Miller (X - X - X)
t1.new_ab()
t1.out("F7")

# 2. SEA #6  Nick Franklin (X - X - X)
t1.new_ab()
t1.pitch_list("c b c s")
t1.out("K")

# 3. SEA #15 Kyle Seager (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f")
t1.out("G4-3")


# Bot 1st
# Pitching: SEA #18 Hisashi Iwakuma
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "18 1B")
b1.advance(3, "15 1B")
b1.thrown_out(4, "34 DP1-2-3", 1, 18)

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("b c b b c")
b1.hit(1)
b1.advance(2, "15 1B")
b1.advance(3, "34 DP1-2-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "34 DP1-2-3")

# 4. BOS #34 David Ortiz (2 - 18 - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b d f b c")
b1.out("DP1-2-3")

# 5. BOS #12 Mike Napoli (18 - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c s b b")
b1.reach("BB")

# 6. BOS #39 Jarrod Saltalamacchia (18 - 15 - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("L3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(1)
t2.thrown_out(2, "28 DP5-6-3", 1, 41)

# 5. SEA #28 Raul Ibanez (X - X - 8)
t2.new_ab()
t2.pitch_list("s")
t2.out("DP5-6-3")

# 6. SEA #38 Michael Morse (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("F9")


# Bot 2nd
# Pitching: SEA #18 Hisashi Iwakuma
b2 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 9. BOS #26 Brock Holt (X - X - 7)
b2.new_ab()
b2.pitch_list("c b f")
b2.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b2.new_ab()
b2.pitch_list("c 1 b b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 7. SEA #55 Michael Saunders (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("G6-3")

# 8. SEA #13 Dustin Ackley (X - X - X)
t3.new_ab()
t3.pitch_list("c c b f f b")
t3.hit(1)
t3.thrown_out(2, "35 DP4-6-3", 2, 41)

# 9. SEA #35 Humberto Quintero (X - X - 13)
t3.new_ab()
t3.pitch_list("1")
t3.out("DP4-6-3")


# Bot 3rd
# Pitching: SEA #18 Hisashi Iwakuma
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f f f")
b3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f")
b3.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("s b s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
t4.new_ab()
t4.pitch_list("b c f")
t4.hit(1)
t4.advance(2, "6 SB")
t4.advance(4, "15 2B")

# 2. SEA #6  Nick Franklin (X - X - 5)
t4.new_ab()
t4.pitch_list("s c f b b s")
t4.out("K")

# 3. SEA #15 Kyle Seager (X - 5 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c c")
t4.hit(2, rbis=1)
t4.advance(3, "8 G6-3")

# 4. SEA #8  Kendrys Morales (X - 15 - X)
t4.new_ab(is_risp=True)
t4.out("G6-3")

# 5. SEA #28 Raul Ibanez (15 - X - X)
t4.new_ab(is_risp=True)
t4.out("(F)P3")


# Bot 4th
# Pitching: SEA #18 Hisashi Iwakuma
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("F8")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.hit(1)

# 7. BOS #37 Mike Carp (X - X - 39)
b4.new_ab()
b4.pitch_list("b c c s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - X - 39)
b4.new_ab()
b4.pitch_list("c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 6. SEA #38 Michael Morse (X - X - X)
t5.new_ab()
t5.pitch_list("f b s f s")
t5.out("K")

# 7. SEA #55 Michael Saunders (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("P6")

# 8. SEA #13 Dustin Ackley (X - X - X)
t5.new_ab()
t5.pitch_list("b f f s")
t5.out("K")


# Bot 5th
# Pitching: SEA #18 Hisashi Iwakuma
b5 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.hit(2)
b5.advance(3, "2 E8")
b5.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 26 - X)
b5.new_ab(is_risp=True)
b5.error(8)
b5.reach("E8")
b5.advance(3, "18 1B")
b5.advance("U", "15 FC5-4")

# 2. BOS #18 Shane Victorino (26 - X - 2)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f 1 1 f b")
b5.hit(1, rbis=1)
b5.thrown_out(2, "15 FC5-4", 1, 18)

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
b5.new_ab(is_risp=True)
b5.reach("FC5-4", rbis=1)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("c b b s s")
b5.out("K")

# 5. BOS #12 Mike Napoli (X - X - 15)
b5.new_ab()
b5.pitch_list("b b c s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 9. SEA #35 Humberto Quintero (X - X - X)
t6.new_ab()
t6.pitch_list("s")
t6.hit(1)
t6.advance(2, "5 BB")
t6.advance(3, "15 1B")
t6.advance(4, "8 SF7")

# 1. SEA #5  Brad Miller (X - X - 35)
t6.new_ab()
t6.pitch_list("b f b b f b")
t6.reach("BB")
t6.advance(2, "15 1B")
t6.advance(4, "28 1B")

# 2. SEA #6  Nick Franklin (X - 35 - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("b l l c")
t6.out("!K")

# 3. SEA #15 Kyle Seager (X - 35 - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("f b f f")
t6.hit(1)
t6.advance(3, "28 1B")

# 4. SEA #8  Kendrys Morales (35 - 5 - 15)
t6.new_ab(is_risp=True)
t6.pitch_list("s b")
t6.out("SF7", rbis=1)

# 5. SEA #28 Raul Ibanez (X - 5 - 15)
t6.new_ab(is_risp=True)
t6.pitch_list("b c")
t6.hit(1, rbis=1)

# 6. SEA #38 Michael Morse (15 - X - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("b c")
t6.out("F8")


# Bot 6th
# Pitching: SEA #18 Hisashi Iwakuma
b6 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f b")
b6.hit(1)
b6.advance(2, "7 BB")
b6.advance(3, "26 G3")

# 7. BOS #37 Mike Carp (X - X - 39)
b6.new_ab()
b6.out("L9")

# 8. BOS #7  Stephen Drew (X - X - 39)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "26 G3")

# 9. BOS #26 Brock Holt (X - 39 - 7)
b6.new_ab(is_risp=True)
b6.pitch_list("c f f f b")
b6.out("G3")

# Pitching change (SEA): #59 Oliver Pérez replaces #18 Hisashi Iwakuma
b6.pitching_substitution(59)

# 1. BOS #2  Jacoby Ellsbury (39 - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f b c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 7. SEA #55 Michael Saunders (X - X - X)
t7.new_ab()
t7.pitch_list("b f b b f s")
t7.out("K")

# 8. SEA #13 Dustin Ackley (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("L8")

# 9. SEA #35 Humberto Quintero (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(1)

# 1. SEA #5  Brad Miller (X - X - 35)
t7.new_ab()
t7.pitch_list("b c")
t7.out("L8")


# Bot 7th
# Pitching: SEA #59 Oliver Pérez
b7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b b s f f f")
b7.hit(1)
b7.advance(4, "15 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b7.new_ab()
b7.pitch_list("b 1 b c b c")
b7.hit(4, rbis=2)

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("f f f")
b7.hit(1)
b7.thrown_out(2, "12 DP6-4-3", 1, 31)

# Pitching change (SEA): #31 Yoervis Medina replaces #59 Oliver Pérez
b7.pitching_substitution(31)

# 5. BOS #12 Mike Napoli (X - X - 34)
b7.new_ab()
b7.pitch_list("f c d")
b7.out("DP6-4-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b f b f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #41 John Lackey
t8.pitching_substitution(36)

# Defensive change (BOS): #29 Daniel Nava replaces #37 Mike Carp (LF), playing LF, batting 7th
t8.defensive_substitution(7, 29, "7")

# 2. SEA #6  Nick Franklin (X - X - X)
t8.new_ab()
t8.out("L3")

# 3. SEA #15 Kyle Seager (X - X - X)
t8.new_ab()
t8.hit(4)

# 4. SEA #8  Kendrys Morales (X - X - X)
t8.new_ab()
t8.hit(1)

# 5. SEA #28 Raul Ibanez (X - X - 8)
t8.new_ab()
t8.pitch_list("b s f s")
t8.out("K")

# 6. SEA #38 Michael Morse (X - X - 8)
t8.new_ab()
t8.pitch_list("c")
t8.out("G3")


# Bot 8th
# Pitching: SEA #31 Yoervis Medina
b8 = game.new_inning()

# 7. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.out("F7")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c s f s")
b8.out("K")

# 9. BOS #26 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("b f c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# 7. SEA #55 Michael Saunders (X - X - X)
t9.new_ab()
t9.pitch_list("c f c")
t9.out("!K")

# 8. SEA #13 Dustin Ackley (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F8")

# 9. SEA #35 Humberto Quintero (X - X - X)
t9.new_ab()
t9.pitch_list("f s")
t9.out("G5-3")


# Bot 9th
# Pitching: SEA #41 Charlie Furbush
b9 = game.new_inning()

# Pitching change (SEA): #41 Charlie Furbush replaces #31 Yoervis Medina
b9.pitching_substitution(41)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("c c b s")
b9.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b9.new_ab()
b9.pitch_list("c b f b b d")
b9.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b9.new_ab()
b9.pitch_list("c 1 b c s")
b9.out("K")

# 4. BOS #34 David Ortiz (X - X - 18)
b9.new_ab()
b9.pitch_list("d b")
b9.out("P5")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #19 Koji Uehara
t10 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
t10.new_ab()
t10.pitch_list("c t")
t10.out("P6")

# 2. SEA #6  Nick Franklin (X - X - X)
t10.new_ab()
t10.pitch_list("s s t")
t10.out("KT")

# 3. SEA #15 Kyle Seager (X - X - X)
t10.new_ab()
t10.pitch_list("c b s b s")
t10.out("K")


# Bot 10th
# Pitching: SEA #40 Danny Farquhar
b10 = game.new_inning()

# Pitching change (SEA): #40 Danny Farquhar replaces #41 Charlie Furbush
b10.pitching_substitution(40)

# 5. BOS #12 Mike Napoli (X - X - X)
b10.new_ab()
b10.pitch_list("f b b c s")
b10.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b10.new_ab()
b10.pitch_list("c")
b10.out("G6-3")

# 7. BOS #29 Daniel Nava (X - X - X)
b10.new_ab()
b10.pitch_list("b c f f f b f b f f s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #38 Matt Thornton
t11 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #19 Koji Uehara
t11.pitching_substitution(38)

# 4. SEA #8  Kendrys Morales (X - X - X)
t11.new_ab()
t11.pitch_list("b b f b")
t11.hit(1)
# Offensive change (SEA): Pinch-runner #26 Brendan Ryan replaces #8 Kendrys Morales
t11.offensive_substitution(4, 26, "PR")
t11.atbase("PR")
t11.thrown_out(2, "38 FC6-4", 2, 38)

# 5. SEA #28 Raul Ibanez (X - X - 8)
t11.new_ab()
t11.pitch_list("1 b b f")
t11.out("F8")

# 6. SEA #38 Michael Morse (X - X - 26)
t11.new_ab()
t11.pitch_list("b")
t11.reach("FC6-4")
t11.advance(2, "55 1B")
# Offensive change (SEA): Pinch-runner #9 Endy Chavez replaces #38 Michael Morse
t11.offensive_substitution(6, 9, "PR")
t11.atbase("PR")

# 7. SEA #55 Michael Saunders (X - X - 38)
t11.new_ab()
t11.hit(1)

# 8. SEA #13 Dustin Ackley (X - 38 - 55)
t11.new_ab(is_risp=True)
t11.pitch_list("b")
t11.out("L8")


# Bot 11th
# Pitching: SEA #40 Danny Farquhar
b11 = game.new_inning()

# Defensive switch (SEA): #26 Brendan Ryan moves to DH
b11.defensive_switch(26, "0")

# Defensive switch (SEA): #9 Endy Chavez moves to RF
b11.defensive_switch(9, "9")

# Defensive switch (SEA): #55 Michael Saunders moves to CF
b11.defensive_switch(55, "8")

# Defensive switch (SEA): #13 Dustin Ackley moves to 1B
b11.defensive_switch(13, "3")

# 8. BOS #7  Stephen Drew (X - X - X)
b11.new_ab()
b11.pitch_list("c f s")
b11.out("K")

# 9. BOS #26 Brock Holt (X - X - X)
b11.new_ab()
b11.pitch_list("f b")
b11.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b11.new_ab()
b11.pitch_list("b b f b")
b11.out("G3")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BOS #32 Craig Breslow
t12 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #38 Matt Thornton
t12.pitching_substitution(32)

# 9. SEA #35 Humberto Quintero (X - X - X)
t12.new_ab()
t12.out("G3")

# 1. SEA #5  Brad Miller (X - X - X)
t12.new_ab()
t12.pitch_list("b c b b b")
t12.reach("BB")
t12.advance(2, "6 G3")
t12.advance(3, "15 WP")

# 2. SEA #6  Nick Franklin (X - X - 5)
t12.new_ab()
t12.pitch_list("b")
t12.out("G3")

# 3. SEA #15 Kyle Seager (X - 5 - X)
t12.new_ab(is_risp=True)
t12.pitch_list("b b c b b")
t12.wp()
t12.reach("BB")

# 4. SEA #26 Brendan Ryan (5 - X - 15)
t12.new_ab(is_risp=True)
t12.pitch_list("s s")
t12.out("(F)P3")


# Bot 12th
# Pitching: SEA #40 Danny Farquhar
b12 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b12.new_ab()
b12.pitch_list("c f s")
b12.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b12.new_ab()
b12.pitch_list("c")
b12.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b12.new_ab()
b12.pitch_list("b f b")
b12.out("F9")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: BOS #32 Craig Breslow
t13 = game.new_inning()

# 5. SEA #28 Raul Ibanez (X - X - X)
t13.new_ab()
t13.pitch_list("c")
t13.out("L4")

# 6. SEA #9  Endy Chavez (X - X - X)
t13.new_ab()
t13.pitch_list("b")
t13.out("F8")

# 7. SEA #55 Michael Saunders (X - X - X)
t13.new_ab()
t13.pitch_list("b f c b b")
t13.hit(2)

# 8. SEA #13 Dustin Ackley (X - 55 - X)
t13.new_ab(is_risp=True)
t13.pitch_list("b c b")
t13.out("F8")


# Bot 13th
# Pitching: SEA #44 Lucas Luetge
b13 = game.new_inning()

# Pitching change (SEA): #44 Lucas Luetge replaces #40 Danny Farquhar
b13.pitching_substitution(44)

# 5. BOS #12 Mike Napoli (X - X - X)
b13.new_ab()
b13.pitch_list("b c")
b13.out("F9")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b13.new_ab()
b13.pitch_list("b b")
b13.out("F7")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 7th
b13.offensive_substitution(7, 5, "PH")

# 7. BOS #5  Jonny Gomes (X - X - X)
b13.new_ab()
b13.pitch_list("b b b c b")
b13.reach("BB")
b13.advance(2, "7 WP")

# 8. BOS #7  Stephen Drew (X - X - 5)
b13.new_ab(is_risp=True)
b13.pitch_list("b b b c")
b13.wp()
b13.out("P4")


##########################################################
# 14th Inning
##########################################################
# Top 14th
# Pitching: BOS #66 Drake Britton
t14 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #32 Craig Breslow
t14.pitching_substitution(66)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t14.defensive_switch(5, "7")

# 9. SEA #35 Humberto Quintero (X - X - X)
t14.new_ab()
t14.pitch_list("c b c f f b f f s")
t14.out("K")

# 1. SEA #5  Brad Miller (X - X - X)
t14.new_ab()
t14.pitch_list("f b")
t14.hit(1)

# 2. SEA #6  Nick Franklin (X - X - 5)
t14.new_ab()
t14.pitch_list("b 1 c")
t14.out("L8")

# 3. SEA #15 Kyle Seager (X - X - 5)
t14.new_ab()
t14.pitch_list("b s c s")
t14.out("K")


# Bot 14th
# Pitching: SEA #44 Lucas Luetge
b14 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #26 Brock Holt, batting 9th
b14.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Brandon Snyder (X - X - X)
b14.new_ab()
b14.pitch_list("c b b")
b14.hit(2)
b14.advance(3, "2 SAC1-4")
b14.thrown_out(4, "18 DP8-2", 3, 44)

# 1. BOS #2  Jacoby Ellsbury (X - 23 - X)
b14.new_ab(is_risp=True)
b14.pitch_list("c")
b14.out("SAC1-4")

# 2. BOS #18 Shane Victorino (23 - X - X)
b14.new_ab(is_risp=True)
b14.pitch_list("c s")
b14.out("DP8-2")


##########################################################
# 15th Inning
##########################################################
# Top 15th
# Pitching: BOS #66 Drake Britton
t15 = game.new_inning()

# Defensive switch (BOS): #23 Brandon Snyder moves to 3B
t15.defensive_switch(23, "5")

# 4. SEA #26 Brendan Ryan (X - X - X)
t15.new_ab()
t15.pitch_list("c b b")
t15.out("F9")

# 5. SEA #28 Raul Ibanez (X - X - X)
t15.new_ab()
t15.pitch_list("b f f")
t15.hit(1)
t15.advance(2, "9 1B")
t15.thrown_out(2, "55 DP7", 3, 66)

# 6. SEA #9  Endy Chavez (X - X - 28)
t15.new_ab()
t15.pitch_list("c f f")
t15.hit(1)

# 7. SEA #55 Michael Saunders (X - 28 - 9)
t15.new_ab(is_risp=True)
t15.pitch_list("c b s")
t15.out("DP7")


# Bot 15th
# Pitching: SEA #44 Lucas Luetge
b15 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b15.new_ab()
b15.pitch_list("b b b b")
b15.reach("BB")
b15.advance(2, "34 G3")
b15.advance(3, "5 BB")
b15.advance(4, "7 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b15.new_ab()
b15.pitch_list("b")
b15.out("G3")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b15.new_ab(is_risp=True)
b15.pitch_list("i i i i")
b15.reach("IBB")
b15.advance(2, "5 BB")
b15.advance(3, "7 1B")

# 6. BOS #39 Jarrod Saltalamacchia (X - 15 - 12)
b15.new_ab(is_risp=True)
b15.pitch_list("s f c")
b15.out("!K")

# 7. BOS #5  Jonny Gomes (X - 15 - 12)
b15.new_ab(is_risp=True)
b15.pitch_list("d b d d")
b15.reach("BB")
b15.advance(2, "7 1B")

# 8. BOS #7  Stephen Drew (15 - 12 - 5)
b15.new_ab(is_risp=True)
b15.pitch_list("b s b")
b15.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #66 Drake Britton
game.winning_pitcher(66)

# Loser team: SEA
# LP: SEA #44 Lucas Luetge
game.losing_pitcher(44, is_away_team=True)

# print(game)
game.generate_scorecard()
