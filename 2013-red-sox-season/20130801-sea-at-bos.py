import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2013-08-01
# https://www.baseball-reference.com/boxes/BOS/BOS201308010.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2013/08/01/348362/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-01 19:11-22:28",
        "at": "Fenway Park, Boston, MA",
        "att": "35,886",
        "temp": "76F, Cloudy",
        "wind": "18mph, Out To RF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 34,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                15: "Kyle Seager",
                8: "Kendrys Morales",
                55: "Michael Saunders",
                17: "Justin Smoak",
                9: "Endy Chavez",
                13: "Dustin Ackley",
                33: "Henry Blanco",
                # Starting pitcher
                34: "Félix Hernández",
                # Bench
                26: "Brendan Ryan",
                35: "Humberto Quintero",
                38: "Michael Morse",
                28: "Raul Ibanez",
                # Bullpen
                44: "Lucas Luetge",
                39: "Aaron Harang",
                50: "Erasmo Ramírez",
                40: "Danny Farquhar",
                37: "Brandon Maurer",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                31: "Yoervis Medina",
                54: "Tom Wilhelmsen",
                23: "Joe Saunders",
                18: "Hisashi Iwakuma",
            },
            "lefties": [44, 41, 59, 23],
            "lineup": [
                [5, "6"],
                [6, "4"],
                [15, "5"],
                [8, "0"],
                [55, "8"],
                [17, "3"],
                [9, "9"],
                [13, "7"],
                [33, "2"],
            ],
            "bench": [
                [26, "SS"],
                [35, "C"],
                [38, "LF"],
                [28, "LF"],
            ],
            "bullpen": [44, 39, 50, 40, 37, 41, 59, 31, 54, 23, 18],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                7: "Stephen Drew",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                26: "Brock Holt",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [7, "6"],
                [29, "7"],
                [20, "2"],
                [26, "5"],
            ],
            "bench": [
                [39, "C"],
                [5, "LF"],
                [12, "1B"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 32, 66, 44, 31, 36, 19, 38, 54, 22],
        },
        "umpires": {
            "HP": "David Rackley",
            "1B": "Jerry Meals",
            "2B": "Chris Conroy",
            "3B": "Gary Darling",
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

# 1. SEA #5  Brad Miller (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(3)
t1.advance(4, "15 1B")

# 2. SEA #6  Nick Franklin (5 - X - X)
t1.new_ab()
t1.pitch_list("f s f f s")
t1.out("K")

# 3. SEA #15 Kyle Seager (5 - X - X)
t1.new_ab()
t1.hit(1, rbis=1)
t1.advance(2, "55 SB")
t1.advance(3, "17 BB")

# 4. SEA #8  Kendrys Morales (X - X - 15)
t1.new_ab()
t1.pitch_list("b b c s f c")
t1.out("!K")

# 5. SEA #55 Michael Saunders (X - X - 15)
t1.new_ab()
t1.pitch_list("c b d b b")
t1.reach("BB")
t1.advance(2, "17 BB")

# 6. SEA #17 Justin Smoak (X - 15 - 55)
t1.new_ab()
t1.pitch_list("b b f b s d")
t1.reach("BB")

# 7. SEA #9  Endy Chavez (15 - 55 - 17)
t1.new_ab()
t1.out("G3")


# Bot 1st
# Pitching: SEA #34 Félix Hernández
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(1)
b1.thrown_out(2, "18 FC3-6", 1, 34)

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("1 b")
b1.reach("FC3-6")
b1.advance(3, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c 1 f b d c")
b1.out("!K")

# 4. BOS #34 David Ortiz (X - X - 18)
b1.new_ab()
b1.hit(1)

# 5. BOS #37 Mike Carp (18 - X - 34)
b1.new_ab()
b1.pitch_list("b s c s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 8. SEA #13 Dustin Ackley (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F9")

# 9. SEA #33 Henry Blanco (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b b")
t2.reach("BB")

# 1. SEA #5  Brad Miller (X - X - 33)
t2.new_ab()
t2.pitch_list("c c b s")
t2.out("K")

# 2. SEA #6  Nick Franklin (X - X - 33)
t2.new_ab()
t2.pitch_list("b")
t2.out("F8")


# Bot 2nd
# Pitching: SEA #34 Félix Hernández
b2 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b f b b")
b2.hit(1)
b2.advance(2, "29 G4-3")

# 7. BOS #29 Daniel Nava (X - X - 7)
b2.new_ab()
b2.pitch_list("b c 1")
b2.out("G4-3")

# 8. BOS #20 Ryan Lavarnway (X - 7 - X)
b2.new_ab()
b2.pitch_list("b f d s f f s")
b2.out("K")

# 9. BOS #26 Brock Holt (X - 7 - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 3. SEA #15 Kyle Seager (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b b")
t3.reach("BB")
t3.advance(2, "8 1B")
t3.advance(4, "17 1B")

# 4. SEA #8  Kendrys Morales (X - X - 15)
t3.new_ab()
t3.hit(1)
t3.advance(3, "17 1B")

# 5. SEA #55 Michael Saunders (X - 15 - 8)
t3.new_ab()
t3.pitch_list("l c s")
t3.out("K")

# 6. SEA #17 Justin Smoak (X - 15 - 8)
t3.new_ab()
t3.pitch_list("c f b")
t3.hit(1, rbis=1)

# 7. SEA #9  Endy Chavez (8 - X - 17)
t3.new_ab()
t3.pitch_list("b b f")
t3.out("L7")

# 8. SEA #13 Dustin Ackley (8 - X - 17)
t3.new_ab()
t3.pitch_list("f d")
t3.out("P6")


# Bot 3rd
# Pitching: SEA #34 Félix Hernández
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(2)
b3.advance(3, "18 L8")
b3.advance(4, "34 SFDP7-5-4")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("L8")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b3.new_ab()
b3.pitch_list("b b f b b")
b3.reach("BB")
b3.thrown_out(2, "34 SFDP7-5-4", 3, 34)

# 4. BOS #34 David Ortiz (2 - X - 15)
b3.new_ab()
b3.out("SFDP7-5-4", rbis=1)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 9. SEA #33 Henry Blanco (X - X - X)
t4.new_ab()
t4.pitch_list("b c c f")
t4.out("F9")

# 1. SEA #5  Brad Miller (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("F9")

# 2. SEA #6  Nick Franklin (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")


# Bot 4th
# Pitching: SEA #34 Félix Hernández
b4 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b")
b4.out("G3")

# 6. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b f c b")
b4.out("G6-3")

# 7. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c")
b4.hit(2)

# 8. BOS #20 Ryan Lavarnway (X - 29 - X)
b4.new_ab()
b4.pitch_list("c t b b t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 3. SEA #15 Kyle Seager (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.hit(3)
t5.advance(4, "8 1B")

# 4. SEA #8  Kendrys Morales (15 - X - X)
t5.new_ab()
t5.hit(1, rbis=1)
t5.advance(3, "17 2B")
t5.advance(4, "33 HR")

# 5. SEA #55 Michael Saunders (X - X - 8)
t5.new_ab()
t5.pitch_list("c b d s f b s")
t5.out("K")

# 6. SEA #17 Justin Smoak (X - X - 8)
t5.new_ab()
t5.hit(2)
t5.advance(4, "33 HR")

# 7. SEA #9  Endy Chavez (8 - 17 - X)
t5.new_ab()
t5.pitch_list("s f")
t5.out("F7")

# 8. SEA #13 Dustin Ackley (8 - 17 - X)
t5.new_ab()
t5.pitch_list("b c b b f d")
t5.reach("BB")
t5.advance(4, "33 HR")

# 9. SEA #33 Henry Blanco (8 - 17 - 13)
t5.new_ab()
t5.pitch_list("f")
t5.hit(4, rbis=4)

# 1. SEA #5  Brad Miller (X - X - X)
t5.new_ab()
t5.pitch_list("b c f c")
t5.out("!K")


# Bot 5th
# Pitching: SEA #34 Félix Hernández
b5 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("s b b f c")
b5.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 2. SEA #6  Nick Franklin (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.out("F8")

# 3. SEA #15 Kyle Seager (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F7")

# 4. SEA #8  Kendrys Morales (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b")
t6.hit(1)
t6.thrown_out(2, "55 FC4-6", 3, 46)

# 5. SEA #55 Michael Saunders (X - X - 8)
t6.new_ab()
t6.pitch_list("s")
t6.reach("FC4-6")


# Bot 6th
# Pitching: SEA #34 Félix Hernández
b6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("f b s")
b6.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("s s b s")
b6.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("f c b s")
b6.out("K2-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #46 Ryan Dempster
t7.pitching_substitution(35)

# 6. SEA #17 Justin Smoak (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("L3")

# 7. SEA #9  Endy Chavez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L8")

# 8. SEA #13 Dustin Ackley (X - X - X)
t7.new_ab()
t7.pitch_list("c f f")
t7.out("G6-3")


# Bot 7th
# Pitching: SEA #34 Félix Hernández
b7 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("f f b f b b f d")
b7.reach("BB")
b7.advance(2, "20 1B")

# 7. BOS #29 Daniel Nava (X - X - 7)
b7.new_ab()
b7.out("L7")

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
b7.new_ab()
b7.pitch_list("b c s d b f")
b7.hit(1)

# 9. BOS #26 Brock Holt (X - 7 - 20)
b7.new_ab()
b7.out("L6")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 20)
b7.new_ab()
b7.pitch_list("s c d s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# 9. SEA #33 Henry Blanco (X - X - X)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K2-3")

# 1. SEA #5  Brad Miller (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b b")
t8.reach("BB")
t8.thrown_out(2, "6 FC3-6", 2, 35)

# 2. SEA #6  Nick Franklin (X - X - 5)
t8.new_ab()
t8.pitch_list("c b b b")
t8.reach("FC3-6")

# 3. SEA #15 Kyle Seager (X - X - 6)
t8.new_ab()
t8.pitch_list("b")
t8.out("F7")


# Bot 8th
# Pitching: SEA #41 Charlie Furbush
b8 = game.new_inning()

# Pitching change (SEA): #41 Charlie Furbush replaces #34 Félix Hernández
b8.pitching_substitution(41)

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("L9")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("c s")
b8.out("G4-1")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 5th
b8.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c b b")
b8.reach("BB")

# 6. BOS #7  Stephen Drew (X - X - 5)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #35 Steven Wright
t9 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t9.defensive_switch(5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
t9.defensive_switch(29, "3")

# 4. SEA #8  Kendrys Morales (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "55 1B")
t9.thrown_out(3, "55 7-5", 1, 35)

# 5. SEA #55 Michael Saunders (X - X - 8)
t9.new_ab()
t9.pitch_list("f s b f f b")
t9.hit(1)
t9.advance(2, "T")

# 6. SEA #17 Justin Smoak (X - 55 - X)
t9.new_ab()
t9.pitch_list("b b c f b f c")
t9.out("!K")

# 7. SEA #9  Endy Chavez (X - 55 - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L7")


# Bot 9th
# Pitching: SEA #54 Tom Wilhelmsen
b9 = game.new_inning()

# Pitching change (SEA): #54 Tom Wilhelmsen replaces #41 Charlie Furbush
b9.pitching_substitution(54)

# 7. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("b b b b")
b9.reach("BB")
b9.advance(2, "20 1B")
b9.advance(4, "26 2B")

# 8. BOS #20 Ryan Lavarnway (X - X - 29)
b9.new_ab()
b9.pitch_list("b c f f d")
b9.hit(1)
b9.advance(3, "26 2B")
b9.advance(4, "18 1B")

# 9. BOS #26 Brock Holt (X - 29 - 20)
b9.new_ab()
b9.pitch_list("c b b")
b9.hit(2, rbis=1)
b9.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (20 - 26 - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.advance(2, "18 1B")
b9.advance(4, "15 1B")

# Pitching change (SEA): #59 Oliver Pérez replaces #54 Tom Wilhelmsen
b9.pitching_substitution(59)

# 2. BOS #18 Shane Victorino (20 - 26 - 2)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1, rbis=2)
b9.advance(2, "15 1B")
b9.advance(4, "5 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1, rbis=1)
b9.advance(2, "5 1B")
b9.advance(3, "7 BB")
b9.advance(4, "29 1B")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# Pitching change (SEA): #31 Yoervis Medina replaces #59 Oliver Pérez
b9.pitching_substitution(31)

# 5. BOS #5  Jonny Gomes (X - 18 - 15)
b9.new_ab()
b9.pitch_list("c c b b f b")
b9.hit(1, rbis=1)
b9.advance(2, "7 BB")
b9.advance(3, "29 1B")

# 6. BOS #7  Stephen Drew (X - 15 - 5)
b9.new_ab()
b9.pitch_list("s f b b b b")
b9.reach("BB")
b9.advance(2, "29 1B")

# 7. BOS #29 Daniel Nava (15 - 5 - 7)
b9.new_ab()
b9.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #35 Steven Wright
game.winning_pitcher(35)

# Loser team: SEA
# LP: SEA #59 Oliver Pérez
game.losing_pitcher(59, is_away_team=True)

# print(game)
game.generate_scorecard()
