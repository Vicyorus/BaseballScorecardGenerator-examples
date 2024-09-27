import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-09-27
# https://www.baseball-reference.com/boxes/BAL/BAL201309270.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/09/27/349130/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-27 19:07-22:23",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "30,774",
        "temp": "70F, Partly Cloudy",
        "wind": "3mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                50: "Quintin Berry",
                37: "Mike Carp",
                18: "Shane Victorino",
                26: "Brock Holt",
                3: "David Ross",
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
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [37, "1B"],
                [18, "CF"],
                [26, "2B"],
                [3, "C"],
                [72, "2B"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 31, 36, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 34,
            "roster": {
                # Lineup
                1: "Brian Roberts",
                21: "Nick Markakis",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                9: "Nate McLouth",
                6: "Jonathan Schoop",
                3: "Ryan Flaherty",
                # Starting pitcher
                34: "Scott Feldman",
                # Bench
                28: "Steve Pearce",
                36: "Chris Dickerson",
                48: "Chris Snyder",
                24: "Jason Pridie",
                38: "Michael Morse",
                51: "Henry Urrutia",
                45: "Steve Clevenger",
                55: "Dan Johnson",
                12: "Alexi Casilla",
                35: "Danny Valencia",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                60: "Josh Stinson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
                25: "Bud Norris",
                53: "Zack Britton",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
                52: "Steve Johnson",
                65: "Mike Belfiore",
                16: "Wei-Yin Chen",
            },
            "lefties": [40, 66, 53, 17, 65, 16],
            "lineup": [
                [1, "0"],
                [21, "9"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [9, "7"],
                [6, "4"],
                [3, "5"],
            ],
            "bench": [
                [28, "1B"],
                [36, "LF"],
                [48, "C"],
                [24, "CF"],
                [38, "LF"],
                [51, "OF"],
                [45, "C"],
                [55, "1B"],
                [12, "2B"],
                [35, "3B"],
            ],
            "bullpen": [50, 30, 40, 66, 60, 57, 29, 39, 56, 25, 53, 39, 17, 43, 52, 65, 16],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Bill Welke",
            "2B": "Brian O'Nora",
            "3B": "Fieldin Culbreth",
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
# Pitching: BAL #34 Scott Feldman
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 2. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.hit(1)
t1.advance(3, "34 1B")
t1.advance(4, "12 2B")

# 3. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("f 1 1 d")
t1.hit(1)
t1.advance(3, "12 2B")
t1.advance(4, "29 HR")

# 4. BOS #12 Mike Napoli (15 - X - 34)
t1.new_ab()
t1.pitch_list("b f")
t1.hit(2, rbis=1)
t1.advance(4, "29 HR")

# 5. BOS #29 Daniel Nava (34 - 12 - X)
t1.new_ab()
t1.hit(4, rbis=3)

# 6. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c b b")
t1.reach("BB")
t1.advance(4, "7 3B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t1.new_ab()
t1.pitch_list("c f")
t1.out("(F)P5")

# 8. BOS #7  Stephen Drew (X - X - 5)
t1.new_ab()
t1.pitch_list("b b f s")
t1.hit(3, rbis=1)

# 9. BOS #16 Will Middlebrooks (7 - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("G2-3")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b s f f")
b1.hit(1)
b1.advance(2, "19 1B")

# 2. BAL #21 Nick Markakis (X - X - 1)
b1.new_ab()
b1.pitch_list("1 f")
b1.out("L7")

# 3. BAL #10 Adam Jones (X - X - 1)
b1.new_ab()
b1.pitch_list("c s")
b1.out("F8")

# 4. BAL #19 Chris Davis (X - X - 1)
b1.new_ab()
b1.pitch_list("s")
b1.hit(1)

# 5. BAL #32 Matt Wieters (X - 1 - 19)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #34 Scott Feldman
t2 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("L6")

# 2. BOS #15 Dustin Pedroia (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("L7")

# 3. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b s")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 6. BAL #2  J.J. Hardy (X - X - X)
b2.new_ab()
b2.pitch_list("c f f b s")
b2.out("K")

# 7. BAL #9  Nate McLouth (X - X - X)
b2.new_ab()
b2.pitch_list("s f f b b f f f")
b2.out("G3-1")

# 8. BAL #6  Jonathan Schoop (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #34 Scott Feldman
t3 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b b c")
t3.out("!K")

# 5. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b")
t3.hit(1)
t3.advance(2, "5 1B")
t3.advance(4, "39 2B")

# 6. BOS #5  Jonny Gomes (X - X - 29)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.advance(3, "39 2B")
t3.advance(4, "7 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - 5)
t3.new_ab()
t3.pitch_list("s b b s")
t3.hit(2, rbis=1)
t3.advance(4, "7 1B")

# Pitching change (BAL): #53 Zack Britton replaces #34 Scott Feldman
t3.pitching_substitution(53)

# 8. BOS #7  Stephen Drew (5 - 39 - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1, rbis=2)
t3.thrown_out(2, "8-3-6-3", 2, 53)

# 9. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b b f b")
t3.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
t3.new_ab()
t3.pitch_list("d b")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 9. BAL #3  Ryan Flaherty (X - X - X)
b3.new_ab()
b3.pitch_list("b c f b b t")
b3.out("KT")

# 1. BAL #1  Brian Roberts (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(4, "10 HR")

# 2. BAL #21 Nick Markakis (X - X - 1)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 3. BAL #10 Adam Jones (X - X - 1)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(4, rbis=2)

# 4. BAL #19 Chris Davis (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #53 Zack Britton
t4 = game.new_inning()

# 2. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.thrown_out(2, "34 FC4-6", 1, 53)

# 3. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("c s d")
t4.reach("FC4-6")

# 4. BOS #12 Mike Napoli (X - X - 34)
t4.new_ab()
t4.pitch_list("c b f c")
t4.out("!K")

# 5. BOS #29 Daniel Nava (X - X - 34)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G3")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 5. BAL #32 Matt Wieters (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c f")
b4.out("L8")

# 6. BAL #2  J.J. Hardy (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "9 FC1-6", 2, 11)

# 7. BAL #9  Nate McLouth (X - X - 2)
b4.new_ab()
b4.pitch_list("c")
b4.reach("FC1-6")

# 8. BAL #6  Jonathan Schoop (X - X - 9)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #53 Zack Britton
t5 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.thrown_out(2, "7 FC4-6", 2, 53)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t5.new_ab()
t5.pitch_list("f s s")
t5.out("K")

# 8. BOS #7  Stephen Drew (X - X - 5)
t5.new_ab()
t5.pitch_list("c")
t5.reach("FC4-6")

# 9. BOS #16 Will Middlebrooks (X - X - 7)
t5.new_ab()
t5.pitch_list("b b s f f b")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 9. BAL #3  Ryan Flaherty (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c f")
b5.hit(1)
b5.thrown_out(2, "21 DP4-6-3", 2, 11)

# 1. BAL #1  Brian Roberts (X - X - 3)
b5.new_ab()
b5.pitch_list("c b f b")
b5.out("F7")

# 2. BAL #21 Nick Markakis (X - X - 3)
b5.new_ab()
b5.pitch_list("b 1 b b c")
b5.out("DP4-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #53 Zack Britton
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.out("L6")

# 2. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.hit(1)
t6.thrown_out(2, "34 DP4-6-3", 2, 53)

# 3. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("c f b f")
t6.out("DP4-6-3")


# Bot 6th
# Pitching: BOS #11 Clay Buchholz
b6 = game.new_inning()

# 3. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("b b s s")
b6.out("F9")

# 4. BAL #19 Chris Davis (X - X - X)
b6.new_ab()
b6.hit(4)

# 5. BAL #32 Matt Wieters (X - X - X)
b6.new_ab()
b6.out("F8")

# 6. BAL #2  J.J. Hardy (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("(F)P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #52 Steve Johnson
t7 = game.new_inning()

# Pitching change (BAL): #52 Steve Johnson replaces #53 Zack Britton
t7.pitching_substitution(52)

# 4. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b b f b b")
t7.reach("BB")
t7.thrown_out(2, "5 FC3-6", 2, 52)

# 5. BOS #29 Daniel Nava (X - X - 12)
t7.new_ab()
t7.pitch_list("c s f s")
t7.out("K")

# 6. BOS #5  Jonny Gomes (X - X - 12)
t7.new_ab()
t7.pitch_list("c b c")
t7.reach("FC3-6")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t7.new_ab()
t7.pitch_list("b s s c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #11 Clay Buchholz
b7 = game.new_inning()

# Defensive change (BOS): #25 Jackie Bradley Jr. replaces #2 Jacoby Ellsbury (CF), playing CF, batting 1st
b7.defensive_substitution(1, 25, "8")

# 7. BAL #9  Nate McLouth (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b f c")
b7.out("!K")

# 8. BAL #6  Jonathan Schoop (X - X - X)
b7.new_ab()
b7.pitch_list("f s f f f")
b7.out("G1-3")

# 9. BAL #3  Ryan Flaherty (X - X - X)
b7.new_ab()
b7.pitch_list("c s b f f b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #52 Steve Johnson
t8 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("c b b s f b")
t8.out("P5")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("f c b c")
t8.out("!K")

# 1. BOS #25 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b f b b c b")
t8.reach("BB")
t8.advance(2, "15 BB")
t8.advance(4, "34 HR")

# 2. BOS #15 Dustin Pedroia (X - X - 25)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")
t8.advance(4, "34 HR")

# Pitching change (BAL): #65 Mike Belfiore replaces #52 Steve Johnson
t8.pitching_substitution(65)

# 3. BOS #34 David Ortiz (X - 25 - 15)
t8.new_ab()
t8.pitch_list("b c b")
t8.hit(4, rbis=3)

# 4. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("s b f b b b")
t8.reach("BB")
# Offensive change (BOS): Pinch-runner #23 Brandon Snyder replaces #12 Mike Napoli
t8.offensive_substitution(4, 23, "PR")
t8.atbase("PR")
t8.thrown_out(2, "29 FC5-4", 3, 65)

# 5. BOS #29 Daniel Nava (X - X - 12)
t8.new_ab()
t8.pitch_list("b b")
t8.reach("FC5-4")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #11 Clay Buchholz
b8.pitching_substitution(32)

# Defensive change (BOS): #26 Brock Holt replaces #15 Dustin Pedroia (2B), playing 2B, batting 2nd
b8.defensive_substitution(2, 26, "4")

# Defensive switch (BOS): #23 Brandon Snyder moves to 1B
b8.defensive_switch(23, "3")

# 1. BAL #1  Brian Roberts (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("(F)P4")

# Offensive change (BAL): Pinch-hitter #28 Steve Pearce replaces #21 Nick Markakis, batting 2nd
b8.offensive_substitution(2, 28, "PH")

# 2. BAL #28 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("c f b b b f f b")
b8.reach("BB")
b8.advance(2, "35 1B")

# 3. BAL #10 Adam Jones (X - X - 28)
b8.new_ab()
b8.pitch_list("b f f s")
b8.out("K")

# Offensive change (BAL): Pinch-hitter #35 Danny Valencia replaces #19 Chris Davis, batting 4th
b8.offensive_substitution(4, 35, "PH")

# 4. BAL #35 Danny Valencia (X - X - 28)
b8.new_ab()
b8.hit(1)

# 5. BAL #32 Matt Wieters (X - 28 - 35)
b8.new_ab()
b8.pitch_list("b")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #65 Mike Belfiore
t9 = game.new_inning()

# Defensive switch (BAL): #28 Steve Pearce moves to RF
t9.defensive_switch(28, "9")

# Defensive change (BAL): #24 Jason Pridie replaces #10 Adam Jones (CF), playing CF, batting 3rd
t9.defensive_substitution(3, 24, "8")

# Defensive switch (BAL): #35 Danny Valencia moves to 3B
t9.defensive_switch(35, "5")

# Defensive change (BAL): #48 Chris Snyder replaces #2 J.J. Hardy (SS), playing C, batting 6th
t9.defensive_substitution(6, 48, "2")

# Defensive change (BAL): #55 Dan Johnson replaces #32 Matt Wieters (C), playing 1B, batting 5th
t9.defensive_substitution(5, 55, "3")

# Defensive switch (BAL): #3 Ryan Flaherty moves to SS
t9.defensive_switch(3, "6")

# 6. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.hit(4)

# Offensive change (BOS): Pinch-hitter #20 Ryan Lavarnway replaces #39 Jarrod Saltalamacchia, batting 7th
t9.offensive_substitution(7, 20, "PH")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b f")
t9.out("P4")

# Offensive change (BOS): Pinch-hitter #72 Xander Bogaerts replaces #7 Stephen Drew, batting 8th
t9.offensive_substitution(8, 72, "PH")

# 8. BOS #72 Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b b f c b")
t9.hit(1)
t9.thrown_out(2, "16 DP6-4-3", 2, 65)

# 9. BOS #16 Will Middlebrooks (X - X - 72)
t9.new_ab()
t9.pitch_list("f b d c f b f")
t9.out("DP6-4-3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b9.pitching_substitution(19)

# Defensive switch (BOS): #20 Ryan Lavarnway moves to C
b9.defensive_switch(20, "2")

# Defensive switch (BOS): #72 Xander Bogaerts moves to SS
b9.defensive_switch(72, "6")

# 6. BAL #48 Chris Snyder (X - X - X)
b9.new_ab()
b9.pitch_list("b b b f f s")
b9.out("K")

# 7. BAL #9  Nate McLouth (X - X - X)
b9.new_ab()
b9.pitch_list("c c b b")
b9.out("L9")

# 8. BAL #6  Jonathan Schoop (X - X - X)
b9.new_ab()
b9.pitch_list("c b f b")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)

# Loser team: BAL
# LP: BAL #34 Scott Feldman
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
