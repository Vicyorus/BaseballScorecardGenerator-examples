import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-09-07
# https://www.baseball-reference.com/boxes/NYA/NYA201309070.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/09/07/348855/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-07 13:06-16:38",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "49,046",
        "temp": "76F, Sunny",
        "wind": "7mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                72: "Xander Bogaerts",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                7: "Stephen Drew",
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                3: "David Ross",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
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
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [18, "9"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [16, "5"],
                [25, "8"],
                [20, "2"],
                [72, "6"],
            ],
            "bench": [
                [7, "SS"],
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [3, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 60,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                2: "Derek Jeter",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                14: "Curtis Granderson",
                26: "Eduardo Núñez",
                55: "Lyle Overbay",
                31: "Ichiro Suzuki",
                53: "Austin Romine",
                # Starting pitcher
                60: "David Huff",
                # Bench
                19: "Chris Stewart",
                22: "Vernon Wells",
                39: "Mark Reynolds",
                45: "David Adams",
                66: "John Ryan Murphy",
                13: "Alex Rodriguez",
                # Bullpen
                61: "Dellin Betances",
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                34: "Jim Miller",
                43: "Adam Warren",
                64: "Cesar Cabral",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                70: "Brett Marshall",
                62: "Joba Chamberlain",
                30: "David Robertson",
                40: "Matt Daley",
            },
            "lefties": [60, 52, 48, 64, 46],
            "lineup": [
                [11, "8"],
                [2, "6"],
                [24, "4"],
                [12, "7"],
                [14, "0"],
                [26, "5"],
                [55, "3"],
                [31, "9"],
                [53, "2"],
            ],
            "bench": [
                [19, "C"],
                [22, "CF"],
                [39, "3B"],
                [45, "3B"],
                [66, "C"],
                [13, "SS"],
            ],
            "bullpen": [61, 18, 65, 27, 47, 52, 38, 48, 34, 43, 64, 42, 46, 70, 62, 30, 40],
        },
        "umpires": {
            "HP": "Sam Holbrook",
            "1B": "Andy Fletcher",
            "2B": "Rob Drake",
            "3B": "Joe West",
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
# Pitching: NYY #60 David Huff
t1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b c s")
t1.out("K")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G6-3")

# 2. NYY #2  Derek Jeter (X - X - X)
b1.new_ab()
b1.out("G6-3")

# 3. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.pitch_list("b c t f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #60 David Huff
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b s")
t2.hit(2)
t2.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (X - 34 - X)
t2.new_ab()
t2.pitch_list("b b b")
t2.hit(4, rbis=2)

# 6. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b c s b")
t2.out("P4")

# 7. BOS #25 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.out("P6")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("P3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
b2.new_ab()
b2.pitch_list("b f f f b f b b")
b2.reach("BB")
b2.advance(2, "14 SAC1-3")
b2.advance(4, "55 1B")

# 5. NYY #14 Curtis Granderson (X - X - 12)
b2.new_ab()
b2.pitch_list("c")
b2.out("SAC1-3")

# 6. NYY #26 Eduardo Núñez (X - 12 - X)
b2.new_ab()
b2.pitch_list("b c c s")
b2.out("K")

# 7. NYY #55 Lyle Overbay (X - 12 - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.advance(2, "31 1B")

# 8. NYY #31 Ichiro Suzuki (X - X - 55)
b2.new_ab()
b2.pitch_list("c b s")
b2.hit(1)

# 9. NYY #53 Austin Romine (X - 55 - 31)
b2.new_ab()
b2.pitch_list("f")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #60 David Huff
t3 = game.new_inning()

# 9. BOS #72 Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(2)
t3.advance(4, "5 HR")

# 1. BOS #18 Shane Victorino (X - 72 - X)
t3.new_ab()
t3.pitch_list("l b m d")
t3.reach("HBP")
t3.advance(4, "5 HR")

# 2. BOS #5  Jonny Gomes (X - 72 - 18)
t3.new_ab()
t3.hit(4, rbis=3)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("(F)P2")

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("f b b")
t3.out("F9")

# 5. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c b")
t3.out("L4")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("c c f")
b3.hit(1)
b3.advance(2, "2 WP")
b3.advance(3, "2 G3")
b3.advance(4, "24 1B")

# 2. NYY #2  Derek Jeter (X - X - 11)
b3.new_ab()
b3.pitch_list("c b f d b")
b3.wp()
b3.out("G3")

# 3. NYY #24 Robinson Canó (11 - X - X)
b3.new_ab()
b3.pitch_list("f f")
b3.hit(1, rbis=1)

# 4. NYY #12 Alfonso Soriano (X - X - 24)
b3.new_ab()
b3.pitch_list("c")
b3.out("F9")

# 5. NYY #14 Curtis Granderson (X - X - 24)
b3.new_ab()
b3.pitch_list("b f b c f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #60 David Huff
t4 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.hit(1)
t4.advance(2, "25 1B")
t4.advance(4, "20 2B")

# 7. BOS #25 Jackie Bradley Jr. (X - X - 16)
t4.new_ab()
t4.hit(1)
t4.advance(3, "20 2B")
t4.advance(4, "72 G4-3")

# 8. BOS #20 Ryan Lavarnway (X - 16 - 25)
t4.new_ab()
t4.pitch_list("c b b")
t4.hit(2, rbis=1)
t4.advance(3, "72 G4-3")
t4.advance(4, "18 2B")

# 9. BOS #72 Xander Bogaerts (25 - 20 - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("G4-3", rbis=1)

# 1. BOS #18 Shane Victorino (20 - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.hit(2, rbis=1)
t4.advance(4, "5 1B")

# Pitching change (NYY): #34 Jim Miller replaces #60 David Huff
t4.pitching_substitution(34)

# 2. BOS #5  Jonny Gomes (X - 18 - X)
t4.new_ab()
t4.pitch_list("c f")
t4.hit(1, rbis=1)
t4.advance(3, "15 2B")
t4.advance(4, "34 SF8")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t4.new_ab()
t4.pitch_list("b b b c")
t4.hit(2)
t4.advance(3, "34 SF8")

# 4. BOS #34 David Ortiz (5 - 15 - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("SF8", rbis=1)

# 5. BOS #12 Mike Napoli (15 - X - X)
t4.new_ab()
t4.pitch_list("d c f f b f f b")
t4.out("F7")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 6. NYY #26 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(2)
b4.advance(3, "55 G4-3")
b4.advance(4, "31 2B")

# 7. NYY #55 Lyle Overbay (X - 26 - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("G4-3")

# 8. NYY #31 Ichiro Suzuki (26 - X - X)
b4.new_ab()
b4.hit(2, rbis=1)

# 9. NYY #53 Austin Romine (X - 31 - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 1. NYY #11 Brett Gardner (X - 31 - X)
b4.new_ab()
b4.reach("HBP")

# 2. NYY #2  Derek Jeter (X - 31 - 11)
b4.new_ab()
b4.pitch_list("b f f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #34 Jim Miller
t5 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("f b s b")
t5.out("L9")

# 7. BOS #25 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b f f b f f b b")
t5.reach("BB")
t5.advance(4, "72 HR")

# 8. BOS #20 Ryan Lavarnway (X - X - 25)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("F8")

# 9. BOS #72 Xander Bogaerts (X - X - 25)
t5.new_ab()
t5.pitch_list("b d b c")
t5.hit(4, rbis=2)

# Pitching change (NYY): #70 Brett Marshall replaces #34 Jim Miller
t5.pitching_substitution(70)

# 1. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c b c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G6-3")

# 4. NYY #12 Alfonso Soriano (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 5. NYY #14 Curtis Granderson (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("G3-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #70 Brett Marshall
t6 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "34 DP3-6-1", 2, 70)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F9")

# 4. BOS #34 David Ortiz (X - X - 5)
t6.new_ab()
t6.pitch_list("b c b c b f f f f f f")
t6.out("DP3-6-1")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# Defensive change (BOS): #10 John McDonald replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
b6.defensive_substitution(3, 10, "4")

# 6. NYY #26 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "31 BB")
b6.advance(3, "66 FC3-6")
b6.advance(4, "11 2B")

# 7. NYY #55 Lyle Overbay (X - X - 26)
b6.new_ab()
b6.pitch_list("c f b s")
b6.out("K")

# 8. NYY #31 Ichiro Suzuki (X - X - 26)
b6.new_ab()
b6.pitch_list("c f f f b f b f b b")
b6.reach("BB")
b6.thrown_out(2, "66 FC3-6", 2, 41)

# Offensive change (NYY): Pinch-hitter #66 John Ryan Murphy replaces #53 Austin Romine, batting 9th
b6.offensive_substitution(9, 66, "PH")

# 9. NYY #66 John Ryan Murphy (X - 26 - 31)
b6.new_ab()
b6.pitch_list("b b b c")
b6.reach("FC3-6")
b6.advance(2, "11 DI")
b6.advance(4, "11 2B")

# 1. NYY #11 Brett Gardner (26 - X - 66)
b6.new_ab()
b6.pitch_list("f b f b")
b6.hit(2, rbis=2)
b6.advance(4, "2 1B")

# 2. NYY #2  Derek Jeter (X - 11 - X)
b6.new_ab()
b6.pitch_list("s b")
b6.hit(1, rbis=1)
# Offensive change (NYY): Pinch-runner #39 Mark Reynolds replaces #2 Derek Jeter
b6.offensive_substitution(2, 39, "PR")
b6.atbase("PR")
b6.advance(2, "24 1B")
b6.advance(4, "12 1B")

# Pitching change (BOS): #38 Matt Thornton replaces #41 John Lackey
b6.pitching_substitution(38)

# 3. NYY #24 Robinson Canó (X - X - 2)
b6.new_ab()
b6.pitch_list("s")
b6.hit(1)
b6.advance(2, "12 1B")

# 4. NYY #12 Alfonso Soriano (X - 39 - 24)
b6.new_ab()
b6.pitch_list("b b b")
b6.hit(1, rbis=1)

# 5. NYY #14 Curtis Granderson (X - 24 - 12)
b6.new_ab()
b6.pitch_list("c f d")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #70 Brett Marshall
t7 = game.new_inning()

# Defensive switch (NYY): #39 Mark Reynolds moves to 3B
t7.defensive_switch(39, "5")

# Defensive switch (NYY): #26 Eduardo Núñez moves to SS
t7.defensive_switch(26, "6")

# Defensive switch (NYY): #66 John Ryan Murphy moves to C
t7.defensive_switch(66, "2")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c c b")
t7.hit(1)
t7.advance(2, "25 WP")

# 7. BOS #25 Jackie Bradley Jr. (X - X - 16)
t7.new_ab()
t7.pitch_list("c f f b s")
t7.wp()
t7.out("K")

# 8. BOS #20 Ryan Lavarnway (X - 16 - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F7")


# Bot 7th
# Pitching: BOS #66 Drake Britton
b7 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #38 Matt Thornton
b7.pitching_substitution(66)

# 6. NYY #26 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 7. NYY #55 Lyle Overbay (X - X - X)
b7.new_ab()
b7.pitch_list("b c b f")
b7.out("F7")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b7.new_ab()
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #70 Brett Marshall
t8 = game.new_inning()

# 9. BOS #72 Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("F8")

# 1. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.out("G1-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.reach("HBP")

# 3. BOS #10 John McDonald (X - X - 5)
t8.new_ab()
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #66 Drake Britton
b8 = game.new_inning()

# 9. NYY #66 John Ryan Murphy (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "11 PB")
b8.advance(4, "39 2B")

# 1. NYY #11 Brett Gardner (X - X - 66)
b8.new_ab()
b8.pitch_list("c c d b b f b")
b8.pb()
b8.reach("BB")
b8.advance(4, "39 2B")

# 2. NYY #39 Mark Reynolds (X - 66 - 11)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2, rbis=2)

# 3. NYY #24 Robinson Canó (X - 39 - X)
b8.new_ab()
b8.pitch_list("c s")
b8.out("F7")

# Pitching change (BOS): #36 Junichi Tazawa replaces #66 Drake Britton
b8.pitching_substitution(36)

# 4. NYY #12 Alfonso Soriano (X - 39 - X)
b8.new_ab()
b8.pitch_list("c f b f")
b8.out("P4")

# 5. NYY #14 Curtis Granderson (X - 39 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #70 Brett Marshall
t9 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b f f s")
t9.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(4)

# 6. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("f b b b b")
t9.reach("BB")
t9.advance(2, "25 G3")

# 7. BOS #25 Jackie Bradley Jr. (X - X - 16)
t9.new_ab()
t9.pitch_list("b b f f f d f f 1")
t9.out("G3")

# 8. BOS #20 Ryan Lavarnway (X - 16 - X)
t9.new_ab()
t9.out("F7")


# Bot 9th
# Pitching: BOS #36 Junichi Tazawa
b9 = game.new_inning()

# 6. NYY #26 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c b s b")
b9.out("(F)P2")

# 7. NYY #55 Lyle Overbay (X - X - X)
b9.new_ab()
b9.pitch_list("b b b b")
b9.reach("BB")

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b9.pitching_substitution(32)

# 8. NYY #31 Ichiro Suzuki (X - X - 55)
b9.new_ab()
b9.pitch_list("b f b s")
b9.out("(F)P2")

# Offensive change (NYY): Pinch-hitter #22 Vernon Wells replaces #66 John Ryan Murphy, batting 9th
b9.offensive_substitution(9, 22, "PH")

# 9. NYY #22 Vernon Wells (X - X - 55)
b9.new_ab()
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41, is_away_team=True)

# Loser team: NYY
# LP: NYY #60 David Huff
game.losing_pitcher(60)

# print(game)
game.generate_scorecard()
