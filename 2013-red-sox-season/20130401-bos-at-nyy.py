import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-04-01
# https://www.baseball-reference.com/boxes/NYA/NYA201304010.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/04/01/346755/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-01 13:10-16:47",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "49,514",
        "temp": "62F, Partly Cloudy",
        "wind": "17mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                44: "Jackie Bradley Jr.",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [16, "5"],
                [39, "2"],
                [5, "0"],
                [44, "7"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 30, 91, 52, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                26: "Eduardo Núñez",
                24: "Robinson Canó",
                36: "Kevin Youkilis",
                12: "Vernon Wells",
                45: "Ben Francisco",
                31: "Ichiro Suzuki",
                17: "Jayson Nix",
                29: "Francisco Cervelli",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                19: "Chris Stewart",
                22: "Brennan Boesch",
                33: "Travis Hafner",
                55: "Lyle Overbay",
                # Bullpen
                18: "Hiroki Kuroda",
                27: "Shawn Kelley",
                47: "Iván Nova",
                48: "Boone Logan",
                41: "David Phelps",
                43: "Adam Warren",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                62: "Joba Chamberlain",
                38: "Cody Eppley",
                30: "David Robertson",
            },
            "lefties": [52, 48, 46],
            "lineup": [
                [11, "8"],
                [26, "6"],
                [24, "4"],
                [36, "3"],
                [12, "7"],
                [45, "0"],
                [31, "9"],
                [17, "5"],
                [29, "2"],
            ],
            "bench": [
                [19, "C"],
                [22, "RF"],
                [33, "DH"],
                [55, "1B"],
            ],
            "bullpen": [18, 27, 47, 48, 41, 43, 42, 46, 62, 38, 30],
        },
        "umpires": {
            "HP": "Ted Barrett",
            "1B": "Alfonso Márquez",
            "2B": "Mike DiMuro",
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
# Pitching: NYY #52 CC Sabathia
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c f b f s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
t1.new_ab()
t1.pitch_list("b s s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b l f s")
b1.out("K")

# 2. NYY #26 Eduardo Núñez (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G6-3")

# 3. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b b f s")
b1.wp()
b1.reach("K")

# 4. NYY #36 Kevin Youkilis (X - X - 24)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #52 CC Sabathia
t2 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b b")
t2.out("G5-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b b")
t2.reach("BB")
t2.advance(2, "5 1B")
t2.advance(3, "44 BB")
t2.advance(4, "10 1B")

# 7. BOS #5  Jonny Gomes (X - X - 39)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "44 BB")
t2.advance(3, "10 1B")
t2.thrown_out(4, "2 FC3-2", 2, 52)

# 8. BOS #44 Jackie Bradley Jr. (X - 39 - 5)
t2.new_ab(is_risp=True)
t2.pitch_list("c s d b f b b")
t2.reach("BB")
t2.advance(2, "10 1B")
t2.advance(3, "2 FC3-2")
t2.advance(4, "18 1B")

# 9. BOS #10 Jose Iglesias (39 - 5 - 44)
t2.new_ab(is_risp=True)
t2.hit(1, rbis=1)
t2.advance(2, "2 FC3-2")
t2.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (5 - 44 - 10)
t2.new_ab(is_risp=True)
t2.reach("FC3-2")
t2.advance(2, "18 1B")
t2.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (44 - 10 - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("c b")
t2.hit(1, rbis=2)
t2.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("b c")
t2.hit(1, rbis=1)

# 4. BOS #12 Mike Napoli (X - 18 - 15)
t2.new_ab(is_risp=True)
t2.pitch_list("b s s b f")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. NYY #12 Vernon Wells (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")

# 6. NYY #45 Ben Francisco (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b b b")
b2.reach("BB")
b2.thrown_out(2, "31 FC6-4", 2, 31)

# 7. NYY #31 Ichiro Suzuki (X - X - 45)
b2.new_ab()
b2.pitch_list("1 c c 1")
b2.reach("FC6-4")

# 8. NYY #17 Jayson Nix (X - X - 31)
b2.new_ab()
b2.pitch_list("f b b f b c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #52 CC Sabathia
t3 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f s")
t3.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("c c c")
t3.out("!K")

# 7. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("f s f")
t3.out("P6")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. NYY #29 Francisco Cervelli (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.hit(1)
b3.advance(2, "24 WP")

# 2. NYY #26 Eduardo Núñez (X - X - 11)
b3.new_ab()
b3.pitch_list("c f f f d f c")
b3.out("!K")

# 3. NYY #24 Robinson Canó (X - X - 11)
b3.new_ab(is_risp=True)
b3.pitch_list("b d")
b3.wp()
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #52 CC Sabathia
t4 = game.new_inning()

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c s s")
t4.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "2 1B")
t4.advance(3, "18 G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t4.new_ab()
t4.pitch_list("b 1 c b c")
t4.hit(1)
t4.advance(2, "18 G1-3")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b s s")
t4.out("G1-3")

# 3. BOS #15 Dustin Pedroia (10 - 2 - X)
t4.new_ab(is_risp=True)
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 4. NYY #36 Kevin Youkilis (X - X - X)
b4.new_ab()
b4.pitch_list("c s b f b b f")
b4.hit(2)
b4.advance(3, "31 1B")
b4.advance(4, "29 1B")

# 5. NYY #12 Vernon Wells (X - 36 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f f f d f b b b")
b4.reach("BB")
b4.advance(2, "31 1B")
b4.advance(4, "29 1B")

# 6. NYY #45 Ben Francisco (X - 36 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.out("(F)P2")

# 7. NYY #31 Ichiro Suzuki (X - 36 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.hit(1)
b4.advance(3, "29 1B")

# 8. NYY #17 Jayson Nix (36 - 12 - 31)
b4.new_ab(is_risp=True)
b4.pitch_list("b f b f d f c")
b4.out("!K")

# 9. NYY #29 Francisco Cervelli (36 - 12 - 31)
b4.new_ab(is_risp=True)
b4.pitch_list("f b s")
b4.hit(1, rbis=2)

# 1. NYY #11 Brett Gardner (31 - X - 29)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #52 CC Sabathia
t5 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.out("G4-3")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.out("(F)P3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b s f b b")
t5.hit(2)
t5.advance(3, "44 BB")

# 7. BOS #5  Jonny Gomes (X - 39 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("i i i i")
t5.reach("IBB")
t5.advance(2, "44 BB")

# 8. BOS #44 Jackie Bradley Jr. (X - 39 - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("b f b b b")
t5.reach("BB")

# 9. BOS #10 Jose Iglesias (39 - 5 - 44)
t5.new_ab(is_risp=True)
t5.pitch_list("b c b f")
t5.out("P3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 2. NYY #26 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("l b f f s")
b5.out("K")

# 3. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)

# 4. NYY #36 Kevin Youkilis (X - X - 24)
b5.new_ab()
b5.pitch_list("c")
b5.out("F8")

# 5. NYY #12 Vernon Wells (X - X - 24)
b5.new_ab()
b5.pitch_list("c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #41 David Phelps
t6 = game.new_inning()

# Pitching change (NYY): #41 David Phelps replaces #52 CC Sabathia
t6.pitching_substitution(41)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b f b f")
t6.hit(3)
t6.thrown_out(4, "15 FC5-2", 2, 41)

# 2. BOS #18 Shane Victorino (2 - X - X)
t6.new_ab(is_risp=True)
t6.out("G4-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c b")
t6.reach("FC5-2")

# 4. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("c f b d")
t6.out("F7")


# Bot 6th
# Pitching: BOS #19 Koji Uehara
b6 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #31 Jon Lester
b6.pitching_substitution(19)

# Offensive change (NYY): Pinch-hitter #33 Travis Hafner replaces #45 Ben Francisco, batting 6th
b6.offensive_substitution(6, 33, "PH")

# 6. NYY #33 Travis Hafner (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("P6")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
b6.new_ab()
b6.out("P5")

# Offensive change (NYY): Pinch-hitter #55 Lyle Overbay replaces #17 Jayson Nix, batting 8th
b6.offensive_substitution(8, 55, "PH")

# 8. NYY #55 Lyle Overbay (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #41 David Phelps
t7 = game.new_inning()

# Defensive switch (NYY): #36 Kevin Youkilis moves to 3B
t7.defensive_switch(36, "5")

# Defensive switch (NYY): #33 Travis Hafner moves to DH
t7.defensive_switch(33, "0")

# Defensive switch (NYY): #55 Lyle Overbay moves to 1B
t7.defensive_switch(55, "3")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c b f f b")
t7.reach("BB")
t7.advance(2, "39 BB")
t7.advance(3, "5 F9")
t7.advance(4, "44 G1-4-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 16)
t7.new_ab()
t7.pitch_list("f s b d 1 f f b 1 b")
t7.reach("BB")
t7.advance(2, "44 G1-4-3")
t7.advance(3, "10 1B")

# 7. BOS #5  Jonny Gomes (X - 16 - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("c b")
t7.out("F9")

# Pitching change (NYY): #48 Boone Logan replaces #41 David Phelps
t7.pitching_substitution(48)

# 8. BOS #44 Jackie Bradley Jr. (16 - X - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("b b f b")
t7.out("G1-4-3", rbis=1)

# 9. BOS #10 Jose Iglesias (X - 39 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c t b f b")
t7.hit(1)

# 1. BOS #2  Jacoby Ellsbury (39 - X - 10)
t7.new_ab(is_risp=True)
t7.pitch_list("c b 1 c")
t7.out("L6")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #19 Koji Uehara
b7.pitching_substitution(30)

# 9. NYY #29 Francisco Cervelli (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.advance(2, "11 BB")

# 1. NYY #11 Brett Gardner (X - X - 29)
b7.new_ab()
b7.pitch_list("b c c b b b")
b7.reach("BB")

# 2. NYY #26 Eduardo Núñez (X - 29 - 11)
b7.new_ab(is_risp=True)
b7.pitch_list("c s f c")
b7.out("!K")

# 3. NYY #24 Robinson Canó (X - 29 - 11)
b7.new_ab(is_risp=True)
b7.pitch_list("s f f d b s")
b7.out("K")

# Pitching change (BOS): #40 Andrew Bailey replaces #30 Andrew Miller
b7.pitching_substitution(40)

# 4. NYY #36 Kevin Youkilis (X - 29 - 11)
b7.new_ab(is_risp=True)
b7.pitch_list("c s b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #27 Shawn Kelley
t8 = game.new_inning()

# Pitching change (NYY): #27 Shawn Kelley replaces #48 Boone Logan
t8.pitching_substitution(27)

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G6-3")

# 4. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("f f b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #40 Andrew Bailey
b8.pitching_substitution(36)

# 5. NYY #12 Vernon Wells (X - X - X)
b8.new_ab()
b8.out("F9")

# 6. NYY #33 Travis Hafner (X - X - X)
b8.new_ab()
b8.pitch_list("f b s f f")
b8.hit(1)
b8.thrown_out(2, "31 DP1-6-3", 2, 36)

# 7. NYY #31 Ichiro Suzuki (X - X - 33)
b8.new_ab()
b8.pitch_list("c")
b8.out("DP1-6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #62 Joba Chamberlain
t9 = game.new_inning()

# Pitching change (NYY): #62 Joba Chamberlain replaces #27 Shawn Kelley
t9.pitching_substitution(62)

# 5. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f b c")
t9.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("s b c b b b")
t9.reach("BB")
t9.advance(2, "5 1B")
t9.advance(3, "44 BB")
t9.advance(4, "2 1B")

# 7. BOS #5  Jonny Gomes (X - X - 39)
t9.new_ab()
t9.hit(1)
t9.advance(2, "44 BB")
t9.advance(4, "2 1B")

# 8. BOS #44 Jackie Bradley Jr. (X - 39 - 5)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b f b b")
t9.reach("BB")
t9.advance(3, "2 1B")
t9.advance(4, "18 1B")

# 9. BOS #10 Jose Iglesias (39 - 5 - 44)
t9.new_ab(is_risp=True)
t9.pitch_list("f s s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (39 - 5 - 44)
t9.new_ab(is_risp=True)
t9.hit(1, rbis=2)
t9.advance(2, "18 1B")
t9.advance(3, "15 WP")

# 2. BOS #18 Shane Victorino (44 - X - 2)
t9.new_ab(is_risp=True)
t9.pitch_list("d")
t9.hit(1, rbis=1)
t9.advance(2, "15 WP")

# Pitching change (NYY): #38 Cody Eppley replaces #62 Joba Chamberlain
t9.pitching_substitution(38)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t9.new_ab(is_risp=True)
t9.pitch_list("c b")
t9.wp()
t9.out("G6-3")


# Bot 9th
# Pitching: BOS #52 Joel Hanrahan
b9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #36 Junichi Tazawa
b9.pitching_substitution(52)

# 8. NYY #55 Lyle Overbay (X - X - X)
b9.new_ab()
b9.pitch_list("c f b")
b9.out("F9")

# 9. NYY #29 Francisco Cervelli (X - X - X)
b9.new_ab()
b9.out("G6-3")

# 1. NYY #11 Brett Gardner (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s f b")
b9.out("(F)P5")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: NYY
# LP: NYY #52 CC Sabathia
game.losing_pitcher(52)

# print(game)
game.generate_scorecard()
