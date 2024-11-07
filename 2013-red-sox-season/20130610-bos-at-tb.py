import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-06-10
# https://www.baseball-reference.com/boxes/TBA/TBA201306100.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/06/10/347696/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-10 19:12-00:36 +1",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "15,477",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                3: "David Ross",
                10: "Jose Iglesias",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                # Bullpen
                40: "Andrew Bailey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [37, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [10, "2B"],
                [12, "1B"],
                [5, "LF"],
            ],
            "bullpen": [40, 56, 30, 32, 19, 31, 59, 36, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 53,
            "roster": {
                # Lineup
                20: "Matt Joyce",
                18: "Ben Zobrist",
                2: "Kelly Johnson",
                3: "Evan Longoria",
                21: "James Loney",
                30: "Luke Scott",
                8: "Desmond Jennings",
                59: "Jose Lobaton",
                11: "Yunel Escobar",
                # Starting pitcher
                53: "Alex Cobb",
                # Bench
                28: "José Molina",
                1: "Sean Rodríguez",
                19: "Ryan Roberts",
                5: "Sam Fuld",
                # Bullpen
                58: "Jeremy Hellickson",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [20, "9"],
                [18, "4"],
                [2, "7"],
                [3, "5"],
                [21, "3"],
                [30, "0"],
                [8, "8"],
                [59, "2"],
                [11, "6"],
            ],
            "bench": [
                [28, "C"],
                [1, "2B"],
                [19, "3B"],
                [5, "LF"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 57, 54, 27, 56, 22, 40],
        },
        "umpires": {
            "HP": "Tom Hallion",
            "1B": "Chris Guccione",
            "2B": "Ron Kulpa",
            "3B": "Phil Cuzzi",
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
t1.pitch_list("c f b f b f f")
t1.hit(1)
t1.advance(3, "18 2B")
t1.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("b")
t1.hit(2)
t1.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (2 - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.hit(1, rbis=2)
t1.advance(2, "34 BB")
t1.advance(4, "29 2B")

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(3, "29 2B")
t1.advance(4, "37 1B")

# 5. BOS #29 Daniel Nava (X - 15 - 34)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b b f")
t1.hit(2, rbis=1)
t1.advance(4, "37 1B")

# 6. BOS #37 Mike Carp (34 - 29 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("f f b b")
t1.hit(1, rbis=2)
t1.advance(3, "39 2B")
t1.advance(4, "16 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t1.new_ab()
t1.pitch_list("c c")
t1.hit(2)
t1.advance(3, "16 1B")

# 8. BOS #16 Will Middlebrooks (37 - 39 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c f b b")
t1.hit(1, rbis=1)
t1.thrown_out(2, "2 DP6-3", 2, 53)

# 9. BOS #7  Stephen Drew (39 - X - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("P6")

# 1. BOS #2  Jacoby Ellsbury (39 - X - 16)
t1.new_ab(is_risp=True)
t1.out("DP6-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(4)

# 2. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("c c f c")
b1.out("!K")

# 3. TBR #2  Kelly Johnson (X - X - X)
b1.new_ab()
b1.pitch_list("b b c f b")
b1.out("F8")

# 4. TBR #3  Evan Longoria (X - X - X)
b1.new_ab()
b1.hit(4)

# 5. TBR #21 James Loney (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #53 Alex Cobb
t2 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t2.new_ab()
t2.pitch_list("c b f f")
t2.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s b f b")
t2.reach("BB")

# 5. BOS #29 Daniel Nava (X - X - 34)
t2.new_ab()
t2.pitch_list("c b 1 b s")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 6. TBR #30 Luke Scott (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("F8")

# 7. TBR #8  Desmond Jennings (X - X - X)
b2.new_ab()
b2.pitch_list("c s")
b2.hit(1)
b2.advance(2, "59 SB")
b2.advance(3, "59 G1")

# 8. TBR #59 Jose Lobaton (X - X - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("1 c s b b b f")
b2.out("G1")

# 9. TBR #11 Yunel Escobar (8 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("d b c b c d")
b2.reach("BB")

# 1. TBR #20 Matt Joyce (8 - X - 11)
b2.new_ab(is_risp=True)
b2.pitch_list("b d b f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #53 Alex Cobb
t3 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b s b b c s")
t3.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c c b f f f")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 2. TBR #18 Ben Zobrist (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)
b3.advance(2, "2 1B")
b3.advance(3, "3 1B")
b3.advance(4, "30 FC4-6")

# 3. TBR #2  Kelly Johnson (X - X - 18)
b3.new_ab()
b3.pitch_list("f f")
b3.hit(1)
b3.advance(2, "3 1B")
b3.advance(3, "30 FC4-6")

# 4. TBR #3  Evan Longoria (X - 18 - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("c b d")
b3.hit(1)
b3.thrown_out(2, "30 FC4-6", 2, 41)

# 5. TBR #21 James Loney (18 - 2 - 3)
b3.new_ab(is_risp=True)
b3.out("L3")

# 6. TBR #30 Luke Scott (18 - 2 - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("c b")
b3.reach("FC4-6", rbis=1)

# 7. TBR #8  Desmond Jennings (2 - X - 30)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #53 Alex Cobb
t4 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c f f s")
t4.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("b b f s b s")
t4.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b b b")
t4.reach("BB")
t4.error(3)
t4.advance(2, "15 POE3")
t4.advance(3, "15 WP")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("t 1 1 1 s 1 b b f c")
t4.wp()
t4.out("!K")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 8. TBR #59 Jose Lobaton (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "11 1B")
b4.advance(4, "18 1B")

# 9. TBR #11 Yunel Escobar (X - X - 59)
b4.new_ab()
b4.hit(1)
b4.advance(2, "18 1B")
b4.advance(3, "2 F8")

# 1. TBR #20 Matt Joyce (X - 59 - 11)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b c f")
b4.out("(F)P5")

# 2. TBR #18 Ben Zobrist (X - 59 - 11)
b4.new_ab(is_risp=True)
b4.pitch_list("b s b f b")
b4.hit(1, rbis=1)
b4.advance(2, "2 F8")

# 3. TBR #2  Kelly Johnson (X - 11 - 18)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.out("F8")

# 4. TBR #3  Evan Longoria (11 - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c d s")
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #54 Alex Torres
t5 = game.new_inning()

# Pitching change (TBR): #54 Alex Torres replaces #53 Alex Cobb
t5.pitching_substitution(54)

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b c f c")
t5.out("!K")

# 5. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c b b s f c")
t5.out("!K")

# 6. BOS #37 Mike Carp (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 5. TBR #21 James Loney (X - X - X)
b5.new_ab()
b5.pitch_list("b c f")
b5.out("G3-1")

# 6. TBR #30 Luke Scott (X - X - X)
b5.new_ab()
b5.out("F7")

# 7. TBR #8  Desmond Jennings (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #54 Alex Torres
t6 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G1-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("b s s s")
t6.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c c f f f b")
t6.hit(1)

# 2. BOS #18 Shane Victorino (X - X - 2)
t6.new_ab()
t6.pitch_list("b f")
t6.out("F7")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 8. TBR #59 Jose Lobaton (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("L1-4-3")

# 9. TBR #11 Yunel Escobar (X - X - X)
b6.new_ab()
b6.out("G6-3")

# 1. TBR #20 Matt Joyce (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.reach("HBP")
b6.advance(3, "18 2B")

# 2. TBR #18 Ben Zobrist (X - X - 20)
b6.new_ab()
b6.hit(2)

# Pitching change (BOS): #32 Craig Breslow replaces #41 John Lackey
b6.pitching_substitution(32)

# 3. TBR #2  Kelly Johnson (20 - 18 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s b b s c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #62 Joel Peralta
t7 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #54 Alex Torres
t7.pitching_substitution(62)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b b")
t7.reach("BB")
t7.thrown_out(2, "34 DP5-3", 1, 62)

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("b c")
t7.out("DP5-3")

# 5. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.out("F8")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #32 Craig Breslow
b7.pitching_substitution(30)

# 4. TBR #3  Evan Longoria (X - X - X)
b7.new_ab()
b7.out("F8")

# 5. TBR #21 James Loney (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.hit(4)

# 6. TBR #30 Luke Scott (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")

# Pitching change (BOS): #36 Junichi Tazawa replaces #30 Andrew Miller
b7.pitching_substitution(36)

# 7. TBR #8  Desmond Jennings (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("(F)P2")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #57 Jake McGee
t8 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #62 Joel Peralta
t8.pitching_substitution(57)

# 6. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("c b c c")
t8.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b f b s b")
t8.out("G5-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("b s b s f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# 8. TBR #59 Jose Lobaton (X - X - X)
b8.new_ab()
b8.pitch_list("c s")
b8.out("G3")

# 9. TBR #11 Yunel Escobar (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(2)
b8.advance(3, "20 G4-3")
b8.advance(4, "18 WP")

# 1. TBR #20 Matt Joyce (X - 11 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b f")
b8.out("G4-3")

# 2. TBR #18 Ben Zobrist (11 - X - X)
b8.new_ab()
b8.pitch_list("d b c b")
b8.wp()
b8.hit(2)

# 3. TBR #2  Kelly Johnson (X - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #57 Jake McGee
t9.pitching_substitution(56)

# 9. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c b c b c")
t9.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("s b b b")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #59 Clayton Mortensen
b9 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #36 Junichi Tazawa
b9.pitching_substitution(59)

# 4. TBR #3  Evan Longoria (X - X - X)
b9.new_ab()
b9.pitch_list("b c b c s")
b9.out("K")

# 5. TBR #21 James Loney (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
# Offensive change (TBR): Pinch-runner #1 Sean Rodríguez replaces #21 James Loney
b9.offensive_substitution(5, 1, "PR")
b9.atbase("PR")

# 6. TBR #30 Luke Scott (X - X - 21)
b9.new_ab()
b9.pitch_list("b c 1")
b9.out("F8")

# 7. TBR #8  Desmond Jennings (X - X - 1)
b9.new_ab()
b9.pitch_list("1 c s 1 f f")
b9.out("(F)P3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TBR #56 Fernando Rodney
t10 = game.new_inning()

# Defensive switch (TBR): #1 Sean Rodríguez moves to 1B
t10.defensive_switch(1, "3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t10.new_ab()
t10.pitch_list("b b b b")
t10.reach("BB")
t10.advance(2, "34 G4-3")
t10.advance(3, "29 SB")
t10.advance(4, "39 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t10.new_ab()
t10.pitch_list("c")
t10.out("G4-3")

# 5. BOS #29 Daniel Nava (X - 15 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("b c b b f b")
t10.reach("BB")
t10.advance(2, "39 DI")
t10.advance(4, "39 1B")

# 6. BOS #37 Mike Carp (15 - X - 29)
t10.new_ab(is_risp=True)
t10.pitch_list("c s f s")
t10.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (15 - X - 29)
t10.new_ab(is_risp=True)
t10.pitch_list("c")
t10.hit(1, rbis=2)

# Pitching change (TBR): #35 Jamey Wright replaces #56 Fernando Rodney
t10.pitching_substitution(35)

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t10.new_ab()
t10.pitch_list("c c f b b c")
t10.out("!K")


# Bot 10th
# Pitching: BOS #40 Andrew Bailey
b10 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #59 Clayton Mortensen
b10.pitching_substitution(40)

# 8. TBR #59 Jose Lobaton (X - X - X)
b10.new_ab()
b10.pitch_list("c s b")
b10.hit(4)

# 9. TBR #11 Yunel Escobar (X - X - X)
b10.new_ab()
b10.pitch_list("b b b c b")
b10.reach("BB")
b10.advance(2, "20 BB")
b10.advance(3, "18 1B")
b10.advance(4, "2 BB")

# 1. TBR #20 Matt Joyce (X - X - 11)
b10.new_ab()
b10.pitch_list("b f f b b b")
b10.reach("BB")
b10.advance(2, "18 1B")
b10.advance(3, "2 BB")
b10.thrown_out(4, "3 DP5-2-3", 1, 40)

# 2. TBR #18 Ben Zobrist (X - 11 - 20)
b10.new_ab(is_risp=True)
b10.pitch_list("d f b")
b10.hit(1)
b10.advance(2, "2 BB")
b10.advance(3, "3 DP5-2-3")

# 3. TBR #2  Kelly Johnson (11 - 20 - 18)
b10.new_ab(is_risp=True)
b10.pitch_list("s c f b b f b f b")
b10.reach("BB", rbis=1)
b10.advance(2, "3 DP5-2-3")

# 4. TBR #3  Evan Longoria (20 - 18 - 2)
b10.new_ab(is_risp=True)
b10.pitch_list("f s")
b10.out("DP5-2-3")

# Offensive change (TBR): Pinch-hitter #5 Sam Fuld replaces #1 Sean Rodríguez, batting 5th
b10.offensive_substitution(5, 5, "PH")

# 5. TBR #5  Sam Fuld (18 - 2 - X)
b10.new_ab(is_risp=True)
b10.out("B4-3")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: TBR #35 Jamey Wright
t11 = game.new_inning()

# Defensive switch (TBR): #2 Kelly Johnson moves to 1B
t11.defensive_switch(2, "3")

# Defensive switch (TBR): #5 Sam Fuld moves to LF
t11.defensive_switch(5, "7")

# 9. BOS #7  Stephen Drew (X - X - X)
t11.new_ab()
t11.pitch_list("b c f b b s")
t11.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t11.new_ab()
t11.pitch_list("c b f b f f b b")
t11.reach("BB")
t11.advance(2, "15 SB")
t11.advance(3, "15 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t11.new_ab()
t11.pitch_list("b 1 c d")
t11.out("F8")

# Pitching change (TBR): #43 Kyle Farnsworth replaces #35 Jamey Wright
t11.pitching_substitution(43)

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t11.new_ab(is_risp=True)
t11.pitch_list("1 c 1 b 1 c b f f b c")
t11.out("!K")


# Bot 11th
# Pitching: BOS #19 Koji Uehara
b11 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #40 Andrew Bailey
b11.pitching_substitution(19)

# 6. TBR #30 Luke Scott (X - X - X)
b11.new_ab()
b11.pitch_list("f")
b11.out("P6")

# 7. TBR #8  Desmond Jennings (X - X - X)
b11.new_ab()
b11.pitch_list("b s")
b11.out("G5-3")

# 8. TBR #59 Jose Lobaton (X - X - X)
b11.new_ab()
b11.pitch_list("c")
b11.out("P6")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: TBR #27 Cesár Ramos
t12 = game.new_inning()

# Pitching change (TBR): #27 Cesár Ramos replaces #43 Kyle Farnsworth
t12.pitching_substitution(27)

# 4. BOS #34 David Ortiz (X - X - X)
t12.new_ab()
t12.out("P5")

# 5. BOS #29 Daniel Nava (X - X - X)
t12.new_ab()
t12.out("B2")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
t12.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (X - X - X)
t12.new_ab()
t12.pitch_list("b s c b c")
t12.out("!K")


# Bot 12th
# Pitching: BOS #19 Koji Uehara
b12 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b12.defensive_switch(29, "3")

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b12.defensive_switch(5, "7")

# 9. TBR #11 Yunel Escobar (X - X - X)
b12.new_ab()
b12.pitch_list("s")
b12.out("(F)P2")

# 1. TBR #20 Matt Joyce (X - X - X)
b12.new_ab()
b12.pitch_list("c b")
b12.out("F8")

# 2. TBR #18 Ben Zobrist (X - X - X)
b12.new_ab()
b12.pitch_list("b f s s")
b12.out("K")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: TBR #27 Cesár Ramos
t13 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t13.new_ab()
t13.pitch_list("f f b b")
t13.hit(1)
t13.thrown_out(2, "16 DP6-4-3", 1, 27)

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t13.new_ab()
t13.pitch_list("f 1 f b f b 1")
t13.out("DP6-4-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t13.new_ab()
t13.pitch_list("b")
t13.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t13.new_ab()
t13.out("F7")


# Bot 13th
# Pitching: BOS #56 Franklin Morales
b13 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #19 Koji Uehara
b13.pitching_substitution(56)

# 3. TBR #2  Kelly Johnson (X - X - X)
b13.new_ab()
b13.pitch_list("c f b b f f s")
b13.out("K")

# 4. TBR #3  Evan Longoria (X - X - X)
b13.new_ab()
b13.pitch_list("c")
b13.out("L8")

# Offensive change (TBR): Pinch-hitter #19 Ryan Roberts replaces #5 Sam Fuld, batting 5th
b13.offensive_substitution(5, 19, "PH")

# 5. TBR #19 Ryan Roberts (X - X - X)
b13.new_ab()
b13.pitch_list("b s s b b b")
b13.reach("BB")

# 6. TBR #30 Luke Scott (X - X - 19)
b13.new_ab()
b13.pitch_list("1 f s b b f b f f t")
b13.out("KT")


##########################################################
# 14th Inning
##########################################################
# Top 14th
# Pitching: TBR #27 Cesár Ramos
t14 = game.new_inning()

# Defensive switch (TBR): #20 Matt Joyce moves to LF
t14.defensive_switch(20, "7")

# Defensive switch (TBR): #18 Ben Zobrist moves to RF
t14.defensive_switch(18, "9")

# Defensive switch (TBR): #19 Ryan Roberts moves to 2B
t14.defensive_switch(19, "4")

# 2. BOS #18 Shane Victorino (X - X - X)
t14.new_ab()
t14.pitch_list("c s b")
t14.hit(1)
t14.advance(2, "15 F9")
t14.advance(4, "29 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t14.new_ab()
t14.pitch_list("c c f")
t14.out("F9")

# 4. BOS #34 David Ortiz (X - 18 - X)
t14.new_ab(is_risp=True)
t14.pitch_list("i i i i")
t14.reach("IBB")
t14.advance(2, "29 1B")
# Offensive change (BOS): Pinch-runner #10 Jose Iglesias replaces #34 David Ortiz
t14.offensive_substitution(4, 10, "PR")
t14.atbase("PR")
t14.advance(4, "39 1B")

# 5. BOS #29 Daniel Nava (X - 18 - 34)
t14.new_ab(is_risp=True)
t14.pitch_list("f")
t14.hit(1, rbis=1)
t14.advance(2, "39 1B")

# 6. BOS #5  Jonny Gomes (X - 34 - 29)
t14.new_ab(is_risp=True)
t14.pitch_list("b")
t14.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - 10 - 29)
t14.new_ab(is_risp=True)
t14.pitch_list("b c")
t14.hit(1, rbis=1)

# 8. BOS #16 Will Middlebrooks (X - 29 - 39)
t14.new_ab(is_risp=True)
t14.pitch_list("b s c")
t14.out("F9")


# Bot 14th
# Pitching: BOS #56 Franklin Morales
b14 = game.new_inning()

# Defensive switch (BOS): #10 Jose Iglesias moves to DH
b14.defensive_switch(10, "0")

# 7. TBR #8  Desmond Jennings (X - X - X)
b14.new_ab()
b14.pitch_list("b c b f")
b14.hit(1)
b14.thrown_out(2, "11 DP4-6-3", 2, 56)

# 8. TBR #59 Jose Lobaton (X - X - 8)
b14.new_ab()
b14.out("F9")

# 9. TBR #11 Yunel Escobar (X - X - 8)
b14.new_ab()
b14.pitch_list("c b c b")
b14.out("DP4-6-3")

# Winning team: BOS
# WP: BOS #56 Franklin Morales
game.winning_pitcher(56, is_away_team=True)

# Loser team: TBR
# LP: TBR #27 Cesár Ramos
game.losing_pitcher(27)

# print(game)
game.generate_scorecard()
