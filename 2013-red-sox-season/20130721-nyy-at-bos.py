import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-07-21
# https://www.baseball-reference.com/boxes/BOS/BOS201307210.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/07/21/348208/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-21 20:07-00:53 +1",
        "at": "Fenway Park, Boston, MA",
        "att": "38,138",
        "temp": "73F, Cloudy",
        "wind": "12mph, R To L",
        "away": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                31: "Ichiro Suzuki",
                24: "Robinson Canó",
                55: "Lyle Overbay",
                12: "Vernon Wells",
                33: "Travis Hafner",
                26: "Eduardo Núñez",
                19: "Chris Stewart",
                61: "Luis Alfonso Cruz",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                39: "Brent Lillibridge",
                53: "Austin Romine",
                60: "Melky Mesa",
                40: "Thomas Neal",
                # Bullpen
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                38: "Preston Claiborne",
                48: "Boone Logan",
                43: "Adam Warren",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [52, 48, 46],
            "lineup": [
                [11, "8"],
                [31, "9"],
                [24, "4"],
                [55, "3"],
                [12, "7"],
                [33, "0"],
                [26, "6"],
                [19, "2"],
                [61, "5"],
            ],
            "bench": [
                [39, "2B"],
                [53, "C"],
                [60, "LF"],
                [40, "LF"],
            ],
            "bullpen": [18, 65, 27, 47, 38, 48, 43, 42, 46, 62, 30],
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
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 31, 36, 19, 38, 54, 22],
        },
        "umpires": {
            "HP": "Paul Emmel",
            "1B": "Dan Bellino",
            "2B": "Mike Everitt",
            "3B": "Tim Welke",
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
t1.pitch_list("b")
t1.hit(1)
t1.error(1)
t1.advance(2, "31 FC1")
t1.advance(3, "31 E1")
t1.error(2)
t1.advance("U", "24 E2")

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t1.new_ab()
t1.pitch_list("b f")
t1.reach("FC1")
t1.advance(3, "24 SB")
t1.advance("U", "12 1B")

# 3. NYY #24 Robinson Canó (11 - X - 31)
t1.new_ab()
t1.pitch_list("b f b f b b")
t1.reach("BB")
t1.advance(2, "12 1B")

# 4. NYY #55 Lyle Overbay (31 - X - 24)
t1.new_ab()
t1.pitch_list("b s s b c")
t1.out("!K")

# 5. NYY #12 Vernon Wells (31 - X - 24)
t1.new_ab()
t1.pitch_list("1")
t1.hit(1, rbis=1)

# 6. NYY #33 Travis Hafner (X - 24 - 12)
t1.new_ab()
t1.pitch_list("b f s f d d s")
t1.out("K")

# 7. NYY #26 Eduardo Núñez (X - 24 - 12)
t1.new_ab()
t1.pitch_list("b c d")
t1.out("G4-3")


# Bot 1st
# Pitching: NYY #52 CC Sabathia
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.reach("HBP")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("c f f s")
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("c")
b1.out("F9")

# 4. BOS #34 David Ortiz (X - X - 2)
b1.new_ab()
b1.pitch_list("c f f 1 f f 1")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 8. NYY #19 Chris Stewart (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b b")
t2.reach("BB")
t2.advance(2, "61 G3")
t2.advance(3, "11 G4-3")
t2.advance(4, "24 1B")

# 9. NYY #61 Luis Alfonso Cruz (X - X - 19)
t2.new_ab()
t2.pitch_list("c f f")
t2.out("G3")

# 1. NYY #11 Brett Gardner (X - 19 - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")

# 2. NYY #31 Ichiro Suzuki (19 - X - X)
t2.new_ab()
t2.pitch_list("c b b f d")
t2.reach("HBP")
t2.advance(3, "24 1B")

# 3. NYY #24 Robinson Canó (19 - X - 31)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1, rbis=1)

# 4. NYY #55 Lyle Overbay (31 - X - 24)
t2.new_ab()
t2.pitch_list("f")
t2.out("G1-3")


# Bot 2nd
# Pitching: NYY #52 CC Sabathia
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b b s s")
b2.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f f")
b2.out("P4")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "7 BB")

# 8. BOS #7  Stephen Drew (X - X - 39)
b2.new_ab()
b2.pitch_list("c b b s b b")
b2.reach("BB")

# 9. BOS #10 Jose Iglesias (X - 39 - 7)
b2.new_ab()
b2.pitch_list("c f d f f")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 5. NYY #12 Vernon Wells (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f")
t3.out("G1-3")

# 6. NYY #33 Travis Hafner (X - X - X)
t3.new_ab()
t3.out("G6-3")

# 7. NYY #26 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F9")


# Bot 3rd
# Pitching: NYY #52 CC Sabathia
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(2)
b3.advance(3, "18 SAC3")
b3.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b3.new_ab()
b3.out("SAC3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b3.new_ab()
b3.hit(1, rbis=1)
b3.advance(3, "34 1B")
b3.advance(4, "12 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
b3.new_ab()
b3.pitch_list("d c f")
b3.hit(1)
b3.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (15 - X - 34)
b3.new_ab()
b3.pitch_list("b f f")
b3.hit(4, rbis=3)

# 6. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("f s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 8. NYY #19 Chris Stewart (X - X - X)
t4.new_ab()
t4.out("L9")

# 9. NYY #61 Luis Alfonso Cruz (X - X - X)
t4.new_ab()
t4.pitch_list("c s t")
t4.out("KT")

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(2, "31 SB")

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t4.new_ab()
t4.pitch_list("f b 1 1 c")
t4.out("F8")


# Bot 4th
# Pitching: NYY #52 CC Sabathia
b4 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.reach("HBP")
b4.advance(2, "10 1B")
b4.advance(3, "2 1B")
b4.advance(4, "18 1B")

# 9. BOS #10 Jose Iglesias (X - X - 7)
b4.new_ab()
b4.hit(1)
b4.advance(2, "2 1B")
b4.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 10)
b4.new_ab()
b4.pitch_list("c t f")
b4.hit(1)
b4.advance(2, "18 1B")
b4.advance(3, "15 F8")

# 2. BOS #18 Shane Victorino (7 - 10 - 2)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1, rbis=2)
b4.advance(2, "12 SB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 4. BOS #34 David Ortiz (2 - X - 18)
b4.new_ab()
b4.pitch_list("b")
b4.out("(F)P5")

# 5. BOS #12 Mike Napoli (2 - X - 18)
b4.new_ab()
b4.pitch_list("b f b s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("L6")

# 4. NYY #55 Lyle Overbay (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("F8")

# 5. NYY #12 Vernon Wells (X - X - X)
t5.new_ab()
t5.pitch_list("b b f s b b")
t5.reach("BB")

# 6. NYY #33 Travis Hafner (X - X - 12)
t5.new_ab()
t5.pitch_list("s f b d s")
t5.out("K")


# Bot 5th
# Pitching: NYY #52 CC Sabathia
b5 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("b b s c b")
b5.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c t f")
b5.out("G6-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c f f s")
b5.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c c f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 7. NYY #26 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.advance(2, "19 SB")
t6.advance(4, "11 1B")

# 8. NYY #19 Chris Stewart (X - X - 26)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "11 1B")
t6.advance(3, "31 1B")
t6.advance(4, "24 1B")

# 9. NYY #61 Luis Alfonso Cruz (X - 26 - 19)
t6.new_ab()
t6.out("F7")

# 1. NYY #11 Brett Gardner (X - 26 - 19)
t6.new_ab()
t6.pitch_list("c b b s")
t6.hit(1, rbis=1)
t6.advance(2, "31 1B")
t6.advance(3, "24 1B")

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t6.pitching_substitution(32)

# 2. NYY #31 Ichiro Suzuki (X - 19 - 11)
t6.new_ab()
t6.pitch_list("c c f b")
t6.hit(1)
t6.advance(2, "24 1B")

# 3. NYY #24 Robinson Canó (19 - 11 - 31)
t6.new_ab()
t6.pitch_list("c b s f")
t6.hit(1, rbis=1)
t6.thrown_out(2, "55 DP4-6-3", 2, 32)

# 4. NYY #55 Lyle Overbay (11 - 31 - 24)
t6.new_ab()
t6.out("DP4-6-3")


# Bot 6th
# Pitching: NYY #52 CC Sabathia
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "18 SB")
b6.advance(3, "18 G3")

# Pitching change (NYY): #38 Preston Claiborne replaces #52 CC Sabathia
b6.pitching_substitution(38)

# 2. BOS #18 Shane Victorino (X - X - 2)
b6.new_ab()
b6.pitch_list("c b 1 1 b l b f")
b6.out("G3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b6.new_ab()
b6.pitch_list("b f f f d f s")
b6.out("K")

# 4. BOS #34 David Ortiz (2 - X - X)
b6.new_ab()
b6.pitch_list("i i i i")
b6.reach("IBB")
b6.advance(2, "12 SB")

# 5. BOS #12 Mike Napoli (2 - X - 34)
b6.new_ab()
b6.pitch_list("b c c b b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# 5. NYY #12 Vernon Wells (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b f b")
t7.reach("BB")
t7.advance(2, "26 1B")
t7.error(5)
t7.advance(3, "19 1B")
t7.advance(4, "19 E5")

# Offensive change (NYY): Pinch-hitter #39 Brent Lillibridge replaces #33 Travis Hafner, batting 6th
t7.offensive_substitution(6, 39, "PH")

# 6. NYY #39 Brent Lillibridge (X - X - 12)
t7.new_ab()
t7.pitch_list("c f")
t7.out("(F)P3")

# 7. NYY #26 Eduardo Núñez (X - X - 12)
t7.new_ab()
t7.pitch_list("b s")
t7.hit(1)
t7.advance(3, "19 E5")
t7.advance("U", "61 G6-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t7.pitching_substitution(36)

# 8. NYY #19 Chris Stewart (X - 12 - 26)
t7.new_ab()
t7.hit(1)
t7.advance(2, "E5")
t7.advance(3, "61 G6-3")

# 9. NYY #61 Luis Alfonso Cruz (26 - 19 - X)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G6-3", rbis=1)

# 1. NYY #11 Brett Gardner (19 - X - X)
t7.new_ab()
t7.pitch_list("b b c f f b f f f f f f f f b")
t7.reach("BB")

# 2. NYY #31 Ichiro Suzuki (19 - X - 11)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G1-3")


# Bot 7th
# Pitching: NYY #38 Preston Claiborne
b7 = game.new_inning()

# Defensive switch (NYY): #39 Brent Lillibridge moves to DH
b7.defensive_switch(39, "0")

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")

# Pitching change (NYY): #48 Boone Logan replaces #38 Preston Claiborne
b7.pitching_substitution(48)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
b7.new_ab()
b7.pitch_list("c 1 b 1 f f b s")
b7.out("K")

# 8. BOS #7  Stephen Drew (X - X - 5)
b7.new_ab()
b7.pitch_list("c 1 c s")
b7.out("K")

# 9. BOS #10 Jose Iglesias (X - X - 5)
b7.new_ab()
b7.pitch_list("c s 1 f b s")
b7.out("K2-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #38 Matt Thornton
t8 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #36 Junichi Tazawa
t8.pitching_substitution(38)

# 3. NYY #24 Robinson Canó (X - X - X)
t8.new_ab()
t8.pitch_list("f b f b s")
t8.out("K")

# 4. NYY #55 Lyle Overbay (X - X - X)
t8.new_ab()
t8.pitch_list("b f s f b b c")
t8.out("!K")

# 5. NYY #12 Vernon Wells (X - X - X)
t8.new_ab()
t8.pitch_list("f b b f b")
t8.out("G6-3")


# Bot 8th
# Pitching: NYY #30 David Robertson
b8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #48 Boone Logan
b8.pitching_substitution(30)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "15 SB")
b8.advance(3, "15 E5")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b8.new_ab()
b8.pitch_list("b c")
b8.error(5)
b8.reach("E5")
b8.advance(2, "34 BB")

# 4. BOS #34 David Ortiz (18 - X - 15)
b8.new_ab()
b8.pitch_list("b b b s f d")
b8.reach("BB")
b8.thrown_out(2, "12 DP6-4-3", 2, 30)

# 5. BOS #12 Mike Napoli (18 - 15 - 34)
b8.new_ab()
b8.pitch_list("b c c f")
b8.out("DP6-4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #38 Matt Thornton
t9.pitching_substitution(19)

# 6. NYY #39 Brent Lillibridge (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.hit(1)

# 7. NYY #26 Eduardo Núñez (X - X - 39)
t9.new_ab()
t9.pitch_list("1 l f s")
t9.out("K")

# 8. NYY #19 Chris Stewart (X - X - 39)
t9.new_ab()
t9.pitch_list("b")
t9.out("P5")

# 9. NYY #61 Luis Alfonso Cruz (X - X - 39)
t9.new_ab()
t9.pitch_list("b 1 b f f s")
t9.out("K")


# Bot 9th
# Pitching: NYY #27 Shawn Kelley
b9 = game.new_inning()

# Pitching change (NYY): #27 Shawn Kelley replaces #30 David Robertson
b9.pitching_substitution(27)

# 6. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b")
b9.out("(F)P2")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("s b f b b s")
b9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("b b f s c")
b9.out("!K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #66 Drake Britton
t10 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #19 Koji Uehara
t10.pitching_substitution(66)

# 1. NYY #11 Brett Gardner (X - X - X)
t10.new_ab()
t10.pitch_list("b b b c c b")
t10.reach("BB")
t10.advance(2, "24 1B")

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t10.new_ab()
t10.pitch_list("1 b 1")
t10.out("F9")

# 3. NYY #24 Robinson Canó (X - X - 11)
t10.new_ab()
t10.pitch_list("b b f c")
t10.hit(1)
t10.thrown_out(2, "55 DP4-6-3", 2, 66)

# 4. NYY #55 Lyle Overbay (X - 11 - 24)
t10.new_ab()
t10.pitch_list("b")
t10.out("DP4-6-3")


# Bot 10th
# Pitching: NYY #27 Shawn Kelley
b10 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b10.new_ab()
b10.pitch_list("f c b c")
b10.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b10.new_ab()
b10.pitch_list("c c b s")
b10.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b10.new_ab()
b10.pitch_list("s f b t")
b10.out("KT")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #54 Pedro Beato
t11 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #66 Drake Britton
t11.pitching_substitution(54)

# 5. NYY #12 Vernon Wells (X - X - X)
t11.new_ab()
t11.pitch_list("c f")
t11.out("F9")

# 6. NYY #39 Brent Lillibridge (X - X - X)
t11.new_ab()
t11.out("F9")

# 7. NYY #26 Eduardo Núñez (X - X - X)
t11.new_ab()
t11.pitch_list("b s f f")
t11.hit(1)
t11.thrown_out(2, "19 CS", 3, 54)

# 8. NYY #19 Chris Stewart (X - X - 26)
t11.new_ab()
t11.pitch_list("c b 1 b b")
t11.no_ab("CS")


# Bot 11th
# Pitching: NYY #43 Adam Warren
b11 = game.new_inning()

# Pitching change (NYY): #43 Adam Warren replaces #27 Shawn Kelley
b11.pitching_substitution(43)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b11.new_ab()
b11.pitch_list("c b")
b11.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b11.new_ab()
b11.pitch_list("c b")
b11.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b11.new_ab()
b11.pitch_list("b b s s b f")
b11.hit(4)

# Winning team: BOS
# WP: BOS #54 Pedro Beato
game.winning_pitcher(54)

# Loser team: NYY
# LP: NYY #43 Adam Warren
game.losing_pitcher(43, is_away_team=True)

# print(game)
game.generate_scorecard()
