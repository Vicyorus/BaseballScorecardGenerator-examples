import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-09-06
# https://www.baseball-reference.com/boxes/NYA/NYA201309060.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/09/06/348840/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-06 19:08-23:08",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "44,117",
        "temp": "68F, Clear",
        "wind": "5mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                7: "Stephen Drew",
                3: "David Ross",
                16: "Will Middlebrooks",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                72: "Xander Bogaerts",
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
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31, 38],
            "lineup": [
                [18, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [7, "6"],
                [3, "2"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 62, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 46,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                2: "Derek Jeter",
                12: "Alfonso Soriano",
                24: "Robinson Canó",
                13: "Alex Rodriguez",
                22: "Vernon Wells",
                26: "Eduardo Núñez",
                39: "Mark Reynolds",
                19: "Chris Stewart",
                # Starting pitcher
                46: "Andy Pettitte",
                # Bench
                31: "Ichiro Suzuki",
                53: "Austin Romine",
                55: "Lyle Overbay",
                45: "David Adams",
                66: "John Ryan Murphy",
                14: "Curtis Granderson",
                # Bullpen
                61: "Dellin Betances",
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                60: "David Huff",
                43: "Adam Warren",
                64: "Cesar Cabral",
                42: "Mariano Rivera",
                70: "Brett Marshall",
                62: "Joba Chamberlain",
                30: "David Robertson",
                40: "Matt Daley",
            },
            "lefties": [46, 52, 48, 60, 64],
            "lineup": [
                [11, "8"],
                [2, "0"],
                [12, "7"],
                [24, "4"],
                [13, "5"],
                [22, "9"],
                [26, "6"],
                [39, "3"],
                [19, "2"],
            ],
            "bench": [
                [31, "RF"],
                [53, "C"],
                [55, "1B"],
                [45, "3B"],
                [66, "C"],
                [14, "CF"],
            ],
            "bullpen": [61, 18, 65, 27, 47, 52, 38, 48, 60, 43, 64, 42, 70, 62, 30, 40],
        },
        "umpires": {
            "HP": "Joe West",
            "1B": "Sam Holbrook",
            "2B": "Andy Fletcher",
            "3B": "Rob Drake",
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
# Pitching: NYY #46 Andy Pettitte
t1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("c c c")
t1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("s b s 1 s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("B4-3")

# 2. NYY #2  Derek Jeter (X - X - X)
b1.new_ab()
b1.pitch_list("c b b s b f f f b")
b1.reach("BB")
b1.advance(4, "12 HR")

# 3. NYY #12 Alfonso Soriano (X - X - 2)
b1.new_ab()
b1.pitch_list("c d b")
b1.hit(4, rbis=2)

# 4. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.out("G6-3")

# 5. NYY #13 Alex Rodriguez (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.thrown_out(2, "22 POCS", 3, 22)

# 6. NYY #22 Vernon Wells (X - X - 13)
b1.new_ab()
b1.pitch_list("1")
b1.no_ab("POCS")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #46 Andy Pettitte
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(1)
t2.advance(2, "29 BB")
t2.advance(4, "3 1B")

# 6. BOS #29 Daniel Nava (X - X - 12)
t2.new_ab()
t2.pitch_list("b b c d 1 b")
t2.reach("BB")
t2.advance(2, "3 1B")

# 7. BOS #7  Stephen Drew (X - 12 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b s")
t2.out("K")

# 8. BOS #3  David Ross (X - 12 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c c f f")
t2.hit(1, rbis=1)
t2.thrown_out(2, "16 DP6-4-3", 2, 46)

# 9. BOS #16 Will Middlebrooks (X - 29 - 3)
t2.new_ab(is_risp=True)
t2.pitch_list("d b b s")
t2.out("DP6-4-3")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 6. NYY #22 Vernon Wells (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f b b")
b2.reach("BB")
b2.advance(4, "26 3B")

# 7. NYY #26 Eduardo Núñez (X - X - 22)
b2.new_ab()
b2.pitch_list("b b b c 1 f f")
b2.hit(3, rbis=1)
b2.advance(4, "19 SF7")

# 8. NYY #39 Mark Reynolds (26 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c f b c")
b2.out("!K")

# 9. NYY #19 Chris Stewart (26 - X - X)
b2.new_ab(is_risp=True)
b2.out("SF7", rbis=1)

# 1. NYY #11 Brett Gardner (X - X - X)
b2.new_ab()
b2.pitch_list("b c c b b b")
b2.reach("BB")

# 2. NYY #2  Derek Jeter (X - X - 11)
b2.new_ab()
b2.pitch_list("b c 1 1")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #46 Andy Pettitte
t3 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c c s")
t3.out("K")

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b f s")
t3.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB")
t3.advance(2, "34 WP")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab(is_risp=True)
t3.pitch_list("b f c d b")
t3.wp()
t3.out("F9")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 3. NYY #12 Alfonso Soriano (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F9")

# 4. NYY #24 Robinson Canó (X - X - X)
b3.new_ab()
b3.pitch_list("c c b f b f b f s")
b3.out("K")

# 5. NYY #13 Alex Rodriguez (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #46 Andy Pettitte
t4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("s b b s")
t4.hit(2)
t4.advance(3, "29 F9")
t4.advance(4, "7 G3")

# 6. BOS #29 Daniel Nava (X - 12 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c f b f f")
t4.out("F9")

# 7. BOS #7  Stephen Drew (12 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f")
t4.out("G3", rbis=1)

# 8. BOS #3  David Ross (X - X - X)
t4.new_ab()
t4.pitch_list("s c b b f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 6. NYY #22 Vernon Wells (X - X - X)
b4.new_ab()
b4.pitch_list("b s")
b4.out("(F)P2")

# 7. NYY #26 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b")
b4.out("F8")

# 8. NYY #39 Mark Reynolds (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.advance(2, "19 BB")
b4.advance(4, "11 3B")

# 9. NYY #19 Chris Stewart (X - X - 39)
b4.new_ab()
b4.pitch_list("b 1 b c b c b")
b4.reach("BB")
b4.advance(4, "11 3B")

# 1. NYY #11 Brett Gardner (X - 39 - 19)
b4.new_ab(is_risp=True)
b4.pitch_list("f b d c f")
b4.hit(3, rbis=2)

# Pitching change (BOS): #62 Rubby De La Rosa replaces #22 Felix Doubront
b4.pitching_substitution(62)

# 2. NYY #2  Derek Jeter (11 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #46 Andy Pettitte
t5 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c b f")
t5.hit(4)

# 1. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")

# 2. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")


# Bot 5th
# Pitching: BOS #62 Rubby De La Rosa
b5 = game.new_inning()

# 3. NYY #12 Alfonso Soriano (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 4. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.pitch_list("b f f b")
b5.hit(2)
b5.advance(3, "13 F8")
b5.advance(4, "22 1B")

# 5. NYY #13 Alex Rodriguez (X - 24 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d b d c")
b5.out("F8")

# 6. NYY #22 Vernon Wells (24 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d b c b")
b5.hit(1, rbis=1)
b5.advance(2, "26 1B")
b5.advance(4, "39 1B")

# 7. NYY #26 Eduardo Núñez (X - X - 22)
b5.new_ab()
b5.hit(1)
b5.advance(2, "39 1B")
b5.thrown_out(3, "39 9-3-5", 3, 62)

# 8. NYY #39 Mark Reynolds (X - 22 - 26)
b5.new_ab(is_risp=True)
b5.pitch_list("f f")
b5.hit(1, rbis=1)


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #46 Andy Pettitte
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b s f b")
t6.reach("BB")

# 6. BOS #29 Daniel Nava (X - X - 12)
t6.new_ab()
t6.pitch_list("c b s f s")
t6.out("K")

# 7. BOS #7  Stephen Drew (X - X - 12)
t6.new_ab()
t6.pitch_list("b c")
t6.out("(F)P3")


# Bot 6th
# Pitching: BOS #62 Rubby De La Rosa
b6 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 1. NYY #11 Brett Gardner (X - X - X)
b6.new_ab()
b6.out("G3-1")

# 2. NYY #2  Derek Jeter (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #65 Phil Hughes
t7 = game.new_inning()

# Pitching change (NYY): #65 Phil Hughes replaces #46 Andy Pettitte
t7.pitching_substitution(65)

# Defensive change (NYY): #31 Ichiro Suzuki replaces #22 Vernon Wells (RF), playing RF, batting 6th
t7.defensive_substitution(6, 31, "9")

# 8. BOS #3  David Ross (X - X - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.hit(1)
t7.advance(2, "18 1B")
t7.advance(3, "37 BB")
t7.advance(4, "15 1B")

# 9. BOS #16 Will Middlebrooks (X - X - 3)
t7.new_ab()
t7.pitch_list("c d f b f")
t7.out("F8")

# 1. BOS #18 Shane Victorino (X - X - 3)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "37 BB")
t7.advance(3, "15 1B")
t7.advance(4, "12 HR")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 2nd
t7.offensive_substitution(2, 37, "PH")

# 2. BOS #37 Mike Carp (X - 3 - 18)
t7.new_ab(is_risp=True)
t7.pitch_list("c c f b d b f f b")
t7.reach("BB")
t7.advance(2, "15 1B")
t7.advance(4, "12 HR")

# 3. BOS #15 Dustin Pedroia (3 - 18 - 37)
t7.new_ab(is_risp=True)
t7.pitch_list("c b f")
t7.hit(1, rbis=1)
t7.advance(4, "12 HR")

# Pitching change (NYY): #48 Boone Logan replaces #65 Phil Hughes
t7.pitching_substitution(48)

# 4. BOS #34 David Ortiz (18 - 37 - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("c s b b b c")
t7.out("!K")

# 5. BOS #12 Mike Napoli (18 - 37 - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("f b c b d f f")
t7.hit(4, rbis=4)

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b f b c b")
t7.hit(1)

# Pitching change (NYY): #38 Preston Claiborne replaces #48 Boone Logan
t7.pitching_substitution(38)

# 7. BOS #7  Stephen Drew (X - X - 29)
t7.new_ab()
t7.pitch_list("1 c 1 b f b d")
t7.out("F7")


# Bot 7th
# Pitching: BOS #67 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #62 Rubby De La Rosa
b7.pitching_substitution(67)

# Defensive switch (BOS): #37 Mike Carp moves to LF
b7.defensive_switch(37, "7")

# 3. NYY #12 Alfonso Soriano (X - X - X)
b7.new_ab()
b7.pitch_list("c s b s")
b7.out("K")

# 4. NYY #24 Robinson Canó (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 5. NYY #13 Alex Rodriguez (X - X - X)
b7.new_ab()
b7.pitch_list("s s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #38 Preston Claiborne
t8 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t8.new_ab()
t8.pitch_list("c l s")
t8.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(4, "18 HR")

# 1. BOS #18 Shane Victorino (X - X - 16)
t8.new_ab()
t8.pitch_list("c c d")
t8.hit(4, rbis=2)

# 2. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #37 Mike Carp
t8.offensive_substitution(2, 50, "PR")
t8.atbase("PR")
t8.advance(2, "15 G3")
t8.advance(3, "12 WP")
t8.advance(4, "29 BB")

# Pitching change (NYY): #62 Joba Chamberlain replaces #38 Preston Claiborne
t8.pitching_substitution(62)

# 3. BOS #15 Dustin Pedroia (X - X - 37)
t8.new_ab()
t8.pitch_list("1 c 1")
t8.out("G3")

# 4. BOS #34 David Ortiz (X - 50 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("i i i i")
t8.reach("IBB")
t8.advance(2, "12 WP")
t8.advance(3, "29 BB")
t8.advance(4, "7 1B")

# 5. BOS #12 Mike Napoli (X - 50 - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b d c d")
t8.wp()
t8.reach("BB")
t8.advance(2, "29 BB")
t8.advance(3, "7 1B")

# 6. BOS #29 Daniel Nava (50 - 34 - 12)
t8.new_ab(is_risp=True)
t8.pitch_list("d c c b d b")
t8.reach("BB", rbis=1)
t8.advance(2, "7 1B")

# 7. BOS #7  Stephen Drew (34 - 12 - 29)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.hit(1, rbis=1)

# 8. BOS #3  David Ross (12 - 29 - 7)
t8.new_ab(is_risp=True)
t8.pitch_list("b c f b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #67 Brandon Workman
b8 = game.new_inning()

# Defensive switch (BOS): #50 Quintin Berry moves to LF
b8.defensive_switch(50, "7")

# 6. NYY #31 Ichiro Suzuki (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f b")
b8.out("G6-3")

# 7. NYY #26 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(2, "19 BB")
b8.advance(3, "11 WP")

# Pitching change (BOS): #56 Franklin Morales replaces #67 Brandon Workman
b8.pitching_substitution(56)

# Offensive change (NYY): Pinch-hitter #55 Lyle Overbay replaces #39 Mark Reynolds, batting 8th
b8.offensive_substitution(8, 55, "PH")

# 8. NYY #55 Lyle Overbay (X - X - 26)
b8.new_ab()
b8.out("F7")

# 9. NYY #19 Chris Stewart (X - X - 26)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(2, "11 WP")

# 1. NYY #11 Brett Gardner (X - 26 - 19)
b8.new_ab(is_risp=True)
b8.pitch_list("c c d f b s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #40 Matt Daley
t9 = game.new_inning()

# Pitching change (NYY): #40 Matt Daley replaces #62 Joba Chamberlain
t9.pitching_substitution(40)

# Defensive switch (NYY): #55 Lyle Overbay moves to 1B
t9.defensive_switch(55, "3")

# Defensive change (NYY): #66 John Ryan Murphy replaces #19 Chris Stewart (C), playing C, batting 9th
t9.defensive_substitution(9, 66, "2")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# 1. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.reach("HBP")
t9.advance(3, "15 2B")

# 2. BOS #50 Quintin Berry (X - X - 18)
t9.new_ab()
t9.pitch_list("b b f f c")
t9.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t9.new_ab()
t9.pitch_list("c s 1 f b b f f f")
t9.hit(2)

# 4. BOS #34 David Ortiz (18 - 15 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b b")
t9.out("G3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #56 Franklin Morales
b9.pitching_substitution(19)

# 2. NYY #2  Derek Jeter (X - X - X)
b9.new_ab()
b9.pitch_list("s f")
b9.out("G4-3")

# 3. NYY #12 Alfonso Soriano (X - X - X)
b9.new_ab()
b9.pitch_list("c b s f f s")
b9.out("K")

# 4. NYY #24 Robinson Canó (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67, is_away_team=True)

# Loser team: NYY
# LP: NYY #38 Preston Claiborne
game.losing_pitcher(38)

# print(game)
game.generate_scorecard()
