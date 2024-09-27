import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-07-22
# https://www.baseball-reference.com/boxes/BOS/BOS201307220.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/07/22/348226/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-22 19:12-22:04",
        "at": "Fenway Park, Boston, MA",
        "att": "35,016",
        "temp": "72F, Cloudy",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 55,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                21: "James Loney",
                30: "Luke Scott",
                2: "Kelly Johnson",
                20: "Matt Joyce",
                59: "Jose Lobaton",
                11: "Yunel Escobar",
                # Starting pitcher
                55: "Matt Moore",
                # Bench
                28: "José Molina",
                1: "Sean Rodríguez",
                9: "Wil Myers",
                5: "Sam Fuld",
                # Bullpen
                58: "Jeremy Hellickson",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                14: "David Price",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27, 14],
            "lineup": [
                [8, "8"],
                [18, "4"],
                [3, "5"],
                [21, "3"],
                [30, "0"],
                [2, "7"],
                [20, "9"],
                [59, "2"],
                [11, "6"],
            ],
            "bench": [
                [28, "C"],
                [1, "2B"],
                [9, "RF"],
                [5, "LF"],
            ],
            "bullpen": [58, 62, 35, 43, 57, 54, 27, 14, 56, 22, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 67,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                10: "Jose Iglesias",
                # Starting pitcher
                67: "Brandon Workman",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
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
                [5, "7"],
                [20, "2"],
                [23, "5"],
                [10, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
            ],
            "bullpen": [65, 41, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Manny Gonzalez",
            "1B": "Tony Randazzo",
            "2B": "Larry Vanover",
            "3B": "Brian Gorman",
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
# Pitching: BOS #67 Brandon Workman
t1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("c c b f")
t1.hit(1)
t1.thrown_out(1, "18 PO", 1, 67)

# 2. TBR #18 Ben Zobrist (X - X - 8)
t1.new_ab()
t1.pitch_list("c b 1")
t1.hit(1)
t1.advance(3, "3 1B")
t1.advance(4, "21 SF9")

# 3. TBR #3  Evan Longoria (X - X - 18)
t1.new_ab()
t1.pitch_list("d c c b f b f")
t1.hit(1)
t1.advance(2, "30 BB")

# 4. TBR #21 James Loney (18 - X - 3)
t1.new_ab()
t1.pitch_list("1 c f b")
t1.out("SF9", rbis=1)

# 5. TBR #30 Luke Scott (X - X - 3)
t1.new_ab()
t1.pitch_list("b s c f b f f d b")
t1.reach("BB")

# 6. TBR #2  Kelly Johnson (X - 3 - 30)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("F7")


# Bot 1st
# Pitching: TBR #55 Matt Moore
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #67 Brandon Workman
t2 = game.new_inning()

# 7. TBR #20 Matt Joyce (X - X - X)
t2.new_ab()
t2.pitch_list("b c c f b s")
t2.out("K")

# 8. TBR #59 Jose Lobaton (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("P6")

# 9. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.hit(1)

# 1. TBR #8  Desmond Jennings (X - X - 11)
t2.new_ab()
t2.pitch_list("c f b")
t2.out("G5-3")


# Bot 2nd
# Pitching: TBR #55 Matt Moore
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("G2-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.hit(1)

# 6. BOS #5  Jonny Gomes (X - X - 12)
b2.new_ab()
b2.pitch_list("f f b s")
b2.out("K")

# 7. BOS #20 Ryan Lavarnway (X - X - 12)
b2.new_ab()
b2.pitch_list("f c d s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #67 Brandon Workman
t3 = game.new_inning()

# 2. TBR #18 Ben Zobrist (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.hit(1)
t3.advance(2, "21 SB")

# 3. TBR #3  Evan Longoria (X - X - 18)
t3.new_ab()
t3.out("F9")

# 4. TBR #21 James Loney (X - X - 18)
t3.new_ab()
t3.pitch_list("s 1 b")
t3.out("F8")

# 5. TBR #30 Luke Scott (X - 18 - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("(F)P5")


# Bot 3rd
# Pitching: TBR #55 Matt Moore
b3 = game.new_inning()

# 8. BOS #23 Brandon Snyder (X - X - X)
b3.new_ab()
b3.pitch_list("c f b s")
b3.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b c c s")
b3.out("K2-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #67 Brandon Workman
t4 = game.new_inning()

# 6. TBR #2  Kelly Johnson (X - X - X)
t4.new_ab()
t4.pitch_list("s f s")
t4.out("K")

# 7. TBR #20 Matt Joyce (X - X - X)
t4.new_ab()
t4.pitch_list("b c c")
t4.out("F9")

# 8. TBR #59 Jose Lobaton (X - X - X)
t4.new_ab()
t4.pitch_list("b c f f s")
t4.out("K")


# Bot 4th
# Pitching: TBR #55 Matt Moore
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b c s")
b4.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("f b")
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #67 Brandon Workman
t5 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")
t5.advance(2, "8 SAC3")
t5.advance(3, "18 1B")
t5.advance(4, "21 1B")

# 1. TBR #8  Desmond Jennings (X - X - 11)
t5.new_ab()
t5.pitch_list("l")
t5.out("SAC3")

# 2. TBR #18 Ben Zobrist (X - 11 - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "21 1B")

# 3. TBR #3  Evan Longoria (11 - X - 18)
t5.new_ab()
t5.pitch_list("c b 1 s b t")
t5.out("KT")

# 4. TBR #21 James Loney (11 - X - 18)
t5.new_ab()
t5.pitch_list("c d")
t5.hit(1, rbis=1)

# 5. TBR #30 Luke Scott (X - 18 - 21)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: TBR #55 Matt Moore
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b c b")
b5.reach("BB")
b5.thrown_out(2, "5 DP6-4-3", 1, 55)

# 6. BOS #5  Jonny Gomes (X - X - 12)
b5.new_ab()
b5.pitch_list("c")
b5.out("DP6-4-3")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b5.new_ab()
b5.pitch_list("b c f")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #67 Brandon Workman
t6 = game.new_inning()

# 6. TBR #2  Kelly Johnson (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c b")
t6.out("G4-3")

# 7. TBR #20 Matt Joyce (X - X - X)
t6.new_ab()
t6.out("G5-3")

# 8. TBR #59 Jose Lobaton (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F9")


# Bot 6th
# Pitching: TBR #55 Matt Moore
b6 = game.new_inning()

# 8. BOS #23 Brandon Snyder (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #65 Jose De La Torre
t7 = game.new_inning()

# Pitching change (BOS): #65 Jose De La Torre replaces #67 Brandon Workman
t7.pitching_substitution(65)

# 9. TBR #11 Yunel Escobar (X - X - X)
t7.new_ab()
t7.pitch_list("s s s")
t7.out("K")

# 1. TBR #8  Desmond Jennings (X - X - X)
t7.new_ab()
t7.pitch_list("c c b f")
t7.out("P5")

# 2. TBR #18 Ben Zobrist (X - X - X)
t7.new_ab()
t7.out("F8")


# Bot 7th
# Pitching: TBR #55 Matt Moore
b7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("f s b b b")
b7.hit(1)
b7.advance(2, "12 WP")

# 5. BOS #12 Mike Napoli (X - X - 34)
b7.new_ab()
b7.pitch_list("c c f b f")
b7.wp()
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #65 Jose De La Torre
t8 = game.new_inning()

# 3. TBR #3  Evan Longoria (X - X - X)
t8.new_ab()
t8.pitch_list("t s b c")
t8.out("!K")

# 4. TBR #21 James Loney (X - X - X)
t8.new_ab()
t8.pitch_list("b f b")
t8.out("G4-3")

# 5. TBR #30 Luke Scott (X - X - X)
t8.new_ab()
t8.pitch_list("b b s b")
t8.out("G3-1")


# Bot 8th
# Pitching: TBR #55 Matt Moore
b8 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("b s f")
b8.out("(F)P3")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b8.new_ab()
b8.pitch_list("c b f")
b8.out("F9")

# 8. BOS #23 Brandon Snyder (X - X - X)
b8.new_ab()
b8.pitch_list("b b c s f")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #65 Jose De La Torre
t9 = game.new_inning()

# 6. TBR #2  Kelly Johnson (X - X - X)
t9.new_ab()
t9.pitch_list("b s b s t")
t9.out("KT")

# 7. TBR #20 Matt Joyce (X - X - X)
t9.new_ab()
t9.pitch_list("s b b f b")
t9.hit(1)
t9.advance(2, "59 SB")
t9.advance(3, "11 BB")
t9.advance(4, "8 SF8")

# 8. TBR #59 Jose Lobaton (X - X - 20)
t9.new_ab()
t9.pitch_list("b d b f f d")
t9.reach("BB")
t9.advance(2, "11 BB")

# 9. TBR #11 Yunel Escobar (X - 20 - 59)
t9.new_ab()
t9.pitch_list("b b f f f d d")
t9.reach("BB")

# 1. TBR #8  Desmond Jennings (20 - 59 - 11)
t9.new_ab()
t9.pitch_list("b f f")
t9.out("SF8", rbis=1)

# Pitching change (BOS): #32 Craig Breslow replaces #65 Jose De La Torre
t9.pitching_substitution(32)

# 2. TBR #18 Ben Zobrist (X - 59 - 11)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("F9")


# Bot 9th
# Pitching: TBR #55 Matt Moore
b9 = game.new_inning()

# Defensive change (TBR): #5 Sam Fuld replaces #2 Kelly Johnson (LF), playing RF, batting 6th
b9.defensive_substitution(6, 5, "9")

# Defensive switch (TBR): #20 Matt Joyce moves to LF
b9.defensive_switch(20, "7")

# 9. BOS #10 Jose Iglesias (X - X - X)
b9.new_ab()
b9.pitch_list("b c c f")
b9.out("P4")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b9.new_ab()
b9.pitch_list("b c c")
b9.out("L5")

# Winning team: TBR
# WP: TBR #55 Matt Moore
game.winning_pitcher(55, is_away_team=True)

# Loser team: BOS
# LP: BOS #67 Brandon Workman
game.losing_pitcher(67)

# print(game)
game.generate_scorecard()
