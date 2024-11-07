import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-09-15
# https://www.baseball-reference.com/boxes/BOS/BOS201309150.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/09/15/348971/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-15 20:13-23:26",
        "at": "Fenway Park, Boston, MA",
        "att": "37,137",
        "temp": "69F, Cloudy",
        "wind": "6mph, In From LF",
        "away": {
            "team": "New York Yankees",
            "starter": 47,
            "roster": {
                # Lineup
                14: "Curtis Granderson",
                13: "Alex Rodriguez",
                24: "Robinson Canó",
                12: "Alfonso Soriano",
                55: "Lyle Overbay",
                39: "Mark Reynolds",
                31: "Ichiro Suzuki",
                35: "Brendan Ryan",
                19: "Chris Stewart",
                # Starting pitcher
                47: "Iván Nova",
                # Bench
                22: "Vernon Wells",
                26: "Eduardo Núñez",
                53: "Austin Romine",
                63: "Zoilo Almonte",
                11: "Brett Gardner",
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
                41: "David Phelps",
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
                [39, "5"],
                [31, "9"],
                [35, "6"],
                [19, "2"],
            ],
            "bench": [
                [22, "CF"],
                [26, "SS"],
                [53, "C"],
                [63, "LF"],
                [11, "LF"],
                [45, "3B"],
                [66, "C"],
            ],
            "bullpen": [61, 18, 65, 27, 52, 38, 48, 60, 41, 43, 64, 42, 46, 70, 62, 67, 30, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                29: "Daniel Nava",
                34: "David Ortiz",
                37: "Mike Carp",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                5: "Jonny Gomes",
                3: "David Ross",
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
                [29, "9"],
                [34, "0"],
                [37, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [72, "5"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [16, "3B"],
                [18, "CF"],
                [5, "LF"],
                [3, "C"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Ron Kulpa",
            "1B": "Alfonso Márquez",
            "2B": "Ted Barrett",
            "3B": "Mike DiMuro",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. NYY #14 Curtis Granderson (X - X - X)
t1.new_ab()
t1.pitch_list("b f b f f b d")
t1.reach("BB")
t1.error(1)
t1.advance(3, "13 POE1")
t1.advance("U", "13 G6-3")

# 2. NYY #13 Alex Rodriguez (X - X - 14)
t1.new_ab(is_risp=True)
t1.pitch_list("1 c")
t1.out("G6-3", rbis=1)

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("s b b f")
t1.out("L7")

# 4. NYY #12 Alfonso Soriano (X - X - X)
t1.new_ab()
t1.pitch_list("c b b s")
t1.hit(1)

# 5. NYY #55 Lyle Overbay (X - X - 12)
t1.new_ab()
t1.pitch_list("1 f 1 f")
t1.out("L6")


# Bot 1st
# Pitching: NYY #47 Iván Nova
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f d")
b1.out("G5-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c b c")
b1.hit(2)
b1.advance(4, "34 1B")

# 3. BOS #34 David Ortiz (X - 29 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1, rbis=1)
b1.advance(2, "12 WP")
b1.advance(4, "12 HR")

# 4. BOS #37 Mike Carp (X - X - 34)
b1.new_ab()
b1.pitch_list("f b b f")
b1.out("F8")

# 5. BOS #12 Mike Napoli (X - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("d b")
b1.wp()
b1.hit(4, rbis=2)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b1.new_ab()
b1.pitch_list("b f b b")
b1.hit(1)

# 7. BOS #7  Stephen Drew (X - X - 39)
b1.new_ab()
b1.pitch_list("d f b b")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 6. NYY #39 Mark Reynolds (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f")
t2.out("G4-3")

# 8. NYY #35 Brendan Ryan (X - X - X)
t2.new_ab()
t2.pitch_list("t")
t2.out("F9")


# Bot 2nd
# Pitching: NYY #47 Iván Nova
b2 = game.new_inning()

# 8. BOS #72 Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c f d s")
b2.out("K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c f b s")
b2.out("K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b2.new_ab()
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 9. NYY #19 Chris Stewart (X - X - X)
t3.new_ab()
t3.pitch_list("c s b d b")
t3.reach("HBP")
t3.advance(2, "13 1B")

# 1. NYY #14 Curtis Granderson (X - X - 19)
t3.new_ab()
t3.pitch_list("b c 1 b f b s")
t3.out("K")

# 2. NYY #13 Alex Rodriguez (X - X - 19)
t3.new_ab()
t3.pitch_list("s d b")
t3.hit(1)
t3.thrown_out(2, "24 DP4-6-3", 2, 11)

# 3. NYY #24 Robinson Canó (X - 19 - 13)
t3.new_ab(is_risp=True)
t3.out("DP4-6-3")


# Bot 3rd
# Pitching: NYY #47 Iván Nova
b3 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.thrown_out(2, "34 DP6-5-3", 1, 47)

# 3. BOS #34 David Ortiz (X - X - 29)
b3.new_ab()
b3.pitch_list("b b c d")
b3.out("DP6-5-3")

# 4. BOS #37 Mike Carp (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 4. NYY #12 Alfonso Soriano (X - X - X)
t4.new_ab()
t4.pitch_list("b s b s f b f b")
t4.reach("BB")
t4.thrown_out(2, "55 DP6-3", 1, 11)

# 5. NYY #55 Lyle Overbay (X - X - 12)
t4.new_ab()
t4.out("DP6-3")

# 6. NYY #39 Mark Reynolds (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b s b")
t4.reach("BB")
t4.thrown_out(2, "31 FC6-4", 3, 11)

# 7. NYY #31 Ichiro Suzuki (X - X - 39)
t4.new_ab()
t4.pitch_list("d b")
t4.reach("FC6-4")


# Bot 4th
# Pitching: NYY #47 Iván Nova
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b b")
b4.reach("BB")
b4.thrown_out(2, "39 FC4-5", 1, 47)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b4.new_ab()
b4.pitch_list("c c")
b4.reach("FC4-5")
b4.advance(2, "7 PB")
b4.advance(3, "7 G6-3")
b4.advance("U", "25 SB")

# 7. BOS #7  Stephen Drew (X - X - 39)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.pb()
b4.out("G6-3")

# 8. BOS #72 Xander Bogaerts (39 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b c b b b")
b4.reach("BB")
b4.advance(2, "25 SB")

# 9. BOS #25 Jackie Bradley Jr. (39 - X - 72)
b4.new_ab(is_risp=True)
b4.pitch_list("b f 1 b 1 b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 8. NYY #35 Brendan Ryan (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b c b")
t5.reach("BB")
t5.advance(2, "14 WP")

# 9. NYY #19 Chris Stewart (X - X - 35)
t5.new_ab()
t5.pitch_list("c c")
t5.out("F7")

# 1. NYY #14 Curtis Granderson (X - X - 35)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b s")
t5.wp()
t5.out("K")

# Offensive change (NYY): Pinch-hitter #22 Vernon Wells replaces #13 Alex Rodriguez, batting 2nd
t5.offensive_substitution(2, 22, "PH")

# 2. NYY #22 Vernon Wells (X - 35 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d")
t5.out("G5-3")


# Bot 5th
# Pitching: NYY #47 Iván Nova
b5 = game.new_inning()

# Defensive switch (NYY): #22 Vernon Wells moves to DH
b5.defensive_switch(22, "0")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b b")
b5.reach("BB")
b5.advance(3, "29 2B")
b5.advance(4, "37 HBP")

# 2. BOS #29 Daniel Nava (X - X - 15)
b5.new_ab()
b5.pitch_list("1 c b b 1 c f b")
b5.hit(2)
b5.advance(3, "37 HBP")

# 3. BOS #34 David Ortiz (15 - 29 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("i i i i")
b5.reach("IBB")
b5.advance(2, "37 HBP")

# 4. BOS #37 Mike Carp (15 - 29 - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("c s")
b5.reach("HBP", rbis=1)

# Pitching change (NYY): #43 Adam Warren replaces #47 Iván Nova
b5.pitching_substitution(43)

# 5. BOS #12 Mike Napoli (29 - 34 - 37)
b5.new_ab(is_risp=True)
b5.pitch_list("c c s")
b5.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (29 - 34 - 37)
b5.new_ab(is_risp=True)
b5.pitch_list("c b c b s")
b5.out("K")

# 7. BOS #7  Stephen Drew (29 - 34 - 37)
b5.new_ab(is_risp=True)
b5.pitch_list("c s d")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("F7")

# 4. NYY #12 Alfonso Soriano (X - X - X)
t6.new_ab()
t6.pitch_list("b s f s")
t6.out("K")

# 5. NYY #55 Lyle Overbay (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("G3-1")


# Bot 6th
# Pitching: NYY #43 Adam Warren
b6 = game.new_inning()

# 8. BOS #72 Xander Bogaerts (X - X - X)
b6.new_ab()
b6.hit(2)
b6.advance(4, "29 1B")

# 9. BOS #25 Jackie Bradley Jr. (X - 72 - X)
b6.new_ab(is_risp=True)
b6.out("G6-3")

# 1. BOS #15 Dustin Pedroia (X - 72 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b d d b")
b6.reach("BB")
b6.advance(2, "29 1B")
b6.advance(3, "34 WP")
b6.advance(4, "34 1B")

# 2. BOS #29 Daniel Nava (X - 72 - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.hit(1, rbis=1)
b6.advance(2, "34 WP")
b6.advance(3, "34 1B")

# Pitching change (NYY): #64 Cesar Cabral replaces #43 Adam Warren
b6.pitching_substitution(64)

# 3. BOS #34 David Ortiz (X - 15 - 29)
b6.new_ab(is_risp=True)
b6.pitch_list("b c")
b6.wp()
b6.hit(1, rbis=1)

# Pitching change (NYY): #62 Joba Chamberlain replaces #64 Cesar Cabral
b6.pitching_substitution(62)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 4th
b6.offensive_substitution(4, 5, "PH")

# 4. BOS #5  Jonny Gomes (29 - X - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("c d c")
b6.out("F9")

# 5. BOS #12 Mike Napoli (29 - X - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("s f b b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #38 Matt Thornton
t7 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #11 Clay Buchholz
t7.pitching_substitution(38)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t7.defensive_switch(5, "7")

# Defensive change (BOS): #23 Brandon Snyder replaces #12 Mike Napoli (1B), playing 1B, batting 5th
t7.defensive_substitution(5, 23, "3")

# 6. NYY #39 Mark Reynolds (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b f f c")
t7.out("!K")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "35 1B")

# 8. NYY #35 Brendan Ryan (X - X - 31)
t7.new_ab()
t7.hit(1)
t7.thrown_out(2, "19 DP5-4-3", 2, 38)

# 9. NYY #19 Chris Stewart (X - 31 - 35)
t7.new_ab(is_risp=True)
t7.pitch_list("c c b")
t7.out("DP5-4-3")


# Bot 7th
# Pitching: NYY #62 Joba Chamberlain
b7 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.out("G6-3")

# Pitching change (NYY): #67 Mike Zagurski replaces #62 Joba Chamberlain
b7.pitching_substitution(67)

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")

# 8. BOS #72 Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b c")
b7.hit(1)
b7.advance(2, "25 HBP")
b7.advance(4, "15 2B")

# 9. BOS #25 Jackie Bradley Jr. (X - X - 72)
b7.new_ab()
b7.pitch_list("b")
b7.reach("HBP")
b7.advance(4, "15 2B")

# Pitching change (NYY): #41 David Phelps replaces #67 Mike Zagurski
b7.pitching_substitution(41)

# 1. BOS #15 Dustin Pedroia (X - 72 - 25)
b7.new_ab(is_risp=True)
b7.pitch_list("b c b b f f")
b7.hit(2, rbis=2)

# 2. BOS #29 Daniel Nava (X - 15 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #38 Matt Thornton
t8.pitching_substitution(32)

# Defensive change (BOS): #10 John McDonald replaces #15 Dustin Pedroia (2B), playing 2B, batting 1st
t8.defensive_substitution(1, 10, "4")

# 1. NYY #14 Curtis Granderson (X - X - X)
t8.new_ab()
t8.pitch_list("b b c s f s")
t8.out("K")

# 2. NYY #22 Vernon Wells (X - X - X)
t8.new_ab()
t8.pitch_list("c f b t")
t8.out("KT")

# 3. NYY #24 Robinson Canó (X - X - X)
t8.new_ab()
t8.pitch_list("c f")
t8.out("L5")


# Bot 8th
# Pitching: NYY #61 Dellin Betances
b8 = game.new_inning()

# Pitching change (NYY): #61 Dellin Betances replaces #41 David Phelps
b8.pitching_substitution(61)

# Defensive change (NYY): #26 Eduardo Núñez replaces #12 Alfonso Soriano (LF), playing 2B, batting 4th
b8.defensive_substitution(4, 26, "4")

# Defensive change (NYY): #63 Zoilo Almonte replaces #24 Robinson Canó (2B), playing LF, batting 3rd
b8.defensive_substitution(3, 63, "7")

# Defensive change (NYY): #66 John Ryan Murphy replaces #19 Chris Stewart (C), playing C, batting 9th
b8.defensive_substitution(9, 66, "2")

# 3. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f b s")
b8.out("K")

# 4. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c c b c")
b8.out("!K")

# 5. BOS #23 Brandon Snyder (X - X - X)
b8.new_ab()
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #64 Allen Webster
t9 = game.new_inning()

# Pitching change (BOS): #64 Allen Webster replaces #32 Craig Breslow
t9.pitching_substitution(64)

# 4. NYY #26 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("f b f")
t9.out("G4-3")

# 5. NYY #55 Lyle Overbay (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b b")
t9.reach("BB")
t9.thrown_out(2, "39 FC5-4", 2, 64)

# 6. NYY #39 Mark Reynolds (X - X - 55)
t9.new_ab()
t9.pitch_list("s")
t9.reach("FC5-4")
t9.advance(2, "31 DI")
t9.advance(4, "31 1B")

# 7. NYY #31 Ichiro Suzuki (X - X - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("c b")
t9.hit(1, rbis=1)
t9.advance(2, "35 DI")

# 8. NYY #35 Brendan Ryan (X - X - 31)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("P4")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)

# Loser team: NYY
# LP: NYY #47 Iván Nova
game.losing_pitcher(47, is_away_team=True)

# print(game)
game.generate_scorecard()
