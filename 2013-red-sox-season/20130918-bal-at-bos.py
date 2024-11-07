import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-09-18
# https://www.baseball-reference.com/boxes/BOS/BOS201309180.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/09/18/349009/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-18 19:10-23:11",
        "at": "Fenway Park, Boston, MA",
        "att": "38,540",
        "temp": "70F, Clear",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 16,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                19: "Chris Davis",
                10: "Adam Jones",
                21: "Nick Markakis",
                35: "Danny Valencia",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                1: "Brian Roberts",
                # Starting pitcher
                16: "Wei-Yin Chen",
                # Bench
                28: "Steve Pearce",
                3: "Ryan Flaherty",
                36: "Chris Dickerson",
                6: "Jonathan Schoop",
                48: "Chris Snyder",
                38: "Michael Morse",
                51: "Henry Urrutia",
                45: "Steve Clevenger",
                55: "Dan Johnson",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                60: "Josh Stinson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
                25: "Bud Norris",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
                52: "Steve Johnson",
            },
            "lefties": [16, 40, 66, 17],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [19, "3"],
                [10, "8"],
                [21, "9"],
                [35, "0"],
                [32, "2"],
                [2, "6"],
                [1, "4"],
            ],
            "bench": [
                [28, "1B"],
                [3, "2B"],
                [36, "LF"],
                [6, "2B"],
                [48, "C"],
                [38, "LF"],
                [51, "OF"],
                [45, "C"],
                [55, "1B"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 34, 60, 57, 29, 39, 56, 25, 39, 17, 43, 52],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                26: "Brock Holt",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
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
                [18, "8"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [29, "9"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [26, "2B"],
                [72, "2B"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Mark Wegner",
            "2B": "Tim Timmons",
            "3B": "Mike Winters",
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
# Pitching: BOS #44 Jake Peavy
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("c f c")
t1.out("!K")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G5-3")

# 3. BAL #19 Chris Davis (X - X - X)
t1.new_ab()
t1.pitch_list("s b f s")
t1.out("K")


# Bot 1st
# Pitching: BAL #16 Wei-Yin Chen
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b s")
b1.out("L8")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(1)
b1.advance(4, "34 HR")

# 3. BOS #34 David Ortiz (X - X - 18)
b1.new_ab()
b1.hit(4, rbis=2)

# 4. BOS #12 Mike Napoli (X - X - X)
b1.new_ab()
b1.pitch_list("b c c c")
b1.out("!K")

# 5. BOS #5  Jonny Gomes (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 6. BOS #29 Daniel Nava (X - X - 5)
b1.new_ab()
b1.pitch_list("c b c b b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #44 Jake Peavy
t2 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c s")
t2.out("K")

# 5. BAL #21 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c b s b c")
t2.out("!K")

# 6. BAL #35 Danny Valencia (X - X - X)
t2.new_ab()
t2.pitch_list("b c b c f f")
t2.out("G6-3")


# Bot 2nd
# Pitching: BAL #16 Wei-Yin Chen
b2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b")
b2.hit(1)
b2.thrown_out(2, "3 DP5-4-3", 2, 16)

# 8. BOS #7  Stephen Drew (X - X - 16)
b2.new_ab()
b2.pitch_list("f d c c")
b2.out("!K")

# 9. BOS #3  David Ross (X - X - 16)
b2.new_ab()
b2.pitch_list("b c s f b")
b2.out("DP5-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #44 Jake Peavy
t3 = game.new_inning()

# 7. BAL #32 Matt Wieters (X - X - X)
t3.new_ab()
t3.pitch_list("f b c f")
t3.out("F9")

# 8. BAL #2  J.J. Hardy (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("F8")

# 9. BAL #1  Brian Roberts (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f b f f b")
t3.reach("BB")

# 1. BAL #9  Nate McLouth (X - X - 1)
t3.new_ab()
t3.pitch_list("1 d s b 1 1 f c")
t3.out("!K")


# Bot 3rd
# Pitching: BAL #16 Wei-Yin Chen
b3 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("b b c")
b3.hit(1)
b3.advance(2, "18 1B")
b3.advance(3, "34 1B")
b3.thrown_out(4, "5 DP1-2-3", 2, 16)

# 2. BOS #18 Shane Victorino (X - X - 15)
b3.new_ab()
b3.pitch_list("1 b b c")
b3.hit(1)
b3.advance(2, "34 1B")

# 3. BOS #34 David Ortiz (X - 15 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("d f s b")
b3.hit(1)

# 4. BOS #12 Mike Napoli (15 - 18 - 34)
b3.new_ab(is_risp=True)
b3.pitch_list("s s b b f")
b3.out("L6")

# 5. BOS #5  Jonny Gomes (15 - 18 - 34)
b3.new_ab(is_risp=True)
b3.pitch_list("b c b")
b3.out("DP1-2-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #44 Jake Peavy
t4 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
t4.new_ab()
t4.pitch_list("b f c f b b c")
t4.out("!K")

# 3. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("b f b s f c")
t4.out("!K")

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.reach("HBP")
t4.advance(2, "21 BLK")

# 5. BAL #21 Nick Markakis (X - X - 10)
t4.new_ab(is_risp=True)
t4.pitch_list("c b n")
t4.balk()
t4.out("F7")


# Bot 4th
# Pitching: BAL #16 Wei-Yin Chen
b4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L1")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b f b c")
b4.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Jake Peavy
t5 = game.new_inning()

# 6. BAL #35 Danny Valencia (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.advance(4, "32 2B")

# 7. BAL #32 Matt Wieters (X - X - 35)
t5.new_ab()
t5.pitch_list("f b c f b b")
t5.hit(2, rbis=1)
t5.advance(3, "2 G6-3")
t5.advance(4, "1 2B")

# 8. BAL #2  J.J. Hardy (X - 32 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("G6-3")

# 9. BAL #1  Brian Roberts (32 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b d")
t5.hit(2, rbis=1)

# 1. BAL #9  Nate McLouth (X - 1 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s b s b s")
t5.out("K")

# 2. BAL #13 Manny Machado (X - 1 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("f")
t5.out("F8")


# Bot 5th
# Pitching: BAL #16 Wei-Yin Chen
b5 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F8")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(3, "18 G3-1")

# 2. BOS #18 Shane Victorino (X - 15 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f")
b5.out("G3-1")

# 3. BOS #34 David Ortiz (15 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Jake Peavy
t6 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L9")

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.out("G1-6-3")

# 5. BAL #21 Nick Markakis (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "35 1B")
t6.advance(4, "32 2B")

# 6. BAL #35 Danny Valencia (X - X - 21)
t6.new_ab()
t6.pitch_list("c d s")
t6.hit(1)
t6.advance(3, "32 2B")

# 7. BAL #32 Matt Wieters (X - 21 - 35)
t6.new_ab(is_risp=True)
t6.hit(2, rbis=1)

# 8. BAL #2  J.J. Hardy (35 - 32 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c")
t6.out("G6-3")


# Bot 6th
# Pitching: BAL #16 Wei-Yin Chen
b6 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("b f f b")
b6.hit(4)

# 5. BOS #5  Jonny Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("c b f s")
b6.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("G6-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("s c f b f")
b6.hit(1)
b6.advance(2, "7 1B")

# 8. BOS #7  Stephen Drew (X - X - 16)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "3 FC6-4", 3, 57)

# Pitching change (BAL): #57 Francisco Rodríguez replaces #16 Wei-Yin Chen
b6.pitching_substitution(57)

# 9. BOS #3  David Ross (X - 16 - 7)
b6.new_ab(is_risp=True)
b6.pitch_list("c 2 f d")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Jake Peavy
t7 = game.new_inning()

# 9. BAL #1  Brian Roberts (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f")
t7.out("G3-1")

# 1. BAL #9  Nate McLouth (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G4-3")

# 2. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("c c b")
t7.out("F7")


# Bot 7th
# Pitching: BAL #39 Kevin Gausman
b7 = game.new_inning()

# Pitching change (BAL): #39 Kevin Gausman replaces #57 Francisco Rodríguez
b7.pitching_substitution(39)

# 1. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c f c")
b7.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.out("F8")

# 3. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("f b s f f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #44 Jake Peavy
t8.pitching_substitution(32)

# 3. BAL #19 Chris Davis (X - X - X)
t8.new_ab()
t8.out("F7")

# 4. BAL #10 Adam Jones (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f")
t8.out("G5-3")

# 5. BAL #21 Nick Markakis (X - X - X)
t8.new_ab()
t8.pitch_list("b f f f")
t8.hit(1)

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t8.pitching_substitution(36)

# 6. BAL #35 Danny Valencia (X - X - 21)
t8.new_ab()
t8.pitch_list("s b c b b f f")
t8.out("L9")


# Bot 8th
# Pitching: BAL #39 Kevin Gausman
b8 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c f b f s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 5th
b8.offensive_substitution(5, 37, "PH")

# 5. BOS #37 Mike Carp (X - X - X)
b8.new_ab()
b8.pitch_list("b f c f b s")
b8.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Defensive switch (BOS): #37 Mike Carp moves to LF
t9.defensive_switch(37, "7")

# 7. BAL #32 Matt Wieters (X - X - X)
t9.new_ab()
t9.pitch_list("c f b c")
t9.out("!K")

# 8. BAL #2  J.J. Hardy (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G1-3")

# 9. BAL #1  Brian Roberts (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("G4-3")


# Bot 9th
# Pitching: BAL #29 Tommy Hunter
b9 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #39 Kevin Gausman
b9.pitching_substitution(29)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.thrown_out(2, "7 FC3-6", 1, 29)

# 8. BOS #7  Stephen Drew (X - X - 16)
b9.new_ab()
b9.reach("FC3-6")

# Offensive change (BOS): Pinch-hitter #39 Jarrod Saltalamacchia replaces #3 David Ross, batting 9th
b9.offensive_substitution(9, 39, "PH")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - 7)
b9.new_ab()
b9.pitch_list("c b s s")
b9.out("K")

# 1. BOS #15 Dustin Pedroia (X - X - 7)
b9.new_ab()
b9.pitch_list("c f b")
b9.out("L9")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #19 Koji Uehara
t10 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t10.pitching_substitution(19)

# Defensive switch (BOS): #39 Jarrod Saltalamacchia moves to C
t10.defensive_switch(39, "2")

# 1. BAL #9  Nate McLouth (X - X - X)
t10.new_ab()
t10.pitch_list("f b f f")
t10.out("L4")

# 2. BAL #13 Manny Machado (X - X - X)
t10.new_ab()
t10.pitch_list("c s s")
t10.out("K")

# 3. BAL #19 Chris Davis (X - X - X)
t10.new_ab()
t10.pitch_list("b s b")
t10.out("F8")


# Bot 10th
# Pitching: BAL #29 Tommy Hunter
b10 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b10.new_ab()
b10.pitch_list("b b s l f b")
b10.hit(1)
b10.thrown_out(2, "34 DP6-5-3", 1, 29)

# 3. BOS #34 David Ortiz (X - X - 18)
b10.new_ab()
b10.pitch_list("b c b s 1 f b")
b10.out("DP6-5-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b10.new_ab()
b10.pitch_list("b b")
b10.out("F7")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #56 Franklin Morales
t11 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #19 Koji Uehara
t11.pitching_substitution(56)

# 4. BAL #10 Adam Jones (X - X - X)
t11.new_ab()
t11.out("G4-3")

# 5. BAL #21 Nick Markakis (X - X - X)
t11.new_ab()
t11.pitch_list("c c")
t11.out("L7")

# 6. BAL #35 Danny Valencia (X - X - X)
t11.new_ab()
t11.pitch_list("b b b f f")
t11.out("P4")


# Bot 11th
# Pitching: BAL #66 T.J. McFarland
b11 = game.new_inning()

# Pitching change (BAL): #66 T.J. McFarland replaces #29 Tommy Hunter
b11.pitching_substitution(66)

# 5. BOS #37 Mike Carp (X - X - X)
b11.new_ab()
b11.pitch_list("c")
b11.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #37 Mike Carp
b11.offensive_substitution(5, 50, "PR")
b11.atbase("PR")
b11.advance(2, "29 SAC2-3")

# 6. BOS #29 Daniel Nava (X - X - 37)
b11.new_ab()
b11.out("SAC2-3")

# 7. BOS #16 Will Middlebrooks (X - 50 - X)
b11.new_ab(is_risp=True)
b11.pitch_list("i i i i")
b11.reach("IBB")
b11.thrown_out(2, "7 DP4-6-3", 2, 66)

# 8. BOS #7  Stephen Drew (X - 50 - 16)
b11.new_ab(is_risp=True)
b11.pitch_list("c b")
b11.out("DP4-6-3")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BOS #56 Franklin Morales
t12 = game.new_inning()

# Defensive switch (BOS): #50 Quintin Berry moves to LF
t12.defensive_switch(50, "7")

# 7. BAL #32 Matt Wieters (X - X - X)
t12.new_ab()
t12.pitch_list("b f b")
t12.out("F9")

# 8. BAL #2  J.J. Hardy (X - X - X)
t12.new_ab()
t12.pitch_list("c f")
t12.hit(1)
t12.advance(2, "1 1B")
t12.advance(3, "28 WP")
t12.advance(4, "19 1B")

# 9. BAL #1  Brian Roberts (X - X - 2)
t12.new_ab()
t12.pitch_list("c")
t12.hit(1)
t12.advance(2, "28 WP")
t12.advance(4, "19 1B")

# Offensive change (BAL): Pinch-hitter #28 Steve Pearce replaces #9 Nate McLouth, batting 1st
t12.offensive_substitution(1, 28, "PH")

# 1. BAL #28 Steve Pearce (X - 2 - 1)
t12.new_ab(is_risp=True)
t12.pitch_list("b i i i")
t12.wp()
t12.reach("IBB")
t12.advance(3, "19 1B")

# 2. BAL #13 Manny Machado (2 - 1 - 28)
t12.new_ab(is_risp=True)
t12.pitch_list("f f f f")
t12.out("(F)P3")

# 3. BAL #19 Chris Davis (2 - 1 - 28)
t12.new_ab(is_risp=True)
t12.pitch_list("b f c")
t12.hit(1, rbis=2)
t12.thrown_out(1, "10 PO", 3, 56)

# 4. BAL #10 Adam Jones (28 - X - 19)
t12.new_ab(is_risp=True)
t12.pitch_list("b s 1")
t12.no_ab("PO")


# Bot 12th
# Pitching: BAL #43 Jim Johnson
b12 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #66 T.J. McFarland
b12.pitching_substitution(43)

# Defensive change (BAL): #36 Chris Dickerson replaces #28 Steve Pearce (PH), playing LF, batting 1st
b12.defensive_substitution(1, 36, "7")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
b12.new_ab()
b12.pitch_list("f")
b12.hit(1)
b12.thrown_out(2, "15 FC6-4", 1, 43)

# 1. BOS #15 Dustin Pedroia (X - X - 39)
b12.new_ab()
b12.reach("FC6-4")
b12.thrown_out(2, "25 FC1-6", 2, 43)

# Offensive change (BOS): Pinch-hitter #25 Jackie Bradley Jr. replaces #18 Shane Victorino, batting 2nd
b12.offensive_substitution(2, 25, "PH")

# 2. BOS #25 Jackie Bradley Jr. (X - X - 15)
b12.new_ab()
b12.pitch_list("b d c")
b12.reach("FC1-6")

# 3. BOS #34 David Ortiz (X - X - 25)
b12.new_ab()
b12.out("G4-3")

# Winning team: BAL
# WP: BAL #66 T.J. McFarland
game.winning_pitcher(66, is_away_team=True)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43, is_away_team=True)

# Loser team: BOS
# LP: BOS #56 Franklin Morales
game.losing_pitcher(56)

# print(game)
game.generate_scorecard()
