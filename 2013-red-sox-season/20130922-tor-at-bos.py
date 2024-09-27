import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-09-22
# https://www.baseball-reference.com/boxes/BOS/BOS201309220.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/09/22/349076/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-22 13:37-15:50",
        "at": "Fenway Park, Boston, MA",
        "att": "37,020",
        "temp": "68F, Partly Cloudy",
        "wind": "11mph, Out To RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                13: "Brett Lawrie",
                26: "Adam Lind",
                14: "Moisés Sierra",
                16: "Mark DeRosa",
                17: "Ryan Goins",
                22: "Kevin Pillar",
                22: "Josh Thole",
                # Starting pitcher
                43: "R.A. Dickey",
                # Bench
                66: "Munenori Kawasaki",
                9: "J.P. Arencibia",
                15: "Mike Nickeas",
                # Bullpen
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
                32: "Esmil Rogers",
                8: "Anthony Gose",
            },
            "lefties": [24, 62, 56, 47, 38, 48, 8],
            "lineup": [
                [7, "6"],
                [11, "8"],
                [13, "5"],
                [26, "3"],
                [14, "7"],
                [16, "0"],
                [17, "4"],
                [22, "9"],
                [22, "2"],
            ],
            "bench": [
                [66, "2B"],
                [9, "C"],
                [15, "C"],
            ],
            "bullpen": [45, 24, 62, 50, 64, 56, 47, 38, 58, 29, 4, 33, 21, 48, 44, 32, 8],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                37: "Mike Carp",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
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
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31, 38],
            "lineup": [
                [15, "4"],
                [18, "9"],
                [34, "0"],
                [37, "3"],
                [29, "7"],
                [16, "5"],
                [7, "6"],
                [20, "2"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 46],
        },
        "umpires": {
            "HP": "Eric Cooper",
            "1B": "Tony Randazzo",
            "2B": "Larry Vanover",
            "3B": "Manny Gonzalez",
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

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c f s")
t1.out("K")

# 2. TOR #11 Rajai Davis (X - X - X)
t1.new_ab()
t1.pitch_list("c t f f f")
t1.out("F8")

# 3. TOR #13 Brett Lawrie (X - X - X)
t1.new_ab()
t1.pitch_list("b c b")
t1.out("G4-3")


# Bot 1st
# Pitching: TOR #43 R.A. Dickey
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c f c")
b1.out("!K")

# 3. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G3-1")

# 5. TOR #14 Moisés Sierra (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("F9")

# 6. TOR #16 Mark DeRosa (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b b")
t2.reach("BB")
t2.advance(2, "17 1B")
t2.advance(4, "22 1B")

# 7. TOR #17 Ryan Goins (X - X - 16)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "22 1B")

# 8. TOR #22 Kevin Pillar (X - 16 - 17)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1, rbis=1)

# 9. TOR #22 Josh Thole (X - 17 - 22)
t2.new_ab()
t2.pitch_list("b f f f b c")
t2.out("!K")


# Bot 2nd
# Pitching: TOR #43 R.A. Dickey
b2 = game.new_inning()

# 4. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F8")

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "7 1B")
b2.advance(4, "20 1B")

# 6. BOS #16 Will Middlebrooks (X - X - 29)
b2.new_ab()
b2.pitch_list("c")
b2.out("F8")

# 7. BOS #7  Stephen Drew (X - X - 29)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(1)
b2.advance(3, "20 1B")
b2.advance(4, "25 HR")

# 8. BOS #20 Ryan Lavarnway (X - 29 - 7)
b2.new_ab()
b2.pitch_list("c f")
b2.hit(1, rbis=1)
b2.advance(4, "25 HR")

# 9. BOS #25 Jackie Bradley Jr. (7 - X - 20)
b2.new_ab()
b2.pitch_list("b")
b2.hit(4, rbis=3)

# 1. BOS #15 Dustin Pedroia (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b f")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G6-3")

# 2. TOR #11 Rajai Davis (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.thrown_out(2, "13 DP6-4-3", 2, 22)

# 3. TOR #13 Brett Lawrie (X - X - 11)
t3.new_ab()
t3.pitch_list("b c f 1 d")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: TOR #43 R.A. Dickey
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b")
b3.out("F7")

# 3. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.hit(2)

# 4. BOS #37 Mike Carp (X - 34 - X)
b3.new_ab()
b3.pitch_list("f f b b f t")
b3.out("KT")

# 5. BOS #29 Daniel Nava (X - 34 - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G5-3")

# 5. TOR #14 Moisés Sierra (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "17 WP")

# 6. TOR #16 Mark DeRosa (X - X - 14)
t4.new_ab()
t4.pitch_list("1 b")
t4.out("F8")

# 7. TOR #17 Ryan Goins (X - X - 14)
t4.new_ab()
t4.pitch_list("1 c b c f b f b")
t4.wp()
t4.out("L8")


# Bot 4th
# Pitching: TOR #43 R.A. Dickey
b4 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b c s f c")
b4.out("!K")

# 7. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 8. TOR #22 Kevin Pillar (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(4)

# 9. TOR #22 Josh Thole (X - X - X)
t5.new_ab()
t5.pitch_list("f c b")
t5.out("G5-3")

# 1. TOR #7  José Reyes (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("F7")

# 2. TOR #11 Rajai Davis (X - X - X)
t5.new_ab()
t5.pitch_list("b t s b b")
t5.out("P4")


# Bot 5th
# Pitching: TOR #43 R.A. Dickey
b5 = game.new_inning()

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b c c")
b5.out("!K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c c b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 3. TOR #13 Brett Lawrie (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.out("G4-3")

# 4. TOR #26 Adam Lind (X - X - X)
t6.new_ab()
t6.pitch_list("b s")
t6.out("G3")

# 5. TOR #14 Moisés Sierra (X - X - X)
t6.new_ab()
t6.pitch_list("s f b b f")
t6.out("F8")


# Bot 6th
# Pitching: TOR #43 R.A. Dickey
b6 = game.new_inning()

# 3. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.hit(4)

# 4. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("c c f s")
b6.out("K")

# 5. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("t b b b c")
b6.out("F7")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 6. TOR #16 Mark DeRosa (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.out("L9")

# 7. TOR #17 Ryan Goins (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G1-3")

# 8. TOR #22 Kevin Pillar (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")


# Bot 7th
# Pitching: TOR #43 R.A. Dickey
b7 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b f f b b")
b7.reach("BB")
b7.thrown_out(2, "20 DP5-4-3", 1, 43)

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
b7.new_ab()
b7.pitch_list("f")
b7.out("DP5-4-3")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("f c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Franklin Morales
t8 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #22 Felix Doubront
t8.pitching_substitution(56)

# 9. TOR #22 Josh Thole (X - X - X)
t8.new_ab()
t8.pitch_list("c c b f b f b")
t8.hit(1)
t8.thrown_out(2, "7 DP5-4-3", 1, 56)

# 1. TOR #7  José Reyes (X - X - 22)
t8.new_ab()
t8.pitch_list("b")
t8.out("DP5-4-3")

# 2. TOR #11 Rajai Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "13 WP")
t8.advance(3, "13 SB")

# 3. TOR #13 Brett Lawrie (X - X - 11)
t8.new_ab()
t8.pitch_list("1 b 1 b s c b b")
t8.wp()
t8.reach("BB")

# 4. TOR #26 Adam Lind (11 - X - 13)
t8.new_ab()
t8.pitch_list("c c f s")
t8.out("K")


# Bot 8th
# Pitching: TOR #43 R.A. Dickey
b8 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("c f s")
b8.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("f b s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #56 Franklin Morales
t9.pitching_substitution(19)

# 5. TOR #14 Moisés Sierra (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 6. TOR #16 Mark DeRosa (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F9")

# 7. TOR #17 Ryan Goins (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.out("G3-1")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: TOR
# LP: TOR #43 R.A. Dickey
game.losing_pitcher(43, is_away_team=True)

# print(game)
game.generate_scorecard()
