import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-04-12
# https://www.baseball-reference.com/boxes/BOS/BOS201804120.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/04/12/529593/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-12 19:12-22:58 (0:45 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "36,341",
        "temp": "53F, Cloudy",
        "wind": "15mph, Out To LF",
        "away": {
            "team": "New York Yankees",
            "starter": 55,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                24: "Gary Sánchez",
                31: "Aaron Hicks",
                14: "Neil Walker",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                # Starting pitcher
                55: "Sonny Gray",
                # Bench
                28: "Austin Romine",
                41: "Miguel Andujar",
                26: "Tyler Austin",
                # Bullpen
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                19: "Masahiro Tanaka",
                43: "Adam Warren",
                57: "Chad Green",
                48: "Tommy Kahnle",
                85: "Luis Cessa",
                47: "Jordan Montgomery",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 47, 54],
            "lineup": [
                [11, "8"],
                [99, "9"],
                [27, "7"],
                [18, "6"],
                [24, "2"],
                [31, "0"],
                [14, "3"],
                [12, "4"],
                [74, "5"],
            ],
            "bench": [
                [28, "C"],
                [41, "LF"],
                [26, "1B"],
            ],
            "bullpen": [68, 40, 45, 65, 19, 43, 57, 48, 85, 47, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                12: "Brock Holt",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [3, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 41, 61, 37, 24, 46, 76, 64, 56, 32],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "David Rackley",
            "2B": "Larry Vanover",
            "3B": "Hunter Wendelstedt",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("c f b b b")
t1.out("G3")

# 2. NYY #99 Aaron Judge (X - X - X)
t1.new_ab()
t1.pitch_list("f c b")
t1.out("G5-3")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G1-3")


# Bot 1st
# Pitching: NYY #55 Sonny Gray
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f b")
b1.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(1)
b1.advance(2, "13 HBP")
b1.advance(3, "28 F9")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b1.new_ab()
b1.pitch_list("1")
b1.reach("HBP")
# Offensive change (BOS): Pinch-runner #18 Mitch Moreland replaces #13 Hanley Ramirez
b1.offensive_substitution(3, 18, "PR")
b1.atbase("PR")

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
b1.new_ab()
b1.pitch_list("b c")
b1.out("F9")

# 5. BOS #11 Rafael Devers (16 - X - 18)
b1.new_ab()
b1.pitch_list("d")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# Defensive switch (BOS): #18 Mitch Moreland moves to 1B
t2.defensive_switch(18, "3")

# 4. NYY #18 Didi Gregorius (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b f b f f")
t2.out("F8")

# 5. NYY #24 Gary Sánchez (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 6. NYY #31 Aaron Hicks (X - X - X)
t2.new_ab()
t2.pitch_list("f f b f f")
t2.out("F7")


# Bot 2nd
# Pitching: NYY #55 Sonny Gray
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f")
b2.hit(1)
b2.advance(2, "19 BB")
b2.advance(3, "3 WP")
b2.advance(4, "3 1B")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
b2.new_ab()
b2.pitch_list("b 1 1 b b c b")
b2.reach("BB")
b2.advance(2, "3 1B")
b2.advance(3, "12 BB")
b2.advance(4, "50 SF8")

# 8. BOS #3  Sandy León (X - 36 - 19)
b2.new_ab()
b2.pitch_list("b")
b2.wp()
b2.hit(1, rbis=1)
b2.advance(2, "12 BB")
b2.advance(3, "50 SF8")
b2.advance(4, "16 FC4")

# 9. BOS #12 Brock Holt (X - 19 - 3)
b2.new_ab()
b2.pitch_list("b c d b b")
b2.reach("BB")
b2.advance(2, "50 SF8")
b2.advance(3, "16 FC4")
b2.advance(4, "18 1B")

# 1. BOS #50 Mookie Betts (19 - 3 - 12)
b2.new_ab()
b2.out("SF8", rbis=1)

# 2. BOS #16 Andrew Benintendi (3 - 12 - X)
b2.new_ab()
b2.pitch_list("c c f")
b2.reach("FC4", rbis=1)
b2.error(4)
b2.advance(2, "E4")
b2.advance(3, "18 1B")

# 3. BOS #18 Mitch Moreland (12 - 16 - X)
b2.new_ab()
b2.pitch_list("f s f")
b2.hit(1, rbis=1)
b2.advance(2, "28 WP")

# 4. BOS #28 J.D. Martinez (16 - X - 18)
b2.new_ab()
b2.pitch_list("b c f s")
b2.wp()
b2.out("K")

# 5. BOS #11 Rafael Devers (16 - 18 - X)
b2.new_ab()
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 7. NYY #14 Neil Walker (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c f")
t3.out("F7")

# 8. NYY #12 Tyler Wade (X - X - X)
t3.new_ab()
t3.pitch_list("s f b s")
t3.out("K")

# 9. NYY #74 Ronald Torreyes (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f")
t3.out("G1-3")


# Bot 3rd
# Pitching: NYY #55 Sonny Gray
b3 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(2)
b3.advance(4, "19 2B")

# 7. BOS #19 Jackie Bradley Jr. (X - 36 - X)
b3.new_ab()
b3.pitch_list("s c")
b3.hit(2, rbis=1)
b3.advance(3, "3 WP")
b3.advance(4, "50 FC5-4")

# 8. BOS #3  Sandy León (X - 19 - X)
b3.new_ab()
b3.pitch_list("f c s")
b3.wp()
b3.reach("K")
b3.thrown_out(2, "50 FC5-4", 2, 55)

# 9. BOS #12 Brock Holt (19 - X - 3)
b3.new_ab()
b3.pitch_list("b c s c")
b3.out("!K")

# 1. BOS #50 Mookie Betts (19 - X - 3)
b3.new_ab()
b3.reach("FC5-4", rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("d")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F7")

# 2. NYY #99 Aaron Judge (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.reach("HBP")

# 4. NYY #18 Didi Gregorius (X - X - 27)
t4.new_ab()
t4.pitch_list("b b c f")
t4.out("F7")


# Bot 4th
# Pitching: NYY #55 Sonny Gray
b4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b")
b4.hit(1)

# Pitching change (NYY): #65 Domingo Germán replaces #55 Sonny Gray
b4.pitching_substitution(65)

# 4. BOS #28 J.D. Martinez (X - X - 18)
b4.new_ab()
b4.pitch_list("c f f")
b4.out("F9")

# 5. BOS #11 Rafael Devers (X - X - 18)
b4.new_ab()
b4.pitch_list("f f")
b4.out("(F)P2")

# 6. BOS #36 Eduardo Núñez (X - X - 18)
b4.new_ab()
b4.pitch_list("b c d")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 5. NYY #24 Gary Sánchez (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 6. NYY #31 Aaron Hicks (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F8")

# 7. NYY #14 Neil Walker (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G3")


# Bot 5th
# Pitching: NYY #65 Domingo Germán
b5 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("f s s")
b5.out("K")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G5-3")

# 9. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #36 Eduardo Núñez (2B), playing SS, batting 6th
t6.defensive_substitution(6, 5, "6")

# Defensive switch (BOS): #12 Brock Holt moves to 2B
t6.defensive_switch(12, "4")

# 8. NYY #12 Tyler Wade (X - X - X)
t6.new_ab()
t6.pitch_list("b c s f")
t6.out("G3-1")

# 9. NYY #74 Ronald Torreyes (X - X - X)
t6.new_ab()
t6.pitch_list("c c f c")
t6.out("!K")

# 1. NYY #11 Brett Gardner (X - X - X)
t6.new_ab()
t6.pitch_list("b b c s s")
t6.out("K")


# Bot 6th
# Pitching: NYY #65 Domingo Germán
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b c f b")
b6.hit(1)

# 3. BOS #18 Mitch Moreland (X - X - 16)
b6.new_ab()
b6.pitch_list("s s c")
b6.out("!K")

# 4. BOS #28 J.D. Martinez (X - X - 16)
b6.new_ab()
b6.pitch_list("b s b b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
t7 = game.new_inning()

# 2. NYY #99 Aaron Judge (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.hit(2)

# 3. NYY #27 Giancarlo Stanton (X - 99 - X)
t7.new_ab()
t7.pitch_list("f s b b f b")
t7.hit(1)

# 4. NYY #18 Didi Gregorius (X - 99 - 27)
t7.new_ab()
t7.out("F9")

# 5. NYY #24 Gary Sánchez (X - 99 - 27)
t7.new_ab()
t7.pitch_list("f s b f c")
t7.out("!K")

# 6. NYY #31 Aaron Hicks (X - 99 - 27)
t7.new_ab()
t7.pitch_list("f b b f f f b s")
t7.out("K")


# Bot 7th
# Pitching: NYY #48 Tommy Kahnle
b7 = game.new_inning()

# Pitching change (NYY): #48 Tommy Kahnle replaces #65 Domingo Germán
b7.pitching_substitution(48)

# 5. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b f s f s")
b7.out("K")

# 6. BOS #5  Tzu-Wei Lin (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b s d")
b7.reach("BB")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 5)
b7.new_ab()
b7.pitch_list("b d f s s")
b7.out("K")

# 8. BOS #3  Sandy León (X - X - 5)
b7.new_ab()
b7.pitch_list("b c")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #64 Marcus Walden
t8 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #22 Rick Porcello
t8.pitching_substitution(64)

# 7. NYY #14 Neil Walker (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 8. NYY #12 Tyler Wade (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f b c")
t8.out("!K")

# 9. NYY #74 Ronald Torreyes (X - X - X)
t8.new_ab()
t8.hit(2)

# 1. NYY #11 Brett Gardner (X - 74 - X)
t8.new_ab()
t8.pitch_list("c b c s")
t8.out("K2-3")


# Bot 8th
# Pitching: NYY #43 Adam Warren
b8 = game.new_inning()

# Pitching change (NYY): #43 Adam Warren replaces #48 Tommy Kahnle
b8.pitching_substitution(43)

# 9. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.out("G3-1")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b c s")
b8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f f")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #64 Marcus Walden
t9 = game.new_inning()

# 2. NYY #99 Aaron Judge (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b b")
t9.reach("BB")
t9.error(5)
t9.advance(2, "27 1B")
t9.advance(3, "27 E5")
t9.advance(4, "24 2B")

# 3. NYY #27 Giancarlo Stanton (X - X - 99)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "18 SB")
t9.advance(4, "24 2B")

# 4. NYY #18 Didi Gregorius (99 - X - 27)
t9.new_ab()
t9.pitch_list("b b b c b")
t9.reach("BB")
t9.advance(4, "24 2B")

# 5. NYY #24 Gary Sánchez (99 - 27 - 18)
t9.new_ab()
t9.hit(2, rbis=3)
t9.advance(3, "31 G3-1")

# Pitching change (BOS): #46 Craig Kimbrel replaces #64 Marcus Walden
t9.pitching_substitution(46)

# 6. NYY #31 Aaron Hicks (X - 24 - X)
t9.new_ab()
t9.pitch_list("b s b f f f")
t9.out("G3-1")

# 7. NYY #14 Neil Walker (24 - X - X)
t9.new_ab()
t9.pitch_list("c s f s")
t9.out("K")

# 8. NYY #12 Tyler Wade (24 - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: NYY
# LP: NYY #55 Sonny Gray
game.losing_pitcher(55, is_away_team=True)

# print(game)
game.generate_scorecard()
