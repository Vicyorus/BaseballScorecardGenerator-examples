import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-06-30
# https://www.baseball-reference.com/boxes/NYA/NYA201806300.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/06/30/530639/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-30 19:15-22:32",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "47,125",
        "temp": "92F, Clear",
        "wind": "7mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 44, 22, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 55,
            "roster": {
                # Lineup
                31: "Aaron Hicks",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                25: "Gleyber Torres",
                18: "Didi Gregorius",
                41: "Miguel Andujar",
                29: "Brandon Drury",
                28: "Austin Romine",
                11: "Brett Gardner",
                # Starting pitcher
                55: "Sonny Gray",
                # Bench
                33: "Greg Bird",
                66: "Kyle Higashioka",
                14: "Neil Walker",
                # Bullpen
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                61: "Giovanny Gallegos",
                38: "Jonathan Loáisiga",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                43: "Adam Warren",
                57: "Chad Green",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 52, 54],
            "lineup": [
                [31, "8"],
                [99, "9"],
                [27, "0"],
                [25, "4"],
                [18, "6"],
                [41, "5"],
                [29, "3"],
                [28, "2"],
                [11, "7"],
            ],
            "bench": [
                [33, "1B"],
                [66, "C"],
                [14, "2B"],
            ],
            "bullpen": [68, 40, 45, 65, 61, 38, 56, 52, 43, 57, 30, 54],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "Fieldin Culbreth",
            "2B": "CB Bucknor",
            "3B": "Chris Conroy",
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
# Pitching: NYY #55 Sonny Gray
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f f")
t1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f f b f")
t1.hit(1)
t1.advance(2, "18 BB")
t1.advance(3, "2 1B")
t1.advance(4, "11 HR")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t1.new_ab()
t1.pitch_list("c b b s f b b")
t1.reach("BB")
t1.advance(2, "2 1B")
t1.advance(4, "11 HR")

# 5. BOS #2  Xander Bogaerts (X - 28 - 18)
t1.new_ab()
t1.hit(1)
t1.advance(4, "11 HR")

# 6. BOS #11 Rafael Devers (28 - 18 - 2)
t1.new_ab()
t1.pitch_list("d s f")
t1.hit(4, rbis=4)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f f")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.reach("HBP")
b1.advance(2, "27 1B")

# 2. NYY #99 Aaron Judge (X - X - 31)
b1.new_ab()
b1.pitch_list("s c b f s")
b1.out("K")

# 3. NYY #27 Giancarlo Stanton (X - X - 31)
b1.new_ab()
b1.pitch_list("f c")
b1.hit(1)

# 4. NYY #25 Gleyber Torres (X - 31 - 27)
b1.new_ab()
b1.pitch_list("c s s")
b1.out("K")

# 5. NYY #18 Didi Gregorius (X - 31 - 27)
b1.new_ab()
b1.pitch_list("b f")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #55 Sonny Gray
t2 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c b c f")
t2.hit(2)
t2.advance(4, "16 1B")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("L7")

# 1. BOS #50 Mookie Betts (X - 3 - X)
t2.new_ab()
t2.pitch_list("c b b d d")
t2.reach("BB")
t2.advance(3, "16 1B")
t2.advance(4, "28 SF9")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
t2.new_ab()
t2.pitch_list("f d")
t2.hit(1, rbis=1)
t2.advance(2, "18 SB")

# 3. BOS #28 J.D. Martinez (50 - X - 16)
t2.new_ab()
t2.pitch_list("f b 1")
t2.out("SF9", rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - 16)
t2.new_ab()
t2.pitch_list("b d 1 b f s f")
t2.out("G3-1")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
b2.new_ab()
b2.pitch_list("c s b")
b2.out("(F)P3")

# 7. NYY #29 Brandon Drury (X - X - X)
b2.new_ab()
b2.pitch_list("s b c c")
b2.out("!K")

# 8. NYY #28 Austin Romine (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f b b")
b2.reach("BB")
b2.advance(2, "11 WP")

# 9. NYY #11 Brett Gardner (X - X - 28)
b2.new_ab()
b2.pitch_list("c b f b c")
b2.wp()
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #55 Sonny Gray
t3 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.advance(2, "11 1B")
t3.advance(3, "36 FC6-4")
t3.thrown_out(4, "3 DP9-2", 3, 43)

# 6. BOS #11 Rafael Devers (X - X - 2)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.thrown_out(2, "36 FC6-4", 1, 55)

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
t3.new_ab()
t3.pitch_list("b f")
t3.reach("FC6-4")

# Pitching change (NYY): #43 Adam Warren replaces #55 Sonny Gray
t3.pitching_substitution(43)

# 8. BOS #3  Sandy León (2 - X - 36)
t3.new_ab()
t3.pitch_list("c b")
t3.out("DP9-2")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b3.new_ab()
b3.pitch_list("c s f")
b3.out("F8")

# 2. NYY #99 Aaron Judge (X - X - X)
b3.new_ab()
b3.pitch_list("s b c s")
b3.out("K")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b3.new_ab()
b3.pitch_list("s c f")
b3.out("L6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #43 Adam Warren
t4 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b")
t4.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t4.new_ab()
t4.pitch_list("b c 1 f f s")
t4.out("K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t4.new_ab()
t4.pitch_list("1 f b s b b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 4. NYY #25 Gleyber Torres (X - X - X)
b4.new_ab()
b4.pitch_list("c b c f t")
b4.out("KT")

# 5. NYY #18 Didi Gregorius (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P1")

# 6. NYY #41 Miguel Andujar (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #43 Adam Warren
t5 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b c b")
t5.out("G5-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("b f s b")
t5.hit(1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t5.new_ab()
t5.pitch_list("s s s")
t5.out("K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 7. NYY #29 Brandon Drury (X - X - X)
b5.new_ab()
b5.pitch_list("c c s")
b5.out("K2-3")

# 8. NYY #28 Austin Romine (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G4-3")

# 9. NYY #11 Brett Gardner (X - X - X)
b5.new_ab()
b5.pitch_list("c c b b f")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #61 Giovanny Gallegos
t6 = game.new_inning()

# Pitching change (NYY): #61 Giovanny Gallegos replaces #43 Adam Warren
t6.pitching_substitution(61)

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f t")
t6.out("KT")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.advance(2, "50 SB")
t6.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
t6.new_ab()
t6.pitch_list("c b f b b b")
t6.reach("BB")
t6.advance(3, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
t6.new_ab()
t6.pitch_list("s f b s")
t6.out("K")

# 3. BOS #28 J.D. Martinez (X - 19 - 50)
t6.new_ab()
t6.pitch_list("b c")
t6.hit(1, rbis=1)

# 4. BOS #18 Mitch Moreland (50 - X - 28)
t6.new_ab()
t6.out("F7")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b6.new_ab()
b6.pitch_list("c b s b b f f f f s")
b6.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b s")
b6.out("K")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b6.new_ab()
b6.pitch_list("b s s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #61 Giovanny Gallegos
t7 = game.new_inning()

# Defensive change (NYY): #66 Kyle Higashioka replaces #28 Austin Romine (C), playing C, batting 8th
t7.defensive_substitution(8, 66, "2")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("c s b")
t7.hit(2)
t7.advance(4, "3 HR")

# 7. BOS #36 Eduardo Núñez (X - 11 - X)
t7.new_ab()
t7.pitch_list("c c d f s")
t7.out("K")

# 8. BOS #3  Sandy León (X - 11 - X)
t7.new_ab()
t7.pitch_list("f b c")
t7.hit(4, rbis=2)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 4. NYY #25 Gleyber Torres (X - X - X)
b7.new_ab()
b7.pitch_list("s b b f f s")
b7.out("K")

# 5. NYY #18 Didi Gregorius (X - X - X)
b7.new_ab()
b7.pitch_list("s b b f")
b7.out("G3-1")

# 6. NYY #41 Miguel Andujar (X - X - X)
b7.new_ab()
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #56 Jonathan Holder
t8 = game.new_inning()

# Pitching change (NYY): #56 Jonathan Holder replaces #61 Giovanny Gallegos
t8.pitching_substitution(56)

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b f")
t8.hit(2)
t8.advance(3, "16 G3")
t8.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G3")

# 3. BOS #28 J.D. Martinez (50 - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1, rbis=1)
t8.thrown_out(2, "2 FC6-4", 3, 56)

# 4. BOS #18 Mitch Moreland (X - X - 28)
t8.new_ab()
t8.pitch_list("b s b b")
t8.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t8.new_ab()
t8.pitch_list("c f")
t8.reach("FC6-4")


# Bot 8th
# Pitching: BOS #37 Heath Hembree
b8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #41 Chris Sale
b8.pitching_substitution(37)

# Defensive change (BOS): #12 Brock Holt replaces #36 Eduardo Núñez (2B), playing 2B, batting 7th
b8.defensive_substitution(7, 12, "4")

# Defensive change (BOS): #23 Blake Swihart replaces #3 Sandy León (C), playing C, batting 8th
b8.defensive_substitution(8, 23, "2")

# 7. NYY #29 Brandon Drury (X - X - X)
b8.new_ab()
b8.pitch_list("b b c c s")
b8.out("K")

# 8. NYY #66 Kyle Higashioka (X - X - X)
b8.new_ab()
b8.pitch_list("f f f")
b8.out("P4")

# 9. NYY #11 Brett Gardner (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f b b")
b8.reach("BB")

# 1. NYY #31 Aaron Hicks (X - X - 11)
b8.new_ab()
b8.pitch_list("c")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #45 Chasen Shreve
t9 = game.new_inning()

# Pitching change (NYY): #45 Chasen Shreve replaces #56 Jonathan Holder
t9.pitching_substitution(45)

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "12 WP")
t9.advance(4, "12 1B")

# 7. BOS #12 Brock Holt (X - X - 11)
t9.new_ab()
t9.pitch_list("b b f f b")
t9.wp()
t9.hit(1, rbis=1)

# 8. BOS #23 Blake Swihart (X - X - 12)
t9.new_ab()
t9.pitch_list("c c b t")
t9.out("KT")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
t9.new_ab()
t9.pitch_list("s")
t9.out("L4")

# 1. BOS #50 Mookie Betts (X - X - 12)
t9.new_ab()
t9.pitch_list("c b c f b b s")
t9.out("K")


# Bot 9th
# Pitching: BOS #76 Hector Velázquez
b9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #37 Heath Hembree
b9.pitching_substitution(76)

# Defensive change (BOS): #25 Steve Pearce replaces #18 Mitch Moreland (1B), playing 1B, batting 4th
b9.defensive_substitution(4, 25, "3")

# 2. NYY #99 Aaron Judge (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("G5-3")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b")
b9.out("G6-3")

# 4. NYY #25 Gleyber Torres (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1)
b9.thrown_out(2, "18 FC6", 3, 76)

# 5. NYY #18 Didi Gregorius (X - X - 25)
b9.new_ab()
b9.pitch_list("c d b c")
b9.reach("FC6")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)

# Loser team: NYY
# LP: NYY #55 Sonny Gray
game.losing_pitcher(55)

# print(game)
game.generate_scorecard()
