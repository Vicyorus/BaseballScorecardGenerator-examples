import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-09-29
# https://www.baseball-reference.com/boxes/BAL/BAL201309290.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/09/29/349160/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-29 13:38-17:01",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "44,230",
        "temp": "71F, Partly Cloudy",
        "wind": "2mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                72: "Xander Bogaerts",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                10: "John McDonald",
                50: "Quintin Berry",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                7: "Stephen Drew",
                18: "Shane Victorino",
                26: "Brock Holt",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                3: "David Ross",
                15: "Dustin Pedroia",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
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
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [72, "6"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [16, "5"],
                [39, "2"],
                [10, "4"],
                [50, "9"],
            ],
            "bench": [
                [7, "SS"],
                [18, "CF"],
                [26, "2B"],
                [29, "LF"],
                [5, "LF"],
                [3, "C"],
                [15, "2B"],
                [25, "CF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 31, 36, 11, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 30,
            "roster": {
                # Lineup
                1: "Brian Roberts",
                21: "Nick Markakis",
                2: "J.J. Hardy",
                19: "Chris Davis",
                28: "Steve Pearce",
                9: "Nate McLouth",
                35: "Danny Valencia",
                45: "Steve Clevenger",
                6: "Jonathan Schoop",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                3: "Ryan Flaherty",
                36: "Chris Dickerson",
                10: "Adam Jones",
                48: "Chris Snyder",
                24: "Jason Pridie",
                38: "Michael Morse",
                51: "Henry Urrutia",
                55: "Dan Johnson",
                12: "Alexi Casilla",
                32: "Matt Wieters",
                # Bullpen
                50: "Miguel González",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
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
                [2, "6"],
                [19, "3"],
                [28, "7"],
                [9, "8"],
                [35, "5"],
                [45, "2"],
                [6, "4"],
            ],
            "bench": [
                [3, "2B"],
                [36, "LF"],
                [10, "CF"],
                [48, "C"],
                [24, "CF"],
                [38, "LF"],
                [51, "OF"],
                [55, "1B"],
                [12, "2B"],
                [32, "C"],
            ],
            "bullpen": [50, 40, 66, 34, 60, 57, 29, 39, 56, 25, 53, 39, 17, 43, 52, 65, 16],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "Fieldin Culbreth",
            "2B": "Adrian Johnson",
            "3B": "Bill Welke",
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
# Pitching: BAL #30 Chris Tillman
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(4)

# 2. BOS #72 Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("s b f t")
t1.out("KT")

# 3. BOS #34 David Ortiz (X - X - X)
t1.new_ab()
t1.pitch_list("b s b b")
t1.hit(1)
t1.advance(3, "12 2B")
t1.advance(4, "37 G6-3")

# 4. BOS #12 Mike Napoli (X - X - 34)
t1.new_ab()
t1.hit(2)
t1.advance(3, "37 G6-3")

# 5. BOS #37 Mike Carp (34 - 12 - X)
t1.new_ab()
t1.pitch_list("b d")
t1.out("G6-3", rbis=1)

# 6. BOS #16 Will Middlebrooks (12 - X - X)
t1.new_ab()
t1.out("L7")


# Bot 1st
# Pitching: BOS #64 Allen Webster
b1 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "21 BB")
b1.advance(3, "19 BB")

# 2. BAL #21 Nick Markakis (X - X - 1)
b1.new_ab()
b1.pitch_list("b d b c b")
b1.reach("BB")
b1.advance(2, "19 BB")

# 3. BAL #2  J.J. Hardy (X - 1 - 21)
b1.new_ab()
b1.pitch_list("b c d f f f s")
b1.out("K")

# 4. BAL #19 Chris Davis (X - 1 - 21)
b1.new_ab()
b1.pitch_list("s f b b b f f f f f d")
b1.reach("BB")
b1.thrown_out(2, "9 FC6", 3, 64)

# 5. BAL #28 Steve Pearce (1 - 21 - 19)
b1.new_ab()
b1.out("P6")

# 6. BAL #9  Nate McLouth (1 - 21 - 19)
b1.new_ab()
b1.pitch_list("b s s b f")
b1.reach("FC6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #30 Chris Tillman
t2 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b f c")
t2.out("L9")

# 8. BOS #10 John McDonald (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.hit(1)
t2.advance(4, "50 HR")

# 9. BOS #50 Quintin Berry (X - X - 10)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(4, rbis=2)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("f b s b c")
t2.out("!K")

# 2. BOS #72 Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("s b b")
t2.out("(F)P3")


# Bot 2nd
# Pitching: BOS #64 Allen Webster
b2 = game.new_inning()

# 7. BAL #35 Danny Valencia (X - X - X)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 8. BAL #45 Steve Clevenger (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G3")

# 9. BAL #6  Jonathan Schoop (X - X - X)
b2.new_ab()
b2.pitch_list("b f s")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #30 Chris Tillman
t3 = game.new_inning()

# 3. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("F9")

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f s")
t3.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #64 Allen Webster
b3 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("G3-1")

# 2. BAL #21 Nick Markakis (X - X - X)
b3.new_ab()
b3.out("L7")

# 3. BAL #2  J.J. Hardy (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #30 Chris Tillman
t4 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G3-1")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b s f b")
t4.hit(1)
t4.advance(2, "10 1B")
t4.error(2)
t4.advance(3, "2 1B")
t4.advance("U", "2 E2")

# 8. BOS #10 John McDonald (X - X - 39)
t4.new_ab()
t4.pitch_list("c c")
t4.hit(1)
t4.advance(3, "2 E2")

# 9. BOS #50 Quintin Berry (X - 39 - 10)
t4.new_ab()
t4.pitch_list("s s s")
t4.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - 10)
t4.new_ab()
t4.pitch_list("f c")
t4.hit(1)

# Defensive change (BAL): #3 Ryan Flaherty replaces #19 Chris Davis (1B), playing 1B, batting 4th
t4.defensive_substitution(4, 3, "3")

# 2. BOS #72 Xander Bogaerts (10 - X - 2)
t4.new_ab()
t4.pitch_list("s f b d f b f f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# Pitching change (BOS): #22 Felix Doubront replaces #64 Allen Webster
b4.pitching_substitution(22)

# 4. BAL #3  Ryan Flaherty (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("G3")

# 5. BAL #28 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b f b b")
b4.reach("BB")

# 6. BAL #9  Nate McLouth (X - X - 28)
b4.new_ab()
b4.pitch_list("f c c")
b4.out("!K")

# 7. BAL #35 Danny Valencia (X - X - 28)
b4.new_ab()
b4.pitch_list("b f f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #30 Chris Tillman
t5 = game.new_inning()

# 3. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("G3")

# 4. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b b f b b")
t5.reach("BB")
t5.advance(2, "16 WP")

# 5. BOS #37 Mike Carp (X - X - 12)
t5.new_ab()
t5.pitch_list("f b b b")
t5.out("F7")

# 6. BOS #16 Will Middlebrooks (X - X - 12)
t5.new_ab()
t5.pitch_list("b")
t5.wp()
t5.out("F7")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 8. BAL #45 Steve Clevenger (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "6 1B")
b5.advance(3, "21 BB")
b5.advance(4, "2 2B")

# 9. BAL #6  Jonathan Schoop (X - X - 45)
b5.new_ab()
b5.pitch_list("c d")
b5.hit(1)
b5.advance(2, "21 BB")
b5.advance(4, "2 2B")

# 1. BAL #1  Brian Roberts (X - 45 - 6)
b5.new_ab()
b5.pitch_list("c s d f f f f b s")
b5.out("K")

# 2. BAL #21 Nick Markakis (X - 45 - 6)
b5.new_ab()
b5.pitch_list("b b f b f b")
b5.reach("BB")
b5.advance(3, "2 2B")
b5.advance(4, "3 1B")

# 3. BAL #2  J.J. Hardy (45 - 6 - 21)
b5.new_ab()
b5.hit(2, rbis=2)
b5.advance(3, "3 1B")
b5.advance(4, "9 2B")

# 4. BAL #3  Ryan Flaherty (21 - 2 - X)
b5.new_ab()
b5.pitch_list("b f s")
b5.hit(1, rbis=1)
b5.advance(2, "28 BB")
b5.advance(4, "9 2B")

# 5. BAL #28 Steve Pearce (2 - X - 3)
b5.new_ab()
b5.pitch_list("f f d b f d f b")
b5.reach("BB")
b5.advance(3, "9 2B")

# 6. BAL #9  Nate McLouth (2 - 3 - 28)
b5.new_ab()
b5.pitch_list("b c s b")
b5.hit(2, rbis=2)

# Pitching change (BOS): #62 Rubby De La Rosa replaces #22 Felix Doubront
b5.pitching_substitution(62)

# 7. BAL #35 Danny Valencia (28 - 9 - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("G3")

# 8. BAL #45 Steve Clevenger (28 - 9 - X)
b5.new_ab()
b5.pitch_list("b f d c")
b5.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #66 T.J. McFarland
t6 = game.new_inning()

# Pitching change (BAL): #66 T.J. McFarland replaces #30 Chris Tillman
t6.pitching_substitution(66)

# Offensive change (BOS): Pinch-hitter #20 Ryan Lavarnway replaces #39 Jarrod Saltalamacchia, batting 7th
t6.offensive_substitution(7, 20, "PH")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b")
t6.out("G6-3")

# 8. BOS #10 John McDonald (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b s b")
t6.reach("BB")
t6.advance(2, "50 1B")
t6.advance(3, "2 F9")

# 9. BOS #50 Quintin Berry (X - X - 10)
t6.new_ab()
t6.hit(1)
t6.advance(2, "72 SB")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - 50)
t6.new_ab()
t6.pitch_list("s d s b f")
t6.out("F9")

# 2. BOS #72 Xander Bogaerts (10 - X - 50)
t6.new_ab()
t6.pitch_list("b b b c d")
t6.reach("BB")

# 3. BOS #34 David Ortiz (10 - 50 - 72)
t6.new_ab()
t6.out("G3")


# Bot 6th
# Pitching: BOS #62 Rubby De La Rosa
b6 = game.new_inning()

# Defensive switch (BOS): #20 Ryan Lavarnway moves to C
b6.defensive_switch(20, "2")

# 9. BAL #6  Jonathan Schoop (X - X - X)
b6.new_ab()
b6.pitch_list("c s f b f")
b6.hit(1)
b6.advance(3, "1 2B")
b6.advance(4, "21 WP")

# Pitching change (BOS): #38 Matt Thornton replaces #62 Rubby De La Rosa
b6.pitching_substitution(38)

# 1. BAL #1  Brian Roberts (X - X - 6)
b6.new_ab()
b6.hit(2)
b6.advance(3, "21 WP")
b6.advance(4, "3 2B")

# 2. BAL #21 Nick Markakis (6 - 1 - X)
b6.new_ab()
b6.pitch_list("b")
b6.wp()
b6.out("G6-3")

# Pitching change (BOS): #46 Ryan Dempster replaces #38 Matt Thornton
b6.pitching_substitution(46)

# 3. BAL #2  J.J. Hardy (1 - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("G6-3")

# 4. BAL #3  Ryan Flaherty (1 - X - X)
b6.new_ab()
b6.pitch_list("c b d s b")
b6.hit(2, rbis=1)

# 5. BAL #28 Steve Pearce (X - 3 - X)
b6.new_ab()
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #39 Jason Hammel
t7 = game.new_inning()

# Pitching change (BAL): #39 Jason Hammel replaces #66 T.J. McFarland
t7.pitching_substitution(39)

# 4. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b s b c f s")
t7.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(2)

# 6. BOS #16 Will Middlebrooks (X - 37 - X)
t7.new_ab()
t7.pitch_list("s b s d s")
t7.out("K2-3")

# 7. BOS #20 Ryan Lavarnway (X - 37 - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
b7.pitching_substitution(32)

# 6. BAL #9  Nate McLouth (X - X - X)
b7.new_ab()
b7.pitch_list("b f t b t")
b7.out("KT")

# 7. BAL #35 Danny Valencia (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c c f")
b7.hit(1)
b7.thrown_out(2, "45 DP6-4-3", 2, 32)

# 8. BAL #45 Steve Clevenger (X - X - 35)
b7.new_ab()
b7.pitch_list("c s")
b7.out("DP6-4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #39 Jason Hammel
t8 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #10 John McDonald, batting 8th
t8.offensive_substitution(8, 5, "PH")

# 8. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b s c")
t8.out("F8")

# 9. BOS #50 Quintin Berry (X - X - X)
t8.new_ab()
t8.out("L5")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("G4-3")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b8.pitching_substitution(19)

# Defensive change (BOS): #26 Brock Holt replaces #5 Jonny Gomes (PH), playing 2B, batting 8th
b8.defensive_substitution(8, 26, "4")

# 9. BAL #6  Jonathan Schoop (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.out("G5-3")

# 1. BAL #1  Brian Roberts (X - X - X)
b8.new_ab()
b8.pitch_list("s s b s")
b8.out("K")

# 2. BAL #21 Nick Markakis (X - X - X)
b8.new_ab()
b8.pitch_list("c f f")
b8.hit(2)

# 3. BAL #2  J.J. Hardy (X - 21 - X)
b8.new_ab()
b8.pitch_list("s")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #43 Jim Johnson
t9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #39 Jason Hammel
t9.pitching_substitution(43)

# 2. BOS #72 Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("f c b f f f s")
t9.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.hit(1)
t9.advance(2, "12 WP")
t9.advance(4, "12 1B")

# 4. BOS #12 Mike Napoli (X - X - 34)
t9.new_ab()
t9.pitch_list("b f b")
t9.wp()
t9.hit(1, rbis=1)
# Offensive change (BOS): Pinch-runner #25 Jackie Bradley Jr. replaces #12 Mike Napoli
t9.offensive_substitution(4, 25, "PR")
t9.atbase("PR")
t9.advance(3, "37 1B")

# 5. BOS #37 Mike Carp (X - X - 12)
t9.new_ab()
t9.pitch_list("1 c")
t9.hit(1)
t9.thrown_out(2, "16 DP5-4-3", 2, 43)

# 6. BOS #16 Will Middlebrooks (25 - X - 37)
t9.new_ab()
t9.pitch_list("b f")
t9.out("DP5-4-3")

# Winning team: BAL
# WP: BAL #66 T.J. McFarland
game.winning_pitcher(66)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #62 Rubby De La Rosa
game.losing_pitcher(62, is_away_team=True)

# print(game)
game.generate_scorecard()
