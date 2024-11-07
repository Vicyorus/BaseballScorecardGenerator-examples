import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-05-15
# https://www.baseball-reference.com/boxes/TBA/TBA201305150.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/05/15/347333/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-15 19:10-22:41",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "15,767",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [39, "2"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 14,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                2: "Kelly Johnson",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                11: "Yunel Escobar",
                21: "James Loney",
                1: "Sean Rodríguez",
                28: "José Molina",
                19: "Ryan Roberts",
                # Starting pitcher
                14: "David Price",
                # Bench
                30: "Luke Scott",
                20: "Matt Joyce",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                # Bullpen
                58: "Jeremy Hellickson",
                53: "Alex Cobb",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [14, 55, 57, 27],
            "lineup": [
                [8, "8"],
                [2, "0"],
                [18, "9"],
                [3, "5"],
                [11, "6"],
                [21, "3"],
                [1, "7"],
                [28, "2"],
                [19, "4"],
            ],
            "bench": [
                [30, "DH"],
                [20, "RF"],
                [59, "C"],
                [5, "LF"],
            ],
            "bullpen": [58, 53, 55, 62, 35, 43, 57, 27, 52, 56, 40],
        },
        "umpires": {
            "HP": "Sam Holbrook",
            "1B": "Joe West",
            "2B": "David Rackley",
            "3B": "Rob Drake",
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
# Pitching: TBR #14 David Price
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b c c")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b s")
t1.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b f")
t1.out("L7")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b1.new_ab()
b1.pitch_list("b b t c b f f f f")
b1.hit(1)
b1.advance(2, "18 SB")

# 2. TBR #2  Kelly Johnson (X - X - 8)
b1.new_ab()
b1.pitch_list("f s")
b1.out("F8")

# 3. TBR #18 Ben Zobrist (X - X - 8)
b1.new_ab(is_risp=True)
b1.pitch_list("c s b b b s")
b1.out("K")

# 4. TBR #3  Evan Longoria (X - 8 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("L1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #14 David Price
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("s b b")
t2.out("G5-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("P3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)

# 8. BOS #39 Jarrod Saltalamacchia (X - 16 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. TBR #11 Yunel Escobar (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G6-3")

# 6. TBR #21 James Loney (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(1)
b2.advance(2, "1 WP")
b2.thrown_out(2, "1 FC6-4", 2, 31)

# 7. TBR #1  Sean Rodríguez (X - X - 21)
b2.new_ab(is_risp=True)
b2.pitch_list("f f f d d b")
b2.wp()
b2.reach("FC6-4")

# 8. TBR #28 José Molina (X - X - 1)
b2.new_ab()
b2.pitch_list("c c f f")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #14 David Price
t3 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("f b b f b f f b")
t3.reach("BB")
t3.advance(2, "2 1B")
t3.advance(4, "15 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t3.new_ab()
t3.pitch_list("c b b b")
t3.hit(1)
t3.advance(3, "15 1B")
t3.advance(4, "34 1B")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b")
t3.out("L7")

# 3. BOS #15 Dustin Pedroia (X - 7 - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b")
t3.hit(1, rbis=1)
t3.advance(2, "34 1B")
t3.advance(4, "12 2B")

# 4. BOS #34 David Ortiz (2 - X - 15)
t3.new_ab(is_risp=True)
t3.pitch_list("c f f b f f")
t3.hit(1, rbis=1)
t3.advance(3, "12 2B")
t3.advance(4, "5 1B")

# Pitching change (TBR): #35 Jamey Wright replaces #14 David Price
t3.pitching_substitution(35)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("s")
t3.hit(2, rbis=1)
t3.advance(3, "5 1B")
t3.advance(4, "7 HR")

# 6. BOS #5  Jonny Gomes (34 - 12 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=1)
t3.advance(2, "39 BB")
t3.advance(4, "7 HR")

# 7. BOS #16 Will Middlebrooks (12 - X - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("b 1 1 f 1")
t3.out("F8")

# 8. BOS #39 Jarrod Saltalamacchia (12 - X - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("b 1 b b b")
t3.reach("BB")
t3.advance(4, "7 HR")

# 9. BOS #7  Stephen Drew (12 - 5 - 39)
t3.new_ab(is_risp=True)
t3.pitch_list("c b")
t3.hit(4, rbis=4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c f f t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. TBR #19 Ryan Roberts (X - X - X)
b3.new_ab()
b3.pitch_list("b c f f")
b3.hit(1)
b3.advance(4, "8 3B")

# 1. TBR #8  Desmond Jennings (X - X - 19)
b3.new_ab()
b3.pitch_list("b")
b3.hit(3, rbis=1)
b3.advance(4, "18 G5-3")

# 2. TBR #2  Kelly Johnson (8 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c")
b3.out("P6")

# 3. TBR #18 Ben Zobrist (8 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("s b")
b3.out("G5-3", rbis=1)

# 4. TBR #3  Evan Longoria (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #35 Jamey Wright
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("b b c")
t4.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c b b t")
t4.out("G5-3")

# Pitching change (TBR): #27 Cesár Ramos replaces #35 Jamey Wright
t4.pitching_substitution(27)

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b b c s")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 5. TBR #11 Yunel Escobar (X - X - X)
b4.new_ab()
b4.pitch_list("f b c")
b4.out("F8")

# 6. TBR #21 James Loney (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")

# 7. TBR #1  Sean Rodríguez (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(3, "28 1B")

# 8. TBR #28 José Molina (X - X - 1)
b4.new_ab()
b4.hit(1)

# 9. TBR #19 Ryan Roberts (1 - X - 28)
b4.new_ab(is_risp=True)
b4.pitch_list("d f b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #27 Cesár Ramos
t5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("f b c b f s")
t5.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("f s b")
t5.out("G1-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c s b s")
t5.out("K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G6-3")

# 2. TBR #2  Kelly Johnson (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("F7")

# 3. TBR #18 Ben Zobrist (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #27 Cesár Ramos
t6 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.out("L8")

# 9. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c b s b f")
t6.hit(2)
t6.advance(3, "18 WP")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.out("(F)P5")

# 2. BOS #18 Shane Victorino (X - 7 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b c c f")
t6.wp()
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b6.new_ab()
b6.pitch_list("c s b c")
b6.out("!K")

# 5. TBR #11 Yunel Escobar (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(2)

# 6. TBR #21 James Loney (X - 11 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("d c c b f s")
b6.out("K")

# 7. TBR #1  Sean Rodríguez (X - 11 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c d")
b6.reach("HBP")

# 8. TBR #28 José Molina (X - 11 - 1)
b6.new_ab(is_risp=True)
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #27 Cesár Ramos
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b f")
t7.out("G3-1")

# Pitching change (TBR): #43 Kyle Farnsworth replaces #27 Cesár Ramos
t7.pitching_substitution(43)

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# Defensive change (BOS): #29 Daniel Nava replaces #5 Jonny Gomes (LF), playing LF, batting 6th
b7.defensive_substitution(6, 29, "7")

# 9. TBR #19 Ryan Roberts (X - X - X)
b7.new_ab()
b7.hit(1)
b7.thrown_out(2, "2 FC5-4", 2, 31)

# 1. TBR #8  Desmond Jennings (X - X - 19)
b7.new_ab()
b7.pitch_list("f")
b7.out("F9")

# 2. TBR #2  Kelly Johnson (X - X - 19)
b7.new_ab()
b7.pitch_list("b b c c f")
b7.reach("FC5-4")
b7.thrown_out(2, "18 FC5-4", 3, 31)

# 3. TBR #18 Ben Zobrist (X - X - 2)
b7.new_ab()
b7.pitch_list("b")
b7.reach("FC5-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #43 Kyle Farnsworth
t8 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("G3-1")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.hit(4)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f s")
t8.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b c c s")
t8.out("K")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #31 Jon Lester
b8.pitching_substitution(19)

# 4. TBR #3  Evan Longoria (X - X - X)
b8.new_ab()
b8.pitch_list("f b f f b")
b8.hit(1)
b8.thrown_out(2, "11 FC6-4", 1, 19)

# 5. TBR #11 Yunel Escobar (X - X - 3)
b8.new_ab()
b8.pitch_list("c f b")
b8.reach("FC6-4")
b8.advance(2, "21 BB")

# 6. TBR #21 James Loney (X - X - 11)
b8.new_ab()
b8.pitch_list("b b c b b")
b8.reach("BB")

# Offensive change (TBR): Pinch-hitter #20 Matt Joyce replaces #1 Sean Rodríguez, batting 7th
b8.offensive_substitution(7, 20, "PH")

# 7. TBR #20 Matt Joyce (X - 11 - 21)
b8.new_ab(is_risp=True)
b8.pitch_list("s t f f f b f b f")
b8.out("F7")

# Offensive change (TBR): Pinch-hitter #30 Luke Scott replaces #28 José Molina, batting 8th
b8.offensive_substitution(8, 30, "PH")

# 8. TBR #30 Luke Scott (X - 11 - 21)
b8.new_ab(is_risp=True)
b8.pitch_list("b s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #52 Josh Lueke
t9 = game.new_inning()

# Pitching change (TBR): #52 Josh Lueke replaces #43 Kyle Farnsworth
t9.pitching_substitution(52)

# Defensive switch (TBR): #18 Ben Zobrist moves to 2B
t9.defensive_switch(18, "4")

# Defensive switch (TBR): #20 Matt Joyce moves to RF
t9.defensive_switch(20, "9")

# Defensive switch (TBR): #30 Luke Scott moves to LF
t9.defensive_switch(30, "7")

# Defensive change (TBR): #59 Jose Lobaton replaces #19 Ryan Roberts (2B), playing C, batting 9th
t9.defensive_substitution(9, 59, "2")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c f b")
t9.reach("BB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t9.new_ab()
t9.pitch_list("c b c f f")
t9.out("(F)P2")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t9.new_ab()
t9.pitch_list("f s f")
t9.out("F8")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #34 David Ortiz, batting 4th
t9.offensive_substitution(4, 37, "PH")

# 4. BOS #37 Mike Carp (X - X - 2)
t9.new_ab()
t9.pitch_list("c b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #65 Jose De La Torre
b9 = game.new_inning()

# Pitching change (BOS): #65 Jose De La Torre replaces #19 Koji Uehara
b9.pitching_substitution(65)

# Defensive switch (BOS): #37 Mike Carp moves to DH
b9.defensive_switch(37, "0")

# 9. TBR #59 Jose Lobaton (X - X - X)
b9.new_ab()
b9.pitch_list("b s b b f")
b9.out("G3")

# 1. TBR #8  Desmond Jennings (X - X - X)
b9.new_ab()
b9.pitch_list("b f s s")
b9.out("K")

# 2. TBR #2  Kelly Johnson (X - X - X)
b9.new_ab()
b9.pitch_list("c b b c b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: TBR
# LP: TBR #14 David Price
game.losing_pitcher(14)

# print(game)
game.generate_scorecard()
