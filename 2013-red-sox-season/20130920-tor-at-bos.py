import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-09-20
# https://www.baseball-reference.com/boxes/BOS/BOS201309200.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/09/20/349046/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-20 19:10-22:36",
        "at": "Fenway Park, Boston, MA",
        "att": "37,215",
        "temp": "68F, Clear",
        "wind": "8mph, In From LF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 32,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                13: "Brett Lawrie",
                28: "Colby Rasmus",
                14: "Moisés Sierra",
                16: "Mark DeRosa",
                8: "Anthony Gose",
                9: "J.P. Arencibia",
                17: "Ryan Goins",
                # Starting pitcher
                32: "Esmil Rogers",
                # Bench
                66: "Munenori Kawasaki",
                26: "Adam Lind",
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
                56: "Mark Buehrle",
                47: "Luis Perez",
                38: "Darren Oliver",
                58: "Todd Redmond",
                29: "Dustin McGowan",
                4: "Kyle Drabek",
                33: "Jeremy Jeffress",
                21: "Sergio Santos",
                48: "J.A. Happ",
                44: "Casey Janssen",
            },
            "lefties": [24, 62, 56, 47, 38, 48],
            "lineup": [
                [7, "6"],
                [11, "7"],
                [13, "5"],
                [28, "8"],
                [14, "0"],
                [16, "3"],
                [8, "9"],
                [9, "2"],
                [17, "4"],
            ],
            "bench": [
                [66, "2B"],
                [26, "1B"],
                [22, "CF"],
                [15, "C"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 24, 62, 50, 64, 56, 47, 38, 58, 29, 4, 33, 21, 48, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                29: "Daniel Nava",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
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
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 38, 22],
            "lineup": [
                [15, "4"],
                [29, "9"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [18, "CF"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Larry Vanover",
            "1B": "Manny Gonzalez",
            "2B": "Eric Cooper",
            "3B": "Tony Randazzo",
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
# Pitching: BOS #31 Jon Lester
t1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. TOR #11 Rajai Davis (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b s")
t1.out("K")

# 3. TOR #13 Brett Lawrie (X - X - X)
t1.new_ab()
t1.pitch_list("b f s")
t1.out("L7")


# Bot 1st
# Pitching: TOR #32 Esmil Rogers
b1 = game.new_inning()

# Defensive switch (TOR): #11 Rajai Davis moves to RF
b1.defensive_switch(11, "9")

# Defensive change (TOR): #22 Kevin Pillar replaces #28 Colby Rasmus (CF), playing LF, batting 4th
b1.defensive_substitution(4, 22, "7")

# Defensive switch (TOR): #8 Anthony Gose moves to CF
b1.defensive_switch(8, "8")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.hit(2)
b1.advance(3, "29 F8")
b1.advance(4, "34 WP")

# 2. BOS #29 Daniel Nava (X - 15 - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F8")

# 3. BOS #34 David Ortiz (15 - X - X)
b1.new_ab()
b1.pitch_list("b d b c d")
b1.wp()
b1.reach("BB")
b1.advance(2, "12 BB")
b1.advance(3, "39 1B")
b1.thrown_out(4, "39 8-2", 3, 32)

# 4. BOS #12 Mike Napoli (X - X - 34)
b1.new_ab()
b1.pitch_list("c b c b b b")
b1.reach("BB")
b1.advance(2, "39 8-2")

# 5. BOS #37 Mike Carp (X - 34 - 12)
b1.new_ab()
b1.pitch_list("c f b d")
b1.out("L6")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 4. TOR #22 Kevin Pillar (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f f f")
t2.out("P4")

# 5. TOR #14 Moisés Sierra (X - X - X)
t2.new_ab()
t2.pitch_list("f b s b b b")
t2.reach("BB")
t2.advance(2, "16 1B")
t2.advance(3, "8 FC6-4")

# 6. TOR #16 Mark DeRosa (X - X - 14)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "8 FC6-4", 2, 31)

# 7. TOR #8  Anthony Gose (X - 14 - 16)
t2.new_ab()
t2.pitch_list("c b f f")
t2.reach("FC6-4")

# 8. TOR #9  J.P. Arencibia (14 - X - 8)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #32 Esmil Rogers
b2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b s")
b2.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 9. TOR #17 Ryan Goins (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.thrown_out(2, "7 FC4-6", 1, 31)

# 1. TOR #7  José Reyes (X - X - 17)
t3.new_ab()
t3.pitch_list("b")
t3.reach("FC4-6")

# 2. TOR #11 Rajai Davis (X - X - 7)
t3.new_ab()
t3.out("P4")

# 3. TOR #13 Brett Lawrie (X - X - 7)
t3.new_ab()
t3.out("G6-3")


# Bot 3rd
# Pitching: TOR #32 Esmil Rogers
b3 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b f b")
b3.hit(2)
b3.advance(3, "12 BB")
b3.advance(4, "37 BB")

# 3. BOS #34 David Ortiz (X - 29 - X)
b3.new_ab()
b3.pitch_list("b b b i")
b3.reach("IBB")
b3.advance(2, "12 BB")
b3.advance(3, "37 BB")

# 4. BOS #12 Mike Napoli (X - 29 - 34)
b3.new_ab()
b3.pitch_list("b b b c f b")
b3.reach("BB")
b3.advance(2, "37 BB")

# 5. BOS #37 Mike Carp (29 - 34 - 12)
b3.new_ab()
b3.pitch_list("b f f f b b b")
b3.reach("BB", rbis=1)
b3.thrown_out(2, "39 DP3-6-1", 2, 64)

# Pitching change (TOR): #64 Chad Jenkins replaces #32 Esmil Rogers
b3.pitching_substitution(64)

# 6. BOS #39 Jarrod Saltalamacchia (34 - 12 - 37)
b3.new_ab()
b3.pitch_list("c")
b3.out("DP3-6-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 4. TOR #22 Kevin Pillar (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b b")
t4.reach("BB")
t4.advance(2, "14 E5")
t4.advance(3, "16 1B")
t4.thrown_out(4, "8 DP5-2-5-2", 2, 31)

# 5. TOR #14 Moisés Sierra (X - X - 22)
t4.new_ab()
t4.pitch_list("b f f b")
t4.error(5)
t4.reach("E5")
t4.advance(2, "16 1B")
t4.thrown_out(3, "8 DP5-2-5-2", 1, 31)

# 6. TOR #16 Mark DeRosa (X - 22 - 14)
t4.new_ab()
t4.pitch_list("c f b f f f f b")
t4.hit(1)
t4.advance(2, "8 DP5-2-5-2")

# 7. TOR #8  Anthony Gose (22 - 14 - 16)
t4.new_ab()
t4.pitch_list("s s f f b")
t4.reach("DP5-2-5-2")

# 8. TOR #9  J.P. Arencibia (X - 16 - 8)
t4.new_ab()
t4.pitch_list("s b f b s")
t4.out("K")


# Bot 4th
# Pitching: TOR #64 Chad Jenkins
b4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b c s b b s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b f b")
b4.reach("BB")
b4.advance(2, "25 1B")

# 9. BOS #25 Jackie Bradley Jr. (X - X - 7)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.thrown_out(2, "15 DP4-3", 2, 64)

# 1. BOS #15 Dustin Pedroia (X - 7 - 25)
b4.new_ab()
b4.pitch_list("c b s")
b4.out("DP4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 9. TOR #17 Ryan Goins (X - X - X)
t5.new_ab()
t5.pitch_list("b c c b b f s")
t5.out("K")

# 1. TOR #7  José Reyes (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 2. TOR #11 Rajai Davis (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.advance(2, "13 SB")
t5.advance(3, "13 SB")
t5.advance(4, "13 1B")

# 3. TOR #13 Brett Lawrie (X - X - 11)
t5.new_ab()
t5.pitch_list("b c s f f d")
t5.hit(1, rbis=1)
t5.thrown_out(2, "22 CS", 3, 31)

# 4. TOR #22 Kevin Pillar (X - X - 13)
t5.new_ab()
t5.pitch_list("b b")
t5.no_ab("CS")


# Bot 5th
# Pitching: TOR #64 Chad Jenkins
b5 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b c c")
b5.out("F7")

# 3. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.out("G4-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 4. TOR #22 Kevin Pillar (X - X - X)
t6.new_ab()
t6.pitch_list("f c")
t6.error(6)
t6.reach("E6")

# 5. TOR #14 Moisés Sierra (X - X - 22)
t6.new_ab()
t6.pitch_list("c b f t")
t6.out("KT")

# 6. TOR #16 Mark DeRosa (X - X - 22)
t6.new_ab()
t6.pitch_list("f f b s")
t6.out("K")

# 7. TOR #8  Anthony Gose (X - X - 22)
t6.new_ab()
t6.pitch_list("b f c b f f b c")
t6.out("!K")


# Bot 6th
# Pitching: TOR #64 Chad Jenkins
b6 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G1-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(2)

# 7. BOS #16 Will Middlebrooks (X - 39 - X)
b6.new_ab()
b6.pitch_list("s b")
b6.out("F8")

# Pitching change (TOR): #62 Aaron Loup replaces #64 Chad Jenkins
b6.pitching_substitution(62)

# 8. BOS #7  Stephen Drew (X - 39 - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 8. TOR #9  J.P. Arencibia (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 9. TOR #17 Ryan Goins (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 1. TOR #7  José Reyes (X - X - X)
t7.new_ab()
t7.pitch_list("c s d f f f d d f c")
t7.out("!K")


# Bot 7th
# Pitching: TOR #45 Neil Wagner
b7 = game.new_inning()

# Pitching change (TOR): #45 Neil Wagner replaces #62 Aaron Loup
b7.pitching_substitution(45)

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.advance(2, "15 1B")
b7.advance(3, "29 1B")
b7.advance(4, "34 1B")

# 1. BOS #15 Dustin Pedroia (X - X - 25)
b7.new_ab()
b7.pitch_list("c 1")
b7.hit(1)
b7.advance(2, "29 1B")
b7.advance(3, "34 1B")
b7.thrown_out(4, "12 DP6-2-3", 1, 33)

# 2. BOS #29 Daniel Nava (X - 25 - 15)
b7.new_ab()
b7.pitch_list("b b b c")
b7.hit(1)
b7.advance(2, "34 1B")
b7.advance(3, "12 DP6-2-3")
b7.advance(4, "37 1B")

# 3. BOS #34 David Ortiz (25 - 15 - 29)
b7.new_ab()
b7.hit(1, rbis=1)
b7.advance(2, "12 DP6-2-3")
b7.advance(4, "37 1B")

# Pitching change (TOR): #33 Jeremy Jeffress replaces #45 Neil Wagner
b7.pitching_substitution(33)

# 4. BOS #12 Mike Napoli (15 - 29 - 34)
b7.new_ab()
b7.pitch_list("s")
b7.out("DP6-2-3")

# 5. BOS #37 Mike Carp (29 - 34 - X)
b7.new_ab()
b7.pitch_list("c f b")
b7.hit(1, rbis=2)
# Offensive change (BOS): Pinch-runner #5 Jonny Gomes replaces #37 Mike Carp
b7.offensive_substitution(5, 5, "PR")
b7.atbase("PR")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b7.new_ab()
b7.pitch_list("b b b c s f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t8.pitching_substitution(36)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 2. TOR #11 Rajai Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(2)
t8.advance(3, "13 G4-3")
t8.advance(4, "26 HR")

# 3. TOR #13 Brett Lawrie (X - 11 - X)
t8.new_ab()
t8.pitch_list("c f d")
t8.out("G4-3")

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #22 Kevin Pillar, batting 4th
t8.offensive_substitution(4, 26, "PH")

# 4. TOR #26 Adam Lind (11 - X - X)
t8.new_ab()
t8.pitch_list("b s b f d")
t8.hit(4, rbis=2)

# 5. TOR #14 Moisés Sierra (X - X - X)
t8.new_ab()
t8.pitch_list("s s d b f b")
t8.hit(1)
t8.advance(2, "8 1B")

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t8.pitching_substitution(19)

# 6. TOR #16 Mark DeRosa (X - X - 14)
t8.new_ab()
t8.pitch_list("b s b")
t8.out("F8")

# 7. TOR #8  Anthony Gose (X - X - 14)
t8.new_ab()
t8.pitch_list("1")
t8.hit(1)

# 8. TOR #9  J.P. Arencibia (X - 14 - 8)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K")


# Bot 8th
# Pitching: TOR #38 Darren Oliver
b8 = game.new_inning()

# Pitching change (TOR): #38 Darren Oliver replaces #33 Jeremy Jeffress
b8.pitching_substitution(38)

# Defensive switch (TOR): #26 Adam Lind moves to 1B
b8.defensive_switch(26, "3")

# Defensive switch (TOR): #16 Mark DeRosa moves to LF
b8.defensive_switch(16, "7")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.advance(2, "15 SB")
b8.advance(4, "15 1B")

# 8. BOS #7  Stephen Drew (X - X - 16)
b8.new_ab()
b8.pitch_list("b b 1 f")
b8.out("(F)P5")

# 9. BOS #25 Jackie Bradley Jr. (X - X - 16)
b8.new_ab()
b8.pitch_list("c b 1 1 s b c")
b8.out("!K")

# 1. BOS #15 Dustin Pedroia (X - X - 16)
b8.new_ab()
b8.pitch_list("c b s 1 b f")
b8.hit(1, rbis=1)
b8.advance(2, "T")

# 2. BOS #29 Daniel Nava (X - 15 - X)
b8.new_ab()
b8.pitch_list("s b b c")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Defensive change (BOS): #18 Shane Victorino replaces #25 Jackie Bradley Jr. (CF), playing CF, batting 9th
t9.defensive_substitution(9, 18, "8")

# 9. TOR #17 Ryan Goins (X - X - X)
t9.new_ab()
t9.pitch_list("b s b")
t9.out("G6-3")

# 1. TOR #7  José Reyes (X - X - X)
t9.new_ab()
t9.pitch_list("f b f d")
t9.hit(1)
t9.advance(2, "13 DI")

# 2. TOR #11 Rajai Davis (X - X - 7)
t9.new_ab()
t9.pitch_list("f b f")
t9.out("F8")

# 3. TOR #13 Brett Lawrie (X - X - 7)
t9.new_ab()
t9.pitch_list("b c b c s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: TOR
# LP: TOR #32 Esmil Rogers
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
