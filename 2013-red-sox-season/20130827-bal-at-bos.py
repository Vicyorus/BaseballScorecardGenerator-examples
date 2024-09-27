import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-08-27
# https://www.baseball-reference.com/boxes/BOS/BOS201308270.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/08/27/348703/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-27 19:14-22:13",
        "at": "Fenway Park, Boston, MA",
        "att": "36,226",
        "temp": "69F, Partly Cloudy",
        "wind": "7mph, R To L",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 16,
            "roster": {
                # Lineup
                1: "Brian Roberts",
                13: "Manny Machado",
                19: "Chris Davis",
                10: "Adam Jones",
                21: "Nick Markakis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                35: "Danny Valencia",
                28: "Steve Pearce",
                # Starting pitcher
                16: "Wei-Yin Chen",
                # Bench
                24: "Wilson Betemit",
                31: "Taylor Teagarden",
                9: "Nate McLouth",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                25: "Bud Norris",
                17: "Brian Matusz",
                43: "Jim Johnson",
            },
            "lefties": [16, 40, 66, 17],
            "lineup": [
                [1, "4"],
                [13, "5"],
                [19, "3"],
                [10, "8"],
                [21, "9"],
                [32, "2"],
                [2, "6"],
                [35, "0"],
                [28, "7"],
            ],
            "bench": [
                [24, "3B"],
                [31, "C"],
                [9, "CF"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 34, 57, 29, 56, 25, 17, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                3: "David Ross",
                72: "Xander Bogaerts",
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
                19: "Koji Uehara",
                38: "Matt Thornton",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [3, "C"],
                [72, "2B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 46],
        },
        "umpires": {
            "HP": "Wally Bell",
            "1B": "Marvin Hudson",
            "2B": "Tim McClelland",
            "3B": "Marty Foster",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G6-3")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.out("L8")

# 3. BAL #19 Chris Davis (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b b f s")
t1.out("K")


# Bot 1st
# Pitching: BAL #16 Wei-Yin Chen
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c s c")
b1.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")
b1.advance(3, "15 2B")
b1.advance(4, "34 SF8")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c b f b")
b1.hit(2)
b1.advance(3, "34 SF8")

# 4. BOS #34 David Ortiz (18 - 15 - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("SF8", rbis=1)

# 5. BOS #5  Jonny Gomes (15 - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b s")
t2.out("K")

# 5. BAL #21 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b s")
t2.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G3")


# Bot 2nd
# Pitching: BAL #16 Wei-Yin Chen
b2 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c c f s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c b s s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 7. BAL #2  J.J. Hardy (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b f")
t3.hit(1)
t3.advance(2, "35 1B")
t3.advance(3, "28 HBP")
t3.advance(4, "1 BB")

# 8. BAL #35 Danny Valencia (X - X - 2)
t3.new_ab()
t3.pitch_list("d c b f")
t3.hit(1)
t3.advance(2, "28 HBP")
t3.advance(3, "1 BB")
t3.advance(4, "13 SF9")

# 9. BAL #28 Steve Pearce (X - 2 - 35)
t3.new_ab()
t3.reach("HBP")
t3.advance(2, "1 BB")
t3.advance(3, "13 SF9")

# 1. BAL #1  Brian Roberts (2 - 35 - 28)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB", rbis=1)

# 2. BAL #13 Manny Machado (35 - 28 - 1)
t3.new_ab()
t3.pitch_list("f")
t3.out("SF9", rbis=1)

# 3. BAL #19 Chris Davis (28 - X - 1)
t3.new_ab()
t3.pitch_list("1 f b d")
t3.out("P5")

# 4. BAL #10 Adam Jones (28 - X - 1)
t3.new_ab()
t3.pitch_list("s f b d s")
t3.out("K")


# Bot 3rd
# Pitching: BAL #16 Wei-Yin Chen
b3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.hit(1)
b3.advance(4, "18 HR")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b3.new_ab()
b3.pitch_list("b f f b")
b3.out("F7")

# 2. BOS #18 Shane Victorino (X - X - 16)
b3.new_ab()
b3.pitch_list("b b c d")
b3.hit(4, rbis=2)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
b3.new_ab()
b3.out("P4")

# 5. BOS #5  Jonny Gomes (X - X - 15)
b3.new_ab()
b3.pitch_list("b f c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 5. BAL #21 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("c c b b b s")
t4.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
t4.new_ab()
t4.pitch_list("c c b f s")
t4.out("K")

# 7. BAL #2  J.J. Hardy (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("(F)P5")


# Bot 4th
# Pitching: BAL #16 Wei-Yin Chen
b4 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("s b f b")
b4.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)
b4.advance(2, "7 BB")
b4.advance(3, "2 1B")
b4.advance(4, "15 2B")

# 8. BOS #7  Stephen Drew (X - X - 39)
b4.new_ab()
b4.pitch_list("b b d b")
b4.reach("BB")
b4.advance(2, "2 1B")
b4.thrown_out(3, "2 8-2-4-5", 2, 16)

# 9. BOS #16 Will Middlebrooks (X - 39 - 7)
b4.new_ab()
b4.pitch_list("c b b b f f c")
b4.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - 7)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)
b4.advance(2, "8-2-4-5")
b4.advance(4, "15 2B")

# 2. BOS #18 Shane Victorino (39 - 2 - X)
b4.new_ab()
b4.pitch_list("c")
b4.reach("HBP")
b4.advance(3, "15 2B")
b4.advance(4, "5 2B")

# 3. BOS #15 Dustin Pedroia (39 - 2 - 18)
b4.new_ab()
b4.pitch_list("b d d c")
b4.hit(2, rbis=2)
b4.advance(4, "5 2B")

# 4. BOS #34 David Ortiz (18 - 15 - X)
b4.new_ab()
b4.pitch_list("i i i i")
b4.reach("IBB")
b4.advance(3, "5 2B")

# Pitching change (BAL): #50 Miguel González replaces #16 Wei-Yin Chen
b4.pitching_substitution(50)

# 5. BOS #5  Jonny Gomes (18 - 15 - 34)
b4.new_ab()
b4.pitch_list("f")
b4.hit(2, rbis=2)

# 6. BOS #12 Mike Napoli (34 - 5 - X)
b4.new_ab()
b4.pitch_list("b f c b d")
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 8. BAL #35 Danny Valencia (X - X - X)
t5.new_ab()
t5.pitch_list("b b c")
t5.hit(1)
t5.thrown_out(2, "13 FC6-4", 3, 22)

# 9. BAL #28 Steve Pearce (X - X - 35)
t5.new_ab()
t5.out("L7")

# 1. BAL #1  Brian Roberts (X - X - 35)
t5.new_ab()
t5.pitch_list("f c")
t5.out("F8")

# 2. BAL #13 Manny Machado (X - X - 35)
t5.new_ab()
t5.pitch_list("c b")
t5.reach("FC6-4")


# Bot 5th
# Pitching: BAL #40 Troy Patton
b5 = game.new_inning()

# Pitching change (BAL): #40 Troy Patton replaces #50 Miguel González
b5.pitching_substitution(40)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f s")
b5.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("s s b b b b")
b5.reach("BB")
b5.advance(2, "2 1B")
b5.advance(4, "18 HR")

# 9. BOS #16 Will Middlebrooks (X - X - 7)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b5.new_ab()
b5.pitch_list("b s f b")
b5.hit(1)
b5.advance(4, "18 HR")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
b5.new_ab()
b5.pitch_list("b")
b5.hit(4, rbis=3)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3")

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b f")
t6.out("G6-3")

# 5. BAL #21 Nick Markakis (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f")
t6.out("(F)P2")


# Bot 6th
# Pitching: BAL #40 Troy Patton
b6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("c b s s")
b6.out("K")

# 5. BOS #5  Jonny Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("c c b f s")
b6.out("K")

# 6. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
t7.new_ab()
t7.pitch_list("b c s f f s")
t7.out("K")

# 7. BAL #2  J.J. Hardy (X - X - X)
t7.new_ab()
t7.pitch_list("b c b s")
t7.hit(1)

# 8. BAL #35 Danny Valencia (X - X - 2)
t7.new_ab()
t7.pitch_list("b c b f b f f f")
t7.out("L8")

# Pitching change (BOS): #38 Matt Thornton replaces #22 Felix Doubront
t7.pitching_substitution(38)

# 9. BAL #28 Steve Pearce (X - X - 2)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G1-3")


# Bot 7th
# Pitching: BAL #17 Brian Matusz
b7 = game.new_inning()

# Pitching change (BAL): #17 Brian Matusz replaces #40 Troy Patton
b7.pitching_substitution(17)

# Offensive change (BOS): Pinch-hitter #3 David Ross replaces #39 Jarrod Saltalamacchia, batting 7th
b7.offensive_substitution(7, 3, "PH")

# 7. BOS #3  David Ross (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s c")
b7.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.out("L9")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("s b b b c")
b7.hit(1)
b7.advance(3, "2 2B")
b7.advance(4, "18 2B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b7.new_ab()
b7.pitch_list("b")
b7.hit(2)
b7.advance(4, "18 2B")

# 2. BOS #18 Shane Victorino (16 - 2 - X)
b7.new_ab()
b7.pitch_list("c f")
b7.hit(2, rbis=2)

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #66 Drake Britton
t8 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #38 Matt Thornton
t8.pitching_substitution(66)

# Defensive switch (BOS): #3 David Ross moves to C
t8.defensive_switch(3, "2")

# 1. BAL #1  Brian Roberts (X - X - X)
t8.new_ab()
t8.out("G5-3")

# 2. BAL #13 Manny Machado (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G6-3")

# Offensive change (BAL): Pinch-hitter #31 Taylor Teagarden replaces #19 Chris Davis, batting 3rd
t8.offensive_substitution(3, 31, "PH")

# 3. BAL #31 Taylor Teagarden (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("G4-3")


# Bot 8th
# Pitching: BAL #57 Francisco Rodríguez
b8 = game.new_inning()

# Pitching change (BAL): #57 Francisco Rodríguez replaces #17 Brian Matusz, batting 2nd
b8.pitching_substitution(57)
b8.defensive_substitution(2, 57, "1")

# Defensive switch (BAL): #31 Taylor Teagarden moves to C
b8.defensive_switch(31, "2")

# Defensive change (BAL): #9 Nate McLouth replaces #2 J.J. Hardy (SS), playing CF, batting 7th
b8.defensive_substitution(7, 9, "8")

# Defensive change (BAL): #24 Wilson Betemit replaces #32 Matt Wieters (C), playing 1B, batting 6th
b8.defensive_substitution(6, 24, "3")

# Defensive switch (BAL): #35 Danny Valencia moves to 3B
b8.defensive_switch(35, "5")

# Defensive change (BAL): #12 Alexi Casilla replaces #10 Adam Jones (CF), playing SS, batting 4th
b8.defensive_substitution(4, 12, "6")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("f f")
b8.out("G6-3")

# 5. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c b c s")
b8.out("K")

# 6. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b b f s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Drake Britton
t9 = game.new_inning()

# Defensive change (BOS): #72 Xander Bogaerts replaces #15 Dustin Pedroia (2B), playing 3B, batting 3rd
t9.defensive_substitution(3, 72, "5")

# Defensive switch (BOS): #16 Will Middlebrooks moves to 2B
t9.defensive_switch(16, "4")

# 4. BAL #12 Alexi Casilla (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# 5. BAL #21 Nick Markakis (X - X - X)
t9.new_ab()
t9.pitch_list("c f b s")
t9.out("K")

# 6. BAL #24 Wilson Betemit (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)

# Loser team: BAL
# LP: BAL #16 Wei-Yin Chen
game.losing_pitcher(16, is_away_team=True)

# print(game)
game.generate_scorecard()
