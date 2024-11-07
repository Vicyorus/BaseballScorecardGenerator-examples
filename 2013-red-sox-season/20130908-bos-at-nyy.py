import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-09-08
# https://www.baseball-reference.com/boxes/NYA/NYA201309080.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/09/08/348870/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-08 13:08-16:23",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "43,078",
        "temp": "80F, Partly Cloudy",
        "wind": "13mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
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
                [29, "9"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [18, "CF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 18,
            "roster": {
                # Lineup
                31: "Ichiro Suzuki",
                22: "Vernon Wells",
                12: "Alfonso Soriano",
                24: "Robinson Canó",
                13: "Alex Rodriguez",
                39: "Mark Reynolds",
                14: "Curtis Granderson",
                26: "Eduardo Núñez",
                19: "Chris Stewart",
                # Starting pitcher
                18: "Hiroki Kuroda",
                # Bench
                53: "Austin Romine",
                55: "Lyle Overbay",
                11: "Brett Gardner",
                45: "David Adams",
                66: "John Ryan Murphy",
                # Bullpen
                61: "Dellin Betances",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                60: "David Huff",
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
            "lefties": [52, 48, 60, 64, 46],
            "lineup": [
                [31, "9"],
                [22, "0"],
                [12, "7"],
                [24, "4"],
                [13, "5"],
                [39, "3"],
                [14, "8"],
                [26, "6"],
                [19, "2"],
            ],
            "bench": [
                [53, "C"],
                [55, "1B"],
                [11, "LF"],
                [45, "3B"],
                [66, "C"],
            ],
            "bullpen": [61, 65, 27, 47, 52, 38, 48, 60, 34, 43, 64, 42, 46, 70, 62, 30, 40],
        },
        "umpires": {
            "HP": "Andy Fletcher",
            "1B": "Rob Drake",
            "2B": "Joe West",
            "3B": "Sam Holbrook",
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
# Pitching: NYY #18 Hiroki Kuroda
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. NYY #31 Ichiro Suzuki (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("B1-3")

# 2. NYY #22 Vernon Wells (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G5-3")

# 3. NYY #12 Alfonso Soriano (X - X - X)
b1.new_ab()
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #18 Hiroki Kuroda
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b b")
t2.hit(2)
t2.advance(4, "37 2B")

# 5. BOS #37 Mike Carp (X - 34 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("f f b")
t2.hit(2, rbis=1)
t2.advance(3, "25 BB")

# 6. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b d f f f")
t2.out("F9")

# 7. BOS #7  Stephen Drew (X - 37 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b s b b f f f f s")
t2.out("K")

# 8. BOS #16 Will Middlebrooks (X - 37 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("s b b b b")
t2.reach("BB")
t2.advance(2, "25 BB")

# 9. BOS #25 Jackie Bradley Jr. (X - 37 - 16)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b c s b")
t2.reach("BB")

# 1. BOS #29 Daniel Nava (37 - 16 - 25)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. NYY #24 Robinson Canó (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f f")
b2.hit(1)
b2.advance(2, "13 1B")

# 5. NYY #13 Alex Rodriguez (X - X - 24)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)

# 6. NYY #39 Mark Reynolds (X - 24 - 13)
b2.new_ab(is_risp=True)
b2.out("(F)B2")

# 7. NYY #14 Curtis Granderson (X - 24 - 13)
b2.new_ab(is_risp=True)
b2.pitch_list("c s s")
b2.out("K")

# 8. NYY #26 Eduardo Núñez (X - 24 - 13)
b2.new_ab(is_risp=True)
b2.pitch_list("s b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #18 Hiroki Kuroda
t3 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.hit(1)
t3.thrown_out(2, "37 FC6", 3, 18)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t3.new_ab()
t3.pitch_list("f")
t3.out("F8")

# 4. BOS #34 David Ortiz (X - X - 5)
t3.new_ab()
t3.pitch_list("s d s 1 f s")
t3.out("K")

# 5. BOS #37 Mike Carp (X - X - 5)
t3.new_ab()
t3.pitch_list("d b")
t3.reach("FC6")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.reach("HBP")
b3.thrown_out(2, "22 DP4-6-3", 2, 31)

# 1. NYY #31 Ichiro Suzuki (X - X - 19)
b3.new_ab()
b3.out("F7")

# 2. NYY #22 Vernon Wells (X - X - 19)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("DP4-6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #18 Hiroki Kuroda
t4 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b f f")
t4.out("G3")

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f f b f s")
t4.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b c c f b")
t4.hit(1)
t4.advance(2, "25 PB")

# 9. BOS #25 Jackie Bradley Jr. (X - X - 16)
t4.new_ab(is_risp=True)
t4.pitch_list("s f b f c")
t4.pb()
t4.out("!K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 3. NYY #12 Alfonso Soriano (X - X - X)
b4.new_ab()
b4.pitch_list("c b c b f b")
b4.out("F9")

# 4. NYY #24 Robinson Canó (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("L3")

# 5. NYY #13 Alex Rodriguez (X - X - X)
b4.new_ab()
b4.pitch_list("c b s")
b4.hit(1)
b4.advance(4, "39 2B")

# 6. NYY #39 Mark Reynolds (X - X - 13)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2, rbis=1)

# 7. NYY #14 Curtis Granderson (X - 39 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c d f f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #18 Hiroki Kuroda
t5 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("F7")

# 2. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("b s s b s")
t5.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 8. NYY #26 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("P3")

# 9. NYY #19 Chris Stewart (X - X - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "31 1B")
b5.advance(3, "22 1B")
b5.advance(4, "24 2B")

# 1. NYY #31 Ichiro Suzuki (X - X - 19)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "22 1B")
b5.advance(4, "24 2B")

# 2. NYY #22 Vernon Wells (X - 19 - 31)
b5.new_ab(is_risp=True)
b5.pitch_list("s f d b")
b5.hit(1)
b5.advance(3, "24 2B")

# 3. NYY #12 Alfonso Soriano (19 - 31 - 22)
b5.new_ab(is_risp=True)
b5.pitch_list("c f s")
b5.out("K")

# 4. NYY #24 Robinson Canó (19 - 31 - 22)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b")
b5.hit(2, rbis=2)

# 5. NYY #13 Alex Rodriguez (22 - 24 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b c b s b b")
b5.reach("BB")
b5.thrown_out(2, "39 FC6-4", 3, 31)

# 6. NYY #39 Mark Reynolds (22 - 24 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("f b c f")
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #18 Hiroki Kuroda
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.hit(2)
t6.advance(3, "37 G4-3")
t6.advance(4, "39 G4-3")

# 5. BOS #37 Mike Carp (X - 34 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("d")
t6.out("G4-3")

# 6. BOS #39 Jarrod Saltalamacchia (34 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c b")
t6.out("G4-3", rbis=1)

# 7. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("b b f")
t6.out("F7")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 7. NYY #14 Curtis Granderson (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("F7")

# 8. NYY #26 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K2-3")

# Offensive change (NYY): Pinch-hitter #53 Austin Romine replaces #19 Chris Stewart, batting 9th
b6.offensive_substitution(9, 53, "PH")

# 9. NYY #53 Austin Romine (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #27 Shawn Kelley
t7 = game.new_inning()

# Pitching change (NYY): #27 Shawn Kelley replaces #18 Hiroki Kuroda
t7.pitching_substitution(27)

# Defensive switch (NYY): #53 Austin Romine moves to C
t7.defensive_switch(53, "2")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b s s s")
t7.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b c")
t7.hit(1)
t7.advance(3, "5 1B")

# 1. BOS #29 Daniel Nava (X - X - 25)
t7.new_ab()
t7.pitch_list("1 b 1 c c 1 b")
t7.out("L9")

# 2. BOS #5  Jonny Gomes (X - X - 25)
t7.new_ab()
t7.pitch_list("c 1")
t7.hit(1)
t7.advance(2, "15 WP")

# 3. BOS #15 Dustin Pedroia (25 - X - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("c d b")
t7.wp()
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 1. NYY #31 Ichiro Suzuki (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G1-3")

# 2. NYY #22 Vernon Wells (X - X - X)
b7.new_ab()
b7.pitch_list("b b b")
b7.out("G5-3")

# 3. NYY #12 Alfonso Soriano (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.advance(2, "24 1B")

# 4. NYY #24 Robinson Canó (X - X - 12)
b7.new_ab()
b7.hit(1)

# 5. NYY #13 Alex Rodriguez (X - 12 - 24)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #42 Mariano Rivera
t8 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #27 Shawn Kelley
t8.pitching_substitution(42)

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c s b b c")
t8.out("!K")

# 5. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("b c s f b f f b")
t8.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #37 Mike Carp
t8.offensive_substitution(5, 50, "PR")
t8.atbase("PR")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t8.new_ab()
t8.pitch_list("1 1 c c s")
t8.out("K")

# 7. BOS #7  Stephen Drew (X - X - 50)
t8.new_ab()
t8.pitch_list("1 1 c 1 b")
t8.out("(F)P5")


# Bot 8th
# Pitching: BOS #31 Jon Lester
b8 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b8.defensive_switch(29, "3")

# Defensive switch (BOS): #50 Quintin Berry moves to RF
b8.defensive_switch(50, "9")

# 6. NYY #39 Mark Reynolds (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c f")
b8.out("(F)P2")

# 7. NYY #14 Curtis Granderson (X - X - X)
b8.new_ab()
b8.pitch_list("c b c s")
b8.out("K2-3")

# 8. NYY #26 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b f s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #42 Mariano Rivera
t9 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.hit(4)

# Offensive change (BOS): Pinch-hitter #12 Mike Napoli replaces #25 Jackie Bradley Jr., batting 9th
t9.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b f s")
t9.out("K")

# 1. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c")
t9.out("G3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.out("L5")


# Bot 9th
# Pitching: BOS #67 Brandon Workman
b9 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #31 Jon Lester
b9.pitching_substitution(67)

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b9.defensive_switch(29, "9")

# Defensive switch (BOS): #50 Quintin Berry moves to CF
b9.defensive_switch(50, "8")

# Defensive switch (BOS): #12 Mike Napoli moves to 1B
b9.defensive_switch(12, "3")

# Offensive change (NYY): Pinch-hitter #11 Brett Gardner replaces #53 Austin Romine, batting 9th
b9.offensive_substitution(9, 11, "PH")

# 9. NYY #11 Brett Gardner (X - X - X)
b9.new_ab()
b9.pitch_list("b b c b s t")
b9.out("KT")

# 1. NYY #31 Ichiro Suzuki (X - X - X)
b9.new_ab()
b9.pitch_list("c c")
b9.hit(1)
b9.advance(2, "22 SB")
b9.advance(3, "22 F9")
b9.advance(4, "12 WP")

# 2. NYY #22 Vernon Wells (X - X - 31)
b9.new_ab(is_risp=True)
b9.pitch_list("c 1 b f 1 b b f f")
b9.out("F9")

# 3. NYY #12 Alfonso Soriano (31 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b")

# Winning team: NYY
# WP: NYY #42 Mariano Rivera
game.winning_pitcher(42)

# Loser team: BOS
# LP: BOS #67 Brandon Workman
game.losing_pitcher(67, is_away_team=True)

# print(game)
game.generate_scorecard()
