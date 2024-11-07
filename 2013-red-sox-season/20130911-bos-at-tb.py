import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-09-11
# https://www.baseball-reference.com/boxes/TBA/TBA201309110.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/09/11/348909/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-11 19:12-23:17",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "19,215",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                3: "David Ross",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                5: "Jonny Gomes",
                72: "Xander Bogaerts",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [18, "9"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [7, "6"],
                [16, "5"],
                [3, "2"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [5, "LF"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 22],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 53,
            "roster": {
                # Lineup
                7: "David DeJesus",
                9: "Wil Myers",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                20: "Matt Joyce",
                8: "Desmond Jennings",
                21: "James Loney",
                59: "Jose Lobaton",
                11: "Yunel Escobar",
                # Starting pitcher
                53: "Alex Cobb",
                # Bench
                28: "José Molina",
                16: "Chris Gimenez",
                30: "Luke Scott",
                1: "Sean Rodríguez",
                15: "Delmon Young",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                49: "Wesley Wright",
                47: "Brandon Gomes",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                14: "David Price",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [49, 55, 57, 54, 27, 14],
            "lineup": [
                [7, "7"],
                [9, "9"],
                [18, "4"],
                [3, "5"],
                [20, "0"],
                [8, "8"],
                [21, "3"],
                [59, "2"],
                [11, "6"],
            ],
            "bench": [
                [28, "C"],
                [16, "C"],
                [30, "DH"],
                [1, "2B"],
                [15, "LF"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 49, 47, 55, 62, 35, 57, 54, 27, 52, 14, 56, 22, 40],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Lance Barksdale",
            "2B": "Gary Cederstrom",
            "3B": "Angel Hernandez",
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

# 1. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("s b b f s")
t1.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
t1.new_ab()
t1.out("L7")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. TBR #7  David DeJesus (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c f s")
b1.out("K")

# 2. TBR #9  Wil Myers (X - X - X)
b1.new_ab()
b1.pitch_list("b c c s")
b1.out("K")

# 3. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #53 Alex Cobb
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b b")
t2.reach("BB")
t2.advance(2, "29 1B")
t2.advance(3, "16 FC1")

# 5. BOS #29 Daniel Nava (X - X - 12)
t2.new_ab()
t2.pitch_list("c c f")
t2.hit(1)
t2.advance(2, "16 FC1")

# 6. BOS #7  Stephen Drew (X - 12 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c f s")
t2.out("K")

# 7. BOS #16 Will Middlebrooks (X - 12 - 29)
t2.new_ab(is_risp=True)
t2.reach("FC1")
t2.thrown_out(2, "3 DP5-4-3", 2, 53)

# 8. BOS #3  David Ross (12 - 29 - 16)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("DP5-4-3")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b2.new_ab()
b2.hit(2)
b2.advance(3, "21 G3-1")

# 5. TBR #20 Matt Joyce (X - 3 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b c s")
b2.out("K")

# 6. TBR #8  Desmond Jennings (X - 3 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "21 G3-1")

# 7. TBR #21 James Loney (X - 3 - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("f c 1 f b f f b f")
b2.out("G3-1")

# 8. TBR #59 Jose Lobaton (3 - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b s s b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #53 Alex Cobb
t3 = game.new_inning()

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b b c")
t3.out("G3")

# 1. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.advance(3, "18 2B")
t3.advance(4, "12 2B")

# 2. BOS #18 Shane Victorino (X - X - 15)
t3.new_ab()
t3.pitch_list("b c 1 1")
t3.hit(2)
t3.advance(4, "12 2B")

# 3. BOS #34 David Ortiz (15 - 18 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("d b i i")
t3.reach("IBB")
t3.advance(3, "12 2B")
t3.advance(4, "29 G4-3")

# 4. BOS #12 Mike Napoli (15 - 18 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("b c")
t3.hit(2, rbis=2)
t3.advance(3, "29 G4-3")

# 5. BOS #29 Daniel Nava (34 - 12 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b")
t3.out("G4-3", rbis=1)

# 6. BOS #7  Stephen Drew (12 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s b d")
t3.out("L8")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(2)
b3.advance(4, "7 2B")

# 1. TBR #7  David DeJesus (X - 11 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f")
b3.hit(2, rbis=1)
b3.advance(3, "20 BB")

# 2. TBR #9  Wil Myers (X - 7 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f c f c")
b3.out("!K")

# 3. TBR #18 Ben Zobrist (X - 7 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b d")
b3.out("F8")

# 4. TBR #3  Evan Longoria (X - 7 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("d b c")
b3.reach("HBP")
b3.advance(2, "20 BB")

# 5. TBR #20 Matt Joyce (X - 7 - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("b b b f b")
b3.reach("BB")
b3.thrown_out(2, "8 FC6-4", 3, 46)

# 6. TBR #8  Desmond Jennings (7 - 3 - 20)
b3.new_ab(is_risp=True)
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #53 Alex Cobb
t4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b c c f f")
t4.out("G5-3")

# 8. BOS #3  David Ross (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b s")
t4.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.hit(2)

# 1. BOS #15 Dustin Pedroia (X - 25 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b b c c")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 7. TBR #21 James Loney (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f s")
b4.out("K")

# 8. TBR #59 Jose Lobaton (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G5-3")

# 9. TBR #11 Yunel Escobar (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #53 Alex Cobb
t5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f f")
t5.out("G5-3")

# 3. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("G5-3")

# 4. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c s f c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 1. TBR #7  David DeJesus (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f b f f f b")
b5.reach("BB")
b5.advance(2, "9 1B")
b5.advance(3, "18 DP4-6-3")

# 2. TBR #9  Wil Myers (X - X - 7)
b5.new_ab()
b5.pitch_list("f c 1")
b5.hit(1)
b5.thrown_out(2, "18 DP4-6-3", 1, 46)

# 3. TBR #18 Ben Zobrist (X - 7 - 9)
b5.new_ab(is_risp=True)
b5.pitch_list("b s")
b5.out("DP4-6-3")

# 4. TBR #3  Evan Longoria (7 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b f b b")
b5.reach("BB")
b5.advance(2, "20 BB")

# 5. TBR #20 Matt Joyce (7 - X - 3)
b5.new_ab(is_risp=True)
b5.pitch_list("d s b b b")
b5.reach("BB")

# 6. TBR #8  Desmond Jennings (7 - 3 - 20)
b5.new_ab(is_risp=True)
b5.pitch_list("s c b t")
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #53 Alex Cobb
t6 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c")
t6.hit(1)
t6.advance(2, "7 1B")
t6.thrown_out(3, "16 DP5-4", 1, 53)

# 6. BOS #7  Stephen Drew (X - X - 29)
t6.new_ab()
t6.pitch_list("b c 1 c")
t6.hit(1)
t6.thrown_out(2, "16 DP5-4", 2, 53)

# 7. BOS #16 Will Middlebrooks (X - 29 - 7)
t6.new_ab(is_risp=True)
t6.reach("DP5-4")
t6.advance(2, "3 BB")

# 8. BOS #3  David Ross (X - X - 16)
t6.new_ab()
t6.pitch_list("c d b c b b")
t6.reach("BB")
t6.thrown_out(2, "25 FC4", 3, 49)

# Pitching change (TBR): #49 Wesley Wright replaces #53 Alex Cobb
t6.pitching_substitution(49)

# 9. BOS #25 Jackie Bradley Jr. (X - 16 - 3)
t6.new_ab(is_risp=True)
t6.pitch_list("c s")
t6.reach("FC4")


# Bot 6th
# Pitching: BOS #56 Franklin Morales
b6 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #46 Ryan Dempster
b6.pitching_substitution(56)

# 7. TBR #21 James Loney (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f b")
b6.out("G3")

# 8. TBR #59 Jose Lobaton (X - X - X)
b6.new_ab()
b6.pitch_list("b t b s")
b6.out("P4")

# 9. TBR #11 Yunel Escobar (X - X - X)
b6.new_ab()
b6.pitch_list("b f s b f")
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #35 Jamey Wright
t7 = game.new_inning()

# Pitching change (TBR): #35 Jamey Wright replaces #49 Wesley Wright
t7.pitching_substitution(35)

# 1. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.thrown_out(2, "34 DP4-5-3", 2, 57)

# 2. BOS #18 Shane Victorino (X - X - 15)
t7.new_ab()
t7.pitch_list("1 c f f s")
t7.out("K")

# Pitching change (TBR): #57 Jake McGee replaces #35 Jamey Wright
t7.pitching_substitution(57)

# 3. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("c b s f")
t7.out("DP4-5-3")


# Bot 7th
# Pitching: BOS #67 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #56 Franklin Morales
b7.pitching_substitution(67)

# Offensive change (TBR): Pinch-hitter #1 Sean Rodríguez replaces #7 David DeJesus, batting 1st
b7.offensive_substitution(1, 1, "PH")

# Offensive change (TBR): Pinch-hitter #2 Kelly Johnson replaces #1 Sean Rodríguez, batting 1st
b7.offensive_substitution(1, 2, "PH")

# 1. TBR #2  Kelly Johnson (X - X - X)
b7.new_ab()
b7.pitch_list("c c f b f f b b s")
b7.out("K")

# 2. TBR #9  Wil Myers (X - X - X)
b7.new_ab()
b7.out("G6-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(4, "3 2B")

# 4. TBR #3  Evan Longoria (X - X - 18)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2, rbis=1)

# 5. TBR #20 Matt Joyce (X - 3 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c c b d f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #54 Alex Torres
t8 = game.new_inning()

# Pitching change (TBR): #54 Alex Torres replaces #57 Jake McGee
t8.pitching_substitution(54)

# Defensive switch (TBR): #2 Kelly Johnson moves to LF
t8.defensive_switch(2, "7")

# 4. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("L6")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 5th
t8.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b b s b c")
t8.out("F8")

# 6. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L9")


# Bot 8th
# Pitching: BOS #67 Brandon Workman
b8 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b8.defensive_switch(5, "7")

# 6. TBR #8  Desmond Jennings (X - X - X)
b8.new_ab()
b8.pitch_list("l s s")
b8.out("K")

# 7. TBR #21 James Loney (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c f")
b8.hit(4)

# 8. TBR #59 Jose Lobaton (X - X - X)
b8.new_ab()
b8.pitch_list("b t s b s")
b8.out("K")

# 9. TBR #11 Yunel Escobar (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #54 Alex Torres
t9.pitching_substitution(56)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f")
t9.out("G6-3")

# 8. BOS #3  David Ross (X - X - X)
t9.new_ab()
t9.pitch_list("f b b c b s")
t9.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("c b s c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #67 Brandon Workman
b9.pitching_substitution(19)

# 1. TBR #2  Kelly Johnson (X - X - X)
b9.new_ab()
b9.pitch_list("s c f s")
b9.out("K")

# 2. TBR #9  Wil Myers (X - X - X)
b9.new_ab()
b9.pitch_list("c s b f f b s")
b9.out("K")

# 3. TBR #18 Ben Zobrist (X - X - X)
b9.new_ab()
b9.pitch_list("s s f b b")
b9.out("G4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TBR #62 Joel Peralta
t10 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #56 Fernando Rodney
t10.pitching_substitution(62)

# 1. BOS #15 Dustin Pedroia (X - X - X)
t10.new_ab()
t10.pitch_list("c b b b b")
t10.reach("BB")
t10.advance(2, "18 SAC1-4")
t10.advance(3, "12 BB")
t10.advance(4, "37 HR")

# 2. BOS #18 Shane Victorino (X - X - 15)
t10.new_ab()
t10.pitch_list("l 1")
t10.out("SAC1-4")

# 3. BOS #34 David Ortiz (X - 15 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("i i i i")
t10.reach("IBB")
t10.advance(2, "12 BB")
t10.advance(4, "37 HR")

# Pitching change (TBR): #40 Roberto Hernandez replaces #62 Joel Peralta
t10.pitching_substitution(40)

# 4. BOS #12 Mike Napoli (X - 15 - 34)
t10.new_ab(is_risp=True)
t10.pitch_list("b b b b")
t10.reach("BB")
t10.advance(4, "37 HR")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 5th
t10.offensive_substitution(5, 37, "PH")

# 5. BOS #37 Mike Carp (15 - 34 - 12)
t10.new_ab(is_risp=True)
t10.hit(4, rbis=4)

# 6. BOS #7  Stephen Drew (X - X - X)
t10.new_ab()
t10.pitch_list("b f s b s")
t10.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t10.new_ab()
t10.pitch_list("b c c b")
t10.out("G6-3")


# Bot 10th
# Pitching: BOS #36 Junichi Tazawa
b10 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
b10.pitching_substitution(36)

# Defensive change (BOS): #50 Quintin Berry replaces #37 Mike Carp (PH), playing LF, batting 5th
b10.defensive_substitution(5, 50, "7")

# 4. TBR #3  Evan Longoria (X - X - X)
b10.new_ab()
b10.out("L8")

# 5. TBR #20 Matt Joyce (X - X - X)
b10.new_ab()
b10.pitch_list("b b b b")
b10.reach("BB")

# 6. TBR #8  Desmond Jennings (X - X - 20)
b10.new_ab()
b10.pitch_list("d f t b f f c")
b10.out("!K")

# 7. TBR #21 James Loney (X - X - 20)
b10.new_ab()
b10.out("L9")

# Winning team: BOS
# WP: BOS #19 Koji Uehara
game.winning_pitcher(19, is_away_team=True)

# Loser team: TBR
# LP: TBR #62 Joel Peralta
game.losing_pitcher(62)

# print(game)
game.generate_scorecard()
