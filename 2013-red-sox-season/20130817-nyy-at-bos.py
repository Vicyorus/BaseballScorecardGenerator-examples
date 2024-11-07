import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-08-17
# https://www.baseball-reference.com/boxes/BOS/BOS201308170.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/08/17/348576/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-17 16:07-19:33",
        "at": "Fenway Park, Boston, MA",
        "att": "37,517",
        "temp": "72F, Partly Cloudy",
        "wind": "11mph, R To L",
        "away": {
            "team": "New York Yankees",
            "starter": 18,
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
                18: "Hiroki Kuroda",
                # Bench
                22: "Vernon Wells",
                39: "Mark Reynolds",
                53: "Austin Romine",
                17: "Jayson Nix",
                # Bullpen
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
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
            "bullpen": [65, 27, 47, 52, 48, 60, 43, 42, 46, 62, 30],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                29: "Daniel Nava",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                26: "Brock Holt",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                # Bullpen
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
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [29, "7"],
                [7, "6"],
                [39, "2"],
                [16, "5"],
            ],
            "bench": [
                [26, "2B"],
                [5, "LF"],
                [12, "1B"],
                [20, "C"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 19, 62, 22, 46],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Brian O'Nora",
            "2B": "Fieldin Culbreth",
            "3B": "Bill Welke",
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

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b f")
t1.out("G1-3")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t1.new_ab()
t1.pitch_list("b f b c f b f")
t1.out("G1-3")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.out("G4-3")


# Bot 1st
# Pitching: NYY #18 Hiroki Kuroda
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.hit(1)

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("b f s s")
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("1 1 c f d s")
b1.out("K")

# 4. BOS #34 David Ortiz (X - X - 2)
b1.new_ab()
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "13 SB")
t2.thrown_out(2, "14 DP6-4", 2, 41)

# 5. NYY #13 Alex Rodriguez (X - X - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c b c 2 d 2 d b")
t2.reach("BB")
t2.advance(2, "26 BB")
t2.advance(3, "55 1B")

# 6. NYY #14 Curtis Granderson (X - 12 - 13)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("DP6-4")

# 7. NYY #26 Eduardo Núñez (X - X - 13)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "55 1B")

# 8. NYY #55 Lyle Overbay (X - 13 - 26)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.hit(1)

# 9. NYY #19 Chris Stewart (13 - 26 - 55)
t2.new_ab(is_risp=True)
t2.pitch_list("c f")
t2.out("F8")


# Bot 2nd
# Pitching: NYY #18 Hiroki Kuroda
b2 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("G3-1")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b c b")
b2.hit(2)
b2.advance(3, "7 F9")

# 7. BOS #7  Stephen Drew (X - 29 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b")
b2.out("F9")

# 8. BOS #39 Jarrod Saltalamacchia (29 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G3")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")

# 3. NYY #24 Robinson Canó (X - X - X)
t3.new_ab()
t3.pitch_list("b c s f")
t3.out("G1-3")


# Bot 3rd
# Pitching: NYY #18 Hiroki Kuroda
b3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.thrown_out(2, "2 DP4-3", 1, 18)

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b3.new_ab()
b3.pitch_list("b b f f")
b3.out("DP4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b c t f b")
b3.hit(1)
b3.thrown_out(2, "15 FC4", 3, 18)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.reach("FC4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.hit(1)
t4.thrown_out(2, "13 CS", 1, 41)

# 5. NYY #13 Alex Rodriguez (X - X - 12)
t4.new_ab()
t4.pitch_list("c b f b c")
t4.out("!K")

# 6. NYY #14 Curtis Granderson (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "26 SB")

# 7. NYY #26 Eduardo Núñez (X - X - 14)
t4.new_ab(is_risp=True)
t4.pitch_list("1 b c b")
t4.out("G1-3")


# Bot 4th
# Pitching: NYY #18 Hiroki Kuroda
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b b c c b f")
b4.hit(2)
b4.advance(3, "37 1B")
b4.advance(4, "7 E3")

# 5. BOS #37 Mike Carp (X - 34 - X)
b4.new_ab(is_risp=True)
b4.hit(1)
b4.advance(2, "7 E3")
b4.advance(3, "39 SB")
b4.advance("U", "16 1B")

# 6. BOS #29 Daniel Nava (34 - X - 37)
b4.new_ab(is_risp=True)
b4.pitch_list("c f b b c")
b4.out("!K")

# 7. BOS #7  Stephen Drew (34 - X - 37)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b 1 f b")
b4.error(3)
b4.reach("E3", rbis=1)
b4.advance(2, "39 SB")
b4.advance(3, "16 1B")
b4.advance("U", "2 1B")

# 8. BOS #39 Jarrod Saltalamacchia (X - 37 - 7)
b4.new_ab(is_risp=True)
b4.pitch_list("b t f b s")
b4.out("K")

# 9. BOS #16 Will Middlebrooks (37 - 7 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b f s f b")
b4.hit(1, rbis=1)
b4.advance(2, "2 1B")
b4.thrown_out(3, "18 FC5", 3, 18)

# 1. BOS #2  Jacoby Ellsbury (7 - X - 16)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)
b4.advance(2, "18 FC5")

# 2. BOS #18 Shane Victorino (X - 16 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("c b f b")
b4.reach("FC5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 8. NYY #55 Lyle Overbay (X - X - X)
t5.new_ab()
t5.pitch_list("b c c b")
t5.hit(1)
t5.advance(3, "19 2B")
t5.advance(4, "31 G4-3")

# 9. NYY #19 Chris Stewart (X - X - 55)
t5.new_ab()
t5.hit(2)
t5.advance(3, "31 G4-3")

# 1. NYY #11 Brett Gardner (55 - 19 - X)
t5.new_ab(is_risp=True)
t5.out("G1-3")

# 2. NYY #31 Ichiro Suzuki (55 - 19 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b f d")
t5.out("G4-3", rbis=1)

# 3. NYY #24 Robinson Canó (19 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("f f f f")
t5.out("G4-3")


# Bot 5th
# Pitching: NYY #18 Hiroki Kuroda
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("L4")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f t")
b5.out("KT")

# 5. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
t6.new_ab()
t6.pitch_list("f b")
t6.out("G5-3")

# 5. NYY #13 Alex Rodriguez (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b b")
t6.out("G4-3")

# 6. NYY #14 Curtis Granderson (X - X - X)
t6.new_ab()
t6.pitch_list("b b c s f")
t6.out("G4-3")


# Bot 6th
# Pitching: NYY #18 Hiroki Kuroda
b6 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.advance(3, "7 G4-3")
b6.advance(4, "39 1B")

# 7. BOS #7  Stephen Drew (X - 29 - X)
b6.new_ab(is_risp=True)
b6.out("G4-3")

# 8. BOS #39 Jarrod Saltalamacchia (29 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b d f f f f f b")
b6.hit(1, rbis=1)
b6.advance(4, "2 E4")

# 9. BOS #16 Will Middlebrooks (X - X - 39)
b6.new_ab()
b6.pitch_list("b c s c")
b6.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(2, rbis=1)
b6.error(4)
b6.advance(3, "E4")

# Pitching change (NYY): #43 Adam Warren replaces #18 Hiroki Kuroda
b6.pitching_substitution(43)

# 2. BOS #18 Shane Victorino (2 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c c")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 7. NYY #26 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b f b")
t7.reach("BB")
t7.thrown_out(2, "55 DP4-6-3", 1, 41)

# 8. NYY #55 Lyle Overbay (X - X - 26)
t7.new_ab()
t7.pitch_list("s")
t7.out("DP4-6-3")

# 9. NYY #19 Chris Stewart (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b b")
t7.reach("HBP")
t7.advance(2, "22 1B")

# Pitching change (BOS): #32 Craig Breslow replaces #41 John Lackey
t7.pitching_substitution(32)

# Offensive change (NYY): Pinch-hitter #22 Vernon Wells replaces #11 Brett Gardner, batting 1st
t7.offensive_substitution(1, 22, "PH")

# 1. NYY #22 Vernon Wells (X - X - 19)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(1)

# 2. NYY #31 Ichiro Suzuki (X - 19 - 22)
t7.new_ab(is_risp=True)
t7.pitch_list("b c c")
t7.out("G3")


# Bot 7th
# Pitching: NYY #43 Adam Warren
b7 = game.new_inning()

# Defensive switch (NYY): #22 Vernon Wells moves to RF
b7.defensive_switch(22, "9")

# Defensive switch (NYY): #31 Ichiro Suzuki moves to CF
b7.defensive_switch(31, "8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c b t")
b7.out("P3")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b b")
b7.hit(4)

# 5. BOS #37 Mike Carp (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(2)

# 6. BOS #29 Daniel Nava (X - 37 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d b b d")
b7.reach("BB")

# 7. BOS #7  Stephen Drew (X - 37 - 29)
b7.new_ab(is_risp=True)
b7.pitch_list("c b")
b7.out("F9")

# 8. BOS #39 Jarrod Saltalamacchia (X - 37 - 29)
b7.new_ab(is_risp=True)
b7.pitch_list("c f")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b")
t8.out("G4-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t8.pitching_substitution(36)

# 4. NYY #12 Alfonso Soriano (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f f b f f s")
t8.out("K")

# 5. NYY #13 Alex Rodriguez (X - X - X)
t8.new_ab()
t8.pitch_list("b f f")
t8.out("F9")


# Bot 8th
# Pitching: NYY #43 Adam Warren
b8 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("b c f b b d")
b8.reach("BB")
b8.advance(2, "18 1B")
b8.advance(3, "34 BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b8.new_ab()
b8.pitch_list("c b f d s")
b8.out("K")

# 2. BOS #18 Shane Victorino (X - X - 16)
b8.new_ab()
b8.pitch_list("c b s")
b8.hit(1)
b8.advance(2, "34 BB")

# 3. BOS #15 Dustin Pedroia (X - 16 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b f c f b f b f s")
b8.out("K")

# 4. BOS #34 David Ortiz (X - 16 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b c f f b")
b8.reach("BB")
b8.thrown_out(2, "37 FC6", 3, 48)

# Pitching change (NYY): #48 Boone Logan replaces #43 Adam Warren
b8.pitching_substitution(48)

# 5. BOS #37 Mike Carp (16 - 18 - 34)
b8.new_ab(is_risp=True)
b8.pitch_list("c")
b8.reach("FC6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# Defensive change (BOS): #26 Brock Holt replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
t9.defensive_substitution(3, 26, "4")

# 6. NYY #14 Curtis Granderson (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 7. NYY #26 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("f b s b f f t")
t9.out("KT")

# 8. NYY #55 Lyle Overbay (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2)

# 9. NYY #19 Chris Stewart (X - 55 - X)
t9.new_ab(is_risp=True)
t9.out("P5")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)

# Loser team: NYY
# LP: NYY #18 Hiroki Kuroda
game.losing_pitcher(18, is_away_team=True)

# print(game)
game.generate_scorecard()
