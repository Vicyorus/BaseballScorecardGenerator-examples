import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SEA, 2013-07-09
# https://www.baseball-reference.com/boxes/SEA/SEA201307090.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2013/07/09/348097/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-09 22:10-01:54 +1",
        "at": "Safeco Field, Seattle, WA",
        "att": "21,076",
        "temp": "79F, Clear",
        "wind": "2mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                26: "Brock Holt",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                2: "Jacoby Ellsbury",
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 31, 22],
            "lineup": [
                [29, "7"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [10, "6"],
                [26, "5"],
                [44, "8"],
            ],
            "bench": [
                [2, "CF"],
                [37, "1B"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [40, 41, 67, 32, 91, 31, 36, 19, 22, 46],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 18,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                28: "Raul Ibanez",
                8: "Kendrys Morales",
                15: "Kyle Seager",
                17: "Justin Smoak",
                55: "Michael Saunders",
                3: "Mike Zunino",
                13: "Dustin Ackley",
                # Starting pitcher
                18: "Hisashi Iwakuma",
                # Bench
                26: "Brendan Ryan",
                9: "Endy Chavez",
                12: "Jason Bay",
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
                34: "Félix Hernández",
                54: "Tom Wilhelmsen",
                23: "Joe Saunders",
            },
            "lefties": [44, 41, 59, 23],
            "lineup": [
                [5, "6"],
                [6, "4"],
                [28, "7"],
                [8, "0"],
                [15, "5"],
                [17, "3"],
                [55, "9"],
                [3, "2"],
                [13, "8"],
            ],
            "bench": [
                [26, "SS"],
                [9, "CF"],
                [12, "LF"],
                [33, "C"],
            ],
            "bullpen": [44, 39, 40, 41, 59, 49, 58, 31, 34, 54, 23],
        },
        "umpires": {
            "HP": "Jim Joyce",
            "1B": "Cory Blaser",
            "2B": "Jeff Nelson",
            "3B": "Ed Hickox",
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
# Pitching: SEA #18 Hisashi Iwakuma
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b f c")
t1.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")


# Bot 1st
# Pitching: BOS #64 Allen Webster
b1 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b1.new_ab()
b1.out("P5")

# 2. SEA #6  Nick Franklin (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.thrown_out(2, "28 FC5-6", 2, 64)

# 3. SEA #28 Raul Ibanez (X - X - 6)
b1.new_ab()
b1.pitch_list("c f")
b1.reach("FC5-6")
b1.advance(4, "8 HR")

# 4. SEA #8  Kendrys Morales (X - X - 28)
b1.new_ab()
b1.pitch_list("f d s f b")
b1.hit(4, rbis=2)

# 5. SEA #15 Kyle Seager (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("G3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #18 Hisashi Iwakuma
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b f b")
t2.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G5-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b f b")
t2.hit(1)
t2.advance(2, "10 1B")
t2.advance(3, "26 G5-3")

# 7. BOS #10 Jose Iglesias (X - X - 39)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "26 G5-3")

# 8. BOS #26 Brock Holt (X - 39 - 10)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 9. BOS #44 Jackie Bradley Jr. (39 - 10 - X)
t2.new_ab()
t2.pitch_list("c f f f b f f f f c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #64 Allen Webster
b2 = game.new_inning()

# 6. SEA #17 Justin Smoak (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f")
b2.hit(1)
b2.advance(2, "55 BB")
b2.advance(3, "13 BB")
b2.advance(4, "5 2B")

# 7. SEA #55 Michael Saunders (X - X - 17)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(2, "13 BB")
b2.advance(4, "5 2B")

# 8. SEA #3  Mike Zunino (X - 17 - 55)
b2.new_ab()
b2.pitch_list("b s f b s")
b2.out("K")

# 9. SEA #13 Dustin Ackley (X - 17 - 55)
b2.new_ab()
b2.pitch_list("b b b d")
b2.reach("BB")
b2.advance(4, "5 2B")

# 1. SEA #5  Brad Miller (17 - 55 - 13)
b2.new_ab()
b2.pitch_list("s")
b2.hit(2, rbis=3)

# 2. SEA #6  Nick Franklin (X - 5 - X)
b2.new_ab()
b2.pitch_list("c f b d b s")
b2.out("K")

# 3. SEA #28 Raul Ibanez (X - 5 - X)
b2.new_ab()
b2.pitch_list("s b c")
b2.out("(F)P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #18 Hisashi Iwakuma
t3 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c c")
t3.out("L7")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.hit(1)
t3.advance(4, "15 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t3.new_ab()
t3.pitch_list("b d")
t3.hit(4, rbis=2)

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(2)
t3.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (X - 34 - X)
t3.new_ab()
t3.hit(4, rbis=2)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(2)
t3.advance(3, "10 WP")
t3.advance(4, "26 SF9")

# 7. BOS #10 Jose Iglesias (X - 39 - X)
t3.new_ab()
t3.pitch_list("c s b s")
t3.wp()
t3.reach("K")

# 8. BOS #26 Brock Holt (39 - X - 10)
t3.new_ab()
t3.out("SF9", rbis=1)

# 9. BOS #44 Jackie Bradley Jr. (X - X - 10)
t3.new_ab()
t3.out("G3")


# Bot 3rd
# Pitching: BOS #64 Allen Webster
b3 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b3.new_ab()
b3.hit(4)

# 5. SEA #15 Kyle Seager (X - X - X)
b3.new_ab()
b3.hit(1)
b3.advance(4, "55 3B")

# 6. SEA #17 Justin Smoak (X - X - 15)
b3.new_ab()
b3.pitch_list("b 1 1 1")
b3.out("L9")

# Pitching change (BOS): #91 Alfredo Aceves replaces #64 Allen Webster
b3.pitching_substitution(91)

# 7. SEA #55 Michael Saunders (X - X - 15)
b3.new_ab()
b3.pitch_list("f b d s")
b3.hit(3, rbis=1)

# 8. SEA #3  Mike Zunino (55 - X - X)
b3.new_ab()
b3.pitch_list("b s")
b3.out("G6-3")

# 9. SEA #13 Dustin Ackley (55 - X - X)
b3.new_ab()
b3.pitch_list("b d f b")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #49 Blake Beavan
t4 = game.new_inning()

# Pitching change (SEA): #49 Blake Beavan replaces #18 Hisashi Iwakuma
t4.pitching_substitution(49)

# 1. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.reach("HBP")
t4.advance(2, "18 BB")
t4.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 29)
t4.new_ab()
t4.pitch_list("b c b b b")
t4.reach("BB")
t4.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 29 - 18)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - 18 - 15)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")

# 5. BOS #12 Mike Napoli (X - 18 - 15)
t4.new_ab()
t4.pitch_list("c b s s")
t4.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - 18 - 15)
t4.new_ab()
t4.pitch_list("c b f f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #32 Craig Breslow
b4 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #91 Alfredo Aceves
b4.pitching_substitution(32)

# 1. SEA #5  Brad Miller (X - X - X)
b4.new_ab()
b4.pitch_list("l c b f b")
b4.hit(1)
b4.advance(3, "8 1B")

# 2. SEA #6  Nick Franklin (X - X - 5)
b4.new_ab()
b4.out("(F)F9")

# 3. SEA #28 Raul Ibanez (X - X - 5)
b4.new_ab()
b4.pitch_list("b b s f f f")
b4.out("F8")

# 4. SEA #8  Kendrys Morales (X - X - 5)
b4.new_ab()
b4.pitch_list("1 b b s")
b4.hit(1)

# 5. SEA #15 Kyle Seager (5 - X - 8)
b4.new_ab()
b4.pitch_list("b f b")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #49 Blake Beavan
t5 = game.new_inning()

# 7. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 8. BOS #26 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("(F)P5")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(4)

# 1. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("f b b b s")
t5.out("F7")


# Bot 5th
# Pitching: BOS #32 Craig Breslow
b5 = game.new_inning()

# 6. SEA #17 Justin Smoak (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 7. SEA #55 Michael Saunders (X - X - X)
b5.new_ab()
b5.pitch_list("l b b s f s")
b5.out("K")

# 8. SEA #3  Mike Zunino (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c f b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #40 Danny Farquhar
t6 = game.new_inning()

# Pitching change (SEA): #40 Danny Farquhar replaces #49 Blake Beavan
t6.pitching_substitution(40)

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("s b f b s")
t6.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b b")
t6.reach("BB")
t6.advance(3, "34 2B")

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("b c c f d f")
t6.hit(2)

# 5. BOS #12 Mike Napoli (15 - 34 - X)
t6.new_ab()
t6.pitch_list("c s b b d f c")
t6.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (15 - 34 - X)
t6.new_ab()
t6.pitch_list("c s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #32 Craig Breslow
b6 = game.new_inning()

# 9. SEA #13 Dustin Ackley (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 1. SEA #5  Brad Miller (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s")
b6.hit(2)

# Pitching change (BOS): #40 Andrew Bailey replaces #32 Craig Breslow
b6.pitching_substitution(40)

# 2. SEA #6  Nick Franklin (X - 5 - X)
b6.new_ab()
b6.pitch_list("b c f b s")
b6.out("K")

# 3. SEA #28 Raul Ibanez (X - 5 - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #40 Danny Farquhar
t7 = game.new_inning()

# 7. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.out("G6-3")

# 8. BOS #26 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")

# Pitching change (SEA): #41 Charlie Furbush replaces #40 Danny Farquhar
t7.pitching_substitution(41)

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f s b b b b")
t7.reach("BB")

# 1. BOS #29 Daniel Nava (X - X - 44)
t7.new_ab()
t7.pitch_list("b f 1 c 1 c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #40 Andrew Bailey
b7 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b7.new_ab()
b7.pitch_list("c f f f f f")
b7.out("G4-3")

# 5. SEA #15 Kyle Seager (X - X - X)
b7.new_ab()
b7.hit(1)
b7.thrown_out(2, "17 DP3-6-1", 2, 40)

# 6. SEA #17 Justin Smoak (X - X - 15)
b7.new_ab()
b7.pitch_list("b b")
b7.out("DP3-6-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #41 Charlie Furbush
t8 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("L4")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c s b b")
t8.hit(1)
t8.advance(2, "12 SB")
t8.advance(4, "10 1B")

# Pitching change (SEA): #58 Carter Capps replaces #41 Charlie Furbush
t8.pitching_substitution(58)

# 5. BOS #12 Mike Napoli (X - X - 34)
t8.new_ab()
t8.pitch_list("b s f f c")
t8.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - X)
t8.new_ab()
t8.pitch_list("i i i i")
t8.reach("IBB")
t8.advance(3, "10 1B")
t8.advance(4, "26 1B")

# 7. BOS #10 Jose Iglesias (X - 34 - 39)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1, rbis=1)
t8.advance(3, "26 1B")

# 8. BOS #26 Brock Holt (39 - X - 10)
t8.new_ab()
t8.hit(1, rbis=1)

# Pitching change (SEA): #44 Lucas Luetge replaces #58 Carter Capps
t8.pitching_substitution(44)

# 9. BOS #44 Jackie Bradley Jr. (10 - X - 26)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K2-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #40 Andrew Bailey
b8.pitching_substitution(36)

# 7. SEA #55 Michael Saunders (X - X - X)
b8.new_ab()
b8.pitch_list("b s b c b")
b8.hit(1)
b8.advance(3, "13 1B")
b8.advance(4, "5 G3")

# 8. SEA #3  Mike Zunino (X - X - 55)
b8.new_ab()
b8.pitch_list("b f b")
b8.out("F8")

# 9. SEA #13 Dustin Ackley (X - X - 55)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(1)
b8.advance(2, "5 G3")

# 1. SEA #5  Brad Miller (55 - X - 13)
b8.new_ab()
b8.pitch_list("b f c b d")
b8.out("G3", rbis=1)

# 2. SEA #6  Nick Franklin (X - 13 - X)
b8.new_ab()
b8.pitch_list("b s c t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #44 Lucas Luetge
t9 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b s b c")
t9.hit(1)
t9.thrown_out(2, "15 DP6-4-3", 2, 44)

# 2. BOS #18 Shane Victorino (X - X - 29)
t9.new_ab()
t9.pitch_list("b c")
t9.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t9.new_ab()
t9.pitch_list("b b d c")
t9.out("DP6-4-3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b9.pitching_substitution(19)

# 3. SEA #28 Raul Ibanez (X - X - X)
b9.new_ab()
b9.pitch_list("c s")
b9.out("G5-3")

# 4. SEA #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.out("G5-3")

# 5. SEA #15 Kyle Seager (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("P2")

# Winning team: BOS
# WP: BOS #32 Craig Breslow
game.winning_pitcher(32, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: SEA
# LP: SEA #49 Blake Beavan
game.losing_pitcher(49)

# print(game)
game.generate_scorecard()
