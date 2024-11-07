import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-04-03
# https://www.baseball-reference.com/boxes/NYA/NYA201304030.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/04/03/346764/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-03 19:10-22:45",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "40,216",
        "temp": "43F, Clear",
        "wind": "22mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                44: "Jackie Bradley Jr.",
                10: "Jose Iglesias",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "0"],
                [15, "4"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
                [18, "9"],
                [44, "7"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 30, 91, 52, 31, 59, 36, 19, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 18,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                31: "Ichiro Suzuki",
                24: "Robinson Canó",
                36: "Kevin Youkilis",
                33: "Travis Hafner",
                12: "Vernon Wells",
                55: "Lyle Overbay",
                26: "Eduardo Núñez",
                19: "Chris Stewart",
                # Starting pitcher
                18: "Hiroki Kuroda",
                # Bench
                29: "Francisco Cervelli",
                17: "Jayson Nix",
                22: "Brennan Boesch",
                45: "Ben Francisco",
                # Bullpen
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
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
                [31, "9"],
                [24, "4"],
                [36, "5"],
                [33, "0"],
                [12, "7"],
                [55, "3"],
                [26, "6"],
                [19, "2"],
            ],
            "bench": [
                [29, "C"],
                [17, "3B"],
                [22, "RF"],
                [45, "LF"],
            ],
            "bullpen": [27, 47, 52, 48, 41, 43, 42, 46, 62, 38, 30],
        },
        "umpires": {
            "HP": "Alfonso Márquez",
            "1B": "Mike DiMuro",
            "2B": "Dan Bellino",
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
# Pitching: NYY #18 Hiroki Kuroda
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("P6")

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b")
t1.hit(1)
t1.advance(2, "15 1B")
t1.advance(3, "12 F8")
t1.advance(4, "39 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t1.new_ab()
t1.pitch_list("c b s")
t1.hit(1)
t1.advance(3, "39 1B")

# 4. BOS #12 Mike Napoli (X - 29 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b c t")
t1.out("F8")

# 5. BOS #39 Jarrod Saltalamacchia (29 - X - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("c d b")
t1.hit(1, rbis=1)

# 6. BOS #16 Will Middlebrooks (15 - X - 39)
t1.new_ab(is_risp=True)
t1.pitch_list("b s f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.out("B5-3")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
b1.new_ab()
b1.pitch_list("b f b s b b")
b1.reach("BB")
b1.advance(2, "36 1B")

# 3. NYY #24 Robinson Canó (X - X - 31)
b1.new_ab()
b1.pitch_list("1 1 1 b 1")
b1.out("F7")

# 4. NYY #36 Kevin Youkilis (X - X - 31)
b1.new_ab()
b1.pitch_list("c 1 c f")
b1.hit(1)

# 5. NYY #33 Travis Hafner (X - 31 - 36)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #18 Hiroki Kuroda
t2 = game.new_inning()

# 7. BOS #18 Shane Victorino (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.advance(2, "44 HBP")
t2.thrown_out(3, "10 FC2-5", 1, 18)

# 8. BOS #44 Jackie Bradley Jr. (X - X - 18)
t2.new_ab()
t2.pitch_list("1 b c f")
t2.reach("HBP")
t2.advance(2, "10 FC2-5")
t2.advance(3, "2 BB")
t2.advance(4, "29 HBP")

# 9. BOS #10 Jose Iglesias (X - 18 - 44)
t2.new_ab(is_risp=True)
t2.pitch_list("l l")
t2.reach("FC2-5")
t2.advance(2, "2 BB")
t2.advance(3, "29 HBP")

# 1. BOS #2  Jacoby Ellsbury (X - 44 - 10)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "29 HBP")

# 2. BOS #29 Daniel Nava (44 - 10 - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.reach("HBP", rbis=1)
t2.thrown_out(2, "15 DP6-3", 2, 38)

# Pitching change (NYY): #38 Cody Eppley replaces #18 Hiroki Kuroda
t2.pitching_substitution(38)

# 3. BOS #15 Dustin Pedroia (10 - 2 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c c b")
t2.out("DP6-3")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 6. NYY #12 Vernon Wells (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.thrown_out(2, "55 DP6-4-3", 1, 11)

# 7. NYY #55 Lyle Overbay (X - X - 12)
b2.new_ab()
b2.pitch_list("b f")
b2.out("DP6-4-3")

# 8. NYY #26 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #38 Cody Eppley
t3 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("s b b b")
t3.hit(1)
t3.advance(2, "16 WP")
t3.advance(4, "18 1B")

# 6. BOS #16 Will Middlebrooks (X - X - 39)
t3.new_ab(is_risp=True)
t3.pitch_list("b c c b s")
t3.wp()
t3.out("K")

# 7. BOS #18 Shane Victorino (X - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=1)
t3.advance(2, "44 SB")
t3.advance(4, "44 1B")

# 8. BOS #44 Jackie Bradley Jr. (X - X - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("b s f b")
t3.hit(1, rbis=1)
t3.advance(3, "10 2B")
t3.advance(4, "2 1B")

# 9. BOS #10 Jose Iglesias (X - X - 44)
t3.new_ab()
t3.pitch_list("1 c f f b")
t3.hit(2)
t3.advance(4, "2 1B")

# Pitching change (NYY): #43 Adam Warren replaces #38 Cody Eppley
t3.pitching_substitution(43)

# 1. BOS #2  Jacoby Ellsbury (44 - 10 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b")
t3.hit(1, rbis=2)

# 2. BOS #29 Daniel Nava (X - X - 2)
t3.new_ab()
t3.pitch_list("b 1 f")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.out("L8")

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("b c c b s")
b3.out("K")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #43 Adam Warren
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c f f")
t4.hit(1)
t4.thrown_out(2, "12 DP1-4-3", 1, 43)

# 4. BOS #12 Mike Napoli (X - X - 15)
t4.new_ab()
t4.pitch_list("d b f c b")
t4.out("DP1-4-3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("c f b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G6-3")

# 4. NYY #36 Kevin Youkilis (X - X - X)
b4.new_ab()
b4.pitch_list("b c f b c")
b4.out("!K")

# 5. NYY #33 Travis Hafner (X - X - X)
b4.new_ab()
b4.hit(4)

# 6. NYY #12 Vernon Wells (X - X - X)
b4.new_ab()
b4.hit(1)

# 7. NYY #55 Lyle Overbay (X - X - 12)
b4.new_ab()
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #43 Adam Warren
t5 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c c f f b")
t5.out("F9")

# 7. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c b s b b s")
t5.out("K")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c c d")
t5.out("L7")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 8. NYY #26 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.hit(1)
b5.advance(2, "31 SB")

# 9. NYY #19 Chris Stewart (X - X - 26)
b5.new_ab()
b5.pitch_list("c d c f b b f")
b5.out("F7")

# 1. NYY #11 Brett Gardner (X - X - 26)
b5.new_ab()
b5.pitch_list("1 1")
b5.out("F7")

# 2. NYY #31 Ichiro Suzuki (X - X - 26)
b5.new_ab(is_risp=True)
b5.pitch_list("b b c b f")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #43 Adam Warren
t6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "2 FC4-6", 1, 43)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t6.new_ab()
t6.reach("FC4-6")
t6.advance(3, "29 2B")
t6.advance(4, "15 G6-3")

# 2. BOS #29 Daniel Nava (X - X - 2)
t6.new_ab()
t6.pitch_list("b 1 s f d 1 1")
t6.hit(2)
t6.advance(3, "12 1B")

# 3. BOS #15 Dustin Pedroia (2 - 29 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b f s b")
t6.out("G6-3", rbis=1)

# 4. BOS #12 Mike Napoli (X - 29 - X)
t6.new_ab(is_risp=True)
t6.hit(1)

# 5. BOS #39 Jarrod Saltalamacchia (29 - X - 12)
t6.new_ab(is_risp=True)
t6.pitch_list("s b s b s")
t6.out("K")


# Bot 6th
# Pitching: BOS #11 Clay Buchholz
b6 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
b6.new_ab()
b6.pitch_list("b f b")
b6.out("L8")

# 4. NYY #36 Kevin Youkilis (X - X - X)
b6.new_ab()
b6.pitch_list("f f f")
b6.out("G6-3")

# 5. NYY #33 Travis Hafner (X - X - X)
b6.new_ab()
b6.pitch_list("b b f b t c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #43 Adam Warren
t7 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.out("L8")

# 7. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b s")
t7.out("(F)P2")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b s b b f f")
t7.out("L8")


# Bot 7th
# Pitching: BOS #11 Clay Buchholz
b7 = game.new_inning()

# 6. NYY #12 Vernon Wells (X - X - X)
b7.new_ab()
b7.pitch_list("c s")
b7.out("G6-3")

# 7. NYY #55 Lyle Overbay (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(2, "26 BB")

# 8. NYY #26 Eduardo Núñez (X - X - 55)
b7.new_ab()
b7.pitch_list("b b f b b")
b7.reach("BB")

# Offensive change (NYY): Pinch-hitter #22 Brennan Boesch replaces #19 Chris Stewart, batting 9th
b7.offensive_substitution(9, 22, "PH")

# 9. NYY #22 Brennan Boesch (X - 55 - 26)
b7.new_ab(is_risp=True)
b7.pitch_list("b f f s")
b7.out("K")

# 1. NYY #11 Brett Gardner (X - 55 - 26)
b7.new_ab(is_risp=True)
b7.pitch_list("b b b c c f")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #43 Adam Warren
t8 = game.new_inning()

# Defensive change (NYY): #29 Francisco Cervelli replaces #22 Brennan Boesch (PH), playing C, batting 9th
t8.defensive_substitution(9, 29, "2")

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b c")
t8.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("f b c d")
t8.out("G6-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t8.new_ab()
t8.pitch_list("b")
t8.out("F9")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #11 Clay Buchholz
b8.pitching_substitution(30)

# Offensive change (NYY): Pinch-hitter #45 Ben Francisco replaces #31 Ichiro Suzuki, batting 2nd
b8.offensive_substitution(2, 45, "PH")

# 2. NYY #45 Ben Francisco (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.reach("HBP")
b8.advance(2, "36 1B")
b8.advance(3, "33 G2-3")
b8.advance(4, "12 HR")

# 3. NYY #24 Robinson Canó (X - X - 45)
b8.new_ab()
b8.pitch_list("c b f")
b8.out("L8")

# Pitching change (BOS): #91 Alfredo Aceves replaces #30 Andrew Miller
b8.pitching_substitution(91)

# 4. NYY #36 Kevin Youkilis (X - X - 45)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "33 G2-3")
b8.advance(4, "12 HR")

# 5. NYY #33 Travis Hafner (X - 45 - 36)
b8.new_ab(is_risp=True)
b8.pitch_list("c f f")
b8.out("G2-3")

# 6. NYY #12 Vernon Wells (45 - 36 - X)
b8.new_ab(is_risp=True)
b8.hit(4, rbis=3)

# 7. NYY #55 Lyle Overbay (X - X - X)
b8.new_ab()
b8.pitch_list("b c s b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #27 Shawn Kelley
t9 = game.new_inning()

# Pitching change (NYY): #27 Shawn Kelley replaces #43 Adam Warren
t9.pitching_substitution(27)

# Defensive switch (NYY): #45 Ben Francisco moves to RF
t9.defensive_switch(45, "9")

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f c")
t9.out("!K")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b")
t9.out("L8")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b f d")
t9.reach("BB")
t9.advance(3, "18 2B")

# 7. BOS #18 Shane Victorino (X - X - 16)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(2)

# 8. BOS #44 Jackie Bradley Jr. (16 - 18 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #52 Joel Hanrahan
b9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #91 Alfredo Aceves
b9.pitching_substitution(52)

# 8. NYY #26 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c c b b")
b9.hit(1)
b9.thrown_out(2, "29 FC5-4", 1, 52)

# 9. NYY #29 Francisco Cervelli (X - X - 26)
b9.new_ab()
b9.pitch_list("c b c b b f f")
b9.reach("FC5-4")

# 1. NYY #11 Brett Gardner (X - X - 29)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# 2. NYY #45 Ben Francisco (X - X - 29)
b9.new_ab()
b9.pitch_list("c s b b")
b9.out("F9")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)
# SV: BOS #52 Joel Hanrahan
game.save_pitcher(52, is_away_team=True)

# Loser team: NYY
# LP: NYY #18 Hiroki Kuroda
game.losing_pitcher(18)

# print(game)
game.generate_scorecard()
