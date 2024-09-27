import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-09-21
# https://www.baseball-reference.com/boxes/BOS/BOS201309210.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/09/21/349062/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-21 19:13-22:20",
        "at": "Fenway Park, Boston, MA",
        "att": "37,569",
        "temp": "71F, Partly Cloudy",
        "wind": "18mph, Out To LF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                7: "José Reyes",
                66: "Munenori Kawasaki",
                13: "Brett Lawrie",
                26: "Adam Lind",
                14: "Moisés Sierra",
                11: "Rajai Davis",
                8: "Anthony Gose",
                9: "J.P. Arencibia",
                17: "Ryan Goins",
                # Starting pitcher
                56: "Mark Buehrle",
                # Bench
                16: "Mark DeRosa",
                22: "Kevin Pillar",
                15: "Mike Nickeas",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                24: "Ricky Romero",
                62: "Aaron Loup",
                50: "Steve Delabar",
                64: "Chad Jenkins",
                47: "Luis Perez",
                38: "Darren Oliver",
                58: "Todd Redmond",
                29: "Dustin McGowan",
                4: "Kyle Drabek",
                33: "Jeremy Jeffress",
                21: "Sergio Santos",
                48: "J.A. Happ",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [56, 24, 62, 47, 38, 48],
            "lineup": [
                [7, "6"],
                [66, "0"],
                [13, "5"],
                [26, "3"],
                [14, "7"],
                [11, "9"],
                [8, "8"],
                [9, "2"],
                [17, "4"],
            ],
            "bench": [
                [16, "3B"],
                [22, "CF"],
                [15, "C"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 24, 62, 50, 64, 47, 38, 58, 29, 4, 33, 21, 48, 44, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                7: "Stephen Drew",
                18: "Shane Victorino",
                34: "David Ortiz",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                72: "Xander Bogaerts",
                3: "David Ross",
                10: "John McDonald",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                26: "Brock Holt",
                15: "Dustin Pedroia",
                25: "Jackie Bradley Jr.",
                12: "Mike Napoli",
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
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [7, "6"],
                [18, "8"],
                [34, "0"],
                [5, "7"],
                [29, "9"],
                [16, "3"],
                [72, "5"],
                [3, "2"],
                [10, "4"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [26, "2B"],
                [15, "2B"],
                [25, "CF"],
                [12, "1B"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 31, 36, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Manny Gonzalez",
            "1B": "Eric Cooper",
            "2B": "Tony Randazzo",
            "3B": "Larry Vanover",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f b b s")
t1.out("K")

# 2. TOR #66 Munenori Kawasaki (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("P4")

# 3. TOR #13 Brett Lawrie (X - X - X)
t1.new_ab()
t1.pitch_list("s c s")
t1.out("K")


# Bot 1st
# Pitching: TOR #56 Mark Buehrle
b1 = game.new_inning()

# 1. BOS #7  Stephen Drew (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.hit(1)
b1.advance(2, "18 SAC5-3")
b1.advance(3, "34 L8")

# 2. BOS #18 Shane Victorino (X - X - 7)
b1.new_ab()
b1.out("SAC5-3")

# 3. BOS #34 David Ortiz (X - 7 - X)
b1.new_ab()
b1.pitch_list("b b c f")
b1.out("L8")

# 4. BOS #5  Jonny Gomes (7 - X - X)
b1.new_ab()
b1.pitch_list("b s s t")
b1.out("KT")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("b c b s")
t2.out("G4-3")

# 5. TOR #14 Moisés Sierra (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G6-3")

# 6. TOR #11 Rajai Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b b f f")
t2.out("G1-3")


# Bot 2nd
# Pitching: TOR #56 Mark Buehrle
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("F9")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b s")
b2.out("L7")

# 7. BOS #72 Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 7. TOR #8  Anthony Gose (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c")
t3.out("L9")

# 8. TOR #9  J.P. Arencibia (X - X - X)
t3.new_ab()
t3.out("G6-3")

# 9. TOR #17 Ryan Goins (X - X - X)
t3.new_ab()
t3.pitch_list("b c s b")
t3.out("G3")


# Bot 3rd
# Pitching: TOR #56 Mark Buehrle
b3 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("c b f s")
b3.out("K")

# 9. BOS #10 John McDonald (X - X - X)
b3.new_ab()
b3.pitch_list("b b c c s")
b3.out("K")

# 1. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "66 CS", 1, 11)

# 2. TOR #66 Munenori Kawasaki (X - X - 7)
t4.new_ab()
t4.pitch_list("b 1 1 f 1 1 b s b")
t4.out("L4")

# 3. TOR #13 Brett Lawrie (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b f")
t4.hit(1)
t4.advance(4, "26 2B")

# 4. TOR #26 Adam Lind (X - X - 13)
t4.new_ab()
t4.pitch_list("b 1 s b b f")
t4.hit(2, rbis=1)
t4.advance(3, "14 1B")
t4.advance(4, "11 1B")

# 5. TOR #14 Moisés Sierra (X - 26 - X)
t4.new_ab()
t4.pitch_list("s b c b f b")
t4.hit(1)
t4.advance(3, "11 1B")
t4.advance("U", "8 POE1")

# 6. TOR #11 Rajai Davis (26 - X - 14)
t4.new_ab()
t4.pitch_list("b f s")
t4.hit(1, rbis=1)
t4.error(1)
t4.advance(2, "8 POE1")

# 7. TOR #8  Anthony Gose (14 - X - 11)
t4.new_ab()
t4.pitch_list("1 f")
t4.out("F8")


# Bot 4th
# Pitching: TOR #56 Mark Buehrle
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b c f f b b")
b4.hit(1)
b4.thrown_out(2, "29 FC6-4", 3, 56)

# 3. BOS #34 David Ortiz (X - X - 18)
b4.new_ab()
b4.pitch_list("c b f d 1 s")
b4.out("K")

# 4. BOS #5  Jonny Gomes (X - X - 18)
b4.new_ab()
b4.pitch_list("c f d f c")
b4.out("!K")

# 5. BOS #29 Daniel Nava (X - X - 18)
b4.new_ab()
b4.pitch_list("c d f 1")
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 8. TOR #9  J.P. Arencibia (X - X - X)
t5.new_ab()
t5.pitch_list("b b c")
t5.out("G6-3")

# 9. TOR #17 Ryan Goins (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "7 BB")
t5.advance(3, "66 FC1-6")

# 1. TOR #7  José Reyes (X - X - 17)
t5.new_ab()
t5.pitch_list("1 b c b d b")
t5.reach("BB")
t5.thrown_out(2, "66 FC1-6", 2, 11)

# 2. TOR #66 Munenori Kawasaki (X - 17 - 7)
t5.new_ab()
t5.pitch_list("c s f b f")
t5.reach("FC1-6")

# 3. TOR #13 Brett Lawrie (17 - X - 66)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G3-1")


# Bot 5th
# Pitching: TOR #56 Mark Buehrle
b5 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L6")

# 7. BOS #72 Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("G6-3")

# 8. BOS #3  David Ross (X - X - X)
b5.new_ab()
b5.pitch_list("b b f")
b5.hit(1)

# 9. BOS #10 John McDonald (X - X - 3)
b5.new_ab()
b5.pitch_list("c f")
b5.out("P2")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f")
t6.out("F8")

# 5. TOR #14 Moisés Sierra (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 6. TOR #11 Rajai Davis (X - X - X)
t6.new_ab()
t6.pitch_list("c f b f b b b")
t6.reach("BB")
t6.thrown_out(2, "8 CS", 3, 11)

# 7. TOR #8  Anthony Gose (X - X - 11)
t6.new_ab()
t6.pitch_list("c f f 1 p")
t6.no_ab("CS")


# Bot 6th
# Pitching: TOR #56 Mark Buehrle
b6 = game.new_inning()

# 1. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("f c b f b b")
b6.hit(1)
b6.advance(2, "18 HBP")
b6.advance(4, "5 1B")

# 2. BOS #18 Shane Victorino (X - X - 7)
b6.new_ab()
b6.pitch_list("b b c b c")
b6.reach("HBP")
b6.advance(3, "5 1B")

# 3. BOS #34 David Ortiz (X - 7 - 18)
b6.new_ab()
b6.pitch_list("c b s d")
b6.out("F8")

# 4. BOS #5  Jonny Gomes (X - 7 - 18)
b6.new_ab()
b6.pitch_list("s s d b")
b6.hit(1, rbis=1)
b6.thrown_out(2, "29 DP6-4-3", 2, 56)

# 5. BOS #29 Daniel Nava (18 - X - 5)
b6.new_ab()
b6.pitch_list("b")
b6.out("DP6-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #66 Drake Britton
t7 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #11 Clay Buchholz
t7.pitching_substitution(66)

# 7. TOR #8  Anthony Gose (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f")
t7.hit(1)
t7.thrown_out(2, "17 CS", 2, 66)

# 8. TOR #9  J.P. Arencibia (X - X - 8)
t7.new_ab()
t7.pitch_list("1 f")
t7.out("F9")

# 9. TOR #17 Ryan Goins (X - X - 8)
t7.new_ab()
t7.pitch_list("1 d 1 1 c d s c")
t7.out("!K")


# Bot 7th
# Pitching: TOR #29 Dustin McGowan
b7 = game.new_inning()

# Pitching change (TOR): #29 Dustin McGowan replaces #56 Mark Buehrle
b7.pitching_substitution(29)

# 6. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("c c b s")
b7.out("K")

# 7. BOS #72 Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("t b")
b7.error(5)
b7.reach("E5", end_base=2)
b7.advance(3, "3 WP")
b7.advance("U", "3 G6-3")

# 8. BOS #3  David Ross (X - 72 - X)
b7.new_ab()
b7.pitch_list("c s b b b f")
b7.wp()
b7.out("G6-3", rbis=1)

# Offensive change (BOS): Pinch-hitter #15 Dustin Pedroia replaces #10 John McDonald, batting 9th
b7.offensive_substitution(9, 15, "PH")

# 9. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c s b f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #46 Ryan Dempster
t8 = game.new_inning()

# Pitching change (BOS): #46 Ryan Dempster replaces #66 Drake Britton
t8.pitching_substitution(46)

# Defensive switch (BOS): #15 Dustin Pedroia moves to 2B
t8.defensive_switch(15, "4")

# 1. TOR #7  José Reyes (X - X - X)
t8.new_ab()
t8.pitch_list("c c b f b")
t8.out("L8")

# 2. TOR #66 Munenori Kawasaki (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c")
t8.out("G1-4-3")

# 3. TOR #13 Brett Lawrie (X - X - X)
t8.new_ab()
t8.pitch_list("b s b b f")
t8.hit(1)
t8.advance(2, "26 BB")

# 4. TOR #26 Adam Lind (X - X - 13)
t8.new_ab()
t8.pitch_list("b f b f d d")
t8.reach("BB")

# 5. TOR #14 Moisés Sierra (X - 13 - 26)
t8.new_ab()
t8.pitch_list("f c s")
t8.out("K")


# Bot 8th
# Pitching: TOR #21 Sergio Santos
b8 = game.new_inning()

# Pitching change (TOR): #21 Sergio Santos replaces #29 Dustin McGowan
b8.pitching_substitution(21)

# 1. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("s b c s")
b8.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #38 Matt Thornton
t9 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #46 Ryan Dempster
t9.pitching_substitution(38)

# 6. TOR #11 Rajai Davis (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b b")
t9.reach("BB")
t9.advance(2, "8 SAC5-3")
t9.advance(4, "9 1B")

# 7. TOR #8  Anthony Gose (X - X - 11)
t9.new_ab()
t9.out("SAC5-3")

# 8. TOR #9  J.P. Arencibia (X - 11 - X)
t9.new_ab()
t9.pitch_list("c c f f b")
t9.hit(1, rbis=1)
t9.advance(2, "17 G1")

# 9. TOR #17 Ryan Goins (X - X - 9)
t9.new_ab()
t9.pitch_list("s s b f b")
t9.out("G1")

# 1. TOR #7  José Reyes (X - 9 - X)
t9.new_ab()
t9.pitch_list("b c f b b b")
t9.reach("BB")

# Pitching change (BOS): #62 Rubby De La Rosa replaces #38 Matt Thornton
t9.pitching_substitution(62)

# Offensive change (TOR): Pinch-hitter #16 Mark DeRosa replaces #66 Munenori Kawasaki, batting 2nd
t9.offensive_substitution(2, 16, "PH")

# 2. TOR #16 Mark DeRosa (X - 9 - 7)
t9.new_ab()
t9.pitch_list("s c b b b")
t9.out("G4-3")


# Bot 9th
# Pitching: TOR #44 Casey Janssen
b9 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #21 Sergio Santos
b9.pitching_substitution(44)

# Defensive switch (TOR): #16 Mark DeRosa moves to DH
b9.defensive_switch(16, "0")

# 4. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("c f f c")
b9.out("!K")

# 5. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("f b c b")
b9.out("F7")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.pitch_list("c f b s")
b9.out("K")

# Winning team: TOR
# WP: TOR #56 Mark Buehrle
game.winning_pitcher(56, is_away_team=True)
# SV: TOR #44 Casey Janssen
game.save_pitcher(44, is_away_team=True)

# Loser team: BOS
# LP: BOS #11 Clay Buchholz
game.losing_pitcher(11)

# print(game)
game.generate_scorecard()
