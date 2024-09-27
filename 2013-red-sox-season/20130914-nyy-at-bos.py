import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-09-14
# https://www.baseball-reference.com/boxes/BOS/BOS201309140.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/09/14/348957/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-14 13:07-15:50",
        "at": "Fenway Park, Boston, MA",
        "att": "37,510",
        "temp": "67F, Partly Cloudy",
        "wind": "7mph, L To R",
        "away": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                14: "Curtis Granderson",
                39: "Mark Reynolds",
                24: "Robinson Canó",
                13: "Alex Rodriguez",
                22: "Vernon Wells",
                55: "Lyle Overbay",
                35: "Brendan Ryan",
                31: "Ichiro Suzuki",
                66: "John Ryan Murphy",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                19: "Chris Stewart",
                26: "Eduardo Núñez",
                53: "Austin Romine",
                63: "Zoilo Almonte",
                12: "Alfonso Soriano",
                11: "Brett Gardner",
                45: "David Adams",
                # Bullpen
                61: "Dellin Betances",
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                38: "Preston Claiborne",
                48: "Boone Logan",
                60: "David Huff",
                41: "David Phelps",
                43: "Adam Warren",
                64: "Cesar Cabral",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                70: "Brett Marshall",
                62: "Joba Chamberlain",
                67: "Mike Zagurski",
                30: "David Robertson",
                40: "Matt Daley",
            },
            "lefties": [52, 48, 60, 64, 46, 67],
            "lineup": [
                [14, "8"],
                [39, "5"],
                [24, "4"],
                [13, "0"],
                [22, "7"],
                [55, "3"],
                [35, "6"],
                [31, "9"],
                [66, "2"],
            ],
            "bench": [
                [19, "C"],
                [26, "SS"],
                [53, "C"],
                [63, "LF"],
                [12, "LF"],
                [11, "LF"],
                [45, "3B"],
            ],
            "bullpen": [61, 18, 65, 27, 47, 38, 48, 60, 41, 43, 64, 42, 46, 70, 62, 67, 30, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                3: "David Ross",
                72: "Xander Bogaerts",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                7: "Stephen Drew",
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
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
                [18, "8"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [29, "9"],
                [16, "5"],
                [3, "2"],
                [72, "6"],
            ],
            "bench": [
                [7, "SS"],
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Mike DiMuro",
            "1B": "Ron Kulpa",
            "2B": "Alfonso Márquez",
            "3B": "Ted Barrett",
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

# 1. NYY #14 Curtis Granderson (X - X - X)
t1.new_ab()
t1.pitch_list("s c f")
t1.out("G3-1")

# 2. NYY #39 Mark Reynolds (X - X - X)
t1.new_ab()
t1.pitch_list("b f f")
t1.out("G4-3")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G6-3")


# Bot 1st
# Pitching: NYY #52 CC Sabathia
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.out("F8")

# 3. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 4. NYY #13 Alex Rodriguez (X - X - X)
t2.new_ab()
t2.pitch_list("b c b f f b")
t2.out("G6-3")

# 5. NYY #22 Vernon Wells (X - X - X)
t2.new_ab()
t2.out("L8")

# 6. NYY #55 Lyle Overbay (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f c")
t2.out("!K")


# Bot 2nd
# Pitching: NYY #52 CC Sabathia
b2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c c")
b2.hit(1)
b2.error(5)
b2.advance(2, "E5")
b2.advance(3, "29 SAC1-3")
b2.advance(4, "16 G6-3")

# 5. BOS #5  Jonny Gomes (X - 12 - X)
b2.new_ab()
b2.pitch_list("b b c b b")
b2.reach("BB")
b2.advance(2, "29 SAC1-3")
b2.advance(3, "16 G6-3")

# 6. BOS #29 Daniel Nava (X - 12 - 5)
b2.new_ab()
b2.out("SAC1-3")

# 7. BOS #16 Will Middlebrooks (12 - 5 - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G6-3", rbis=1)

# 8. BOS #3  David Ross (5 - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 9. BOS #72 Xander Bogaerts (5 - X - 3)
b2.new_ab()
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 7. NYY #35 Brendan Ryan (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s s")
t3.out("K")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("P4")

# 9. NYY #66 John Ryan Murphy (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G5-3")


# Bot 3rd
# Pitching: NYY #52 CC Sabathia
b3 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(2, "18 SAC5-3")
b3.advance(4, "34 2B")

# 2. BOS #18 Shane Victorino (X - X - 15)
b3.new_ab()
b3.out("SAC5-3")

# 3. BOS #34 David Ortiz (X - 15 - X)
b3.new_ab()
b3.hit(2, rbis=1)
b3.advance(3, "12 1B")
b3.advance(4, "5 1B")

# 4. BOS #12 Mike Napoli (X - 34 - X)
b3.new_ab()
b3.pitch_list("c f b b")
b3.hit(1)
b3.advance(2, "5 1B")

# 5. BOS #5  Jonny Gomes (34 - X - 12)
b3.new_ab()
b3.pitch_list("b b b c c")
b3.hit(1, rbis=1)

# 6. BOS #29 Daniel Nava (X - 12 - 5)
b3.new_ab()
b3.pitch_list("s c b c")
b3.out("!K")

# 7. BOS #16 Will Middlebrooks (X - 12 - 5)
b3.new_ab()
b3.pitch_list("f c d f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 1. NYY #14 Curtis Granderson (X - X - X)
t4.new_ab()
t4.pitch_list("c c f")
t4.hit(3)
t4.advance(4, "24 G3")

# 2. NYY #39 Mark Reynolds (14 - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("L4")

# 3. NYY #24 Robinson Canó (14 - X - X)
t4.new_ab()
t4.out("G3", rbis=1)

# 4. NYY #13 Alex Rodriguez (X - X - X)
t4.new_ab()
t4.pitch_list("c c b b f b f b")
t4.reach("BB")

# 5. NYY #22 Vernon Wells (X - X - 13)
t4.new_ab()
t4.out("(F)P3")


# Bot 4th
# Pitching: NYY #52 CC Sabathia
b4 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b4.new_ab()
b4.pitch_list("c s")
b4.hit(1)
b4.advance(2, "72 BB")
b4.advance(3, "15 DP6-4-3")
b4.advance(4, "18 1B")

# 9. BOS #72 Xander Bogaerts (X - X - 3)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.thrown_out(2, "15 DP6-4-3", 1, 52)

# 1. BOS #15 Dustin Pedroia (X - 3 - 72)
b4.new_ab()
b4.pitch_list("c")
b4.out("DP6-4-3")

# 2. BOS #18 Shane Victorino (3 - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1, rbis=1)

# 3. BOS #34 David Ortiz (X - X - 18)
b4.new_ab()
b4.pitch_list("1")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 6. NYY #55 Lyle Overbay (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")

# 7. NYY #35 Brendan Ryan (X - X - X)
t5.new_ab()
t5.pitch_list("f f")
t5.hit(1)
t5.thrown_out(2, "31 FC6-4", 2, 31)

# 8. NYY #31 Ichiro Suzuki (X - X - 35)
t5.new_ab()
t5.pitch_list("c f b b f f f")
t5.reach("FC6-4")

# 9. NYY #66 John Ryan Murphy (X - X - 31)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")


# Bot 5th
# Pitching: NYY #52 CC Sabathia
b5 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b b")
b5.reach("BB")
b5.advance(3, "5 2B")
b5.advance(4, "29 SF8")

# 5. BOS #5  Jonny Gomes (X - X - 12)
b5.new_ab()
b5.pitch_list("f c b")
b5.hit(2)

# 6. BOS #29 Daniel Nava (12 - 5 - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("SF8", rbis=1)

# 7. BOS #16 Will Middlebrooks (X - 5 - X)
b5.new_ab()
b5.pitch_list("b b c b c f f f s")
b5.out("K")

# 8. BOS #3  David Ross (X - 5 - X)
b5.new_ab()
b5.pitch_list("b f b b s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 1. NYY #14 Curtis Granderson (X - X - X)
t6.new_ab()
t6.pitch_list("b s")
t6.hit(2)
t6.advance(3, "24 G6-3")

# 2. NYY #39 Mark Reynolds (X - 14 - X)
t6.new_ab()
t6.out("F8")

# 3. NYY #24 Robinson Canó (X - 14 - X)
t6.new_ab()
t6.pitch_list("c b b b c")
t6.out("G6-3")

# 4. NYY #13 Alex Rodriguez (14 - X - X)
t6.new_ab()
t6.pitch_list("b c s f f")
t6.out("G5-3")


# Bot 6th
# Pitching: NYY #52 CC Sabathia
b6 = game.new_inning()

# 9. BOS #72 Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c f b s")
b6.out("K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c f f b f")
b6.hit(2)
b6.advance(3, "34 SB")

# 3. BOS #34 David Ortiz (X - 18 - X)
b6.new_ab()
b6.pitch_list("b s c f")
b6.out("L8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 5. NYY #22 Vernon Wells (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b")
t7.out("G6-3")

# 6. NYY #55 Lyle Overbay (X - X - X)
t7.new_ab()
t7.pitch_list("s s b b c")
t7.out("!K")

# 7. NYY #35 Brendan Ryan (X - X - X)
t7.new_ab()
t7.pitch_list("c s f b")
t7.out("G6-3")


# Bot 7th
# Pitching: NYY #62 Joba Chamberlain
b7 = game.new_inning()

# Pitching change (NYY): #62 Joba Chamberlain replaces #52 CC Sabathia
b7.pitching_substitution(62)

# 4. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c b b c f b f d")
b7.reach("BB")
b7.advance(2, "5 BB")

# 5. BOS #5  Jonny Gomes (X - X - 12)
b7.new_ab()
b7.pitch_list("b c b b b")
b7.reach("BB")
b7.thrown_out(1, "29 DP3", 2, 62)

# 6. BOS #29 Daniel Nava (X - 12 - 5)
b7.new_ab()
b7.out("DP3")

# 7. BOS #16 Will Middlebrooks (X - 12 - X)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #31 Jon Lester
t8 = game.new_inning()

# 8. NYY #31 Ichiro Suzuki (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G4-3")

# 9. NYY #66 John Ryan Murphy (X - X - X)
t8.new_ab()
t8.pitch_list("f b b f b b")
t8.reach("BB")

# 1. NYY #14 Curtis Granderson (X - X - 66)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F7")

# 2. NYY #39 Mark Reynolds (X - X - 66)
t8.new_ab()
t8.pitch_list("b s b f")
t8.out("G1-3")


# Bot 8th
# Pitching: NYY #40 Matt Daley
b8 = game.new_inning()

# Pitching change (NYY): #40 Matt Daley replaces #62 Joba Chamberlain
b8.pitching_substitution(40)

# 8. BOS #3  David Ross (X - X - X)
b8.new_ab()
b8.pitch_list("b f s s")
b8.out("K")

# 9. BOS #72 Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("f b b f c")
b8.out("!K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c f b")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #56 Franklin Morales
t9 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #31 Jon Lester
t9.pitching_substitution(56)

# 3. NYY #24 Robinson Canó (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b")
t9.out("G4-3")

# 4. NYY #13 Alex Rodriguez (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("G6-3")

# 5. NYY #22 Vernon Wells (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.out("P6")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)

# Loser team: NYY
# LP: NYY #52 CC Sabathia
game.losing_pitcher(52, is_away_team=True)

# print(game)
game.generate_scorecard()
