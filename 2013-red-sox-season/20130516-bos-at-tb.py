import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-05-16
# https://www.baseball-reference.com/boxes/TBA/TBA201305160.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/05/16/347347/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-16 19:12-22:55",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "16,055",
        "temp": "72F, Dome",
        "wind": "0mph, None",
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
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [7, "6"],
                [16, "5"],
                [39, "2"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 31, 59, 36, 11, 19, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 53,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                30: "Luke Scott",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                11: "Yunel Escobar",
                21: "James Loney",
                1: "Sean Rodríguez",
                59: "Jose Lobaton",
                19: "Ryan Roberts",
                # Starting pitcher
                53: "Alex Cobb",
                # Bench
                28: "José Molina",
                20: "Matt Joyce",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [8, "8"],
                [30, "0"],
                [18, "9"],
                [3, "5"],
                [11, "6"],
                [21, "3"],
                [1, "7"],
                [59, "2"],
                [19, "4"],
            ],
            "bench": [
                [28, "C"],
                [20, "RF"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 57, 54, 27, 52, 56, 40],
        },
        "umpires": {
            "HP": "Joe West",
            "1B": "David Rackley",
            "2B": "Rob Drake",
            "3B": "Sam Holbrook",
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
# Pitching: TBR #53 Alex Cobb
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b f s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b c b f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b1.new_ab()
b1.pitch_list("s b b c s")
b1.out("K")

# 2. TBR #30 Luke Scott (X - X - X)
b1.new_ab()
b1.pitch_list("c t")
b1.hit(1)
b1.advance(2, "18 BB")
b1.advance(3, "3 F8")

# 3. TBR #18 Ben Zobrist (X - X - 30)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "11 BB")

# 4. TBR #3  Evan Longoria (X - 30 - 18)
b1.new_ab(is_risp=True)
b1.out("F8")

# 5. TBR #11 Yunel Escobar (30 - X - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("d f b 1 f f d f f b")
b1.reach("BB")

# 6. TBR #21 James Loney (30 - 18 - 11)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #53 Alex Cobb
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("f f")
t2.out("G5-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b s b b s")
t2.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 7. TBR #1  Sean Rodríguez (X - X - X)
b2.new_ab()
b2.pitch_list("c c c")
b2.out("!K")

# 8. TBR #59 Jose Lobaton (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("F9")

# 9. TBR #19 Ryan Roberts (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(4)

# 1. TBR #8  Desmond Jennings (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #53 Alex Cobb
t3 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b c c f f b")
t3.out("F8")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("F8")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("L7")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 2. TBR #30 Luke Scott (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")
b3.advance(2, "3 1B")
b3.advance(3, "11 F8")

# 3. TBR #18 Ben Zobrist (X - X - 30)
b3.new_ab()
b3.pitch_list("c b b f c")
b3.out("!K")

# 4. TBR #3  Evan Longoria (X - X - 30)
b3.new_ab()
b3.pitch_list("c b b")
b3.hit(1)

# 5. TBR #11 Yunel Escobar (X - 30 - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("f b b")
b3.out("F8")

# 6. TBR #21 James Loney (30 - X - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("c b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #53 Alex Cobb
t4 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("L6")

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(2)
t4.advance(3, "15 G4-3")
t4.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c f")
t4.out("G4-3")

# 4. BOS #34 David Ortiz (18 - X - X)
t4.new_ab(is_risp=True)
t4.hit(1, rbis=1)

# 5. BOS #12 Mike Napoli (X - X - 34)
t4.new_ab()
t4.pitch_list("d s b f d t")
t4.out("KT")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 7. TBR #1  Sean Rodríguez (X - X - X)
b4.new_ab()
b4.pitch_list("c b c b f f b s")
b4.out("K")

# 8. TBR #59 Jose Lobaton (X - X - X)
b4.new_ab()
b4.pitch_list("c t b f b b s")
b4.out("K")

# 9. TBR #19 Ryan Roberts (X - X - X)
b4.new_ab()
b4.pitch_list("b c c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #53 Alex Cobb
t5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("L3")

# 7. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - 16)
t5.new_ab()
t5.pitch_list("s 1 1 b b s")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b5.new_ab()
b5.pitch_list("c l b s")
b5.out("K")

# 2. TBR #30 Luke Scott (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G4-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.advance(2, "3 BB")

# 4. TBR #3  Evan Longoria (X - X - 18)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 5. TBR #11 Yunel Escobar (X - 18 - 3)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #53 Alex Cobb
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b")
t6.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.out("G5-3")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 6. TBR #21 James Loney (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.thrown_out(2, "20 FC5-6", 1, 59)

# Pitching change (BOS): #59 Clayton Mortensen replaces #22 Felix Doubront
b6.pitching_substitution(59)

# Offensive change (TBR): Pinch-hitter #20 Matt Joyce replaces #1 Sean Rodríguez, batting 7th
b6.offensive_substitution(7, 20, "PH")

# 7. TBR #20 Matt Joyce (X - X - 21)
b6.new_ab()
b6.pitch_list("b")
b6.reach("FC5-6")
b6.advance(2, "59 BB")
b6.advance(3, "19 PB")
b6.advance(4, "8 1B")

# 8. TBR #59 Jose Lobaton (X - X - 20)
b6.new_ab()
b6.pitch_list("s f d b 1 1 b 1 b")
b6.reach("BB")
b6.advance(2, "19 PB")
b6.advance(3, "8 1B")
b6.advance(4, "30 1B")

# 9. TBR #19 Ryan Roberts (X - 20 - 59)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b b f b")
b6.pb()
b6.reach("BB")
b6.advance(2, "8 1B")
b6.advance(3, "30 1B")

# 1. TBR #8  Desmond Jennings (20 - 59 - 19)
b6.new_ab(is_risp=True)
b6.pitch_list("b b f f f")
b6.hit(1, rbis=1)
b6.advance(2, "30 1B")
b6.thrown_out(3, "3 FC5", 3, 30)

# Pitching change (BOS): #30 Andrew Miller replaces #59 Clayton Mortensen
b6.pitching_substitution(30)

# 2. TBR #30 Luke Scott (59 - 19 - 8)
b6.new_ab(is_risp=True)
b6.pitch_list("f f")
b6.hit(1, rbis=1)
b6.advance(2, "3 FC5")

# 3. TBR #18 Ben Zobrist (19 - 8 - 30)
b6.new_ab(is_risp=True)
b6.pitch_list("s c s")
b6.out("K")

# 4. TBR #3  Evan Longoria (19 - 8 - 30)
b6.new_ab(is_risp=True)
b6.pitch_list("b f s")
b6.reach("FC5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #53 Alex Cobb
t7 = game.new_inning()

# Defensive switch (TBR): #20 Matt Joyce moves to LF
t7.defensive_switch(20, "7")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b c f b")
t7.reach("BB")
t7.advance(2, "7 WP")

# 6. BOS #29 Daniel Nava (X - X - 12)
t7.new_ab()
t7.pitch_list("b f")
t7.out("F7")

# Pitching change (TBR): #57 Jake McGee replaces #53 Alex Cobb
t7.pitching_substitution(57)

# 7. BOS #7  Stephen Drew (X - X - 12)
t7.new_ab(is_risp=True)
t7.pitch_list("c c b f b")
t7.wp()
t7.out("P6")

# 8. BOS #16 Will Middlebrooks (X - 12 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("d b s c f b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #30 Andrew Miller
b7.pitching_substitution(32)

# 5. TBR #11 Yunel Escobar (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 6. TBR #21 James Loney (X - X - X)
b7.new_ab()
b7.pitch_list("b b f f b")
b7.out("G4-3")

# 7. TBR #20 Matt Joyce (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #62 Joel Peralta
t8 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #57 Jake McGee
t8.pitching_substitution(62)

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("c c b")
t8.out("P5")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("(F)P5")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b8.pitching_substitution(36)

# 8. TBR #59 Jose Lobaton (X - X - X)
b8.new_ab()
b8.out("F9")

# 9. TBR #19 Ryan Roberts (X - X - X)
b8.new_ab()
b8.pitch_list("f b c b c")
b8.out("!K")

# 1. TBR #8  Desmond Jennings (X - X - X)
b8.new_ab()
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #62 Joel Peralta
t9.pitching_substitution(56)

# Defensive change (TBR): #28 José Molina replaces #59 Jose Lobaton (C), playing C, batting 8th
t9.defensive_substitution(8, 28, "2")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b c b")
t9.reach("BB")
t9.advance(2, "34 BB")
t9.advance(3, "29 BB")
t9.advance(4, "16 2B")

# 4. BOS #34 David Ortiz (X - X - 15)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #34 David Ortiz
t9.offensive_substitution(4, 23, "PR")
t9.atbase("PR")
t9.advance(2, "29 BB")
t9.advance(4, "16 2B")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t9.new_ab(is_risp=True)
t9.pitch_list("b c f b s")
t9.out("K")

# 6. BOS #29 Daniel Nava (X - 15 - 23)
t9.new_ab(is_risp=True)
t9.pitch_list("b f b s b f d")
t9.reach("BB")
t9.advance(4, "16 2B")

# 7. BOS #7  Stephen Drew (15 - 23 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("c s s")
t9.out("K")

# 8. BOS #16 Will Middlebrooks (15 - 23 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("c f b")
t9.hit(2, rbis=3)

# 9. BOS #39 Jarrod Saltalamacchia (X - 16 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("d s b b s b")
t9.reach("BB")

# Pitching change (TBR): #54 Alex Torres replaces #56 Fernando Rodney
t9.pitching_substitution(54)

# 1. BOS #2  Jacoby Ellsbury (X - 16 - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("b c s f")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #36 Junichi Tazawa
b9 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #18 Shane Victorino (RF), playing LF, batting 2nd
b9.defensive_substitution(2, 5, "7")

# Defensive switch (BOS): #23 Pedro Ciriaco moves to DH
b9.defensive_switch(23, "0")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b9.defensive_switch(29, "9")

# 2. TBR #30 Luke Scott (X - X - X)
b9.new_ab()
b9.pitch_list("s b c")
b9.hit(1)
# Offensive change (TBR): Pinch-runner #5 Sam Fuld replaces #30 Luke Scott
b9.offensive_substitution(2, 5, "PR")
b9.atbase("PR")
b9.advance(2, "11 1B")

# 3. TBR #18 Ben Zobrist (X - X - 30)
b9.new_ab()
b9.pitch_list("b f")
b9.out("L6")

# 4. TBR #3  Evan Longoria (X - X - 5)
b9.new_ab()
b9.pitch_list("c c s")
b9.out("K")

# 5. TBR #11 Yunel Escobar (X - X - 5)
b9.new_ab()
b9.pitch_list("b f f f")
b9.hit(1)

# 6. TBR #21 James Loney (X - 5 - 11)
b9.new_ab(is_risp=True)
b9.pitch_list("c s")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #36 Junichi Tazawa
game.winning_pitcher(36, is_away_team=True)

# Loser team: TBR
# LP: TBR #56 Fernando Rodney
game.losing_pitcher(56)

# print(game)
game.generate_scorecard()
