import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-08-14
# https://www.baseball-reference.com/boxes/TOR/TOR201308140.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/08/14/348541/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-14 19:08-22:28",
        "at": "Rogers Centre, Toronto, ON",
        "att": "31,695",
        "temp": "72F, Clear",
        "wind": "12mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [7, "6"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [29, "LF"],
                [20, "C"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 36, 19, 62, 22, 46],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 32,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                19: "José Bautista",
                10: "Edwin Encarnación",
                13: "Brett Lawrie",
                16: "Mark DeRosa",
                9: "J.P. Arencibia",
                22: "Kevin Pillar",
                66: "Munenori Kawasaki",
                # Starting pitcher
                32: "Esmil Rogers",
                # Bench
                3: "Maicer Izturis",
                26: "Adam Lind",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                51: "Thad Weber",
                56: "Mark Buehrle",
                37: "Mickey Storey",
                38: "Darren Oliver",
                58: "Todd Redmond",
                49: "Brad Lincoln",
                27: "Brett Cecil",
                21: "Sergio Santos",
                44: "Casey Janssen",
            },
            "lefties": [62, 56, 38, 27],
            "lineup": [
                [7, "6"],
                [11, "8"],
                [19, "9"],
                [10, "3"],
                [13, "5"],
                [16, "0"],
                [9, "2"],
                [22, "7"],
                [66, "4"],
            ],
            "bench": [
                [3, "3B"],
                [26, "1B"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 51, 56, 37, 38, 58, 49, 27, 21, 44],
        },
        "umpires": {
            "HP": "Phil Cuzzi",
            "1B": "Chris Guccione",
            "2B": "Ron Kulpa",
            "3B": "Tom Hallion",
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
# Pitching: TOR #32 Esmil Rogers
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f f f s")
t1.wp()
t1.reach("K")
t1.advance(2, "18 BB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("b b 1 b b")
t1.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t1.new_ab()
t1.pitch_list("c c f b s")
t1.out("K")

# 4. BOS #34 David Ortiz (X - 2 - 18)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 5. BOS #5  Jonny Gomes (X - 2 - 18)
t1.new_ab()
t1.pitch_list("b c b c")
t1.out("F9")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b")
b1.out("G1-3")

# 2. TOR #11 Rajai Davis (X - X - X)
b1.new_ab()
b1.out("L9")

# 3. TOR #19 José Bautista (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b b b")
b1.reach("BB")

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b1.new_ab()
b1.pitch_list("b b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #32 Esmil Rogers
t2 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("P6")

# 7. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("G6-3")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b c c")
t2.hit(2)

# 9. BOS #16 Will Middlebrooks (X - 39 - X)
t2.new_ab()
t2.out("F9")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. TOR #13 Brett Lawrie (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("G1-3")

# 6. TOR #16 Mark DeRosa (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 7. TOR #9  J.P. Arencibia (X - X - 16)
b2.new_ab()
b2.pitch_list("f b f s")
b2.out("K")

# 8. TOR #22 Kevin Pillar (X - X - 16)
b2.new_ab()
b2.pitch_list("c d f f f")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #32 Esmil Rogers
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c c")
t3.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f s")
t3.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("t f b")
t3.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("d c")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b c")
b3.out("!K")

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b f b")
b3.out("(F)P3")

# 2. TOR #11 Rajai Davis (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f")
b3.hit(1)
b3.error(1)
b3.advance(3, "E1")
b3.error(9)
b3.advance(4, "E9")

# 3. TOR #19 José Bautista (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #32 Esmil Rogers
t4 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.hit(1)
t4.thrown_out(2, "7 DP4-6-3", 1, 32)

# 6. BOS #7  Stephen Drew (X - X - 5)
t4.new_ab()
t4.pitch_list("b f c")
t4.out("DP4-6-3")

# 7. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b c")
t4.out("L4")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("f b b")
b4.hit(2)
b4.advance(4, "16 2B")

# 5. TOR #13 Brett Lawrie (X - 10 - X)
b4.new_ab()
b4.out("L3")

# 6. TOR #16 Mark DeRosa (X - 10 - X)
b4.new_ab()
b4.pitch_list("f c b b f")
b4.hit(2, rbis=1)

# 7. TOR #9  J.P. Arencibia (X - 16 - X)
b4.new_ab()
b4.out("F7")

# 8. TOR #22 Kevin Pillar (X - 16 - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #32 Esmil Rogers
t5 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b f f b c")
t5.out("!K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.hit(2)
t5.advance(3, "2 G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
t5.new_ab()
t5.pitch_list("b c f f b")
t5.out("G4-3")

# 2. BOS #18 Shane Victorino (16 - X - X)
t5.new_ab()
t5.pitch_list("t")
t5.out("L8")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G1-3")

# 1. TOR #7  José Reyes (X - X - X)
b5.new_ab()
b5.out("(F)P3")

# 2. TOR #11 Rajai Davis (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c f f")
b5.hit(2)

# 3. TOR #19 José Bautista (X - 11 - X)
b5.new_ab()
b5.pitch_list("s f b b b")
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #32 Esmil Rogers
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b s b s b")
t6.hit(4)

# 5. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L7")

# 6. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.out("L1")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.advance(3, "16 DP3-6-1")
b6.advance(4, "9 2B")

# 5. TOR #13 Brett Lawrie (X - 10 - X)
b6.new_ab()
b6.pitch_list("l s f b f")
b6.reach("HBP")
b6.thrown_out(2, "16 DP3-6-1", 1, 31)

# 6. TOR #16 Mark DeRosa (X - 10 - 13)
b6.new_ab()
b6.pitch_list("m")
b6.out("DP3-6-1")

# 7. TOR #9  J.P. Arencibia (10 - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(2, rbis=1)

# 8. TOR #22 Kevin Pillar (X - 9 - X)
b6.new_ab()
b6.pitch_list("f")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #45 Neil Wagner
t7 = game.new_inning()

# Pitching change (TOR): #45 Neil Wagner replaces #32 Esmil Rogers
t7.pitching_substitution(45)

# 7. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c f f")
t7.out("F9")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("b c t t")
t7.out("KT")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b7.new_ab()
b7.pitch_list("c b c")
b7.error(1)
b7.reach("E1")

# 1. TOR #7  José Reyes (X - X - 66)
b7.new_ab()
b7.pitch_list("c f b b s")
b7.out("K")

# Pitching change (BOS): #67 Brandon Workman replaces #31 Jon Lester
b7.pitching_substitution(67)

# 2. TOR #11 Rajai Davis (X - X - 66)
b7.new_ab()
b7.pitch_list("1 f s s")
b7.out("K")

# 3. TOR #19 José Bautista (X - X - 66)
b7.new_ab()
b7.pitch_list("f d b d")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #45 Neil Wagner
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c c f b")
t8.out("G3")


# Bot 8th
# Pitching: BOS #67 Brandon Workman
b8 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b8.new_ab()
b8.pitch_list("c b c s")
b8.out("K")

# 5. TOR #13 Brett Lawrie (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("F9")

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #16 Mark DeRosa, batting 6th
b8.offensive_substitution(6, 26, "PH")

# 6. TOR #26 Adam Lind (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")

# 7. TOR #9  J.P. Arencibia (X - X - 26)
b8.new_ab()
b8.pitch_list("c b s b b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #27 Brett Cecil
t9 = game.new_inning()

# Pitching change (TOR): #27 Brett Cecil replaces #45 Neil Wagner
t9.pitching_substitution(27)

# Defensive switch (TOR): #26 Adam Lind moves to DH
t9.defensive_switch(26, "0")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("s")
t9.out("B2-3")

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b c b")
t9.reach("BB")
t9.advance(4, "12 HR")

# 6. BOS #7  Stephen Drew (X - X - 5)
t9.new_ab()
t9.pitch_list("s c b s")
t9.out("K")

# 7. BOS #12 Mike Napoli (X - X - 5)
t9.new_ab()
t9.pitch_list("b")
t9.hit(4, rbis=2)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2)
# Offensive change (BOS): Pinch-runner #26 Brock Holt replaces #39 Jarrod Saltalamacchia
t9.offensive_substitution(8, 26, "PR")
t9.atbase("PR")
t9.advance(3, "2 1B")

# 9. BOS #16 Will Middlebrooks (X - 39 - X)
t9.new_ab()
t9.reach("HBP")
t9.advance(2, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 26 - 16)
t9.new_ab()
t9.pitch_list("s b")
t9.hit(1)

# Pitching change (TOR): #49 Brad Lincoln replaces #27 Brett Cecil
t9.pitching_substitution(49)

# 2. BOS #18 Shane Victorino (26 - 16 - 2)
t9.new_ab()
t9.pitch_list("b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #67 Brandon Workman
b9 = game.new_inning()

# Defensive change (BOS): #20 Ryan Lavarnway replaces #26 Brock Holt (PR), playing C, batting 8th
b9.defensive_substitution(8, 20, "2")

# 8. TOR #22 Kevin Pillar (X - X - X)
b9.new_ab()
b9.pitch_list("c b s f c")
b9.out("!K")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c c f")
b9.out("F7")

# 1. TOR #7  José Reyes (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TOR #49 Brad Lincoln
t10 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t10.new_ab()
t10.pitch_list("c c")
t10.hit(1)
t10.advance(2, "5 SB")

# 4. BOS #34 David Ortiz (X - X - 15)
t10.new_ab()
t10.pitch_list("c")
t10.out("F7")

# 5. BOS #5  Jonny Gomes (X - X - 15)
t10.new_ab()
t10.pitch_list("b b c c f b c")
t10.out("!K")

# 6. BOS #7  Stephen Drew (X - 15 - X)
t10.new_ab()
t10.pitch_list("b b b b")
t10.reach("BB")

# 7. BOS #12 Mike Napoli (X - 15 - 7)
t10.new_ab()
t10.pitch_list("c b f b f b")
t10.out("G5-3")


# Bot 10th
# Pitching: BOS #67 Brandon Workman
b10 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b10.new_ab()
b10.pitch_list("c t f b")
b10.hit(2)
b10.advance(3, "19 G6-3")
b10.advance(4, "13 1B")

# 3. TOR #19 José Bautista (X - 11 - X)
b10.new_ab()
b10.out("G6-3")

# 4. TOR #10 Edwin Encarnación (11 - X - X)
b10.new_ab()
b10.pitch_list("i i i i")
b10.reach("IBB")
b10.advance(2, "13 SB")
b10.advance(3, "13 1B")

# 5. TOR #13 Brett Lawrie (11 - X - 10)
b10.new_ab()
b10.pitch_list("c b s")
b10.hit(1, rbis=1)

# Winning team: TOR
# WP: TOR #49 Brad Lincoln
game.winning_pitcher(49)

# Loser team: BOS
# LP: BOS #67 Brandon Workman
game.losing_pitcher(67, is_away_team=True)

# print(game)
game.generate_scorecard()
