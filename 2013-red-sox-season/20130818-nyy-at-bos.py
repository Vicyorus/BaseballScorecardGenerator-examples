import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-08-18
# https://www.baseball-reference.com/boxes/BOS/BOS201308180.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/08/18/348590/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-18 20:07-00:19 +1",
        "at": "Fenway Park, Boston, MA",
        "att": "37,917",
        "temp": "76F, Partly Cloudy",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                31: "Ichiro Suzuki",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                13: "Alex Rodriguez",
                14: "Curtis Granderson",
                26: "Eduardo Núñez",
                55: "Lyle Overbay",
                19: "Chris Stewart",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                22: "Vernon Wells",
                39: "Mark Reynolds",
                53: "Austin Romine",
                17: "Jayson Nix",
                # Bullpen
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                48: "Boone Logan",
                60: "David Huff",
                43: "Adam Warren",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [52, 48, 60, 46],
            "lineup": [
                [11, "8"],
                [31, "9"],
                [24, "4"],
                [12, "7"],
                [13, "5"],
                [14, "0"],
                [26, "6"],
                [55, "3"],
                [19, "2"],
            ],
            "bench": [
                [22, "CF"],
                [39, "3B"],
                [53, "C"],
                [17, "3B"],
            ],
            "bullpen": [18, 65, 27, 47, 48, 60, 43, 42, 46, 62, 30],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                29: "Daniel Nava",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [39, "2"],
                [29, "3"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [12, "1B"],
                [20, "C"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 19, 62, 22],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "Fieldin Culbreth",
            "2B": "Bill Welke",
            "3B": "Adrian Johnson",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("l c f s")
t1.out("K")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t1.new_ab()
t1.pitch_list("b f b f f f s")
t1.out("K")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.hit(2)
t1.advance(3, "12 WP")

# 4. NYY #12 Alfonso Soriano (X - 24 - X)
t1.new_ab()
t1.pitch_list("s b b c")
t1.wp()
t1.out("G6-3")


# Bot 1st
# Pitching: NYY #52 CC Sabathia
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")
b1.advance(2, "18 1B")
b1.advance(3, "34 BB")
b1.advance(4, "5 SF9")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(1)
b1.advance(2, "34 BB")
b1.advance(3, "5 SF9")
b1.advance(4, "39 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b1.new_ab()
b1.pitch_list("c")
b1.out("F7")

# 4. BOS #34 David Ortiz (X - 2 - 18)
b1.new_ab()
b1.pitch_list("b c b b f f b")
b1.reach("BB")
b1.advance(2, "39 1B")

# 5. BOS #5  Jonny Gomes (2 - 18 - 34)
b1.new_ab()
b1.pitch_list("t c f")
b1.out("SF9", rbis=1)

# 6. BOS #39 Jarrod Saltalamacchia (18 - X - 34)
b1.new_ab()
b1.hit(1, rbis=1)

# 7. BOS #29 Daniel Nava (X - 34 - 39)
b1.new_ab()
b1.pitch_list("c f f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. NYY #13 Alex Rodriguez (X - X - X)
t2.new_ab()
t2.pitch_list("b b b")
t2.reach("HBP")
t2.advance(3, "14 2B")
t2.advance(4, "26 1B")

# 6. NYY #14 Curtis Granderson (X - X - 13)
t2.new_ab()
t2.pitch_list("c d t d")
t2.hit(2)
t2.advance(3, "26 1B")
t2.advance(4, "55 SF7")

# 7. NYY #26 Eduardo Núñez (13 - 14 - X)
t2.new_ab()
t2.hit(1, rbis=1)
t2.advance(2, "11 SB")

# 8. NYY #55 Lyle Overbay (14 - X - 26)
t2.new_ab()
t2.pitch_list("1")
t2.out("SF7", rbis=1)

# 9. NYY #19 Chris Stewart (X - X - 26)
t2.new_ab()
t2.out("(F)P3")

# 1. NYY #11 Brett Gardner (X - X - 26)
t2.new_ab()
t2.pitch_list("1 1 b b b")
t2.out("P3")


# Bot 2nd
# Pitching: NYY #52 CC Sabathia
b2 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G3")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("c f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f f f f f")
t3.hit(1)
t3.advance(2, "24 1B")
t3.advance(3, "12 L9")
t3.advance(4, "13 G6-3")

# 3. NYY #24 Robinson Canó (X - X - 31)
t3.new_ab()
t3.pitch_list("c b f b")
t3.hit(1)
t3.advance(2, "13 G6-3")

# 4. NYY #12 Alfonso Soriano (X - 31 - 24)
t3.new_ab()
t3.pitch_list("c f b d")
t3.out("L9")

# 5. NYY #13 Alex Rodriguez (31 - X - 24)
t3.new_ab()
t3.pitch_list("c b d b s")
t3.out("G6-3", rbis=1)

# 6. NYY #14 Curtis Granderson (X - 24 - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G3")


# Bot 3rd
# Pitching: NYY #52 CC Sabathia
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(2)
b3.advance(3, "34 WP")
b3.advance(4, "34 G3")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("F8")

# 4. BOS #34 David Ortiz (X - 18 - X)
b3.new_ab()
b3.pitch_list("b c b b")
b3.wp()
b3.out("G3", rbis=1)

# 5. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 7. NYY #26 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b c")
t4.hit(1)
t4.advance(2, "55 SB")

# 8. NYY #55 Lyle Overbay (X - X - 26)
t4.new_ab()
t4.pitch_list("s b c b s")
t4.out("K")

# 9. NYY #19 Chris Stewart (X - 26 - X)
t4.new_ab()
t4.out("F7")

# 1. NYY #11 Brett Gardner (X - 26 - X)
t4.new_ab()
t4.pitch_list("b c b c f f")
t4.out("P6")


# Bot 4th
# Pitching: NYY #52 CC Sabathia
b4 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(2)
b4.advance(3, "29 SAC2-4")
b4.advance(4, "7 SF7")

# 7. BOS #29 Daniel Nava (X - 39 - X)
b4.new_ab()
b4.out("SAC2-4")

# 8. BOS #7  Stephen Drew (39 - X - X)
b4.new_ab()
b4.pitch_list("s s")
b4.out("SF7", rbis=1)

# 9. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L4")

# 3. NYY #24 Robinson Canó (X - X - X)
t5.new_ab()
t5.out("F9")

# 4. NYY #12 Alfonso Soriano (X - X - X)
t5.new_ab()
t5.pitch_list("b c s")
t5.out("F9")


# Bot 5th
# Pitching: NYY #52 CC Sabathia
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b f b")
b5.hit(1)
b5.advance(3, "34 2B")
b5.advance(4, "29 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("s b d")
b5.hit(2)
b5.advance(3, "29 BB")

# 5. BOS #5  Jonny Gomes (15 - 34 - X)
b5.new_ab()
b5.out("P6")

# 6. BOS #39 Jarrod Saltalamacchia (15 - 34 - X)
b5.new_ab()
b5.pitch_list("b b b i")
b5.reach("IBB")
b5.advance(2, "29 BB")

# 7. BOS #29 Daniel Nava (15 - 34 - 39)
b5.new_ab()
b5.pitch_list("b f b b b")
b5.reach("BB", rbis=1)

# 8. BOS #7  Stephen Drew (34 - 39 - 29)
b5.new_ab()
b5.pitch_list("c c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 5. NYY #13 Alex Rodriguez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(4)

# 6. NYY #14 Curtis Granderson (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("G3-1")

# 7. NYY #26 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c c")
t6.hit(1)
t6.advance(2, "55 1B")
t6.advance(3, "19 BB")
# Offensive change (NYY): Pinch-runner #17 Jayson Nix replaces #26 Eduardo Núñez
t6.offensive_substitution(7, 17, "PR")
t6.atbase("PR")
t6.advance(4, "11 3B")

# 8. NYY #55 Lyle Overbay (X - X - 26)
t6.new_ab()
t6.pitch_list("f d b")
t6.hit(1)
t6.advance(2, "19 BB")
t6.advance(4, "11 3B")

# 9. NYY #19 Chris Stewart (X - 26 - 55)
t6.new_ab()
t6.pitch_list("b d b b")
t6.reach("BB")
t6.advance(4, "11 3B")

# Pitching change (BOS): #66 Drake Britton replaces #46 Ryan Dempster
t6.pitching_substitution(66)

# 1. NYY #11 Brett Gardner (26 - 55 - 19)
t6.new_ab()
t6.pitch_list("c")
t6.hit(3, rbis=3)
t6.thrown_out(4, "31 FC6-2", 2, 66)

# 2. NYY #31 Ichiro Suzuki (11 - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.reach("FC6-2")
t6.advance(2, "24 1B")

# 3. NYY #24 Robinson Canó (X - X - 31)
t6.new_ab()
t6.pitch_list("b 1 1 d c b c")
t6.hit(1)
t6.thrown_out(2, "12 FC6-4", 3, 67)

# Pitching change (BOS): #67 Brandon Workman replaces #66 Drake Britton
t6.pitching_substitution(67)

# 4. NYY #12 Alfonso Soriano (X - 31 - 24)
t6.new_ab()
t6.reach("FC6-4")


# Bot 6th
# Pitching: NYY #52 CC Sabathia
b6 = game.new_inning()

# Defensive switch (NYY): #17 Jayson Nix moves to SS
b6.defensive_switch(17, "6")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b6.new_ab()
b6.pitch_list("b b c f f f f c")
b6.out("!K")

# Pitching change (NYY): #27 Shawn Kelley replaces #52 CC Sabathia
b6.pitching_substitution(27)

# 2. BOS #18 Shane Victorino (X - X - 16)
b6.new_ab()
b6.pitch_list("c s b s")
b6.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 16)
b6.new_ab()
b6.pitch_list("c f 1")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #67 Brandon Workman
t7 = game.new_inning()

# 5. NYY #13 Alex Rodriguez (X - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.hit(1)
t7.thrown_out(2, "14 FC5-6", 1, 67)

# 6. NYY #14 Curtis Granderson (X - X - 13)
t7.new_ab()
t7.pitch_list("s d t")
t7.reach("FC5-6")
t7.advance(2, "17 SB")
t7.advance(4, "39 1B")

# 7. NYY #17 Jayson Nix (X - X - 14)
t7.new_ab()
t7.pitch_list("c s d b t")
t7.out("KT")

# Pitching change (BOS): #56 Franklin Morales replaces #67 Brandon Workman
t7.pitching_substitution(56)

# Offensive change (NYY): Pinch-hitter #39 Mark Reynolds replaces #55 Lyle Overbay, batting 8th
t7.offensive_substitution(8, 39, "PH")

# 8. NYY #39 Mark Reynolds (X - 14 - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1, rbis=1)

# 9. NYY #19 Chris Stewart (X - X - 39)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")


# Bot 7th
# Pitching: NYY #48 Boone Logan
b7 = game.new_inning()

# Pitching change (NYY): #48 Boone Logan replaces #27 Shawn Kelley
b7.pitching_substitution(48)

# Defensive switch (NYY): #39 Mark Reynolds moves to 1B
b7.defensive_switch(39, "3")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b f f s")
b7.out("K")

# 5. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.thrown_out(2, "39 DP6-4-3", 2, 48)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 5)
b7.new_ab()
b7.out("DP6-4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Franklin Morales
t8 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t8.new_ab()
t8.pitch_list("t b b s f")
t8.reach("HBP")
t8.advance(2, "31 1B")
t8.advance(3, "13 1B")

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t8.new_ab()
t8.hit(1)
t8.advance(2, "13 1B")

# 3. NYY #24 Robinson Canó (X - 11 - 31)
t8.new_ab()
t8.pitch_list("b c d b f s")
t8.out("K")

# Pitching change (BOS): #36 Junichi Tazawa replaces #56 Franklin Morales
t8.pitching_substitution(36)

# 4. NYY #12 Alfonso Soriano (X - 11 - 31)
t8.new_ab()
t8.pitch_list("c d b f s")
t8.out("K")

# 5. NYY #13 Alex Rodriguez (X - 11 - 31)
t8.new_ab()
t8.hit(1)

# 6. NYY #14 Curtis Granderson (11 - 31 - 13)
t8.new_ab()
t8.pitch_list("b s t f d b")
t8.out("F7")


# Bot 8th
# Pitching: NYY #30 David Robertson
b8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #48 Boone Logan
b8.pitching_substitution(30)

# 7. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c b f s")
b8.out("K2-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f s")
b8.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("f c b")
b8.hit(2)
b8.advance(3, "2 WP")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
b8.new_ab()
b8.pitch_list("f b f s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #62 Rubby De La Rosa
t9 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #36 Junichi Tazawa
t9.pitching_substitution(62)

# 7. NYY #17 Jayson Nix (X - X - X)
t9.new_ab()
t9.pitch_list("f b b f f")
t9.reach("HBP")
t9.advance(2, "39 WP")
t9.advance(3, "19 SB")
t9.advance(4, "19 1B")

# 8. NYY #39 Mark Reynolds (X - X - 17)
t9.new_ab()
t9.pitch_list("b t f f")
t9.wp()
t9.out("G5-3")

# 9. NYY #19 Chris Stewart (X - 17 - X)
t9.new_ab()
t9.pitch_list("b b c b c")
t9.hit(1, rbis=1)
t9.advance(2, "11 1B")
t9.advance(3, "31 F8")

# 1. NYY #11 Brett Gardner (X - X - 19)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "24 HBP")

# 2. NYY #31 Ichiro Suzuki (X - 19 - 11)
t9.new_ab()
t9.out("F8")

# 3. NYY #24 Robinson Canó (19 - X - 11)
t9.new_ab()
t9.reach("HBP")

# 4. NYY #12 Alfonso Soriano (19 - 11 - 24)
t9.new_ab()
t9.pitch_list("f b s f")
t9.out("F8")


# Bot 9th
# Pitching: NYY #42 Mariano Rivera
b9 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #30 David Robertson
b9.pitching_substitution(42)

# 2. BOS #18 Shane Victorino (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.hit(1)
b9.advance(2, "5 BB")

# 5. BOS #5  Jonny Gomes (X - X - 34)
b9.new_ab()
b9.pitch_list("c b f b b f b")
b9.reach("BB")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - 5)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("L7")

# Winning team: NYY
# WP: NYY #52 CC Sabathia
game.winning_pitcher(52, is_away_team=True)
# SV: NYY #42 Mariano Rivera
game.save_pitcher(42, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
