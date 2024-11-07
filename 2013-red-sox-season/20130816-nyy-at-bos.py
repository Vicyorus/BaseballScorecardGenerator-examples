import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-08-16
# https://www.baseball-reference.com/boxes/BOS/BOS201308160.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/08/16/348560/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-16 19:12-22:43",
        "at": "Fenway Park, Boston, MA",
        "att": "38,143",
        "temp": "79F, Partly Cloudy",
        "wind": "6mph, Out To RF",
        "away": {
            "team": "New York Yankees",
            "starter": 46,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                26: "Eduardo Núñez",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                13: "Alex Rodriguez",
                22: "Vernon Wells",
                31: "Ichiro Suzuki",
                39: "Mark Reynolds",
                19: "Chris Stewart",
                # Starting pitcher
                46: "Andy Pettitte",
                # Bench
                53: "Austin Romine",
                17: "Jayson Nix",
                55: "Lyle Overbay",
                14: "Curtis Granderson",
                # Bullpen
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                48: "Boone Logan",
                60: "David Huff",
                43: "Adam Warren",
                42: "Mariano Rivera",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [46, 52, 48, 60],
            "lineup": [
                [11, "8"],
                [26, "6"],
                [24, "4"],
                [12, "7"],
                [13, "5"],
                [22, "0"],
                [31, "9"],
                [39, "3"],
                [19, "2"],
            ],
            "bench": [
                [53, "C"],
                [17, "3B"],
                [55, "1B"],
                [14, "CF"],
            ],
            "bullpen": [18, 65, 27, 47, 52, 48, 60, 43, 42, 62, 30],
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
                5: "Jonny Gomes",
                7: "Stephen Drew",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                # Starting pitcher
                22: "Felix Doubront",
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
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31],
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
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 19, 62, 46],
        },
        "umpires": {
            "HP": "Bill Welke",
            "1B": "Adrian Johnson",
            "2B": "Brian O'Nora",
            "3B": "Fieldin Culbreth",
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
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "26 SAC1-3")
t1.advance(3, "24 SB")
t1.advance(4, "12 1B")

# 2. NYY #26 Eduardo Núñez (X - X - 11)
t1.new_ab()
t1.pitch_list("1 b")
t1.out("SAC1-3")

# 3. NYY #24 Robinson Canó (X - 11 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b b f b")
t1.reach("BB")
t1.advance(2, "12 1B")
t1.thrown_out(2, "13 DP5-4", 3, 22)

# 4. NYY #12 Alfonso Soriano (11 - X - 24)
t1.new_ab(is_risp=True)
t1.hit(1, rbis=1)

# 5. NYY #13 Alex Rodriguez (X - 24 - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b c")
t1.out("DP5-4")


# Bot 1st
# Pitching: NYY #46 Andy Pettitte
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("f b b t")
b1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 6. NYY #22 Vernon Wells (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b b")
t2.reach("BB")
t2.advance(4, "39 HR")

# 7. NYY #31 Ichiro Suzuki (X - X - 22)
t2.new_ab()
t2.out("F8")

# 8. NYY #39 Mark Reynolds (X - X - 22)
t2.new_ab()
t2.pitch_list("c s f f")
t2.hit(4, rbis=2)

# 9. NYY #19 Chris Stewart (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F9")

# 1. NYY #11 Brett Gardner (X - X - X)
t2.new_ab()
t2.pitch_list("b c c")
t2.out("G4-3")


# Bot 2nd
# Pitching: NYY #46 Andy Pettitte
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("f c b b")
b2.out("F7")

# 5. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("P4")

# 6. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 2. NYY #26 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("c s b f")
t3.hit(1)
t3.error(6)
t3.advance(2, "24 E6")
t3.advance("U", "12 HR")

# 3. NYY #24 Robinson Canó (X - X - 26)
t3.new_ab()
t3.pitch_list("1 d")
t3.reach("FC6")
t3.advance(4, "12 HR")

# 4. NYY #12 Alfonso Soriano (X - 26 - 24)
t3.new_ab(is_risp=True)
t3.pitch_list("b s 2")
t3.hit(4, rbis=3)

# 5. NYY #13 Alex Rodriguez (X - X - X)
t3.new_ab()
t3.pitch_list("f b f")
t3.hit(1)
t3.advance(2, "22 WP")
t3.advance(3, "31 G4-3")

# 6. NYY #22 Vernon Wells (X - X - 13)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b s")
t3.wp()
t3.out("K")

# 7. NYY #31 Ichiro Suzuki (X - 13 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b")
t3.out("G4-3")

# 8. NYY #39 Mark Reynolds (13 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s b t b f b s")
t3.out("K")


# Bot 3rd
# Pitching: NYY #46 Andy Pettitte
b3 = game.new_inning()

# 7. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("P4")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G6-3")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b3.new_ab()
b3.pitch_list("b f b d")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
t4.new_ab()
t4.out("G6-3")

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("b f b f f f s")
t4.out("K")

# 2. NYY #26 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.hit(3)
t4.advance(4, "24 1B")

# 3. NYY #24 Robinson Canó (26 - X - X)
t4.new_ab(is_risp=True)
t4.hit(1, rbis=1)

# 4. NYY #12 Alfonso Soriano (X - X - 24)
t4.new_ab()
t4.pitch_list("c b f s")
t4.out("K")


# Bot 4th
# Pitching: NYY #46 Andy Pettitte
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)
b4.error(6)
b4.advance(2, "E6")
b4.advance("U", "5 1B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b f f d s")
b4.out("K")

# 5. BOS #5  Jonny Gomes (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c f b b")
b4.hit(1, rbis=1)
b4.thrown_out(1, "7 PO", 3, 46)

# 6. BOS #7  Stephen Drew (X - X - 5)
b4.new_ab()
b4.pitch_list("b s 1")
b4.no_ab("PO")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #62 Rubby De La Rosa
t5 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #22 Felix Doubront
t5.pitching_substitution(62)

# 5. NYY #13 Alex Rodriguez (X - X - X)
t5.new_ab()
t5.pitch_list("s b b b f f b")
t5.reach("BB")

# 6. NYY #22 Vernon Wells (X - X - 13)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F8")

# 7. NYY #31 Ichiro Suzuki (X - X - 13)
t5.new_ab()
t5.pitch_list("b s b b c c")
t5.out("!K")

# 8. NYY #39 Mark Reynolds (X - X - 13)
t5.new_ab()
t5.pitch_list("d b")
t5.out("F9")


# Bot 5th
# Pitching: NYY #46 Andy Pettitte
b5 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b c")
b5.out("!K")

# 7. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b s c t")
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #62 Rubby De La Rosa
t6 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
t6.new_ab()
t6.pitch_list("c s b f b b")
t6.hit(1)
t6.error(1)
t6.advance(2, "E1")
t6.advance(3, "11 1B")

# 1. NYY #11 Brett Gardner (X - 19 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("s f b")
t6.hit(1)
t6.thrown_out(2, "26 DP4-3", 1, 62)

# 2. NYY #26 Eduardo Núñez (19 - X - 11)
t6.new_ab(is_risp=True)
t6.out("DP4-3")

# 3. NYY #24 Robinson Canó (19 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.out("P4")


# Bot 6th
# Pitching: NYY #46 Andy Pettitte
b6 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("s f f b f")
b6.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("f c b c")
b6.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f")
b6.out("P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #62 Rubby De La Rosa
t7 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
t7.new_ab()
t7.pitch_list("c b f")
t7.reach("HBP")
t7.thrown_out(1, "14 PO", 2, 56)

# 5. NYY #13 Alex Rodriguez (X - X - 12)
t7.new_ab()
t7.pitch_list("c")
t7.out("L8")

# Pitching change (BOS): #56 Franklin Morales replaces #62 Rubby De La Rosa
t7.pitching_substitution(56)

# Offensive change (NYY): Pinch-hitter #14 Curtis Granderson replaces #22 Vernon Wells, batting 6th
t7.offensive_substitution(6, 14, "PH")

# 6. NYY #14 Curtis Granderson (X - X - 12)
t7.new_ab()
t7.pitch_list("b 1 s b b 1 b")
t7.reach("BB")
t7.thrown_out(2, "31 FC4-6", 3, 56)

# 7. NYY #31 Ichiro Suzuki (X - X - 14)
t7.new_ab()
t7.pitch_list("c b f f 1")
t7.reach("FC4-6")


# Bot 7th
# Pitching: NYY #46 Andy Pettitte
b7 = game.new_inning()

# Defensive switch (NYY): #14 Curtis Granderson moves to DH
b7.defensive_switch(14, "0")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c s f")
b7.error(6)
b7.reach("E6", end_base=2)
b7.advance("U", "34 1B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b7.new_ab(is_risp=True)
b7.hit(1, rbis=1)
b7.thrown_out(2, "7-4", 1, 46)

# 5. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 6. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)
b7.advance("U", "39 1B")

# 7. BOS #12 Mike Napoli (X - 7 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b f d b")
b7.reach("BB")
b7.advance(2, "39 1B")

# 8. BOS #39 Jarrod Saltalamacchia (X - 7 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("c s b")
b7.hit(1, rbis=1)

# Pitching change (NYY): #27 Shawn Kelley replaces #46 Andy Pettitte
b7.pitching_substitution(27)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #16 Will Middlebrooks, batting 9th
b7.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - 12 - 39)
b7.new_ab(is_risp=True)
b7.pitch_list("b c f d b c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Franklin Morales
t8 = game.new_inning()

# Defensive change (BOS): #26 Brock Holt replaces #37 Mike Carp (PH), playing 3B, batting 9th
t8.defensive_substitution(9, 26, "5")

# 8. NYY #39 Mark Reynolds (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F9")

# 9. NYY #19 Chris Stewart (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("L7")

# 1. NYY #11 Brett Gardner (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.error(4)
t8.reach("E4")

# 2. NYY #26 Eduardo Núñez (X - X - 11)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")


# Bot 8th
# Pitching: NYY #30 David Robertson
b8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #27 Shawn Kelley
b8.pitching_substitution(30)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("l b")
b8.hit(1)
b8.thrown_out(2, "18 FC5-4", 1, 30)

# 2. BOS #18 Shane Victorino (X - X - 2)
b8.new_ab()
b8.pitch_list("c 1")
b8.reach("FC5-4")
b8.advance(2, "15 1B")
b8.thrown_out(2, "34 DP5-6", 3, 30)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b8.new_ab()
b8.pitch_list("c b b c f f")
b8.hit(1)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b8.new_ab(is_risp=True)
b8.out("DP5-6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Drake Britton
t9 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #56 Franklin Morales
t9.pitching_substitution(66)

# Defensive change (BOS): #29 Daniel Nava replaces #18 Shane Victorino (RF), playing RF, batting 2nd
t9.defensive_substitution(2, 29, "9")

# 3. NYY #24 Robinson Canó (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b s")
t9.out("K")

# 4. NYY #12 Alfonso Soriano (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.hit(1)
t9.advance(2, "13 1B")
t9.advance(3, "31 SB")
t9.advance(4, "31 1B")

# 5. NYY #13 Alex Rodriguez (X - X - 12)
t9.new_ab()
t9.pitch_list("b c c b")
t9.hit(1)
t9.advance(2, "31 SB")
t9.advance(3, "31 1B")
t9.advance(4, "39 1B")

# 6. NYY #14 Curtis Granderson (X - 12 - 13)
t9.new_ab(is_risp=True)
t9.pitch_list("c s b t")
t9.out("KT")

# 7. NYY #31 Ichiro Suzuki (X - 12 - 13)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b c")
t9.hit(1, rbis=1)
t9.advance(2, "39 1B")
t9.advance(4, "19 1B")

# 8. NYY #39 Mark Reynolds (13 - X - 31)
t9.new_ab(is_risp=True)
t9.pitch_list("b f c f b b")
t9.hit(1, rbis=1)
t9.advance(3, "19 1B")

# 9. NYY #19 Chris Stewart (X - 31 - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.hit(1, rbis=1)

# 1. NYY #11 Brett Gardner (39 - X - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b f t")
t9.out("KT")


# Bot 9th
# Pitching: NYY #62 Joba Chamberlain
b9 = game.new_inning()

# Pitching change (NYY): #62 Joba Chamberlain replaces #30 David Robertson
b9.pitching_substitution(62)

# 5. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("c b c f")
b9.out("F8")

# 6. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("c c b")
b9.hit(1)
b9.advance(3, "12 2B")

# 7. BOS #12 Mike Napoli (X - X - 7)
b9.new_ab()
b9.pitch_list("d c s")
b9.hit(2)

# 8. BOS #39 Jarrod Saltalamacchia (7 - 12 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b f b")
b9.out("F7")

# 9. BOS #26 Brock Holt (7 - 12 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b c f f d f b b")
b9.reach("BB")

# Pitching change (NYY): #60 David Huff replaces #62 Joba Chamberlain
b9.pitching_substitution(60)

# 1. BOS #2  Jacoby Ellsbury (7 - 12 - 26)
b9.new_ab(is_risp=True)
b9.pitch_list("c f b f b")
b9.out("G4-3")

# Winning team: NYY
# WP: NYY #46 Andy Pettitte
game.winning_pitcher(46, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
