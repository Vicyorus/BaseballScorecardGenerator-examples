import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-07-19
# https://www.baseball-reference.com/boxes/BOS/BOS201307190.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/07/19/348178/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-19 19:15-22:10",
        "at": "Fenway Park, Boston, MA",
        "att": "38,130",
        "temp": "92F, Partly Cloudy",
        "wind": "22mph, Out To RF",
        "away": {
            "team": "New York Yankees",
            "starter": 46,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                31: "Ichiro Suzuki",
                24: "Robinson Canó",
                12: "Vernon Wells",
                45: "Zoilo Almonte",
                55: "Lyle Overbay",
                39: "Brent Lillibridge",
                26: "Eduardo Núñez",
                19: "Chris Stewart",
                # Starting pitcher
                46: "Andy Pettitte",
                # Bench
                61: "Luis Alfonso Cruz",
                53: "Austin Romine",
                33: "Travis Hafner",
                40: "Alberto Gonzalez",
                # Bullpen
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                43: "Adam Warren",
                42: "Mariano Rivera",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [46, 52, 48],
            "lineup": [
                [11, "8"],
                [31, "9"],
                [24, "4"],
                [12, "0"],
                [45, "7"],
                [55, "3"],
                [39, "5"],
                [26, "6"],
                [19, "2"],
            ],
            "bench": [
                [61, "3B"],
                [53, "C"],
                [33, "DH"],
                [40, "2B"],
            ],
            "bullpen": [18, 65, 27, 47, 52, 38, 48, 43, 42, 62, 30],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                23: "Brandon Snyder",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
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
                46: "Ryan Dempster",
            },
            "lefties": [22, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [23, "5"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [29, "LF"],
                [20, "C"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 31, 36, 19, 38, 54, 46],
        },
        "umpires": {
            "HP": "Mike Everitt",
            "1B": "Tim Welke",
            "2B": "Paul Emmel",
            "3B": "Dan Bellino",
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

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("G5-3")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G6-3")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("f b f s")
t1.out("K")


# Bot 1st
# Pitching: NYY #46 Andy Pettitte
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(4)

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b c f f f b f b f")
b1.out("L5")

# 4. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("f f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 4. NYY #12 Vernon Wells (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b s b")
t2.reach("BB")
t2.thrown_out(2, "45 DP6-4-3", 1, 22)

# 5. NYY #45 Zoilo Almonte (X - X - 12)
t2.new_ab()
t2.pitch_list("1 b")
t2.out("DP6-4-3")

# 6. NYY #55 Lyle Overbay (X - X - X)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: NYY #46 Andy Pettitte
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("s b c b b b")
b2.reach("BB")
b2.advance(4, "5 HR")

# 6. BOS #5  Jonny Gomes (X - X - 12)
b2.new_ab()
b2.pitch_list("c c f f b 1 d")
b2.hit(4, rbis=2)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f b f f s")
b2.out("K")

# 8. BOS #23 Brandon Snyder (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("L6")

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 7. NYY #39 Brent Lillibridge (X - X - X)
t3.new_ab()
t3.pitch_list("b f c f c")
t3.out("!K")

# 8. NYY #26 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("P3")

# 9. NYY #19 Chris Stewart (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("F9")


# Bot 3rd
# Pitching: NYY #46 Andy Pettitte
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "18 DP4-6-3", 1, 46)

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab()
b3.pitch_list("b c c")
b3.out("DP4-6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("b c f")
b3.out("(F)P3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# Defensive change (BOS): #29 Daniel Nava replaces #18 Shane Victorino (RF), playing RF, batting 2nd
t4.defensive_substitution(2, 29, "9")

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("l b b c b f f f b")
t4.reach("BB")
t4.advance(2, "24 SB")
t4.error(2)
t4.advance(3, "24 SB")
t4.advance("U", "24 E2")

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t4.new_ab()
t4.pitch_list("f c 1 b f d")
t4.out("P5")

# 3. NYY #24 Robinson Canó (X - X - 11)
t4.new_ab()
t4.pitch_list("f b 1 b f b f f b")
t4.reach("BB")
t4.thrown_out(2, "45 FC5-4", 3, 22)

# 4. NYY #12 Vernon Wells (X - X - 24)
t4.new_ab()
t4.pitch_list("s b b f s")
t4.out("K")

# 5. NYY #45 Zoilo Almonte (X - X - 24)
t4.new_ab()
t4.pitch_list("c c f")
t4.reach("FC5-4")


# Bot 4th
# Pitching: NYY #46 Andy Pettitte
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c f b b b s")
b4.out("K")

# 6. BOS #5  Jonny Gomes (X - 34 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c f d f b b c")
b4.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 34 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.out("P1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 6. NYY #55 Lyle Overbay (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(2)
t5.advance(4, "19 2B")

# 7. NYY #39 Brent Lillibridge (X - 55 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b b s")
t5.out("K")

# 8. NYY #26 Eduardo Núñez (X - 55 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b b f")
t5.out("G5-3")

# 9. NYY #19 Chris Stewart (X - 55 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s")
t5.hit(2, rbis=1)

# 1. NYY #11 Brett Gardner (X - 19 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f b c b c")
t5.out("!K")


# Bot 5th
# Pitching: NYY #46 Andy Pettitte
b5 = game.new_inning()

# Defensive change (NYY): #61 Luis Alfonso Cruz replaces #45 Zoilo Almonte (LF), playing 3B, batting 5th
b5.defensive_substitution(5, 61, "5")

# Defensive switch (NYY): #31 Ichiro Suzuki moves to CF
b5.defensive_switch(31, "8")

# Defensive change (NYY): #40 Alberto Gonzalez replaces #11 Brett Gardner (CF), playing LF, batting 1st
b5.defensive_substitution(1, 40, "7")

# Defensive switch (NYY): #39 Brent Lillibridge moves to RF
b5.defensive_switch(39, "9")

# 8. BOS #23 Brandon Snyder (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("L5")

# 9. BOS #10 Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 3. NYY #24 Robinson Canó (X - X - X)
t6.new_ab()
t6.out("L9")

# 4. NYY #12 Vernon Wells (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# 5. NYY #61 Luis Alfonso Cruz (X - X - 12)
t6.new_ab()
t6.pitch_list("b b f")
t6.out("P2")


# Bot 6th
# Pitching: NYY #46 Andy Pettitte
b6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.hit(1)
b6.thrown_out(2, "34 FC4-6", 2, 46)

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab()
b6.reach("FC4-6")
b6.thrown_out(2, "12 FC6-4", 3, 46)

# 5. BOS #12 Mike Napoli (X - X - 34)
b6.new_ab()
b6.pitch_list("s")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 6. NYY #55 Lyle Overbay (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G4-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #22 Felix Doubront
t7.pitching_substitution(36)

# 7. NYY #39 Brent Lillibridge (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")

# 8. NYY #26 Eduardo Núñez (X - X - 39)
t7.new_ab()
t7.pitch_list("b s")
t7.out("P3")

# 9. NYY #19 Chris Stewart (X - X - 39)
t7.new_ab()
t7.pitch_list("c c b b b")
t7.out("F9")


# Bot 7th
# Pitching: NYY #46 Andy Pettitte
b7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.hit(2)
b7.advance(3, "10 WP")
b7.advance(4, "10 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 5 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d")
b7.out("G5-3")

# Pitching change (NYY): #27 Shawn Kelley replaces #46 Andy Pettitte
b7.pitching_substitution(27)

# Offensive change (BOS): Pinch-hitter #26 Brock Holt replaces #23 Brandon Snyder, batting 8th
b7.offensive_substitution(8, 26, "PH")

# 8. BOS #26 Brock Holt (X - 5 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b f")
b7.out("G1-3")

# 9. BOS #10 Jose Iglesias (X - 5 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d c f d f f b")
b7.wp()
b7.hit(1, rbis=1)
b7.advance(2, "2 BB")
b7.thrown_out(3, "29 FC5", 3, 48)

# Pitching change (NYY): #48 Boone Logan replaces #27 Shawn Kelley
b7.pitching_substitution(48)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b7.new_ab()
b7.pitch_list("1 b b f 1 1 f d f b")
b7.reach("BB")
b7.advance(2, "29 FC5")

# 2. BOS #29 Daniel Nava (X - 10 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b f")
b7.reach("FC5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
t8.pitching_substitution(32)

# Defensive switch (BOS): #26 Brock Holt moves to 3B
t8.defensive_switch(26, "5")

# 1. NYY #40 Alberto Gonzalez (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("(F)P4")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(3, "24 2B")

# 3. NYY #24 Robinson Canó (X - X - 31)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(2)

# 4. NYY #12 Vernon Wells (31 - 24 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("f")
t8.out("P6")

# 5. NYY #61 Luis Alfonso Cruz (31 - 24 - X)
t8.new_ab(is_risp=True)
t8.out("G6-3")


# Bot 8th
# Pitching: NYY #38 Preston Claiborne
b8 = game.new_inning()

# Pitching change (NYY): #38 Preston Claiborne replaces #48 Boone Logan
b8.pitching_substitution(38)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)
b8.advance(3, "12 F9")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c s b")
b8.out("F9")

# 6. BOS #5  Jonny Gomes (34 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t9.pitching_substitution(19)

# 6. NYY #55 Lyle Overbay (X - X - X)
t9.new_ab()
t9.pitch_list("b s f s")
t9.out("K")

# 7. NYY #39 Brent Lillibridge (X - X - X)
t9.new_ab()
t9.out("G4-3")

# 8. NYY #26 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: NYY
# LP: NYY #46 Andy Pettitte
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
