import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SEA, 2013-07-10
# https://www.baseball-reference.com/boxes/SEA/SEA201307100.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2013/07/10/348112/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-10 22:10-01:33 +1",
        "at": "Safeco Field, Seattle, WA",
        "att": "20,468",
        "temp": "69F, Partly Cloudy",
        "wind": "2mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                26: "Brock Holt",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                44: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
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
                46: "Ryan Dempster",
            },
            "lefties": [22, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [10, "6"],
                [26, "5"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [44, "CF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 40, 41, 67, 32, 31, 36, 19, 54, 46],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 39,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                28: "Raul Ibanez",
                8: "Kendrys Morales",
                15: "Kyle Seager",
                12: "Jason Bay",
                17: "Justin Smoak",
                55: "Michael Saunders",
                33: "Henry Blanco",
                # Starting pitcher
                39: "Aaron Harang",
                # Bench
                26: "Brendan Ryan",
                9: "Endy Chavez",
                3: "Mike Zunino",
                13: "Dustin Ackley",
                # Bullpen
                44: "Lucas Luetge",
                40: "Danny Farquhar",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                49: "Blake Beavan",
                58: "Carter Capps",
                31: "Yoervis Medina",
                34: "Félix Hernández",
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
                [55, "8"],
                [33, "2"],
            ],
            "bench": [
                [26, "SS"],
                [9, "CF"],
                [3, "C"],
                [13, "2B"],
            ],
            "bullpen": [44, 40, 41, 59, 49, 58, 31, 34, 54, 23, 18],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Jeff Nelson",
            "2B": "Ed Hickox",
            "3B": "Jim Joyce",
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
# Pitching: SEA #39 Aaron Harang
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(1)
t1.thrown_out(2, "18 DP6-4-3", 1, 39)

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c b")
t1.out("DP6-4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b c b f")
t1.out("G3-1")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G6-3")

# 2. SEA #6  Nick Franklin (X - X - X)
b1.new_ab()
b1.pitch_list("c b f s")
b1.out("K")

# 3. SEA #28 Raul Ibanez (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #39 Aaron Harang
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b")
t2.hit(2)
t2.advance(3, "29 HBP")
t2.advance(4, "39 SF7")

# 5. BOS #12 Mike Napoli (X - 34 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("f f b b f b b")
t2.reach("BB")
t2.advance(2, "29 HBP")
t2.advance(3, "39 SF7")
t2.advance(4, "10 SF9")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b")
t2.reach("HBP")
t2.advance(2, "39 SF7")
t2.advance(3, "10 SF9")

# 7. BOS #39 Jarrod Saltalamacchia (34 - 12 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("b s c")
t2.out("SF7", rbis=1)

# 8. BOS #10 Jose Iglesias (12 - 29 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c s f")
t2.out("SF9", rbis=1)

# 9. BOS #26 Brock Holt (29 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 4. SEA #8  Kendrys Morales (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f f c")
b2.out("!K")

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.thrown_out(2, "12 FC6-4", 2, 22)

# 6. SEA #12 Jason Bay (X - X - 15)
b2.new_ab()
b2.pitch_list("s b c b b")
b2.reach("FC6-4")
b2.thrown_out(2, "17 FC5-4", 3, 22)

# 7. SEA #17 Justin Smoak (X - X - 12)
b2.new_ab()
b2.pitch_list("1 b f b c f")
b2.reach("FC5-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #39 Aaron Harang
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f")
t3.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b c b")
t3.reach("BB")
t3.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("c")
t3.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b b b")
t3.reach("BB")
t3.advance(3, "29 1B")

# 6. BOS #29 Daniel Nava (X - X - 12)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (12 - X - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 8. SEA #55 Michael Saunders (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c")
b3.out("G6-3")

# 9. SEA #33 Henry Blanco (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("(F)P2")

# 1. SEA #5  Brad Miller (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "6 FC6-4", 3, 22)

# 2. SEA #6  Nick Franklin (X - X - 5)
b3.new_ab()
b3.pitch_list("b s c")
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #39 Aaron Harang
t4 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G5-3")

# 9. BOS #26 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.hit(2)
t4.advance(4, "18 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c f")
t4.hit(1, rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t4.new_ab()
t4.pitch_list("f b b")
t4.out("F8")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 3. SEA #28 Raul Ibanez (X - X - X)
b4.new_ab()
b4.pitch_list("b c b f b b")
b4.reach("BB")

# 4. SEA #8  Kendrys Morales (X - X - 28)
b4.new_ab()
b4.pitch_list("b f d")
b4.out("F8")

# 5. SEA #15 Kyle Seager (X - X - 28)
b4.new_ab()
b4.pitch_list("f")
b4.out("F8")

# 6. SEA #12 Jason Bay (X - X - 28)
b4.new_ab()
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #39 Aaron Harang
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("F8")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 7. SEA #17 Justin Smoak (X - X - X)
b5.new_ab()
b5.pitch_list("f b c b s")
b5.out("K")

# 8. SEA #55 Michael Saunders (X - X - X)
b5.new_ab()
b5.hit(2)

# 9. SEA #33 Henry Blanco (X - 55 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("P5")

# 1. SEA #5  Brad Miller (X - 55 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c d b b b")
b5.reach("BB")

# 2. SEA #6  Nick Franklin (X - 55 - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("s d b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #39 Aaron Harang
t6 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.advance(2, "10 1B")
t6.advance(3, "26 FC3-6")
t6.advance(4, "2 1B")

# 8. BOS #10 Jose Iglesias (X - X - 39)
t6.new_ab()
t6.pitch_list("c t")
t6.hit(1)
t6.thrown_out(2, "26 FC3-6", 1, 44)

# Pitching change (SEA): #44 Lucas Luetge replaces #39 Aaron Harang
t6.pitching_substitution(44)

# 9. BOS #26 Brock Holt (X - 39 - 10)
t6.new_ab(is_risp=True)
t6.pitch_list("s b")
t6.reach("FC3-6")
t6.advance(3, "2 1B")
t6.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (39 - X - 26)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)
t6.advance(2, "18 1B")
t6.error(6)
t6.advance(3, "15 FC6")
t6.advance("U", "15 E6")

# 2. BOS #18 Shane Victorino (26 - X - 2)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)
t6.advance(3, "15 E6")
t6.advance("U", "34 SF8")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c")
t6.reach("FC6")
t6.thrown_out(2, "12 FC4", 3, 58)

# 4. BOS #34 David Ortiz (18 - X - 15)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.out("SF8", rbis=1)

# Pitching change (SEA): #58 Carter Capps replaces #44 Lucas Luetge
t6.pitching_substitution(58)

# 5. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("b b c")
t6.reach("FC4")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# Defensive change (BOS): #44 Jackie Bradley Jr. replaces #18 Shane Victorino (RF), playing RF, batting 2nd
b6.defensive_substitution(2, 44, "9/8")

# 3. SEA #28 Raul Ibanez (X - X - X)
b6.new_ab()
b6.pitch_list("c b b c s")
b6.out("K")

# 4. SEA #8  Kendrys Morales (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")

# 5. SEA #15 Kyle Seager (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b f")
b6.out("G3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #58 Carter Capps
t7 = game.new_inning()

# Defensive switch (SEA): #5 Brad Miller moves to 2B
t7.defensive_switch(5, "4")

# Defensive change (SEA): #26 Brendan Ryan replaces #6 Nick Franklin (2B), playing SS, batting 2nd
t7.defensive_substitution(2, 26, "6")

# Defensive change (SEA): #13 Dustin Ackley replaces #28 Raul Ibanez (LF), playing LF, batting 3rd
t7.defensive_substitution(3, 13, "7")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c b b")
t7.reach("BB")
t7.thrown_out(2, "39 FC4-6", 1, 58)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t7.new_ab()
t7.pitch_list("f")
t7.reach("FC4-6")
t7.advance(2, "10 HBP")
t7.advance(3, "26 BB")

# 8. BOS #10 Jose Iglesias (X - X - 39)
t7.new_ab()
t7.reach("HBP")
t7.advance(2, "26 BB")

# 9. BOS #26 Brock Holt (X - 39 - 10)
t7.new_ab(is_risp=True)
t7.pitch_list("f b b b b")
t7.reach("BB")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #2 Jacoby Ellsbury, batting 1st
t7.offensive_substitution(1, 37, "PH")

# 1. BOS #37 Mike Carp (39 - 10 - 26)
t7.new_ab(is_risp=True)
t7.pitch_list("d b s f c")
t7.out("!K")

# 2. BOS #44 Jackie Bradley Jr. (39 - 10 - 26)
t7.new_ab(is_risp=True)
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #22 Felix Doubront
b7 = game.new_inning()

# Defensive switch (BOS): #37 Mike Carp moves to LF
b7.defensive_switch(37, "7")

# Defensive switch (BOS): #44 Jackie Bradley Jr. moves to CF
b7.defensive_switch(44, "8")

# Defensive change (BOS): #23 Brandon Snyder replaces #15 Dustin Pedroia (2B), playing 3B, batting 3rd
b7.defensive_substitution(3, 23, "5")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b7.defensive_switch(29, "9")

# Defensive switch (BOS): #26 Brock Holt moves to 2B
b7.defensive_switch(26, "4")

# 6. SEA #12 Jason Bay (X - X - X)
b7.new_ab()
b7.pitch_list("b f c")
b7.hit(2)
b7.advance(3, "55 G4-3")
b7.advance(4, "33 1B")

# 7. SEA #17 Justin Smoak (X - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f b")
b7.out("F8")

# 8. SEA #55 Michael Saunders (X - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f d d c f")
b7.out("G4-3")

# 9. SEA #33 Henry Blanco (12 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.hit(1, rbis=1)

# 1. SEA #5  Brad Miller (X - X - 33)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #59 Oliver Pérez
t8 = game.new_inning()

# Pitching change (SEA): #59 Oliver Pérez replaces #58 Carter Capps
t8.pitching_substitution(59)

# 3. BOS #23 Brandon Snyder (X - X - X)
t8.new_ab()
t8.pitch_list("s b f b f b")
t8.out("L7")

# Offensive change (BOS): Pinch-hitter #20 Ryan Lavarnway replaces #34 David Ortiz, batting 4th
t8.offensive_substitution(4, 20, "PH")

# 4. BOS #20 Ryan Lavarnway (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("b f b c b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #67 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #22 Felix Doubront
b8.pitching_substitution(67)

# Defensive switch (BOS): #20 Ryan Lavarnway moves to DH
b8.defensive_switch(20, "0")

# 2. SEA #26 Brendan Ryan (X - X - X)
b8.new_ab()
b8.pitch_list("f b b s f f b")
b8.hit(4)

# 3. SEA #13 Dustin Ackley (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(2)
b8.advance(4, "8 2B")

# 4. SEA #8  Kendrys Morales (X - 13 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f b b")
b8.hit(2, rbis=1)
b8.advance(3, "15 L8")
b8.advance(4, "17 2B")

# 5. SEA #15 Kyle Seager (X - 8 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.out("L8")

# 6. SEA #12 Jason Bay (8 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c f f s")
b8.out("K")

# 7. SEA #17 Justin Smoak (8 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b s")
b8.hit(2, rbis=1)

# 8. SEA #55 Michael Saunders (X - 17 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #54 Tom Wilhelmsen
t9 = game.new_inning()

# Pitching change (SEA): #54 Tom Wilhelmsen replaces #59 Oliver Pérez
t9.pitching_substitution(54)

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b c b s b b")
t9.reach("BB")
t9.advance(2, "39 BB")
t9.advance(3, "10 F9")
t9.advance(4, "26 WP")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t9.new_ab()
t9.pitch_list("s b d c b b")
t9.reach("BB")
t9.advance(2, "26 WP")
t9.advance(3, "26 1B")
t9.advance(4, "37 1B")

# 8. BOS #10 Jose Iglesias (X - 29 - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("F9")

# 9. BOS #26 Brock Holt (29 - X - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("s b")
t9.wp()
t9.hit(1)
t9.advance(2, "37 1B")

# 1. BOS #37 Mike Carp (39 - X - 26)
t9.new_ab(is_risp=True)
t9.pitch_list("c f b f f f")
t9.hit(1, rbis=1)

# 2. BOS #44 Jackie Bradley Jr. (X - 26 - 37)
t9.new_ab(is_risp=True)
t9.pitch_list("c s f s")
t9.out("K")

# 3. BOS #23 Brandon Snyder (X - 26 - 37)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b b s f f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #67 Brandon Workman
b9 = game.new_inning()

# 9. SEA #33 Henry Blanco (X - X - X)
b9.new_ab()
b9.pitch_list("c b b t f c")
b9.out("!K")

# 1. SEA #5  Brad Miller (X - X - X)
b9.new_ab()
b9.pitch_list("f c b b f")
b9.out("L3")

# 2. SEA #26 Brendan Ryan (X - X - X)
b9.new_ab()
b9.pitch_list("b c f b f f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22, is_away_team=True)

# Loser team: SEA
# LP: SEA #39 Aaron Harang
game.losing_pitcher(39)

# print(game)
game.generate_scorecard()
