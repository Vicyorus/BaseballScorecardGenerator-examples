import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-06-12
# https://www.baseball-reference.com/boxes/TBA/TBA201306120.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/06/12/347721/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-12 19:10-22:32",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "15,091",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 91,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                3: "David Ross",
                18: "Shane Victorino",
                10: "Jose Iglesias",
                5: "Jonny Gomes",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [18, "CF"],
                [10, "2B"],
                [5, "LF"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 19, 31, 36, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 22,
            "roster": {
                # Lineup
                20: "Matt Joyce",
                18: "Ben Zobrist",
                2: "Kelly Johnson",
                3: "Evan Longoria",
                21: "James Loney",
                8: "Desmond Jennings",
                30: "Luke Scott",
                59: "Jose Lobaton",
                11: "Yunel Escobar",
                # Starting pitcher
                22: "Chris Archer",
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
                23: "Jake Odorizzi",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [20, "9"],
                [18, "4"],
                [2, "7"],
                [3, "5"],
                [21, "3"],
                [8, "8"],
                [30, "0"],
                [59, "2"],
                [11, "6"],
            ],
            "bench": [
                [28, "C"],
                [1, "2B"],
                [19, "3B"],
                [5, "LF"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 23, 57, 54, 27, 56, 40],
        },
        "umpires": {
            "HP": "Ron Kulpa",
            "1B": "Phil Cuzzi",
            "2B": "Tom Hallion",
            "3B": "Chris Guccione",
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
# Pitching: TBR #22 Chris Archer
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b b")
t1.reach("BB")
t1.advance(2, "15 SB")

# 2. BOS #29 Daniel Nava (X - X - 2)
t1.new_ab()
t1.pitch_list("c c 1 f f 1 1 b f")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab()
t1.pitch_list("b c d c b c")
t1.out("!K")

# 4. BOS #34 David Ortiz (X - 2 - X)
t1.new_ab()
t1.pitch_list("d c b")
t1.out("G3-1")


# Bot 1st
# Pitching: BOS #91 Alfredo Aceves
b1 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G6-3")

# 2. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("F9")

# 3. TBR #2  Kelly Johnson (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #22 Chris Archer
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b f f s")
t2.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.out("L7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #91 Alfredo Aceves
b2 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "8 BB")
b2.advance(3, "59 BB")

# 5. TBR #21 James Loney (X - X - 3)
b2.new_ab()
b2.pitch_list("f b f f f")
b2.out("F7")

# 6. TBR #8  Desmond Jennings (X - X - 3)
b2.new_ab()
b2.pitch_list("b f b b b")
b2.reach("BB")
b2.advance(2, "59 BB")

# 7. TBR #30 Luke Scott (X - 3 - 8)
b2.new_ab()
b2.out("F9")

# 8. TBR #59 Jose Lobaton (X - 3 - 8)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")

# 9. TBR #11 Yunel Escobar (3 - 8 - 59)
b2.new_ab()
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #22 Chris Archer
t3 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f f b f")
t3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b c c")
t3.hit(1)
t3.error(2)
t3.advance(2, "29 SB")
t3.advance(3, "29 E2")
t3.advance(4, "29 HR")

# 2. BOS #29 Daniel Nava (X - X - 2)
t3.new_ab()
t3.pitch_list("1 b b b c f f f f f")
t3.hit(4, rbis=2)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.hit(1)
t3.advance(2, "34 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("b b s 1 b c f b")
t3.reach("BB")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t3.new_ab()
t3.pitch_list("b b c s c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #91 Alfredo Aceves
b3 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b b")
b3.reach("BB")
b3.advance(3, "18 1B")

# 2. TBR #18 Ben Zobrist (X - X - 20)
b3.new_ab()
b3.pitch_list("b c s b")
b3.hit(1)
b3.thrown_out(2, "3 DP6-4-3", 2, 91)

# 3. TBR #2  Kelly Johnson (20 - X - 18)
b3.new_ab()
b3.pitch_list("b s b f c")
b3.out("!K")

# 4. TBR #3  Evan Longoria (20 - X - 18)
b3.new_ab()
b3.pitch_list("c b f f")
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #22 Chris Archer
t4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "16 BB")
t4.advance(3, "2 BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t4.new_ab()
t4.pitch_list("s b s s")
t4.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - 37)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.advance(2, "2 BB")

# 9. BOS #7  Stephen Drew (X - 37 - 16)
t4.new_ab()
t4.pitch_list("c d f b b s")
t4.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 37 - 16)
t4.new_ab()
t4.pitch_list("b d d c b")
t4.reach("BB")

# 2. BOS #29 Daniel Nava (37 - 16 - 2)
t4.new_ab()
t4.pitch_list("d b c b c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #91 Alfredo Aceves
b4 = game.new_inning()

# 5. TBR #21 James Loney (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G3")

# 6. TBR #8  Desmond Jennings (X - X - X)
b4.new_ab()
b4.pitch_list("c b f")
b4.out("G6-3")

# 7. TBR #30 Luke Scott (X - X - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #43 Kyle Farnsworth
t5 = game.new_inning()

# Pitching change (TBR): #43 Kyle Farnsworth replaces #22 Chris Archer
t5.pitching_substitution(43)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.out("L1-3-1")

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.reach("HBP")
t5.advance(2, "37 SB")

# 6. BOS #37 Mike Carp (X - X - 12)
t5.new_ab()
t5.pitch_list("f b b b")
t5.out("F7")


# Bot 5th
# Pitching: BOS #91 Alfredo Aceves
b5 = game.new_inning()

# 8. TBR #59 Jose Lobaton (X - X - X)
b5.new_ab()
b5.out("G3")

# 9. TBR #11 Yunel Escobar (X - X - X)
b5.new_ab()
b5.hit(1)
b5.thrown_out(2, "20 2-6", 2, 91)

# 1. TBR #20 Matt Joyce (X - X - 11)
b5.new_ab()
b5.pitch_list("b d c f")
b5.hit(2)

# 2. TBR #18 Ben Zobrist (X - 20 - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #43 Kyle Farnsworth
t6 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b")
t6.out("L4")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("f b b c s")
t6.out("K")

# Pitching change (TBR): #35 Jamey Wright replaces #43 Kyle Farnsworth
t6.pitching_substitution(35)

# 9. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b")
t6.out("P6")


# Bot 6th
# Pitching: BOS #91 Alfredo Aceves
b6 = game.new_inning()

# 3. TBR #2  Kelly Johnson (X - X - X)
b6.new_ab()
b6.pitch_list("c f f s")
b6.out("K")

# 4. TBR #3  Evan Longoria (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4)

# 5. TBR #21 James Loney (X - X - X)
b6.new_ab()
b6.pitch_list("f b b")
b6.out("G5-3")

# 6. TBR #8  Desmond Jennings (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #35 Jamey Wright
t7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b f f f s")
t7.out("K")

# Pitching change (TBR): #57 Jake McGee replaces #35 Jamey Wright
t7.pitching_substitution(57)

# 2. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s f f t")
t7.out("KT")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b f b f f f f")
t7.out("F7")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #91 Alfredo Aceves
b7.pitching_substitution(36)

# 7. TBR #30 Luke Scott (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f s")
b7.out("K")

# 8. TBR #59 Jose Lobaton (X - X - X)
b7.new_ab()
b7.out("F8")

# 9. TBR #11 Yunel Escobar (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #62 Joel Peralta
t8 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #57 Jake McGee
t8.pitching_substitution(62)

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("b c b f b f")
t8.out("(F)P6")

# 5. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("b s")
t8.out("P6")

# 6. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b b")
t8.hit(1)
# Offensive change (BOS): Pinch-runner #18 Shane Victorino replaces #37 Mike Carp
t8.offensive_substitution(6, 18, "PR")
t8.atbase("PR")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t8.new_ab()
t8.pitch_list("c 1 b s")
t8.out("P6")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b8.pitching_substitution(32)

# Defensive switch (BOS): #29 Daniel Nava moves to LF
b8.defensive_switch(29, "7")

# Defensive switch (BOS): #18 Shane Victorino moves to RF
b8.defensive_switch(18, "9")

# 1. TBR #20 Matt Joyce (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f b f f s")
b8.out("K")

# 2. TBR #18 Ben Zobrist (X - X - X)
b8.new_ab()
b8.pitch_list("f b f s")
b8.out("K")

# 3. TBR #2  Kelly Johnson (X - X - X)
b8.new_ab()
b8.pitch_list("b f b b c f")
b8.hit(2)

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b8.pitching_substitution(19)

# 4. TBR #3  Evan Longoria (X - 2 - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #54 Alex Torres
t9 = game.new_inning()

# Pitching change (TBR): #54 Alex Torres replaces #62 Joel Peralta
t9.pitching_substitution(54)

# 8. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c c b c")
t9.out("!K")

# 9. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("P5")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 5. TBR #21 James Loney (X - X - X)
b9.new_ab()
b9.hit(1)
# Offensive change (TBR): Pinch-runner #5 Sam Fuld replaces #21 James Loney
b9.offensive_substitution(5, 5, "PR")
b9.atbase("PR")
b9.advance(2, "59 SB")

# 6. TBR #8  Desmond Jennings (X - X - 21)
b9.new_ab()
b9.pitch_list("1 1 b b b c")
b9.out("F8")

# 7. TBR #30 Luke Scott (X - X - 5)
b9.new_ab()
b9.pitch_list("c f c")
b9.out("!K")

# 8. TBR #59 Jose Lobaton (X - X - 5)
b9.new_ab()
b9.pitch_list("c f b b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #91 Alfredo Aceves
game.winning_pitcher(91, is_away_team=True)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40, is_away_team=True)

# Loser team: TBR
# LP: TBR #22 Chris Archer
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
