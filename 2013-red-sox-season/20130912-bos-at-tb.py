import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-09-12
# https://www.baseball-reference.com/boxes/TBA/TBA201309120.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/09/12/348924/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-12 19:11-22:28",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "20,360",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                29: "Daniel Nava",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                3: "David Ross",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [29, "9"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [5, "7"],
                [7, "6"],
                [72, "5"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [37, "1B"],
                [16, "3B"],
                [18, "CF"],
                [3, "C"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 58,
            "roster": {
                # Lineup
                7: "David DeJesus",
                18: "Ben Zobrist",
                21: "James Loney",
                3: "Evan Longoria",
                20: "Matt Joyce",
                9: "Wil Myers",
                8: "Desmond Jennings",
                59: "Jose Lobaton",
                11: "Yunel Escobar",
                # Starting pitcher
                58: "Jeremy Hellickson",
                # Bench
                28: "José Molina",
                16: "Chris Gimenez",
                30: "Luke Scott",
                1: "Sean Rodríguez",
                15: "Delmon Young",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                49: "Wesley Wright",
                53: "Alex Cobb",
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
                [18, "4"],
                [21, "3"],
                [3, "5"],
                [20, "0"],
                [9, "9"],
                [8, "8"],
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
            "bullpen": [49, 53, 47, 55, 62, 35, 57, 54, 27, 52, 14, 56, 22, 40],
        },
        "umpires": {
            "HP": "Lance Barksdale",
            "1B": "Gary Cederstrom",
            "2B": "Angel Hernandez",
            "3B": "Vic Carapazza",
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
# Pitching: TBR #58 Jeremy Hellickson
t1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.out("P6")

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.hit(1)
t1.advance(2, "34 BB")
t1.advance(3, "12 G6-3")

# 3. BOS #34 David Ortiz (X - X - 29)
t1.new_ab()
t1.pitch_list("b b c b b")
t1.reach("BB")
t1.advance(2, "12 G6-3")

# 4. BOS #12 Mike Napoli (X - 29 - 34)
t1.new_ab(is_risp=True)
t1.out("G6-3")

# 5. BOS #39 Jarrod Saltalamacchia (29 - 34 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s b s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. TBR #7  David DeJesus (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 2. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("G4-3")

# 3. TBR #21 James Loney (X - X - X)
b1.new_ab()
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #58 Jeremy Hellickson
t2 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("b c f b b")
t2.out("F9")

# 7. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.thrown_out(2, "25 FC4-6", 3, 58)

# 8. BOS #72 Xander Bogaerts (X - X - 7)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - 7)
t2.new_ab()
t2.reach("FC4-6")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b2.new_ab()
b2.pitch_list("b s b b s")
b2.hit(3)
b2.advance(4, "9 1B")

# 5. TBR #20 Matt Joyce (3 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f")
b2.out("F7")

# 6. TBR #9  Wil Myers (3 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f f b")
b2.hit(1, rbis=1)

# 7. TBR #8  Desmond Jennings (X - X - 9)
b2.new_ab()
b2.pitch_list("b c f s")
b2.out("K")

# 8. TBR #59 Jose Lobaton (X - X - 9)
b2.new_ab()
b2.pitch_list("b b c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #58 Jeremy Hellickson
t3 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("L4")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s f")
t3.out("F7")

# 3. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("b c f f b f f f t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G6-3")

# 1. TBR #7  David DeJesus (X - X - X)
b3.new_ab()
b3.pitch_list("b c b s b f f f b")
b3.reach("BB")
b3.advance(2, "18 G3")
b3.advance(4, "21 2B")

# 2. TBR #18 Ben Zobrist (X - X - 7)
b3.new_ab()
b3.out("G3")

# 3. TBR #21 James Loney (X - 7 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b")
b3.hit(2, rbis=1)

# 4. TBR #3  Evan Longoria (X - 21 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c d s b")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #58 Jeremy Hellickson
t4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b c f s")
t4.out("K")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b s f b b")
t4.hit(4)

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("c s b s")
t4.out("K")

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("s c b b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 5. TBR #20 Matt Joyce (X - X - X)
b4.new_ab()
b4.pitch_list("b b s b b")
b4.reach("BB")
b4.thrown_out(2, "8 CS", 2, 44)

# 6. TBR #9  Wil Myers (X - X - 20)
b4.new_ab()
b4.pitch_list("c b c s")
b4.out("K")

# 7. TBR #8  Desmond Jennings (X - X - 20)
b4.new_ab()
b4.pitch_list("1 s b f")
b4.hit(4)

# 8. TBR #59 Jose Lobaton (X - X - X)
b4.new_ab()
b4.pitch_list("s b b c c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #58 Jeremy Hellickson
t5 = game.new_inning()

# 8. BOS #72 Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b s f s")
t5.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b")
t5.out("P4")

# 1. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c f b b f f b")
t5.hit(1)
t5.advance(2, "29 WP")

# 2. BOS #29 Daniel Nava (X - X - 15)
t5.new_ab(is_risp=True)
t5.pitch_list("d f b s")
t5.wp()
t5.out("F8")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
b5.new_ab()
b5.pitch_list("f b s b b b")
b5.reach("BB")
b5.advance(2, "7 BB")

# 1. TBR #7  David DeJesus (X - X - 11)
b5.new_ab()
b5.pitch_list("f l b b b f 1 b")
b5.reach("BB")
b5.thrown_out(2, "3 FC5-4", 3, 44)

# 2. TBR #18 Ben Zobrist (X - 11 - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("d c")
b5.out("IF5")

# 3. TBR #21 James Loney (X - 11 - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b")
b5.out("F7")

# 4. TBR #3  Evan Longoria (X - 11 - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("d")
b5.reach("FC5-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #58 Jeremy Hellickson
t6 = game.new_inning()

# 3. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(4)

# 4. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("b s c f")
t6.out("G6-3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b b s c b b")
t6.reach("BB")
t6.advance(2, "7 SB")
t6.advance(4, "7 2B")

# Pitching change (TBR): #35 Jamey Wright replaces #58 Jeremy Hellickson
t6.pitching_substitution(35)

# 6. BOS #5  Jonny Gomes (X - X - 39)
t6.new_ab()
t6.pitch_list("c b 1 c s")
t6.out("K")

# 7. BOS #7  Stephen Drew (X - X - 39)
t6.new_ab(is_risp=True)
t6.pitch_list("b 1 s f b")
t6.hit(2, rbis=1)

# 8. BOS #72 Xander Bogaerts (X - 7 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f f d d")
t6.out("F8")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 5. TBR #20 Matt Joyce (X - X - X)
b6.new_ab()
b6.pitch_list("s s b")
b6.out("G5-3")

# 6. TBR #9  Wil Myers (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.thrown_out(2, "8 FC1-5-4", 2, 44)

# 7. TBR #8  Desmond Jennings (X - X - 9)
b6.new_ab()
b6.pitch_list("b 1 1 b c b")
b6.reach("FC1-5-4")

# 8. TBR #59 Jose Lobaton (X - X - 8)
b6.new_ab()
b6.pitch_list("1 f f")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #35 Jamey Wright
t7 = game.new_inning()

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c b f s")
t7.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #66 Drake Britton
b7 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #44 Jake Peavy
b7.pitching_substitution(66)

# 9. TBR #11 Yunel Escobar (X - X - X)
b7.new_ab()
b7.pitch_list("b f s b b")
b7.out("L8")

# Offensive change (TBR): Pinch-hitter #15 Delmon Young replaces #7 David DeJesus, batting 1st
b7.offensive_substitution(1, 15, "PH")

# 1. TBR #15 Delmon Young (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
# Offensive change (TBR): Pinch-runner #5 Sam Fuld replaces #15 Delmon Young
b7.offensive_substitution(1, 5, "PR")
b7.atbase("PR")
b7.thrown_out(2, "18 DP1-6-3", 2, 66)

# 2. TBR #18 Ben Zobrist (X - X - 15)
b7.new_ab()
b7.out("DP1-6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #57 Jake McGee
t8 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #35 Jamey Wright
t8.pitching_substitution(57)

# Defensive switch (TBR): #5 Sam Fuld moves to LF
t8.defensive_switch(5, "7")

# 3. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 4. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b s s")
t8.out("K")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b f f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #66 Drake Britton
b8 = game.new_inning()

# 3. TBR #21 James Loney (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G1-3")

# Pitching change (BOS): #62 Rubby De La Rosa replaces #66 Drake Britton
b8.pitching_substitution(62)

# 4. TBR #3  Evan Longoria (X - X - X)
b8.new_ab()
b8.pitch_list("c s")
b8.hit(2)
b8.advance(4, "9 2B")

# 5. TBR #20 Matt Joyce (X - 3 - X)
b8.new_ab(is_risp=True)
b8.out("(F)P5")

# 6. TBR #9  Wil Myers (X - 3 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f")
b8.hit(2, rbis=1)
b8.advance(3, "8 E6")

# 7. TBR #8  Desmond Jennings (X - 9 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f c f")
b8.error(6)
b8.reach("E6")

# Pitching change (BOS): #38 Matt Thornton replaces #62 Rubby De La Rosa
b8.pitching_substitution(38)

# 8. TBR #59 Jose Lobaton (9 - X - 8)
b8.new_ab(is_risp=True)
b8.pitch_list("f b 1 f b f f f 1 f")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #57 Jake McGee
t9.pitching_substitution(56)

# 6. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.out("G4-3")

# 7. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c c b")
t9.hit(1)
t9.advance(2, "37 BB")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #72 Xander Bogaerts, batting 8th
t9.offensive_substitution(8, 37, "PH")

# 8. BOS #37 Mike Carp (X - X - 7)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #37 Mike Carp
t9.offensive_substitution(8, 50, "PR")
t9.atbase("PR")

# Offensive change (BOS): Pinch-hitter #16 Will Middlebrooks replaces #25 Jackie Bradley Jr., batting 9th
t9.offensive_substitution(9, 16, "PH")

# 9. BOS #16 Will Middlebrooks (X - 7 - 37)
t9.new_ab(is_risp=True)
t9.pitch_list("c f")
t9.out("L5")

# 1. BOS #15 Dustin Pedroia (X - 7 - 50)
t9.new_ab(is_risp=True)
t9.pitch_list("f s f b")
t9.out("P6")

# Winning team: TBR
# WP: TBR #57 Jake McGee
game.winning_pitcher(57)
# SV: TBR #56 Fernando Rodney
game.save_pitcher(56)

# Loser team: BOS
# LP: BOS #62 Rubby De La Rosa
game.losing_pitcher(62, is_away_team=True)

# print(game)
game.generate_scorecard()
