import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-09-13
# https://www.baseball-reference.com/boxes/BOS/BOS201309130.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/09/13/348941/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-13 19:10-22:16",
        "at": "Fenway Park, Boston, MA",
        "att": "37,542",
        "temp": "67F, Cloudy",
        "wind": "8mph, In From LF",
        "away": {
            "team": "New York Yankees",
            "starter": 18,
            "roster": {
                # Lineup
                14: "Curtis Granderson",
                13: "Alex Rodriguez",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                55: "Lyle Overbay",
                26: "Eduardo Núñez",
                31: "Ichiro Suzuki",
                35: "Brendan Ryan",
                19: "Chris Stewart",
                # Starting pitcher
                18: "Hiroki Kuroda",
                # Bench
                22: "Vernon Wells",
                39: "Mark Reynolds",
                53: "Austin Romine",
                63: "Zoilo Almonte",
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
                43: "Adam Warren",
                64: "Cesar Cabral",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                70: "Brett Marshall",
                62: "Joba Chamberlain",
                67: "Mike Zagurski",
                30: "David Robertson",
                40: "Matt Daley",
            },
            "lefties": [52, 48, 60, 64, 46, 67],
            "lineup": [
                [14, "8"],
                [13, "0"],
                [24, "4"],
                [12, "7"],
                [55, "3"],
                [26, "5"],
                [31, "9"],
                [35, "6"],
                [19, "2"],
            ],
            "bench": [
                [22, "CF"],
                [39, "3B"],
                [53, "C"],
                [63, "LF"],
                [11, "LF"],
                [45, "3B"],
                [66, "C"],
            ],
            "bullpen": [61, 65, 27, 47, 52, 38, 48, 60, 43, 64, 42, 46, 70, 62, 67, 30, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                37: "Mike Carp",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
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
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [18, "9"],
                [34, "0"],
                [37, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Ted Barrett",
            "1B": "Mike DiMuro",
            "2B": "Ron Kulpa",
            "3B": "Alfonso Márquez",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. NYY #14 Curtis Granderson (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("P5")

# 2. NYY #13 Alex Rodriguez (X - X - X)
t1.new_ab()
t1.pitch_list("c b s b b s")
t1.out("K")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(2)

# 4. NYY #12 Alfonso Soriano (X - 24 - X)
t1.new_ab()
t1.pitch_list("f s b s")
t1.out("K")


# Bot 1st
# Pitching: NYY #18 Hiroki Kuroda
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.hit(1)
b1.advance(3, "34 2B")
b1.advance(4, "37 G3")

# 2. BOS #18 Shane Victorino (X - X - 15)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 3. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("b c d 1 c")
b1.hit(2)
b1.advance(3, "37 G3")
b1.advance(4, "29 1B")

# 4. BOS #37 Mike Carp (15 - 34 - X)
b1.new_ab()
b1.pitch_list("b b f")
b1.out("G3", rbis=1)

# 5. BOS #29 Daniel Nava (34 - X - X)
b1.new_ab()
b1.pitch_list("b d b c")
b1.hit(1, rbis=1)
b1.advance(2, "39 BB")
b1.advance(4, "7 2B")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(4, "7 2B")

# 7. BOS #7  Stephen Drew (X - 29 - 39)
b1.new_ab()
b1.pitch_list("b b c c d")
b1.hit(2, rbis=2)

# 8. BOS #16 Will Middlebrooks (X - 7 - X)
b1.new_ab()
b1.pitch_list("b s c")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 5. NYY #55 Lyle Overbay (X - X - X)
t2.new_ab()
t2.pitch_list("c f f")
t2.out("G4-3")

# 6. NYY #26 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G1-3")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
t2.new_ab()
t2.out("L7")


# Bot 2nd
# Pitching: NYY #18 Hiroki Kuroda
b2 = game.new_inning()

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G3")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.advance(2, "18 HBP")
b2.advance(3, "34 PB")

# 2. BOS #18 Shane Victorino (X - X - 15)
b2.new_ab()
b2.pitch_list("c")
b2.reach("HBP")
b2.advance(2, "34 PB")

# 3. BOS #34 David Ortiz (X - 15 - 18)
b2.new_ab()
b2.pitch_list("s i i i i")
b2.pb()
b2.reach("IBB")

# 4. BOS #37 Mike Carp (15 - 18 - 34)
b2.new_ab()
b2.pitch_list("c f b d c")
b2.out("!K")

# 5. BOS #29 Daniel Nava (15 - 18 - 34)
b2.new_ab()
b2.pitch_list("c")
b2.out("L7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 8. NYY #35 Brendan Ryan (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b c")
t3.hit(4)

# 9. NYY #19 Chris Stewart (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("P4")

# 1. NYY #14 Curtis Granderson (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("B1-3")

# 2. NYY #13 Alex Rodriguez (X - X - X)
t3.new_ab()
t3.pitch_list("b f b s b c")
t3.out("!K")


# Bot 3rd
# Pitching: NYY #18 Hiroki Kuroda
b3 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(2)
b3.advance(3, "7 F8")

# 7. BOS #7  Stephen Drew (X - 39 - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")

# 8. BOS #16 Will Middlebrooks (39 - X - X)
b3.new_ab()
b3.pitch_list("b b s d c s")
b3.out("K")

# 9. BOS #25 Jackie Bradley Jr. (39 - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t4.new_ab()
t4.hit(1)
t4.error(4)
t4.advance(2, "55 E4")
t4.advance(3, "26 F8")

# 4. NYY #12 Alfonso Soriano (X - X - 24)
t4.new_ab()
t4.pitch_list("s")
t4.out("F8")

# 5. NYY #55 Lyle Overbay (X - X - 24)
t4.new_ab()
t4.pitch_list("b")
t4.reach("FC4")

# 6. NYY #26 Eduardo Núñez (X - 24 - 55)
t4.new_ab()
t4.pitch_list("f")
t4.out("F8")

# 7. NYY #31 Ichiro Suzuki (24 - X - 55)
t4.new_ab()
t4.pitch_list("c b c")
t4.out("G4-3")


# Bot 4th
# Pitching: NYY #18 Hiroki Kuroda
b4 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f")
b4.out("G6-3")

# 3. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 8. NYY #35 Brendan Ryan (X - X - X)
t5.new_ab()
t5.out("F9")

# 9. NYY #19 Chris Stewart (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G1-3")

# 1. NYY #14 Curtis Granderson (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b f f")
t5.out("F8")


# Bot 5th
# Pitching: NYY #18 Hiroki Kuroda
b5 = game.new_inning()

# 4. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.out("G6-3")

# 5. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1)
b5.thrown_out(2, "7 FC6-4", 3, 18)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b5.new_ab()
b5.pitch_list("d")
b5.out("F9")

# 7. BOS #7  Stephen Drew (X - X - 29)
b5.new_ab()
b5.pitch_list("c 1 d b b")
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 2. NYY #13 Alex Rodriguez (X - X - X)
t6.new_ab()
t6.pitch_list("s")
t6.out("F8")

# 3. NYY #24 Robinson Canó (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.hit(2)
t6.advance(3, "12 1B")
t6.advance(4, "55 SF9")

# 4. NYY #12 Alfonso Soriano (X - 24 - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.hit(1)
t6.advance(2, "26 SB")

# 5. NYY #55 Lyle Overbay (24 - X - 12)
t6.new_ab()
t6.out("SF9", rbis=1)

# 6. NYY #26 Eduardo Núñez (X - X - 12)
t6.new_ab()
t6.pitch_list("1 c c b b f")
t6.out("F8")


# Bot 6th
# Pitching: NYY #18 Hiroki Kuroda
b6 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.out("P4")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("c b c")
b6.out("G3-1")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.out("G3-1")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 7. NYY #31 Ichiro Suzuki (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3-1")

# 8. NYY #35 Brendan Ryan (X - X - X)
t7.new_ab()
t7.pitch_list("c s b")
t7.hit(1)
t7.advance(3, "19 1B")
t7.advance(4, "24 2B")

# 9. NYY #19 Chris Stewart (X - X - 35)
t7.new_ab()
t7.hit(1)
t7.advance(2, "13 BB")
t7.advance(4, "24 2B")

# Pitching change (BOS): #32 Craig Breslow replaces #41 John Lackey
t7.pitching_substitution(32)

# 1. NYY #14 Curtis Granderson (35 - X - 19)
t7.new_ab()
t7.pitch_list("b b b c f f s")
t7.out("K")

# 2. NYY #13 Alex Rodriguez (35 - X - 19)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(3, "24 2B")

# 3. NYY #24 Robinson Canó (35 - 19 - 13)
t7.new_ab()
t7.pitch_list("c b d")
t7.hit(2, rbis=2)

# Pitching change (BOS): #67 Brandon Workman replaces #32 Craig Breslow
t7.pitching_substitution(67)

# 4. NYY #12 Alfonso Soriano (13 - 24 - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.out("G5-3")


# Bot 7th
# Pitching: NYY #18 Hiroki Kuroda
b7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.hit(1)
b7.advance(2, "34 HBP")
b7.advance(3, "5 BB")
b7.advance(4, "39 HR")

# Pitching change (NYY): #64 Cesar Cabral replaces #18 Hiroki Kuroda
b7.pitching_substitution(64)

# 3. BOS #34 David Ortiz (X - X - 18)
b7.new_ab()
b7.pitch_list("c")
b7.reach("HBP")
b7.advance(2, "5 BB")
b7.advance(4, "39 HR")

# Pitching change (NYY): #38 Preston Claiborne replaces #64 Cesar Cabral
b7.pitching_substitution(38)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 4th
b7.offensive_substitution(4, 5, "PH")

# 4. BOS #5  Jonny Gomes (X - 18 - 34)
b7.new_ab()
b7.pitch_list("c b b d b")
b7.reach("BB")
b7.advance(4, "39 HR")

# 5. BOS #29 Daniel Nava (18 - 34 - 5)
b7.new_ab()
b7.pitch_list("f b d s s")
b7.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (18 - 34 - 5)
b7.new_ab()
b7.pitch_list("c")
b7.hit(4, rbis=4)

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(2)

# 8. BOS #16 Will Middlebrooks (X - 7 - X)
b7.new_ab()
b7.pitch_list("b c c d")
b7.out("P3")

# 9. BOS #25 Jackie Bradley Jr. (X - 7 - X)
b7.new_ab()
b7.pitch_list("c s d s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #67 Brandon Workman
t8.pitching_substitution(36)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
t8.defensive_switch(29, "3")

# 5. NYY #55 Lyle Overbay (X - X - X)
t8.new_ab()
t8.pitch_list("s")
t8.out("L5")

# 6. NYY #26 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("s f f f f")
t8.out("F8")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F9")


# Bot 8th
# Pitching: NYY #40 Matt Daley
b8 = game.new_inning()

# Pitching change (NYY): #40 Matt Daley replaces #38 Preston Claiborne
b8.pitching_substitution(40)

# 1. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b c f b b")
b8.hit(2)

# 4. BOS #5  Jonny Gomes (X - 34 - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# Defensive change (BOS): #12 Mike Napoli replaces #29 Daniel Nava (LF), playing 1B, batting 5th
t9.defensive_substitution(5, 12, "3")

# 8. NYY #35 Brendan Ryan (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("(F)P5")

# Offensive change (NYY): Pinch-hitter #22 Vernon Wells replaces #19 Chris Stewart, batting 9th
t9.offensive_substitution(9, 22, "PH")

# 9. NYY #22 Vernon Wells (X - X - X)
t9.new_ab()
t9.pitch_list("s f")
t9.out("F7")

# 1. NYY #14 Curtis Granderson (X - X - X)
t9.new_ab()
t9.pitch_list("s s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67)

# Loser team: NYY
# LP: NYY #18 Hiroki Kuroda
game.losing_pitcher(18, is_away_team=True)

# print(game)
game.generate_scorecard()
