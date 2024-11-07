import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-09-05
# https://www.baseball-reference.com/boxes/NYA/NYA201309050.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/09/05/348833/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-05 19:07-23:39",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "40,481",
        "temp": "71F, Clear",
        "wind": "14mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                16: "Will Middlebrooks",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                50: "Quintin Berry",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
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
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [7, "6"],
                [20, "2"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [39, "C"],
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 31, 36, 11, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 47,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                2: "Derek Jeter",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                14: "Curtis Granderson",
                13: "Alex Rodriguez",
                55: "Lyle Overbay",
                31: "Ichiro Suzuki",
                19: "Chris Stewart",
                # Starting pitcher
                47: "Iván Nova",
                # Bench
                22: "Vernon Wells",
                26: "Eduardo Núñez",
                39: "Mark Reynolds",
                53: "Austin Romine",
                45: "David Adams",
                66: "John Ryan Murphy",
                # Bullpen
                61: "Dellin Betances",
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                60: "David Huff",
                43: "Adam Warren",
                64: "Cesar Cabral",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                70: "Brett Marshall",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [52, 48, 60, 64, 46],
            "lineup": [
                [11, "8"],
                [2, "6"],
                [24, "4"],
                [12, "7"],
                [14, "0"],
                [13, "5"],
                [55, "3"],
                [31, "9"],
                [19, "2"],
            ],
            "bench": [
                [22, "CF"],
                [26, "SS"],
                [39, "3B"],
                [53, "C"],
                [45, "3B"],
                [66, "C"],
            ],
            "bullpen": [61, 18, 65, 27, 52, 38, 48, 60, 43, 64, 42, 46, 70, 62, 30],
        },
        "umpires": {
            "HP": "Rob Drake",
            "1B": "Joe West",
            "2B": "Sam Holbrook",
            "3B": "Andy Fletcher",
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
# Pitching: NYY #47 Iván Nova
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s b")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F8")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("(F)P2")

# 2. NYY #2  Derek Jeter (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G4-3")

# 3. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.pitch_list("c f f f f d f b f")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #47 Iván Nova
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c s b f b b")
t2.hit(1)

# 5. BOS #29 Daniel Nava (X - X - 34)
t2.new_ab()
t2.pitch_list("c b c")
t2.out("F8")

# 6. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")

# 7. BOS #7  Stephen Drew (X - X - 34)
t2.new_ab()
t2.pitch_list("c f b 1 f d d s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
b2.new_ab()
b2.pitch_list("s b")
b2.out("L5")

# 5. NYY #14 Curtis Granderson (X - X - X)
b2.new_ab()
b2.pitch_list("c s b f f b")
b2.out("F7")

# 6. NYY #13 Alex Rodriguez (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #47 Iván Nova
t3 = game.new_inning()

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t3.new_ab()
t3.pitch_list("c f f b b f f")
t3.hit(1)
t3.advance(2, "16 1B")
t3.advance(4, "2 2B")

# 9. BOS #16 Will Middlebrooks (X - X - 20)
t3.new_ab()
t3.pitch_list("f d f d")
t3.hit(1)
t3.advance(3, "2 2B")
t3.advance(4, "18 G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - 20 - 16)
t3.new_ab(is_risp=True)
t3.pitch_list("c f f d b b f")
t3.hit(2, rbis=1)
t3.advance(3, "29 BB")

# 2. BOS #18 Shane Victorino (16 - 2 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c s d b")
t3.out("G6-3", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b f b c")
t3.out("G6-3")

# 4. BOS #34 David Ortiz (X - 2 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("i i i i")
t3.reach("IBB")
t3.advance(2, "29 BB")

# 5. BOS #29 Daniel Nava (X - 2 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("d b b b")
t3.reach("BB")

# 6. BOS #12 Mike Napoli (2 - 34 - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("c b c b f c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 7. NYY #55 Lyle Overbay (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c")
b3.out("F8")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b3.new_ab()
b3.pitch_list("s b f")
b3.hit(1)
b3.advance(2, "19 SB")
b3.advance(3, "11 1B")
b3.advance(4, "24 2B")

# 9. NYY #19 Chris Stewart (X - X - 31)
b3.new_ab(is_risp=True)
b3.pitch_list("c s f")
b3.out("P3")

# 1. NYY #11 Brett Gardner (X - 31 - X)
b3.new_ab(is_risp=True)
b3.hit(1)
b3.advance(2, "2 SB")
b3.advance(4, "24 2B")

# 2. NYY #2  Derek Jeter (31 - X - 11)
b3.new_ab(is_risp=True)
b3.pitch_list("c t b b f b b")
b3.reach("BB")
b3.advance(3, "24 2B")

# 3. NYY #24 Robinson Canó (31 - 11 - 2)
b3.new_ab(is_risp=True)
b3.hit(2, rbis=2)

# 4. NYY #12 Alfonso Soriano (2 - 24 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #47 Iván Nova
t4 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("L7")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b")
t4.out("F8")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("b f t")
t4.out("F7")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 5. NYY #14 Curtis Granderson (X - X - X)
b4.new_ab()
b4.out("(F)P6")

# 6. NYY #13 Alex Rodriguez (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.hit(2)
b4.advance(3, "31 SB")

# 7. NYY #55 Lyle Overbay (X - 13 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b c b b")
b4.reach("BB")
b4.advance(2, "31 SB")

# 8. NYY #31 Ichiro Suzuki (X - 13 - 55)
b4.new_ab(is_risp=True)
b4.pitch_list("c f b f f f d f s")
b4.out("K")

# 9. NYY #19 Chris Stewart (13 - 55 - X)
b4.new_ab(is_risp=True)
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #38 Preston Claiborne
t5 = game.new_inning()

# Pitching change (NYY): #38 Preston Claiborne replaces #47 Iván Nova
t5.pitching_substitution(38)

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b b f s f b")
t5.hit(1)
t5.advance(2, "34 1B")
t5.advance(3, "29 BB")
t5.advance(4, "12 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("c d f b")
t5.hit(1)
t5.advance(2, "29 BB")
t5.advance(3, "12 1B")
t5.advance(4, "20 FC6")

# 5. BOS #29 Daniel Nava (X - 15 - 34)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c s f d b")
t5.reach("BB")
t5.advance(2, "12 1B")
t5.advance(3, "20 FC6")

# 6. BOS #12 Mike Napoli (15 - 34 - 29)
t5.new_ab(is_risp=True)
t5.pitch_list("s c d")
t5.hit(1, rbis=1)
t5.thrown_out(2, "20 FC6", 2, 43)

# Pitching change (NYY): #64 Cesar Cabral replaces #38 Preston Claiborne
t5.pitching_substitution(64)

# 7. BOS #7  Stephen Drew (34 - 29 - 12)
t5.new_ab(is_risp=True)
t5.pitch_list("s c d c")
t5.out("!K")

# Pitching change (NYY): #43 Adam Warren replaces #64 Cesar Cabral
t5.pitching_substitution(43)

# 8. BOS #20 Ryan Lavarnway (34 - 29 - 12)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c")
t5.reach("FC6", rbis=1)

# 9. BOS #16 Will Middlebrooks (29 - X - 20)
t5.new_ab(is_risp=True)
t5.pitch_list("c s t")
t5.out("KT")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("(F)P5")

# 2. NYY #2  Derek Jeter (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("L3")

# 3. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #43 Adam Warren
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.thrown_out(1, "15 PO", 2, 43)

# 2. BOS #18 Shane Victorino (X - X - 2)
t6.new_ab()
t6.pitch_list("1 b c 1 1 1")
t6.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t6.new_ab()
t6.pitch_list("b 1 b c 1 b s f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("F7")

# 5. NYY #14 Curtis Granderson (X - X - X)
b6.new_ab()
b6.pitch_list("b s f b c")
b6.out("!K")

# 6. NYY #13 Alex Rodriguez (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f f b")
b6.hit(2)

# 7. NYY #55 Lyle Overbay (X - 13 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s f b b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #43 Adam Warren
t7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c f s")
t7.out("K")

# 5. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.hit(2)
t7.advance(4, "20 1B")

# 6. BOS #12 Mike Napoli (X - 29 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c b s b f b b")
t7.reach("BB")
t7.advance(3, "20 1B")

# 7. BOS #7  Stephen Drew (X - 29 - 12)
t7.new_ab(is_risp=True)
t7.pitch_list("c f s")
t7.out("K")

# 8. BOS #20 Ryan Lavarnway (X - 29 - 12)
t7.new_ab(is_risp=True)
t7.pitch_list("b f s")
t7.hit(1, rbis=1)

# 9. BOS #16 Will Middlebrooks (12 - X - 20)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.out("F7")


# Bot 7th
# Pitching: BOS #44 Jake Peavy
b7 = game.new_inning()

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f f b b b")
b7.reach("BB")
b7.advance(3, "22 1B")
b7.advance(4, "11 1B")

# Offensive change (NYY): Pinch-hitter #22 Vernon Wells replaces #19 Chris Stewart, batting 9th
b7.offensive_substitution(9, 22, "PH")

# 9. NYY #22 Vernon Wells (X - X - 31)
b7.new_ab()
b7.pitch_list("b b c")
b7.hit(1)
b7.advance(2, "11 1B")
b7.advance(3, "2 SB")
b7.advance(4, "24 FC4-6")

# Pitching change (BOS): #38 Matt Thornton replaces #44 Jake Peavy
b7.pitching_substitution(38)

# 1. NYY #11 Brett Gardner (31 - X - 22)
b7.new_ab(is_risp=True)
b7.pitch_list("c f f")
b7.hit(1, rbis=1)
b7.advance(2, "2 BB")
b7.advance(3, "24 FC4-6")
b7.advance(4, "12 1B")

# 2. NYY #2  Derek Jeter (X - 22 - 11)
b7.new_ab(is_risp=True)
b7.pitch_list("b d d 1 c b")
b7.reach("BB")
b7.thrown_out(2, "24 FC4-6", 1, 38)

# 3. NYY #24 Robinson Canó (22 - 11 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("d f")
b7.reach("FC4-6", rbis=1)
b7.advance(2, "12 1B")
b7.advance(4, "14 2B")

# Pitching change (BOS): #36 Junichi Tazawa replaces #38 Matt Thornton
b7.pitching_substitution(36)

# 4. NYY #12 Alfonso Soriano (11 - X - 24)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.hit(1, rbis=1)
b7.advance(3, "14 2B")
b7.advance(4, "55 1B")

# 5. NYY #14 Curtis Granderson (X - 24 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("c c f")
b7.hit(2, rbis=1)
b7.advance(4, "55 1B")

# 6. NYY #13 Alex Rodriguez (12 - 14 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f b f s")
b7.out("K")

# 7. NYY #55 Lyle Overbay (12 - 14 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s d s")
b7.hit(1, rbis=2)
b7.advance(2, "T")

# 8. NYY #31 Ichiro Suzuki (X - 55 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #30 David Robertson
t8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #43 Adam Warren
t8.pitching_substitution(30)

# Defensive change (NYY): #53 Austin Romine replaces #22 Vernon Wells (PH), playing C, batting 9th
t8.defensive_substitution(9, 53, "2")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b b c")
t8.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b s f b f s")
t8.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b8.pitching_substitution(32)

# 9. NYY #53 Austin Romine (X - X - X)
b8.new_ab()
b8.out("G1-3")

# 1. NYY #11 Brett Gardner (X - X - X)
b8.new_ab()
b8.pitch_list("c c b s")
b8.out("K")

# 2. NYY #2  Derek Jeter (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #42 Mariano Rivera
t9 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #30 David Robertson
t9.pitching_substitution(42)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L3")

# 5. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b b")
t9.out("G3")

# 6. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #12 Mike Napoli
t9.offensive_substitution(6, 50, "PR")
t9.atbase("PR")
t9.error(2)
t9.advance(2, "7 SB")
t9.advance(3, "7 E2")
t9.advance(4, "7 1B")

# 7. BOS #7  Stephen Drew (X - X - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.hit(1, rbis=1)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #20 Ryan Lavarnway, batting 8th
t9.offensive_substitution(8, 5, "PH")

# 8. BOS #5  Jonny Gomes (X - X - 7)
t9.new_ab()
t9.pitch_list("1 b f")
t9.out("(F)P2")


# Bot 9th
# Pitching: BOS #32 Craig Breslow
b9 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b9.defensive_switch(29, "3")

# Defensive switch (BOS): #50 Quintin Berry moves to LF
b9.defensive_switch(50, "7")

# Defensive change (BOS): #3 David Ross replaces #5 Jonny Gomes (PH), playing C, batting 8th
b9.defensive_substitution(8, 3, "2")

# 3. NYY #24 Robinson Canó (X - X - X)
b9.new_ab()
b9.out("L4")

# 4. NYY #12 Alfonso Soriano (X - X - X)
b9.new_ab()
b9.pitch_list("b b b b")
b9.reach("BB")
b9.advance(2, "14 SB")
b9.thrown_out(3, "14 CS", 2, 32)

# 5. NYY #14 Curtis Granderson (X - X - 12)
b9.new_ab()
b9.pitch_list("1 1 c b s 1 1 n s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: NYY #62 Joba Chamberlain
t10 = game.new_inning()

# Pitching change (NYY): #62 Joba Chamberlain replaces #42 Mariano Rivera
t10.pitching_substitution(62)

# 9. BOS #16 Will Middlebrooks (X - X - X)
t10.new_ab()
t10.pitch_list("c b b s f")
t10.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t10.new_ab()
t10.pitch_list("b b f")
t10.hit(1)
t10.advance(2, "18 SB")
t10.advance(4, "18 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t10.new_ab(is_risp=True)
t10.pitch_list("1 b 1 c s f f b")
t10.hit(1, rbis=1)
t10.advance(2, "T")
t10.advance(3, "23 SB")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("c")
t10.out("F8")

# Pitching change (NYY): #48 Boone Logan replaces #62 Joba Chamberlain
t10.pitching_substitution(48)

# 4. BOS #34 David Ortiz (X - 18 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("i i i i")
t10.reach("IBB")

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #29 Daniel Nava, batting 5th
t10.offensive_substitution(5, 23, "PH")

# 5. BOS #23 Brandon Snyder (X - 18 - 34)
t10.new_ab(is_risp=True)
t10.pitch_list("b b c")
t10.out("F8")


# Bot 10th
# Pitching: BOS #19 Koji Uehara
b10 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b10.pitching_substitution(19)

# Defensive switch (BOS): #23 Brandon Snyder moves to 1B
b10.defensive_switch(23, "3")

# 6. NYY #13 Alex Rodriguez (X - X - X)
b10.new_ab()
b10.pitch_list("s")
b10.out("P4")

# 7. NYY #55 Lyle Overbay (X - X - X)
b10.new_ab()
b10.pitch_list("b c b s f f b f f f f s")
b10.out("K")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b10.new_ab()
b10.pitch_list("b b f b s s")
b10.out("K")

# Winning team: BOS
# WP: BOS #32 Craig Breslow
game.winning_pitcher(32, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: NYY
# LP: NYY #62 Joba Chamberlain
game.losing_pitcher(62)

# print(game)
game.generate_scorecard()
